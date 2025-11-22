bl_info = {
    "name": "HTTP Listener",
    "blender": (3, 4, 0),
    "category": "System",
}
import bpy
import threading
import json
import http.server
import socketserver
import queue
import importlib
from urllib.parse import unquote_plus
from bpy.props import EnumProperty
from bpy.types import PropertyGroup

# Import the module with a distinct name to avoid conflict
from . import stroke_consumer as stroke_consumer_module
from . import grease_pencil_stroke_consumer as gp_consumer_module
from . import curve_stroke_consumer as curve_consumer_module
from . import brush_mappings as brush_mappings_module

if "bpy" in locals():
    importlib.reload(stroke_consumer_module)
    importlib.reload(brush_mappings_module)
    importlib.reload(gp_consumer_module)
    importlib.reload(curve_consumer_module)

from .grease_pencil_stroke_consumer import GreasePencilStrokeConsumer
from .curve_stroke_consumer import CurveStrokeConsumer

PORT = 8080
httpd = None
server_thread = None
stroke_queue = queue.Queue()
STROKE_CONSUMER_INSTANCE = None  # Will be set based on preference

def get_stroke_consumer():
    """Get the appropriate stroke consumer based on user preference."""
    global STROKE_CONSUMER_INSTANCE
    
    if STROKE_CONSUMER_INSTANCE is None or \
       (bpy.context.scene.openbrush_settings.stroke_type == 'GREASE_PENCIL' and not isinstance(STROKE_CONSUMER_INSTANCE, GreasePencilStrokeConsumer)) or \
       (bpy.context.scene.openbrush_settings.stroke_type == 'CURVE' and not isinstance(STROKE_CONSUMER_INSTANCE, CurveStrokeConsumer)):
        
        if bpy.context.scene.openbrush_settings.stroke_type == 'CURVE':
            STROKE_CONSUMER_INSTANCE = CurveStrokeConsumer(stroke_queue)
        else:
            STROKE_CONSUMER_INSTANCE = GreasePencilStrokeConsumer(stroke_queue)
    
    return STROKE_CONSUMER_INSTANCE

