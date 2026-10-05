"""Builds gallery/index.qmd from the photo albums in gallery/photos/.

How to use
1. Each album is a folder inside gallery/photos/, named with a number for its order and its
   title, e.g.  1-msc-journey   2-bsc-journey   3-conferences
2. Put photos (jpg, jpeg, png, webp) in the album folder. Name each file as its caption, with
   hyphens for spaces, starting with the date, e.g.  2024-06-hydroponics-setup.jpg
   The date is used for ordering and shown as "June 2024".
3. Optional: an album can have an intro.txt with one or two sentences shown under its title.
4. Run from the website folder:   python3 gallery/make_gallery.py
5. Remove location data from phone photos before adding them (the site guide explains how).
"""
import calendar, re
from pathlib import Path

here = Path(__file__).resolve().parent
ALBUM_TITLES = {"msc": "MSc", "bsc": "BSc"}

def album_title(folder):
    words = re.sub(r"^\d+[-_ ]*", "", folder.name).split("-")
    return " ".join(ALBUM_TITLES.get(w, w) for w in words).capitalize().replace("Msc", "MSc").replace("Bsc", "BSc")

def caption(p):
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-\d{2})?[-_ ]*(.*)$", p.stem)
    when, text = "", p.stem
    if m:
        year, month, text = m.groups()
        when = f"{calendar.month_name[int(month)]} {year}" if month else year
    text = text.replace("-", " ").replace("_", " ").strip()
    text = text[:1].upper() + text[1:]
    for a, b in {"nft": "NFT", "msc": "MSc", "bsc": "BSc", "Msc": "MSc", "Bsc": "BSc", "birmingham": "Birmingham", "dubai": "Dubai", "university": "University"}.items():
        text = re.sub(rf"\b{a}\b", b, text)
    return f"{text}. *{when}*" if when else text

lines = ["---", 'title: "Gallery"', 'subtitle: "Moments from the lab, the field and the lecture theatre"',
         "toc: true", "lightbox: true", "---", ""]
albums = sorted(d for d in (here / "photos").iterdir() if d.is_dir())
total = 0
for album in albums:
    photos = sorted((p for p in album.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}), reverse=True)
    if not photos:
        continue
    total += len(photos)
    lines += [f"## {album_title(album)}", ""]
    intro = album / "intro.txt"
    if intro.exists():
        lines += [intro.read_text().strip(), ""]
    lines.append("::: {.photo-grid}")
    for p in photos:
        lines += [f'![{caption(p)}](photos/{album.name}/{p.name}){{group="{album.name}"}}', ""]
    lines += [":::", ""]
if total == 0:
    lines.append("Photos coming soon.")
(here / "index.qmd").write_text("\n".join(lines) + "\n")
print(f"Gallery written: {len(albums)} album(s), {total} photo(s).")
