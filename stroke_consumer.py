import bpy
import queue
import json
from typing import Optional

class BaseStrokeConsumer:

    """Base class for consuming stroke commands from a queue."""
    def __init__(self, stroke_queue: queue.Queue):
        self.stroke_queue = stroke_queue
        self.current_color: tuple = (1.0, 1.0, 1.0)
        self.current_brush: Optional[str] = None
        self.current_brush_size: float = 1.0
        self.current_path: Optional[list] = None
        self.path_ready: bool = False

    def process_queue(self) -> None:
        """Process all commands in the queue."""
        try:
            while True:
                command = self.stroke_queue.get_nowait()
                self.decode_command(command)
                if self.path_ready:
                    self.process_current_path()
                    self.path_ready = False
        except queue.Empty:
            pass

    def decode_command(self, command: str) -> None:
        """Decode a single command string and update state."""
        parts = command.split('=', 1)
        if len(parts) != 2:
            return
        key, value = parts
        if key == 'brush.type':
            self.current_brush = value
        elif key == 'brush.size':
            try:
                self.current_brush_size = float(value)
            except ValueError:
                pass
        elif key == 'color.set.rgb':
            try:
                rgb = [float(x) for x in value.split(',')]
                self.current_color = tuple(rgb)
            except Exception:
                pass
        elif key == 'draw.stroke':
            try:
                stroke_data = json.loads(f'[{value}]')
                self.current_path = [list(map(float, pt)) for pt in stroke_data]
                self.path_ready = True
            except Exception:
                pass

    def process_current_path(self) -> None:
        """Override in subclasses to process the current path."""
        print(f"Processing path: {self.current_path}")
        print(f"Brush: {self.current_brush}, Size: {self.current_brush_size}, Color: {self.current_color}")
        pass
