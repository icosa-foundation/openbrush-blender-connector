import bpy
from .stroke_consumer import BaseStrokeConsumer

class CurveStrokeConsumer(BaseStrokeConsumer):
    """Consumes stroke commands and creates Bezier curve strokes in Blender."""
    
    def process_current_path(self) -> None:
        if not self.current_path or len(self.current_path) < 2:
            print(f"Skipping path: too few points ({len(self.current_path) if self.current_path else 0})")
            return
        
        print(f"Processing stroke with {len(self.current_path)} points as curve")
        print(f"Brush: {self.current_brush}, Size: {self.current_brush_size}, Color: {self.current_color}")
        
        # Create a new curve for each stroke
        curve_data = bpy.data.curves.new(name='OpenBrushStroke', type='CURVE')
        curve_data.dimensions = '3D'
        curve_data.bevel_depth = self.current_brush_size * 0.01  # Convert to reasonable size
        curve_data.bevel_resolution = 4
        
        # Create a new spline in the curve
        spline = curve_data.splines.new(type='POLY')
        spline.points.add(len(self.current_path) - 1)  # -1 because spline starts with 1 point
        
        # Set point positions
        for i, pt in enumerate(self.current_path):
            # Convert from Unity coordinates (Z forward) to Blender (Z up)
            # Unity: X, Y, Z → Blender: X, Z, Y
            # Curve points use 4D coordinates (x, y, z, w)
            spline.points[i].co = (pt[0], pt[2], pt[1], 1.0)
            # Optionally use pressure to vary radius
            if len(pt) > 6:
                spline.points[i].radius = pt[6]
        
        # Create object from curve
        curve_obj = bpy.data.objects.new('OpenBrushStroke', curve_data)
        bpy.context.collection.objects.link(curve_obj)
        
        # Create or get material
        brush_name = self.current_brush or "Fallback"
        mat_name = f"OpenBrushCurve_{brush_name}"
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
                    bsdf.inputs['Emission Color'].default_value = (*self.current_color, 1.0)
                    bsdf.inputs['Emission Strength'].default_value = 0.5
        
        # Assign material to curve
        if curve_data.materials:
            curve_data.materials[0] = mat
        else:
            curve_data.materials.append(mat)
        
        print(f"Created curve stroke with {len(spline.points)} points")
        
        # Force viewport update
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()