class OpenBrushSettings(PropertyGroup):
    stroke_type: EnumProperty(
        name="Stroke Type",
        description="Choose how strokes are created in Blender",
        items=[
            ('GREASE_PENCIL', "Grease Pencil", "Create strokes as Grease Pencil objects"),
            ('CURVE', "Bezier Curves", "Create strokes as 3D Bezier curve objects"),
        ],
        default='GREASE_PENCIL',
    )

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler for Blender OpenBrush connector."""

    def handle_action(self, action: str, params: dict = None, payload: str = None) -> dict:
        """Dispatches actions to the appropriate handler."""
        if action == 'render':
            bpy.ops.render.render(animation=True)
            return {'status': 'success'}
        if action == 'stroke' and payload:
            stroke_queue.put(payload)
            return {'status': 'queued'}
        return {'status': 'unknown_action', 'action': action}

    def handle_request(self, action: str, params: dict, payload: str = None) -> dict:
        """Handles incoming requests by delegating to handle_action."""
        return self.handle_action(action, params, payload) if action else {'status': 'no_action'}

    def do_POST(self):
        """Handles POST requests with URL-encoded stroke data."""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Decode URL-encoded data
            decoded_data = unquote_plus(post_data.decode('utf-8'))
            print(f"Decoded POST data: {decoded_data}")
            
            # Queue the command for the stroke consumer
            stroke_queue.put(decoded_data)
            result = {'status': 'queued'}
            
        except Exception as e:
            print(f"POST error: {e}")
            import traceback
            traceback.print_exc()
            result = {'status': 'error', 'message': str(e)}
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))

    def do_GET(self):
        """Handles GET requests with URL parameters."""
        from urllib.parse import urlparse, parse_qs, unquote
        try:
            parsed_path = urlparse(self.path)
            query_string = parsed_path.query
            
            print(f"GET query: {query_string}")
            
            # Queue the command directly for the stroke consumer
            if query_string:
                stroke_queue.put(query_string)
            
            result = {'status': 'success'}
        except Exception as e:
            print(f"GET error: {e}")
            result = {'status': 'error', 'message': str(e)}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))


def start_http_server():
    global httpd, server_thread

    if httpd is None:
        handler = RequestHandler
        httpd = socketserver.TCPServer(("", PORT), handler)
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.start()

def stop_http_server():
    global httpd, server_thread

    if httpd is not None:
        httpd.shutdown()
        httpd.server_close()
        server_thread.join()
        httpd = None
        server_thread = None

def process_stroke_queue():
    consumer = get_stroke_consumer()
    consumer.process_queue()
    return 0.1  # seconds until next call

class HTTP_LISTENER_OT_toggle(bpy.types.Operator):
    bl_idname = "http_listener.toggle"
    bl_label = "Start Listener"

    def execute(self, context):
        global httpd
        
        if httpd is None:
            # Start the server
            start_http_server()
            self.report({'INFO'}, "HTTP Listener started on port {}".format(PORT))
        else:
            # Stop the server
            stop_http_server()
            self.report({'INFO'}, "HTTP Listener stopped")
        
        return {'FINISHED'}

class HTTP_LISTENER_OT_register(bpy.types.Operator):
    bl_idname = "http_listener.register"
    bl_label = "Register with Open Brush"

    def execute(self, context):
        import urllib.request
        import urllib.error
        try:
            # Register this Blender instance with Open Brush
            url = f"http://localhost:40074/api/v1?listenfor.strokes=http://localhost:{PORT}/"
            response = urllib.request.urlopen(url, timeout=5)
            
            if response.status == 200:
                self.report({'INFO'}, "Successfully registered with Open Brush")
            else:
                self.report({'WARNING'}, f"Open Brush responded with status {response.status}")
            
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                self.report({'ERROR'}, f"Failed to connect to Open Brush: {e.reason}")
            elif hasattr(e, 'code'):
                self.report({'ERROR'}, f"Open Brush returned error code: {e.code}")
            else:
                self.report({'ERROR'}, f"Failed to register: {str(e)}")
        except Exception as e:
            self.report({'ERROR'}, f"Unexpected error: {str(e)}")
        
        return {'FINISHED'}

class HTTP_LISTENER_PT_panel(bpy.types.Panel):
    bl_label = "HTTP Listener"
    bl_idname = "HTTP_LISTENER_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Open Brush'

    def draw(self, context):
        global httpd
        layout = self.layout
        settings = context.scene.openbrush_settings

        # Stroke type selector
        layout.prop(settings, "stroke_type", text="Stroke Type")
        
        layout.separator()

        # Toggle button with dynamic text
        row = layout.row()
        if httpd is not None:
            row.operator("http_listener.toggle", text="Stop Listener", depress=True)
        else:
            row.operator("http_listener.toggle", text="Start Listener")

        row = layout.row()
        row.operator("http_listener.register")

def register():
    bpy.utils.register_class(OpenBrushSettings)
    bpy.types.Scene.openbrush_settings = bpy.props.PointerProperty(type=OpenBrushSettings)
    
    bpy.utils.register_class(HTTP_LISTENER_OT_toggle)
    bpy.utils.register_class(HTTP_LISTENER_OT_register)
    bpy.utils.register_class(HTTP_LISTENER_PT_panel)
    bpy.app.timers.register(process_stroke_queue)

def unregister():
    bpy.utils.unregister_class(HTTP_LISTENER_OT_toggle)
    bpy.utils.unregister_class(HTTP_LISTENER_OT_register)
    bpy.utils.unregister_class(HTTP_LISTENER_PT_panel)
    
    del bpy.types.Scene.openbrush_settings
    bpy.utils.unregister_class(OpenBrushSettings)
    
    stop_http_server()
    try:
        bpy.app.timers.unregister(process_stroke_queue)
    except Exception:
        pass

if __name__ == "__main__":
    register()