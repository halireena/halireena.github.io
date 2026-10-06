#!/usr/bin/python3
"""Creates a new project page folder from the template."""
import datetime, os, re, shutil, subprocess, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
title = input("Title of the project: ").strip()
if not title:
    sys.exit("No title given, nothing created.")
slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:50]
dest = os.path.join(root, "projects", slug)
if os.path.exists(dest):
    sys.exit(f"A project folder already exists: {dest}")
shutil.copytree(os.path.join(root, "_templates", "project-template"), dest)
qmd = os.path.join(dest, "index.qmd")
s = open(qmd).read().replace('title: "Do warmer days sell more ice cream?"', f'title: "{title}"').replace("date: 2026-10-03", f"date: {datetime.date.today().isoformat()}")
open(qmd, "w").write(s)
print(f"\nCreated: projects/{slug}/index.qmd  (opening the folder in Finder now)")
print("Fill in each section, put your figures in the same folder, then preview and publish.")
subprocess.run(["open", "-R", qmd])
