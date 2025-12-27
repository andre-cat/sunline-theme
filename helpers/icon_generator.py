from pathlib import Path
import cairosvg


def build_svg(size: int = 1024) -> str:
    W = H = size

    # Colors
    sky = "#BBE5ED"
    white = "#FFFFFF"
    sun = "#E67300"
    line_blue = "#007AFF"
    line_blue_shadow = "#007AFF"
    reflection = "#F4F1BB"

    # Fixed background split (sky / sand)
    horizon_y = 512

    # Offset for sun + blue line ONLY
    offset_y = 56
    sun_line_y = horizon_y + offset_y

    # Sun
    sun_r = 184
    sun_cx = W / 2
    sun_cy = sun_line_y

    # Blue line
    line_w = 648
    line_h = 24
    line_x = (W - line_w) / 2
    line_y = sun_line_y
    shadow_h = 8

    # Reflection
    ell_cx = W / 2
    ell_cy = line_y + 84
    ell_rx = 252
    ell_ry = 40

    svg = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
        <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{W}\" height=\"{H}\" viewBox=\"0 0 {W} {H}\">
            <!-- Background -->
            <rect x=\"0\" y=\"0\" width=\"{W}\" height=\"{horizon_y}\" fill=\"{sky}\"/>
            <rect x=\"0\" y=\"{horizon_y}\" width=\"{W}\" height=\"{H - horizon_y}\" fill=\"{white}\"/>

            <!-- Sun clipped at blue line level -->
            <defs>
                <clipPath id=\"clipSunTop\" clipPathUnits=\"userSpaceOnUse\">
                <rect x=\"0\" y=\"0\" width=\"{W}\" height=\"{sun_line_y}\"/>
                </clipPath>
            </defs>
            <g clip-path=\"url(#clipSunTop)\">
                <circle cx=\"{sun_cx}\" cy=\"{sun_cy}\" r=\"{sun_r}\" fill=\"{sun}\"/>
            </g>

            <!-- Blue line -->
            <rect x=\"{line_x}\" y=\"{line_y}\" width=\"{line_w}\" height=\"{line_h}\" fill=\"{line_blue}\"/>
            <rect x=\"{line_x}\" y=\"{line_y + line_h - shadow_h}\" width=\"{line_w}\" height=\"{shadow_h}\" fill=\"{line_blue_shadow}\"/>

            <!-- Reflection -->
            <ellipse cx=\"{ell_cx}\" cy=\"{ell_cy}\" rx=\"{ell_rx}\" ry=\"{ell_ry}\" fill=\"{reflection}\"/>
        </svg>
    """
    return svg


svg_text = build_svg(1024)

folder_path = Path("./drafts")
folder_path.mkdir(parents=True, exist_ok=True)

file_path = folder_path / "icon-draft.png"

cairosvg.svg2png(bytestring=svg_text.encode("utf-8"), write_to=str(file_path), output_width=128, output_height=128, background_color="white")

print(f"Saved: {file_path.as_posix()}")
print("Done!")
