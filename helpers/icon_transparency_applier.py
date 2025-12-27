from pathlib import Path
from PIL import Image


def add_transparent_corners(input_png: "str | Path", output_png: "str | Path", corner_size: int = 16) -> None:
    """
    Sets 4 corner squares to alpha=0 on a PNG.
    corner_size is in pixels (e.g., 16 for a 128x128 icon).
    """
    input_png = Path(input_png)
    output_png = Path(output_png)

    img = Image.open(input_png).convert("RGBA")
    w, h = img.size

    if corner_size <= 0 or corner_size * 2 > min(w, h):
        raise ValueError("corner_size inválido para el tamaño de la imagen.")

    px = img.load()

    # Helper: make a rectangle fully transparent
    def clear_rect(x0: int, y0: int, x1: int, y1: int) -> None:
        for y in range(y0, y1):
            for x in range(x0, x1):
                r, g, b, a = px[x, y]
                px[x, y] = (r, g, b, 0)

    # Top-left
    clear_rect(0, 0, corner_size, corner_size)
    # Top-right
    clear_rect(w - corner_size, 0, w, corner_size)
    # Bottom-left
    clear_rect(0, h - corner_size, corner_size, h)
    # Bottom-right
    clear_rect(w - corner_size, h - corner_size, w, h)

    img.save(output_png, format="PNG")


input_path = "drafts/icon-draft.png"
output_path = "icon-copy.png"

add_transparent_corners(input_path, output_path, corner_size=22)

print(f"Saved: {Path(output_path).as_posix()}")
