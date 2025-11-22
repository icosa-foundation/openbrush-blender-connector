import bpy
from .stroke_consumer import BaseStrokeConsumer

class GreasePencilStrokeConsumer(BaseStrokeConsumer):
    """Consumes stroke commands and creates Grease Pencil strokes in Blender using per-point vertex color.
    Each brush type uses a unique material; unsupported brushes use a fallback material.
    Orientation (rx, ry, rz) is parsed but not used; see commented code for future support."""
    
    def process_current_path(self) -> None:
        if not self.current_path or len(self.current_path) < 2:
            print(f"Skipping path: too few points ({len(self.current_path) if self.current_path else 0})")
            return
        
        print(f"Processing stroke with {len(self.current_path)} points")
        print(f"Brush: {self.current_brush}, Size: {self.current_brush_size}, Color: {self.current_color}")
        
        # Find or create a Grease Pencil object
        gp_obj = None
        for obj in bpy.data.objects:
            if obj.type == 'GPENCIL':
                gp_obj = obj
                break
        
        if gp_obj is None:
            print("Creating new Grease Pencil object")
            gp_data = bpy.data.grease_pencils.new('OpenBrushGP')
            gp_obj = bpy.data.objects.new('OpenBrushGP', gp_data)
            bpy.context.collection.objects.link(gp_obj)
        
        # Get or create a layer
        gp = gp_obj.data
        if not gp.layers:
            layer = gp.layers.new('OpenBrushLayer', set_active=True)
        else:
            layer = gp.layers.active
        
        # Get or create frame at current frame
        current_frame = bpy.context.scene.frame_current
        frame = layer.frames.get(current_frame)
        if frame is None:
            frame = layer.frames.new(current_frame)
        
        # Select or create a material for the current brush
        brush_name = self.current_brush or "Fallback"
        mat_name = f"OpenBrushGP_{brush_name}"
        mat = next((m for m in gp_obj.data.materials if m.name == mat_name), None)
        
        if mat is None:
            print(f"Creating new material: {mat_name}")
            mat = bpy.data.materials.new(mat_name)
            # Enable vertex color for the material
            mat.grease_pencil.show_stroke = True
            mat.grease_pencil.mode = 'LINE'
            mat.grease_pencil.color = (*self.current_color, 1.0)
            mat.grease_pencil.use_stroke_holdout = False
            gp_obj.data.materials.append(mat)
        
        # Create a new stroke
        stroke = frame.strokes.new()
        stroke.display_mode = '3DSPACE'
        stroke.line_width = max(10, int(self.current_brush_size * 200))  # Ensure visible width
        stroke.points.add(count=len(self.current_path))
        
        for i, pt in enumerate(self.current_path):
            stroke.points[i].co = (pt[0], pt[1], pt[2])
            stroke.points[i].pressure = pt[6] if len(pt) > 6 else 1.0
            stroke.points[i].vertex_color = (*self.current_color, 1.0)
        
        stroke.material_index = gp_obj.data.materials.find(mat.name)
        
        print(f"Created stroke with {len(stroke.points)} points, material index: {stroke.material_index}")
        
        # Force viewport update
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()
