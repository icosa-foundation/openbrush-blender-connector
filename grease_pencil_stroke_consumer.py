import bpy
from .stroke_consumer import BaseStrokeConsumer

class GreasePencilStrokeConsumer(BaseStrokeConsumer):
    """Consumes stroke commands and creates Grease Pencil strokes in Blender using per-point vertex color.
    Each brush type uses a unique material; unsupported brushes use a fallback material.
    Orientation (rx, ry, rz) is parsed but not used; see commented code for future support."""
    def process_current_path(self) -> None:
        if not self.current_path or len(self.current_path) < 2:
            return
        # Find or create a Grease Pencil object
        gp_obj = None
        for obj in bpy.data.objects:
            if obj.type == 'GPENCIL':
                gp_obj = obj
                break
        if gp_obj is None:
            gp_data = bpy.data.grease_pencils.new('OpenBrushGP')
            gp_obj = bpy.data.objects.new('OpenBrushGP', gp_data)
            bpy.context.collection.objects.link(gp_obj)
        bpy.context.view_layer.objects.active = gp_obj
        bpy.ops.object.mode_set(mode='PAINT_GPENCIL')
        # Get or create a layer
        gp = gp_obj.data
        if not gp.layers:
            layer = gp.layers.new('OpenBrushLayer', set_active=True)
        else:
            layer = gp.layers.active
        frame = layer.frames.get(0) or layer.frames.new(0)
        # Select or create a material for the current brush
        brush_name = self.current_brush or "Fallback"
        mat_name = f"OpenBrushGP_{brush_name}"
        mat = next((m for m in gp_obj.data.materials if m.name == mat_name), None)
        if mat is None:
            mat = bpy.data.materials.new(mat_name)
            mat.grease_pencil.color = (1.0, 1.0, 1.0, 1.0)
            gp_obj.data.materials.append(mat)
        # Create a new stroke
        stroke = frame.strokes.new()
        stroke.display_mode = '3DSPACE'
        stroke.line_width = int(self.current_brush_size * 100)
        stroke.points.add(count=len(self.current_path))
        for i, pt in enumerate(self.current_path):
            stroke.points[i].co = (pt[0], pt[1], pt[2])
            stroke.points[i].pressure = pt[6] if len(pt) > 6 else 1.0
            stroke.points[i].vertex_color = (*self.current_color, 1.0)
            # Orientation (rx, ry, rz) is available as pt[3:6]
            # Uncomment and use when Blender supports per-point orientation:
            # stroke.points[i].rotation = (pt[3], pt[4], pt[5])
        stroke.material_index = gp_obj.data.materials.find(mat.name)
        bpy.ops.object.mode_set(mode='OBJECT')
