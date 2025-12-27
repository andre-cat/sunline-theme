from pathlib import Path
from PIL import Image

COLORS = {
    "black": "#000000",
    "blue": "#007AFF",
    "blue-denim": "#5085B0",
    "blue-inactive": "#66B3FF",
    "blue-light": "#5A9FD4",
    "blue-pale": "#E3ECFF",
    "gray": "#6c6c70",
    "gray-blue": "#8e8e93",
    "green": "#32A852",
    "green-grass": "#4CB944",
    "orange": "#E67300",
    "red": "#D93526",
    "teal": "#048A81",
    "teal-blue": "#51A3A3",
    "teal-gray": "#5A8A85",
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
