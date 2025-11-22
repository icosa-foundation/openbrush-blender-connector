"""
Brush mapping configuration for Open Brush to Blender Grease Pencil.
Maps Open Brush brush GUIDs to Grease Pencil stroke properties.

COMPLETE MAPPING - All brushes from Open Brush CSV included.

Metadata extracted from:
- https://github.com/icosa-foundation/three-icosa (TiltShaderLoader.js)
- Open Brush Brushes, Materials and Shaders spreadsheet

Each brush includes information about whether it's lit, animated, or audio-reactive.
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class BrushMapping:
    """Configuration for how an Open Brush brush maps to Grease Pencil properties."""
    name: str
    
    # Stroke appearance
    corner_type: str = 'ROUND'  # 'ROUND', 'SHARP', 'FLAT'
    cap_mode: str = 'ROUND'     # 'ROUND', 'FLAT'
    
    # Radius/thickness modifiers
    radius_scale: float = 1.0    # Multiplier for brush size
    use_pressure: bool = True    # Whether to use pressure for radius variation
    
    # Opacity/strength
    opacity_scale: float = 1.0   # Multiplier for opacity
    strength_scale: float = 1.0  # Multiplier for strength
    
    # Material properties
    use_emission: bool = False   # Whether to make material emissive
    emission_strength: float = 0.0
    
    # Metadata (for future use)
    is_lit: bool = False         # Whether brush uses lighting
    is_animated: bool = False    # Whether brush has animation
    is_audio_reactive: bool = False  # Whether brush responds to audio
    is_experimental: bool = False    # Whether brush is experimental


# Complete brush mappings for ALL Open Brush brushes
BRUSH_MAPPINGS = {
    # === STANDARD BRUSHES (Page 1-4) ===
    
    # Oil Paint (1.1)
    "c515dad7-4393-4681-81ad-162ef052241b": BrushMapping(
        name="OilPaint", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True),
    "f72ec0e7-a844-4e38-82e3-140c44772699": BrushMapping(
        name="OilPaint", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True),
    
    # Ink (1.2)
    "c0012095-3ffd-4040-8ee1-fc180d346eaa": BrushMapping(
        name="Ink", corner_type='SHARP', cap_mode='FLAT', radius_scale=1.0, use_pressure=True, is_lit=True),
    "f5c336cf-5108-4b40-ade9-c687504385ab": BrushMapping(
        name="Ink", corner_type='SHARP', cap_mode='FLAT', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # Thick Paint (1.3)
    "75b32cf0-fdd6-4d89-a64b-e2a00b247b0f": BrushMapping(
        name="ThickPaint", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.3, use_pressure=True, is_lit=True),
    "fdf0326a-c0d1-4fed-b101-9db0ff6d071f": BrushMapping(
        name="ThickPaint", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.3, use_pressure=True, is_lit=True),
    
    # Wet Paint (1.4)
    "b67c0e81-ce6d-40a8-aeb0-ef036b081aa3": BrushMapping(
        name="WetPaint", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True),
    "dea67637-cd1a-27e4-c9b1-52f4bbcb84e5": BrushMapping(
        name="WetPaint", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True),
    
    # Marker (1.5)
    "429ed64a-4e97-4466-84d3-145a861ef684": BrushMapping(
        name="Marker", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=False),
    
    # Tapered Marker (1.6)
    "d90c6ad8-af0f-4b54-b422-e0f92abe1b3c": BrushMapping(
        name="TaperedMarker", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True),
    
    # Pinched Marker (1.7)
    "0d3889f3-3ede-470c-8af4-de4813306126": BrushMapping(
        name="DoubleTaperedMarker", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True),
    
    # Highlighter (1.8)
    "cf019139-d41c-4eb0-a1d0-5cf54b0a42f3": BrushMapping(
        name="Highlighter", corner_type='FLAT', cap_mode='FLAT', radius_scale=2.0, use_pressure=False, opacity_scale=0.5),
    
    # Flat (1.9)
    "280c0a7a-aad8-416c-a7d2-df63d129ca70": BrushMapping(
        name="Flat", corner_type='FLAT', cap_mode='FLAT', radius_scale=1.5, use_pressure=False, is_lit=True),
    "2d35bcf0-e4d8-452c-97b1-3311be063130": BrushMapping(
        name="Flat", corner_type='FLAT', cap_mode='FLAT', radius_scale=1.5, use_pressure=False, is_lit=True),
    
    # Tapered Flat (1.10)
    "b468c1fb-f254-41ed-8ec9-57030bc5660c": BrushMapping(
        name="TaperedFlat", corner_type='FLAT', cap_mode='FLAT', radius_scale=1.0, use_pressure=True, is_lit=True),
    "c8ccb53d-ae13-45ef-8afb-b730d81394eb": BrushMapping(
        name="TaperedFlat", corner_type='FLAT', cap_mode='FLAT', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # Pinched Flat (1.11)
    "0d3889f3-3ede-470c-8af4-f44813306126": BrushMapping(
        name="DoubleTaperedFlat", corner_type='FLAT', cap_mode='FLAT', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # Soft Highlighter (1.12)
    "accb32f5-4509-454f-93f8-1df3fd31df1b": BrushMapping(
        name="SoftHighlighter", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.8, use_pressure=False, opacity_scale=0.6, is_audio_reactive=True),
    
    # Light (2.1)
    "2241cd32-8ba2-48a5-9ee7-2caef7e9ed62": BrushMapping(
        name="Light", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.5, use_pressure=False, use_emission=True, emission_strength=2.0, is_audio_reactive=True),
    
    # Fire (2.2)
    "cb92b597-94ca-4255-b017-0e3f42f12f9e": BrushMapping(
        name="Fire", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=False, use_emission=True, emission_strength=3.0, is_animated=True, is_audio_reactive=True),
    
    # Embers (2.3)
    "02ffb866-7fb2-4d15-b761-1012cefb1360": BrushMapping(
        name="Embers", corner_type='ROUND', cap_mode='ROUND', radius_scale=0.8, use_pressure=False, use_emission=True, emission_strength=1.5, is_animated=True, is_audio_reactive=True),
    
    # Smoke (2.4)
    "70d79cca-b159-4f35-990c-f02193947fe8": BrushMapping(
        name="Smoke", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=False, opacity_scale=0.6, is_animated=True),
    
    # Snow (2.5)
    "d902ed8b-d0d1-476c-a8de-878a79e3a34c": BrushMapping(
        name="Snow", corner_type='ROUND', cap_mode='ROUND', radius_scale=0.8, use_pressure=False, is_animated=True, is_audio_reactive=True),
    
    # Rainbow (2.6)
    "ad1ad437-76e2-450d-a23a-e17f8310b960": BrushMapping(
        name="Rainbow", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_animated=True, is_audio_reactive=True),
    
    # Stars (2.7)
    "0eb4db27-3f82-408d-b5a1-19ebd7d5b711": BrushMapping(
        name="Stars", corner_type='ROUND', cap_mode='ROUND', radius_scale=0.8, use_pressure=False, is_animated=True, is_audio_reactive=True),
    
    # Velvet Ink (2.8)
    "d229d335-c334-495a-a801-660ac8a87360": BrushMapping(
        name="VelvetInk", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_audio_reactive=True),
    
    # Waveform (2.9)
    "10201aa3-ebc2-42d8-84b7-2e63f6eeb8ab": BrushMapping(
        name="Waveform", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=False, is_animated=True, is_audio_reactive=True),
    
    # Splatter (2.10)
    "7a1c8107-50c5-4b70-9a39-421576d6617e": BrushMapping(
        name="Splatter", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True),
    "8dc4a70c-d558-4efd-a5ed-d4e860f40dc3": BrushMapping(
        name="Splatter", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # Duct Tape (2.11)
    "3ca16e2f-bdcd-4da2-8631-dcef342f40f1": BrushMapping(
        name="DuctTape", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True),
    "d0262945-853c-4481-9cbd-88586bed93cb": BrushMapping(
        name="DuctTape", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True),
    
    # Paper (2.12)
    "759f1ebd-20cd-4720-8d41-234e0da63716": BrushMapping(
        name="Paper", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # Coarse Bristles (3.1)
    "1161af82-50cf-47db-9706-0c3576d43c43": BrushMapping(
        name="CoarseBristles", corner_type='SHARP', cap_mode='FLAT', radius_scale=1.2, use_pressure=True, is_lit=True),
    "79168f10-6961-464a-8be1-57ed364c5600": BrushMapping(
        name="CoarseBristles", corner_type='SHARP', cap_mode='FLAT', radius_scale=1.2, use_pressure=True, is_lit=True),
    
    # Dr. Wigglez (3.2)
    "5347acf0-a8e2-47b6-8346-30c70719d763": BrushMapping(
        name="WigglyGraphite", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_animated=True, is_audio_reactive=True),
    "e814fef1-97fd-7194-4a2f-50c2bb918be2": BrushMapping(
        name="WigglyGraphite", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_animated=True, is_audio_reactive=True),
    
    # Electricity (3.3)
    "f6e85de3-6dcc-4e7f-87fd-cee8c3d25d51": BrushMapping(
        name="Electricity", corner_type='SHARP', cap_mode='FLAT', radius_scale=0.7, use_pressure=False, use_emission=True, emission_strength=2.5, is_animated=True, is_audio_reactive=True),
    
    # Streamers (3.4)
    "44bb800a-fbc3-4592-8426-94ecb05ddec3": BrushMapping(
        name="Streamers", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_animated=True, is_audio_reactive=True),
    
    # Hypercolor (3.5)
    "dce872c2-7b49-4684-b59b-c45387949c5c": BrushMapping(
        name="Hypercolor", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_animated=True, is_audio_reactive=True),
    "e8ef32b1-baa8-460a-9c2c-9cf8506794f5": BrushMapping(
        name="Hypercolor", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_animated=True, is_audio_reactive=True),
    
    # Bubbles (3.6)
    "89d104cd-d012-426b-b5b3-bbaee63ac43c": BrushMapping(
        name="Bubbles", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=False, is_animated=True),
    
    # Neon Pulse (3.7)
    "b2ffef01-eaaa-4ab5-aa64-95a2c4f5dbc6": BrushMapping(
        name="NeonPulse", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, use_emission=True, emission_strength=2.0, is_lit=True, is_animated=True, is_audio_reactive=True),
    
    # Cel Vinyl (3.8)
    "700f3aa8-9a7c-2384-8b8a-ea028905dd8c": BrushMapping(
        name="CelVinyl", corner_type='SHARP', cap_mode='FLAT', radius_scale=1.0, use_pressure=True),
    
    # Hyper Grid (3.9)
    "6a1cf9f9-032c-45ec-9b6e-a6680bee32e9": BrushMapping(
        name="HyperGrid", corner_type='SHARP', cap_mode='FLAT', radius_scale=0.8, use_pressure=False, is_audio_reactive=True),
    
    # Light Wire (3.10)
    "4391aaaa-df81-4396-9e33-31e4e4930b27": BrushMapping(
        name="LightWire", corner_type='SHARP', cap_mode='FLAT', radius_scale=0.5, use_pressure=False, use_emission=True, emission_strength=1.5, is_lit=True, is_animated=True, is_audio_reactive=True),
    
    # Chromatic Wave (3.11)
    "0f0ff7b2-a677-45eb-a7d6-0cd7206f4816": BrushMapping(
        name="ChromaticWave", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=False, is_animated=True, is_audio_reactive=True),
    
    # Dots (3.12)
    "6a1cf9f9-032c-45ec-9b1d-a6680bee30f7": BrushMapping(
        name="Dots", corner_type='FLAT', cap_mode='FLAT', radius_scale=2.0, use_pressure=False, opacity_scale=0.5, is_audio_reactive=True),
    
    # Petal (4.1)
    "e0abbc80-0f80-e854-4970-8924a0863dcc": BrushMapping(
        name="Petal", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True),
    
    # Icing (4.2)
    "2f212815-f4d3-c1a4-681a-feeaf9c6dc37": BrushMapping(
        name="Icing", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.5, use_pressure=True, is_lit=True),
    
    # Toon (4.3)
    "4391385a-df73-4396-9e33-31e4e4930b27": BrushMapping(
        name="Toon", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=False, is_audio_reactive=True),
    
    # Wire (4.4)
    "4391385a-cf83-4396-9e33-31e4e4930b27": BrushMapping(
        name="Wire", corner_type='SHARP', cap_mode='FLAT', radius_scale=0.5, use_pressure=False),
    
    # Spikes (4.5)
    "cf7f0059-7aeb-53a4-2b67-c83d863a9ffa": BrushMapping(
        name="Spikes", corner_type='SHARP', cap_mode='FLAT', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # Lofted (4.6)
    "d381e0f5-3def-4a0d-8853-31e9200bcbda": BrushMapping(
        name="Lofted", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # Disco (4.7)
    "4391aaaa-df73-4396-9e33-31e4e4930b27": BrushMapping(
        name="Disco", corner_type='SHARP', cap_mode='FLAT', radius_scale=0.5, use_pressure=False, is_lit=True, is_animated=True, is_audio_reactive=True),
    
    # Comet (4.8)
    "1caa6d7d-f015-3f54-3a4b-8b5354d39f81": BrushMapping(
        name="Comet", corner_type='ROUND', cap_mode='ROUND', radius_scale=0.8, use_pressure=True, use_emission=True, emission_strength=1.0, is_animated=True, is_audio_reactive=True),
    
    # Shiny Hull (4.9)
    "faaa4d44-fcfb-4177-96be-753ac0421ba3": BrushMapping(
        name="ShinyHull", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # Matte Hull (4.10)
    "79348357-432d-4746-8e29-0e25c112e3aa": BrushMapping(
        name="MatteHull", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # Unlit Hull (4.11)
    "a8fea537-da7c-4d4b-817f-24f074725d6d": BrushMapping(
        name="UnlitHull", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True),
    
    # Diamond (4.12)
    "c8313697-2563-47fc-832e-290f4c04b901": BrushMapping(
        name="DiamondHull", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # === EXPERIMENTAL BRUSHES ===
    
    # Gouache (5.1)
    "1b897b7e-9b76-425a-b031-a867c48df409": BrushMapping(
        name="Gouache", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True, is_experimental=True),
    "4465b5ef-3605-bec4-2b3e-6b04508ddb6b": BrushMapping(
        name="Gouache", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Mylar Tube (5.2)
    "8e58ceea-7830-49b4-aba9-6215104ab52a": BrushMapping(
        name="MylarTube", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Rain (5.3)
    "03a529e1-f519-3dd4-582d-2d5cd92c3f4f": BrushMapping(
        name="Rain", corner_type='ROUND', cap_mode='ROUND', radius_scale=0.8, use_pressure=False, is_animated=True, is_experimental=True),
    
    # Dry Brush (5.4)
    "725f4c6a-6427-6524-29ab-da371924adab": BrushMapping(
        name="DryBrush", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Leaky Pen (5.5)
    "ddda8745-4bb5-ac54-88b6-d1480370583e": BrushMapping(
        name="LeakyPen", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Sparks (5.6)
    "50e99447-3861-05f4-697d-a1b96e771b98": BrushMapping(
        name="Sparks", corner_type='ROUND', cap_mode='ROUND', radius_scale=0.7, use_pressure=False, use_emission=True, emission_strength=2.0, is_animated=True, is_experimental=True),
    
    # Wind (5.7)
    "7136a729-1aab-bd24-f8b2-ca88b6adfb67": BrushMapping(
        name="Wind", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_animated=True, is_experimental=True),
    
    # Rising Bubbles (5.8)
    "a8147ce1-005e-abe4-88e8-09a1eaadcc89": BrushMapping(
        name="RisingBubbles", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=False, is_animated=True, is_experimental=True),
    
    # Tapered Wire (5.9)
    "9568870f-8594-60f4-1b20-dfbc8a5eac0e": BrushMapping(
        name="TaperedWire", corner_type='SHARP', cap_mode='FLAT', radius_scale=0.5, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Square Flat (5.10)
    "2e03b1bf-3ebd-4609-9d7e-f4cafadc4dfa": BrushMapping(
        name="Square", corner_type='SHARP', cap_mode='FLAT', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Wireframe (5.12)
    "2c1a6a63-6552-4d23-86d7-58f6fba8581b": BrushMapping(
        name="Wireframe", corner_type='SHARP', cap_mode='FLAT', radius_scale=0.8, use_pressure=False, is_audio_reactive=True, is_experimental=True),
    
    # Muscle (6.1)
    "f28c395c-a57d-464b-8f0b-558c59478fa3": BrushMapping(
        name="Muscle", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Guts (6.2)
    "99aafe96-1645-44cd-99bd-979bc6ef37c5": BrushMapping(
        name="Guts", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Fire2 (6.3)
    "53d753ef-083c-45e1-98e7-4459b4471219": BrushMapping(
        name="Fire2", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=False, use_emission=True, emission_strength=3.0, is_animated=True, is_audio_reactive=True, is_experimental=True),
    
    # Tube Toon Inverted (6.4)
    "9871385a-df73-4396-9e33-31e4e4930b27": BrushMapping(
        name="TubeToonInverted", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=False, is_experimental=True),
    
    # Dot Marker (6.5)
    "d1d991f2-e7a0-4cf1-b328-f57e915e6260": BrushMapping(
        name="DotMarker", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=False, is_experimental=True),
    
    # Faceted Tube (6.6)
    "4391ffaa-df73-4396-9e33-31e4e4930b27": BrushMapping(
        name="FacetedTube", corner_type='SHARP', cap_mode='FLAT', radius_scale=0.8, use_pressure=False, is_experimental=True),
    
    # Tapered Marker Flat (6.7)
    "1a26b8c0-8a07-4f8a-9fac-d2ef36e0cad0": BrushMapping(
        name="TaperedMarkerFlat", corner_type='FLAT', cap_mode='FLAT', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Plasma (6.8)
    "c33714d1-b2f9-412e-bd50-1884c9d46336": BrushMapping(
        name="Plasma", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=False, use_emission=True, emission_strength=2.5, is_animated=True, is_audio_reactive=True, is_experimental=True),
    
    # Waveform Particles (6.9)
    "6a1cf9f9-032c-45ec-9b6e-a6680bee30f7": BrushMapping(
        name="WaveformParticles", corner_type='ROUND', cap_mode='ROUND', radius_scale=0.8, use_pressure=False, is_animated=True, is_audio_reactive=True, is_experimental=True),
    
    # Bubble Wand (6.10)
    "eba3f993-f9a1-4d35-b84e-bb08f48981a4": BrushMapping(
        name="BubbleWand", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_animated=True, is_experimental=True),
    
    # Dance Floor (6.11)
    "6a1cf9f9-032c-45ec-311e-a6680bee32e9": BrushMapping(
        name="DanceFloor", corner_type='SHARP', cap_mode='FLAT', radius_scale=1.0, use_pressure=False, is_animated=True, is_audio_reactive=True, is_experimental=True),
    
    # Waveform Tube (6.12)
    "0f5820df-cb6b-4a6c-960e-56e4c8000eda": BrushMapping(
        name="WaveformTube", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=False, is_animated=True, is_audio_reactive=True, is_experimental=True),
    
    # Drafting (7.1)
    "492b36ff-b337-436a-ba5f-1e87ee86747e": BrushMapping(
        name="Drafting", corner_type='SHARP', cap_mode='FLAT', radius_scale=0.8, use_pressure=True, is_experimental=True),
    
    # Single Sided (7.2)
    "f0a2298a-be80-432c-9fee-a86dcc06f4f9": BrushMapping(
        name="SingleSided", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Double Flat (7.3)
    "f4a0550c-332a-4e1a-9793-b71508f4a454": BrushMapping(
        name="DoubleFlat", corner_type='FLAT', cap_mode='FLAT', radius_scale=1.2, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Tube (Highlighter) (7.4)
    "c1c9b26d-673a-4dc6-b373-51715654ab96": BrushMapping(
        name="TubeAdditive", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.5, use_pressure=False, opacity_scale=0.6, is_experimental=True),
    
    # Feather (7.5)
    "a555b809-2017-46cb-ac26-e63173d8f45e": BrushMapping(
        name="Feather", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_audio_reactive=True, is_experimental=True),
    
    # Duct Tape (Geometry) (7.6)
    "84d5bbb2-6634-8434-f8a7-681b576b4664": BrushMapping(
        name="DuctTapeGeometry", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.2, use_pressure=True, is_lit=True, is_experimental=True),
    
    # TaperedHueShift (7.7)
    "3d9755da-56c7-7294-9b1d-5ec349975f52": BrushMapping(
        name="TaperedHueShift", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_audio_reactive=True, is_experimental=True),
    
    # Lacewing (7.8)
    "1cf94f63-f57a-4a1a-ad14-295af4f5ab5c": BrushMapping(
        name="Lacewing", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_animated=True, is_audio_reactive=True, is_experimental=True),
    
    # Marbled Rainbow (7.9)
    "c86c058d-1bda-2e94-08db-f3d6a96ac4a1": BrushMapping(
        name="MarbledRainbow", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_audio_reactive=True, is_experimental=True),
    
    # Charcoal (7.10)
    "fde6e778-0f7a-e584-38d6-89d44cee59f6": BrushMapping(
        name="Charcoal", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Keijiro Tube (7.11)
    "f8ba3d18-01fc-4d7b-b2d9-b99d10b8e7cf": BrushMapping(
        name="KeijiroTube", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_animated=True, is_experimental=True),
    
    # Lofted (Hue Shift) (7.12)
    "c5da2e70-a6e4-63a4-898c-5cfedef09c97": BrushMapping(
        name="LoftedHueShift", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_audio_reactive=True, is_experimental=True),
    
    # Wire (Lit) (8.1)
    "62fef968-e842-3224-4a0e-1fdb7cfb745c": BrushMapping(
        name="LitWire", corner_type='SHARP', cap_mode='FLAT', radius_scale=0.5, use_pressure=False, is_lit=True, is_experimental=True),
    
    # Waveform FFT (8.2)
    "d120944d-772f-4062-99c6-46a6f219eeaf": BrushMapping(
        name="WaveformFFT", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=False, is_animated=True, is_audio_reactive=True, is_experimental=True),
    
    # Fairy (8.3)
    "d9cc5e99-ace1-4d12-96e0-4a7c18c99cfc": BrushMapping(
        name="Fairy", corner_type='ROUND', cap_mode='ROUND', radius_scale=0.8, use_pressure=False, is_animated=True, is_audio_reactive=True, is_experimental=True),
    
    # Space (8.4)
    "bdf65db2-1fb7-4202-b5e0-c6b5e3ea851e": BrushMapping(
        name="Space", corner_type='ROUND', cap_mode='ROUND', radius_scale=0.8, use_pressure=False, is_animated=True, is_audio_reactive=True, is_experimental=True),
    
    # Smooth Hull (8.5)
    "355b3579-bf1d-4ff5-a200-704437fe684b": BrushMapping(
        name="SmoothHull", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Leaves2 (8.6)
    "7259cce5-41c1-ec74-c885-78af28a31d95": BrushMapping(
        name="Leaves2", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Ink (Geometry) (8.7)
    "7c972c27-d3c2-8af4-7bf8-5d9db8f0b7bb": BrushMapping(
        name="InkGeometry", corner_type='SHARP', cap_mode='FLAT', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Concave Hull (8.8)
    "7ae1f880-a517-44a0-99f9-1cab654498c6": BrushMapping(
        name="ConcaveHull", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # 3D Printing Brush (8.9)
    "d3f3b18a-da03-f694-b838-28ba8e749a98": BrushMapping(
        name="3D Printing Brush", corner_type='SHARP', cap_mode='FLAT', radius_scale=1.0, use_pressure=True, is_lit=True, is_experimental=True),
    
    # Leaves (standard)
    "ea19de07-d0c0-4484-9198-18489a3c1487": BrushMapping(
        name="Leaves", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True),
    "4a76a27a-44d8-4bfe-9a8c-713749a499b0": BrushMapping(
        name="Leaves", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True, is_lit=True),
    
    # Taffy
    "0077f88c-d93a-42f3-b59b-b31c50cdb414": BrushMapping(
        name="Taffy", corner_type='ROUND', cap_mode='ROUND', radius_scale=1.0, use_pressure=True),
}


def get_brush_mapping(brush_guid: Optional[str]) -> BrushMapping:
    """
    Get the brush mapping for a given Open Brush brush GUID.
    Returns a default mapping if the GUID is not found.
    """
    if brush_guid and brush_guid in BRUSH_MAPPINGS:
        return BRUSH_MAPPINGS[brush_guid]
    
    # Default fallback mapping
    return BrushMapping(
        name="Default",
        corner_type='ROUND',
        cap_mode='ROUND',
        radius_scale=1.0,
        use_pressure=True,
    )


def get_all_brush_names():
    """Get a list of all unique brush names."""
    return sorted(set(mapping.name for mapping in BRUSH_MAPPINGS.values()))


def get_brushes_by_property(is_lit=None, is_animated=None, is_audio_reactive=None, is_experimental=None):
    """Filter brushes by their properties."""
    results = []
    for guid, mapping in BRUSH_MAPPINGS.items():
        if is_lit is not None and mapping.is_lit != is_lit:
            continue
        if is_animated is not None and mapping.is_animated != is_animated:
            continue
        if is_audio_reactive is not None and mapping.is_audio_reactive != is_audio_reactive:
            continue
        if is_experimental is not None and mapping.is_experimental != is_experimental:
            continue
        results.append((guid, mapping))
    return results
