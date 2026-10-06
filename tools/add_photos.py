#!/usr/bin/python3
"""Takes the photos you dropped into gallery/inbox/, removes hidden location data, shrinks them,
names them with a date and caption, moves them into a gallery chapter, and rebuilds the gallery page."""
import datetime, os, re, shutil, subprocess, sys
from PIL import Image, ImageOps
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
inbox = os.path.join(root, "gallery", "inbox")
photos_dir = os.path.join(root, "gallery", "photos")
files = sorted(f for f in os.listdir(inbox) if f.lower().endswith((".jpg", ".jpeg", ".png", ".heic", ".webp")))
if not files:
    sys.exit("The folder gallery/inbox is empty. Drop your photos in there first, then run this again.")
chapters = sorted(d for d in os.listdir(photos_dir) if os.path.isdir(os.path.join(photos_dir, d)))
print("Chapters:")
for i, c in enumerate(chapters, 1):
    print(f"  {i}. {c}")
print(f"  {len(chapters)+1}. make a new chapter")
choice = input("Which chapter number? ").strip()
if choice == str(len(chapters) + 1):
    name = input("New chapter folder name, e.g. 3-netherlands: ").strip()
    title = input("Chapter heading, e.g. 'Netherlands, 2027': ").strip()
    chapter = os.path.join(photos_dir, name); os.makedirs(chapter, exist_ok=True)
    open(os.path.join(chapter, "title.txt"), "w").write(title + "\n")
    open(os.path.join(chapter, "beats.txt"), "w").write("# One short line per month:  YYYY-MM | text\n")
else:
    chapter = os.path.join(photos_dir, chapters[int(choice) - 1])
for f in files:
    src = os.path.join(inbox, f)
    tmp = os.path.join(inbox, "_tmp.png")
    subprocess.run(["sips", "-s", "format", "png", src, "--out", tmp], check=True, capture_output=True)
    im = ImageOps.exif_transpose(Image.open(tmp)).convert("RGB")
    # date: from the photo's own data if present, otherwise ask
    date = None
    try:
        raw = Image.open(src).getexif().get(36867) or Image.open(src).getexif().get(306)
        if raw: date = raw[:10].replace(":", "-")
    except Exception:
        pass
    print(f"\nPhoto: {f}")
    d = input(f"  Date (YYYY-MM or YYYY-MM-DD) [{date or 'unknown'}]: ").strip() or date
    if not d or not re.match(r"^\d{4}-\d{2}(-\d{2})?$", d):
        print("  Skipped: a date like 2026-07 or 2026-07-04 is needed."); os.remove(tmp); continue
    caption = input("  Caption (plain words): ").strip()
    if not caption:
        print("  Skipped: a caption is needed."); os.remove(tmp); continue
    slug = re.sub(r"[^a-z0-9]+", "-", caption.lower()).strip("-")
    im.thumbnail((1600, 1600))
    dst = os.path.join(chapter, f"{d}-{slug}.jpg")
    im.save(dst, "JPEG", quality=84, optimize=True)   # saved without EXIF: no location, no device info
    os.remove(tmp); os.remove(src)
    print(f"  Added: {os.path.relpath(dst, root)}")
subprocess.run(["python3", os.path.join(root, "gallery", "make_gallery.py")], check=True)
print("\nGallery page rebuilt. Now preview (1) and publish (4).")
