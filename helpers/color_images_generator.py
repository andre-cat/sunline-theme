from pathlib import Path
from PIL import Image

COLORS = {
    # Syntax - Primary
    "black": "#000000",
    "blue": "#007AFF",
    "blue-dark": "#0055B3",
    "blue-denim": "#5085B0",
    "blue-light": "#5A9FD4",
    "orange": "#E67300",
    "teal": "#048A81",
    "teal-blue": "#51A3A3",
    "teal-gray": "#5A8A85",
    "green-grass": "#4CB944",
    
    # UI - Blues
    "blue-inactive": "#66B3FF",
    "blue-pale": "#E3ECFF",
    "blue-selection": "#D6E4FF",
    
    # UI - Status
    "red": "#D93526",
    "green": "#32A852",
    
    # Tropical - Greens (brackets)
    "teal-green": "#0A8A6E",
    "teal-green-light": "#4A9E7E",
    "teal-green-gray": "#5A8A70",
    
    # Tropical - Yellows/Sand (brackets & highlights)
    "yellow-gold": "#D9B835",
    "yellow-mustard": "#CCAD42",
    "yellow-sand": "#B5A044",
    "yellow-honey": "#E6BE38",
    "yellow-highlight": "#E8D888",
    
    # Tropical - Sand backgrounds
    "sand-warm": "#FCECC9",
    "sand-cream": "#EBEBD3",
    
    # Utility
    "gray": "#6c6c70",
    "gray-blue": "#8e8e93",
}

SIZE = (16, 16)

OUTPUT_DIR = Path("./images/colors")


def hex_to_rgb(hex_color: str) -> "tuple":
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def generate_color_png(name: str, hex_color: str):
    rgb = hex_to_rgb(hex_color)
    image = Image.new("RGB", SIZE, rgb)

    output_path = OUTPUT_DIR / f"{name}.png"
    image.save(output_path, "PNG")

    print(f"Saved: {output_path.as_posix()}")


OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for name, hex_color in COLORS.items():
    generate_color_png(name, hex_color)

print("Done!")