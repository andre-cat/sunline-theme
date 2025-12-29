from pathlib import Path
import cairosvg

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600" width="1200" height="600">
  <defs>
    <!-- Clip to show only half of the sun -->
    <clipPath id="sunClip">
      <rect x="0" y="0" width="1200" height="378"/>
    </clipPath>
  </defs>

  <!-- White background (sand below) -->
  <rect width="1200" height="600" fill="#FFFFFF"/>
  
  <!-- Sky - solid blue -->
  <rect width="1200" height="374" fill="#BBE5ED"/>
  
  <!-- Sun - half circle on sunline (clipped) -->
  <circle cx="599" cy="380" r="78" fill="#E67300" clip-path="url(#sunClip)"/>
  
  <!-- Sea sunline line -->
  <rect x="180" y="370" width="839" height="8" fill="#007AFF"/>
  
  <!-- Sand beach -->
  <ellipse cx="599" cy="428" rx="179" ry="34" fill="#F4F1BB"/>
</svg>"""

folder_path = Path("./drafts")
folder_path.mkdir(parents=True, exist_ok=True)

file_path = folder_path / "banner-top-draft.png"

cairosvg.svg2png(bytestring=svg_content.encode(), write_to=str(file_path), output_width=2048, output_height=1024)

print(f"Saved: {file_path.as_posix()}")
print("Done!")
