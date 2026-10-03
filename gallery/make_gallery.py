"""Builds gallery/index.qmd from the pictures in gallery/photos/.

How to use
1. Copy your photos into gallery/photos/  (jpg, jpeg, png, webp)
2. Name each file as the caption you want, with hyphens for spaces, e.g.
       2024-06-hydroponics-setup-at-northumbria.jpg
   A leading date like 2024-06- is removed from the caption and used for ordering.
3. Run from the website folder:   python3 gallery/make_gallery.py
4. Preview or push as usual.
"""
import re
from pathlib import Path

here = Path(__file__).resolve().parent
photos = sorted(p for p in (here / "photos").iterdir()
                if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"})

def caption(p):
    name = p.stem
    name = re.sub(r"^\d{4}(-\d{2}){0,2}[-_ ]*", "", name)  # drop a leading date
    name = name.replace("-", " ").replace("_", " ").strip()
    return name[:1].upper() + name[1:] if name else ""

lines = ["---", 'title: "Gallery"', 'subtitle: "Moments from the lab, the field and the classroom"',
         "toc: false", "lightbox: true", "---", ""]
if not photos:
    lines.append("Photos coming soon.")
else:
    lines.append("::: {.photo-grid}")
    for p in reversed(photos):  # newest first when files start with a date
        lines.append(f"![{caption(p)}](photos/{p.name}){{group=\"gallery\"}}")
        lines.append("")
    lines.append(":::")
(here / "index.qmd").write_text("\n".join(lines) + "\n")
print(f"Gallery written with {len(photos)} photo(s).")
