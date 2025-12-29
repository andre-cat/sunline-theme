from PIL import Image
from pathlib import Path
import numpy as np


def apply_alpha(input_path: "Path", output_path: "Path", sunline: int, power: float):
    img = Image.open(str(input_path)).convert("RGBA")
    width, height = img.size
    alpha = np.zeros((height, width), dtype=np.uint8)

    for y in range(height):
        if y < sunline:
            t = y / sunline
            t_adjusted = t**power
            ease = (1 - np.cos(t_adjusted * np.pi)) / 2
            alpha[y, :] = int(255 * ease)
        else:
            t = (y - sunline) / (height - sunline)
            t_adjusted = 1 - ((1 - t) ** power)
            ease = (1 + np.cos(t_adjusted * np.pi)) / 2
            alpha[y, :] = int(255 * ease)

    img_array = np.array(img)
    img_array[:, :, 3] = alpha

    result = Image.fromarray(img_array, "RGBA")
    result.save(str(output_path))

    print(f"Saved: {output_path.as_posix()}")


input_folder_path = Path("./drafts")
input_folder_path.mkdir(parents=True, exist_ok=True)

output_folder_path = Path("./images/banners")
output_folder_path.mkdir(parents=True, exist_ok=True)

apply_alpha(input_folder_path / "banner-top-draft.png", output_folder_path / "banner-top-copy.png", 650, 0.70)
apply_alpha(input_folder_path / "banner-footer-draft.png", output_folder_path / "banner-footer-copy.png", 650, 0.70)

print("Done!")

"""
POWER = 0.3  →  ░░████████████░░  (extremely opaque)
POWER = 0.5  →  ░░░██████████░░░  (high opacity)
POWER = 1.0  →  ░░░░░██████░░░░░  (normal)
POWER = 2.0  →  ░░░░░░░██░░░░░░░  (low opacity)
"""
