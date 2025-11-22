import bpy
from .stroke_consumer import BaseStrokeConsumer

class GreasePencilStrokeConsumer(BaseStrokeConsumer):
    """Consumes stroke commands and creates Grease Pencil strokes in Blender.
    Compatible with Blender 5.0+ Grease Pencil v3."""
    
    def process_current_path(self) -> None:
        if not self.current_path or len(self.current_path) < 2:
            print(f"Skipping path: too few points ({len(self.current_path) if self.current_path else 0})")
            return
        
        print(f"Processing stroke with {len(self.current_path)} points")
        print(f"Brush: {self.current_brush}, Size: {self.current_brush_size}, Color: {self.current_color}")
        
        # Find or create a Grease Pencil object
        # Blender 5.0 uses 'GREASEPENCIL' instead of 'GPENCIL'
        gp_obj = None
        for obj in bpy.data.objects:
            if obj.type == 'GREASEPENCIL':
                gp_obj = obj
                break
        
        if gp_obj is None:
            print("Creating new Grease Pencil object")
            # Blender 5.0 uses grease_pencils_v3
            gp_data = bpy.data.grease_pencils_v3.new('OpenBrushGP')
            gp_obj = bpy.data.objects.new('OpenBrushGP', gp_data)
            bpy.context.collection.objects.link(gp_obj)
        
        gp = gp_obj.data
        
        # Get or create a layer
        if not gp.layers:
            layer = gp.layers.new('OpenBrushLayer')
        else:
            layer = gp.layers[0]
        
        # Get or create frame
        current_frame = bpy.context.scene.frame_current
        frame = None
        for f in layer.frames:
            if f.frame_number == current_frame:
                frame = f
                break
        if frame is None:
            frame = layer.frames.new(current_frame)
        
        # In Blender 5.0, frame has a 'drawing' attribute
        drawing = frame.drawing
        
        # Create or get material
        brush_name = self.current_brush or "Fallback"
        mat_name = f"OpenBrushGP_{brush_name}"
        mat = bpy.data.materials.get(mat_name)
        
        if mat is None:
            print(f"Creating new material: {mat_name}")
            mat = bpy.data.materials.new(mat_name)
            mat.use_nodes = True
            mat.diffuse_color = (*self.current_color, 1.0)
            if mat.node_tree and mat.node_tree.nodes:
                bsdf = mat.node_tree.nodes.get('Principled BSDF')
                if bsdf:
                    bsdf.inputs['Base Color'].default_value = (*self.current_color, 1.0)
        
        # Assign material to object if not already assigned
        if mat.name not in gp_obj.data.materials:
            gp_obj.data.materials.append(mat)
        
        mat_index = gp_obj.data.materials.find(mat.name)
        
        # Create stroke in the drawing
        # In Blender 5.0, use add_strokes() method on the drawing object
        drawing.add_strokes(sizes=(len(self.current_path),))
        
        # Get the newly created stroke (it's the last one)
        stroke = drawing.strokes[-1]
        
        # Set point positions and attributes
        for i, pt in enumerate(self.current_path):
            # Convert from Unity coordinates (Z forward) to Blender (Z up)
            # Unity: X, Y, Z → Blender: X, Z, Y
            stroke.points[i].position = (pt[0], pt[2], pt[1])
            stroke.points[i].radius = self.current_brush_size * (pt[6] if len(pt) > 6 else 1.0) * 0.01
            stroke.points[i].vertex_color = (*self.current_color, 1.0)
        
        # Set stroke material
        stroke.material_index = mat_index
        
        print(f"Created Grease Pencil stroke with {len(stroke.points)} points")
        
        # Force viewport update
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()
