from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter


def rounded_rect_mask(size, radius):
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, size[0], size[1]], radius=radius, fill=255)
    return mask

def rounded_corners(image, radius):
    mask = rounded_rect_mask(image.size, radius)
    rounded = Image.new("RGBA", image.size, (0, 0, 0, 0))
    rounded.paste(image, (0, 0), mask)
    return rounded


def add_outer_padding(image, padding_left, padding_top, padding_right, padding_bottom, color=(255, 255, 255, 255)):
    image = image.convert("RGBA")
    new_width = image.width + padding_left + padding_right
    new_height = image.height + padding_top + padding_bottom

    canvas = Image.new("RGBA", (new_width, new_height), color)
    canvas.paste(image, (padding_left, padding_top), image)
    return canvas


def add_shadow_rounded(base_size, radius, offsets, blurs, colors, canvas_size, base_pos):
    shadow = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    card_mask = rounded_rect_mask(base_size, radius)

    for (dx, dy), blur, color in zip(offsets, blurs, colors):
        temp = Image.new("RGBA", canvas_size, (0, 0, 0, 0))

        solid = Image.new("RGBA", base_size, color)
        temp.paste(solid, (base_pos[0] + dx, base_pos[1] + dy), card_mask)

        temp = temp.filter(ImageFilter.GaussianBlur(blur))
        shadow = Image.alpha_composite(shadow, temp)

    return shadow


def apply_style(input_path: Path, output_path: Path):
    image = Image.open(input_path).convert("RGBA")

    image = add_outer_padding(image, padding_left=24, padding_top=48, padding_right=48, padding_bottom=48, color=(255, 255, 255, 255))

    em = 16
    padding = em
    border_radius = 12
    background_color = (204, 204, 204, 0)  # #cccccc00

    offsets = [(0, 2)]
    blurs = [10]
    colors = [(0, 0, 0, int(255 * 0.12))]
    
    image = rounded_corners(image, border_radius)

    padded_size = (image.width + padding * 2, image.height + padding * 2)
    padded = Image.new("RGBA", padded_size, (0, 0, 0, 0))
    padded.paste(image, (padding, padding), image)

    canvas_width = padded.width + 32
    canvas_height = padded.height + 32
    canvas_size = (canvas_width, canvas_height)

    background = Image.new("RGBA", canvas_size, background_color)

    x = (canvas_width - padded.width) // 2
    y = (canvas_height - padded.height) // 2

    shadow = add_shadow_rounded(base_size=padded.size, radius=border_radius + padding, offsets=offsets, blurs=blurs, colors=colors, canvas_size=canvas_size, base_pos=(x, y))

    result = Image.alpha_composite(background, shadow)
    result.paste(padded, (x, y), padded)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.save(output_path)
    print(f"Saved: {output_path.as_posix()}")

apply_style(Path("./drafts/python-draft.png"), Path("./images/code/python-copy.png"))
apply_style(Path("./drafts/javascript-draft.png"), Path("./images/code/javascript-copy.png"))
apply_style(Path("./drafts/html-draft.png"), Path("./images/code/html-copy.png"))
apply_style(Path("./drafts/css-draft.png"), Path("./images/code/css-copy.png"))