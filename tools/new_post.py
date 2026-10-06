#!/usr/bin/python3
"""Creates a new blog post folder from the template and opens it for you."""
import datetime, os, re, shutil, subprocess, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
title = input("Title of the post: ").strip()
if not title:
    sys.exit("No title given, nothing created.")
slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:50]
today = datetime.date.today().isoformat()
dest = os.path.join(root, "blog", f"{today}-{slug}")
if os.path.exists(dest):
    sys.exit(f"A post folder already exists: {dest}")
shutil.copytree(os.path.join(root, "_templates", "blog-post-template"), dest)
qmd = os.path.join(dest, "index.qmd")
s = open(qmd).read().replace('title: "My post title"', f'title: "{title}"').replace("date: 2026-10-03", f"date: {today}")
open(qmd, "w").write(s)
print(f"\nCreated: blog/{today}-{slug}/index.qmd")
print("Write your post in that file (opening the folder in Finder now).")
print("When you are done: double-click '1 Preview website.command' to check it, then '4 Publish.command'.")
subprocess.run(["open", "-R", qmd])
