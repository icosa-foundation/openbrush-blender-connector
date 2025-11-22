# Open Brush Blender Connector

Stream your Open Brush drawings directly into Blender in real-time! This addon creates Grease Pencil strokes or 3D Bezier curves in Blender as you paint in Open Brush.

![Open Brush to Blender](https://img.shields.io/badge/Open%20Brush-Blender-orange)
![Blender 5.0+](https://img.shields.io/badge/Blender-5.0%2B-blue)

## Features

 **Real-time Streaming** - See your Open Brush strokes appear in Blender instantly  
 **100+ Brush Support** - All Open Brush brushes mapped with appropriate properties  
️ **Output Modes** - Choose between Grease Pencil or Bezier Curves  
 **Brush-Specific Properties** - Each brush has unique corner types, caps, and emission settings  
 **Pressure Sensitivity** - Pressure data preserved for compatible brushes  
 **Color Matching** - Stroke colors automatically match your Open Brush palette  

## Requirements

- **Blender 5.0 or later**
- **Open Brush** (running on the same machine)
- Windows, macOS, or Linux

## Installation

### Method 1: Blender Extensions (Recommended)

1. Download the latest release as a `.zip` file
2. In Blender, go to **Edit → Preferences → Extensions**
3. Click **Install from Disk** and select the downloaded `.zip` file
4. Enable the "HTTP Listener" extension

### Method 2: Manual Installation

1. Clone or download this repository
2. Copy the entire folder to your Blender extensions directory:
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\5.0\extensions\user_default\`
   - **macOS**: `~/Library/Application Support/Blender/5.0/extensions/user_default/`
   - **Linux**: `~/.config/blender/5.0/extensions/user_default/`
3. Restart Blender
4. Enable the addon in **Edit → Preferences → Extensions**

## Quick Start

### 1. Start the Listener

1. Open Blender and press **N** to show the sidebar
2. Click the **Open Brush** tab
3. Click **Start Listener**

### 2. Connect Open Brush

4. Click **Register with Open Brush** (Open Brush must be running)
5. You should see a confirmation message

### 3. Start Drawing!

6. Draw in Open Brush - your strokes will appear in Blender in real-time!

## Usage

### Stroke Type Selection

Choose how strokes are created in Blender:

- **Grease Pencil** - Creates 2D/3D Grease Pencil strokes (best for animation and 2D workflows)
- **Bezier Curves** - Creates 3D curve objects (best for modeling and precise control)

Switch between modes anytime using the dropdown in the Open Brush panel.

### Supported Brushes

TODO

### Brush Properties

Each brush is configured with:
- **Radius Scale** - Brush-specific thickness multiplier
- **Pressure Sensitivity** - Enabled for pressure-responsive brushes
- **Emission** - Glowing materials for light-based brushes
- **Opacity** - Semi-transparent effects for highlighters

## Troubleshooting

### "Failed to connect to Open Brush"
- Make sure Open Brush is running
- Check that both applications are on the same machine
- Try clicking **Register with Open Brush** again

### Strokes not appearing
- Verify the listener is started (button should say "Stop Listener")
- Check the Blender console for error messages
- Try switching stroke types (Grease Pencil ↔ Bezier Curves)

### Strokes are too small/large
- Brush size is controlled by Open Brush's brush size setting
- Each brush has a radius scale multiplier (see `brush_mappings.py`)
- Adjust the `0.01` scaling factor in `grease_pencil_stroke_consumer.py` if needed

### Coordinate mismatch
- Strokes are automatically converted from Unity coordinates (Z-forward) to Blender coordinates (Z-up)
- If strokes appear rotated, check the coordinate conversion in the stroke consumer

## Advanced Configuration

### Customizing Brush Mappings

Edit `brush_mappings.py` to customize how Open Brush brushes map to Blender properties:

```python
"brush-guid-here": BrushMapping(
    name="MyBrush",
    corner_type='ROUND',      # 'ROUND', 'SHARP', 'FLAT'
    cap_mode='ROUND',         # 'ROUND', 'FLAT'
    radius_scale=1.5,         # Thickness multiplier
    use_pressure=True,        # Enable pressure sensitivity
    use_emission=True,        # Make material glow
    emission_strength=2.0,    # Glow intensity
)
```

### Port Configuration

The default port is `8080`. To change it, edit `PORT` in `__init__.py`:

```python
PORT = 8080  # Change to your preferred port
```

## Technical Details

### Architecture

- **HTTP Server** - Listens on `localhost:8080` for stroke data from Open Brush
- **Stroke Queue** - Processes incoming strokes asynchronously
- **Stroke Consumers** - Convert Open Brush data to Blender objects
  - `GreasePencilStrokeConsumer` - Creates Grease Pencil strokes
  - `CurveStrokeConsumer` - Creates Bezier curve objects
- **Brush Mappings** - Maps 100+ Open Brush brush GUIDs to Blender properties

### Data Flow

1. Open Brush sends stroke data via HTTP POST/GET
2. HTTP server queues the data
3. Blender timer processes queue every 0.1 seconds
4. Stroke consumer creates Blender objects with appropriate properties
5. Viewport updates to show new strokes

### Coordinate Conversion

Open Brush uses Unity's left-handed coordinate system (Z-forward), while Blender uses a right-handed system (Z-up). The conversion is:

- Unity `(X, Y, Z)` → Blender `(X, Z, Y)`

## Contributing

Contributions are welcome! Areas for improvement:

- Additional brush property mappings
- Material/shader enhancements for emissive brushes
- Animation support for audio-reactive brushes
- Performance optimizations for large stroke counts

## License

This project is licensed under the MIT License

## Credits

- **Open Brush** - [icosa-foundation/open-brush](https://github.com/icosa-foundation/open-brush)
- **Brush Metadata** - Extracted from [three-icosa](https://github.com/icosa-foundation/three-icosa)

## Support

For issues, questions, or feature requests, please open an issue on GitHub.

---
