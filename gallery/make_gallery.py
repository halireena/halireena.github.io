"""Builds gallery/index.qmd as a story, one chapter per folder in gallery/photos/.

How to use
1. Each chapter is a folder in gallery/photos/, numbered for order (1-colombo, 2-dubai, ...).
   Put its heading in title.txt, e.g.  Dubai, 2025–2026 · From plants to pixels
2. Add photos named as their captions, starting with the date, e.g.
       2026-07-bioconnect-sprint-team.jpg   ->  "Bioconnect sprint team. July 2026"
3. Story text goes in beats.txt, one line per beat:   2026-07 | what happened that month
   Each beat appears just before that month's photos.
4. Run from the website folder:   python3 gallery/make_gallery.py
5. Remove location data from phone photos before adding them (see HOW_TO_EDIT.md).
"""
import calendar, re
from pathlib import Path

here = Path(__file__).resolve().parent
FIX = {"nft": "NFT", "msc": "MSc", "bsc": "BSc", "birmingham": "Birmingham", "dubai": "Dubai",
       "university": "University", "jenway": "Jenway", "colombo": "Colombo", "sharjah": "Sharjah"}

def month_label(ym):
    y, m = ym.split("-")
    return f"{calendar.month_name[int(m)]} {y}"

def caption(p):
    m = re.match(r"^(\d{4}-\d{2})(?:-\d{2})?[-_ ]*(.*)$", p.stem)
    text = (m.group(2) if m else p.stem).replace("-", " ").replace("_", " ").strip()
    for a, b in FIX.items():
        text = re.sub(rf"\b{a}\b", b, text, flags=re.I)
    return text[:1].upper() + text[1:]

lines = ["---", 'title: "Gallery"', 'subtitle: "Two chapters, two countries: from growing plants to analysing them with data"',
         "toc: true", "toc-depth: 2", "lightbox: true", "---", ""]
for chapter in sorted(d for d in (here / "photos").iterdir() if d.is_dir()):
    title = (chapter / "title.txt").read_text().strip() if (chapter / "title.txt").exists() else chapter.name
    beats = {}
    if (chapter / "beats.txt").exists():
        for raw in (chapter / "beats.txt").read_text().splitlines():
            if "|" in raw and not raw.lstrip().startswith("#"):
                ym, text = raw.split("|", 1); beats[ym.strip()] = text.strip()
    photos = {}
    for p in sorted(chapter.iterdir()):
        if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}:
            photos.setdefault(p.stem[:7] if re.match(r"\d{4}-\d{2}", p.stem) else "9999-99", []).append(p)
    lines += [f"## {title}", ""]
    for ym in sorted(set(beats) | set(photos)):
        if ym in beats:
            lines += ["::: {.beat}", f"[{month_label(ym)}]{{.beat-when}}", "", beats[ym], ":::", ""]
        if ym in photos:
            lines.append("::: {.photo-grid}")
            for p in photos[ym]:
                lines += [f'![{caption(p)}](photos/{chapter.name}/{p.name}){{group="{chapter.name}"}}', ""]
            lines += [":::", ""]
(here / "index.qmd").write_text("\n".join(lines) + "\n")
print("Gallery story written.")
