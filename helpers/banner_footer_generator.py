from pathlib import Path
import cairosvg

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600" width="1200" height="600">
  <!-- White background (sand below) -->
  <rect width="1200" height="600" fill="#FFFFFF"/>
  
  <!-- Sky - solid warm cream color -->
  <rect width="1200" height="336" fill="#BBE5ED"/>
  
  <!-- Sand sunline line -->
  <rect x="150" y="328" width="900" height="8" fill="#FFFFC7"/>

  <!-- Sand beach -->
  <ellipse cx="600" cy="410" rx="180" ry="40" fill="#F4F1BB"/>
  
  <!-- Palm 1 - far left, leaning outward, centered on ellipse -->
  <g opacity="0.75">
    <path d="M360 410 Q330 375 300 325" stroke="#5A8A85" stroke-width="4" fill="none" stroke-linecap="round"/>
    <g transform="translate(300, 325)">
      <path d="M0 0 Q-35 -12 -60 5" stroke="#048A81" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-38 8 -58 35" stroke="#4CB944" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-28 25 -40 55" stroke="#5A8A85" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q30 -18 58 -8" stroke="#048A81" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q40 5 62 30" stroke="#4CB944" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q30 22 42 50" stroke="#5A8A85" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    </g>
  </g>
  
  <!-- Palm 2 - center left, leaning left - 10 leafs (left) -->
  <g opacity="0.95">
    <path d="M540 390 Q510 340 480 270" stroke="#5A8A85" stroke-width="5" fill="none" stroke-linecap="round"/>
    <g transform="translate(480, 270)">
      <!-- Top leaf curved to the right -->
      <path d="M0 0 Q15 -45 55 -35" stroke="#048A81" stroke-width="2" fill="none" stroke-linecap="round"/>
      <!-- Top leaf curved to the left -->
      <path d="M0 0 Q-20 -45 -60 -30" stroke="#4CB944" stroke-width="2" fill="none" stroke-linecap="round"/>
      <!-- Left side - from top to bottom -->
      <path d="M0 0 Q-50 -25 -90 -5" stroke="#048A81" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-58 5 -100 35" stroke="#4CB944" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-50 30 -78 65" stroke="#048A81" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-35 45 -50 88" stroke="#5A8A85" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <!-- Right side - from top to bottom -->
      <path d="M0 0 Q50 -25 90 -5" stroke="#4CB944" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q58 5 100 35" stroke="#048A81" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q50 30 78 65" stroke="#4CB944" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q35 45 50 88" stroke="#048A81" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    </g>
  </g>
  
  <!-- Palm 3 - center right, leaning right - 10 leafs (right) -->
  <g opacity="0.95">
    <path d="M660 390 Q690 340 720 270" stroke="#5A8A85" stroke-width="5" fill="none" stroke-linecap="round"/>
    <g transform="translate(720, 270)">
      <!-- Top leaf curved to the left -->
      <path d="M0 0 Q-15 -45 -55 -35" stroke="#048A81" stroke-width="2" fill="none" stroke-linecap="round"/>
      <!-- Top leaf curved to the right -->
      <path d="M0 0 Q20 -45 60 -30" stroke="#4CB944" stroke-width="2" fill="none" stroke-linecap="round"/>
      <!-- Right side - from top to bottom -->
      <path d="M0 0 Q50 -25 90 -5" stroke="#048A81" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q58 5 100 35" stroke="#4CB944" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q50 30 78 65" stroke="#048A81" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q35 45 50 88" stroke="#5A8A85" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <!-- Left side - from top to bottom -->
      <path d="M0 0 Q-50 -25 -90 -5" stroke="#4CB944" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-58 5 -100 35" stroke="#048A81" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-50 30 -78 65" stroke="#4CB944" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-35 45 -50 88" stroke="#048A81" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    </g>
  </g>
  
  <!-- Palm 4 - far right, leaning outward (mirror of Palm 1), centered on ellipse -->
  <g opacity="0.75">
    <path d="M840 410 Q870 375 900 325" stroke="#5A8A85" stroke-width="4" fill="none" stroke-linecap="round"/>
    <g transform="translate(900, 325)">
      <path d="M0 0 Q35 -12 60 5" stroke="#048A81" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q38 8 58 35" stroke="#4CB944" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q28 25 40 55" stroke="#5A8A85" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-30 -18 -58 -8" stroke="#048A81" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-40 5 -62 30" stroke="#4CB944" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      <path d="M0 0 Q-30 22 -42 50" stroke="#5A8A85" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    </g>
  </g>
</svg>"""

folder_path = Path("./drafts")
folder_path.mkdir(parents=True, exist_ok=True)

file_path = folder_path / "banner-footer-draft.png"

cairosvg.svg2png(bytestring=svg_content.encode(), write_to=str(file_path), output_width=2048, output_height=1024)

print(f"Saved: {file_path.as_posix()}")
print("Done!")
