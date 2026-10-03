# How to edit this website

This is a [Quarto](https://quarto.org) website. You write pages in `.qmd`
files (Markdown with a small settings block at the top), and Quarto turns them
into a website. Every time you push to GitHub, a robot (a "GitHub Action")
rebuilds the site and publishes it at **https://halireena.github.io**.

---

## 0. One-time setup

### Install the tools
1. Install **Quarto**: <https://quarto.org/docs/get-started/> (download, double-click, install).
2. Install **Git**: <https://git-scm.com/downloads> (on a Mac it's usually already there).
3. A good editor helps: **VS Code** or **Positron** with the Quarto extension.
4. Check it worked — open a terminal and run:

   ```bash
   quarto check
   ```

### Put the site on GitHub
1. On GitHub, create a **new public repository named exactly `halireena.github.io`**.
   Don't tick "Add a README".
2. In a terminal, inside this folder, run these one at a time:

   ```bash
   git init -b main
   ```
   ```bash
   git add .
   ```
   ```bash
   git commit -m "First version of my website"
   ```
   ```bash
   git remote add origin https://github.com/halireena/halireena.github.io.git
   ```
   ```bash
   git push -u origin main
   ```
3. On GitHub, open the repository → **Settings → Pages**. Under
   **Build and deployment → Source**, choose **GitHub Actions**.
4. Open the **Actions** tab. You'll see "Publish website" running. When it
   shows a green tick (1–3 minutes), visit https://halireena.github.io.
   If the first run went red because Pages wasn't switched on yet, click the
   run → **Re-run all jobs**.

---

## 1. What's where

```
_quarto.yml              Site settings: title, menu bar
theme.scss               Colours, fonts and all the cute styling
index.qmd                Home page (short landing page)
about.qmd                About page: your story, journey, skills, interests
projects.qmd             Projects page – lists everything in projects/ automatically
projects/                One folder per project
blog.qmd                 Blog page – lists everything in blog/ automatically
blog/                    One folder per blog post
cv.qmd                   CV page (download button); put your PDF at cv/Halireena_Rushdiha_CV.pdf
contact.qmd              Contact form (needs a free Formspree ID, see section 7)
images/                  Pictures used across the site (e.g. the favicon)
_templates/              Templates to copy: project-template, blog-post-template (not published)
styles.css               Optional custom styling
.github/workflows/       The GitHub Action that publishes the site
```

Files and folders starting with `_` or `.` (like `_site/`, `.quarto/`) are
made by Quarto. Don't edit them; they're ignored by Git.

---

## 2. Preview the site on your computer

1. Open a terminal in this folder (the one containing `_quarto.yml`).
2. Run:

   ```bash
   quarto preview
   ```

3. Your browser opens the site. **Leave the terminal running.** Each time you
   save a `.qmd` file, the page in the browser updates by itself.
4. To stop the preview, click in the terminal and press **Ctrl + C**.

Always preview before you push — if the preview shows an error, GitHub
would hit the same error.

---

## 3. Add a project page

1. **Copy** the folder `_templates/project-template` into `projects/` and give
   the copy a short name with no spaces, e.g. `projects/house-prices`.
   (The folder name becomes the web address:
   `halireena.github.io/projects/house-prices/`.)
2. Open `projects/house-prices/index.qmd`.
3. Edit the settings block between the `---` lines at the top:

   ```yaml
   ---
   title: "Predicting house prices in Colombo"
   description: "One sentence that appears on the Projects page."
   date: 2026-11-01
   order: 5
   categories: [R, machine learning]
   image: fig1.png
   ---
   ```

   - `date` must be `YYYY-MM-DD`.
   - `order` sets the position on the Projects page: 1 is first. Change the
     numbers in the other projects if you want to reorder them.
   - `image` is the thumbnail on the Projects page. Use one of your figures,
     e.g. `image: fig1.png`.
4. Replace the text under each heading: **The question → The data → Methods →
   Results (2 figures) → What I learned → Code**.
5. Replace `fig1.png` and `fig2.png` with your own figures (see section 5),
   and change the GitHub link at the bottom to your project's repository.
6. Delete files you don't need (`data.csv`, `make_figures.py`) and remove them
   from the `resources:` line at the top (or delete that line).
7. Run `quarto preview`, click **Projects** — your new card should be there.

Tip: the boxes on the existing project pages (the research question, the
number tiles, the cards) are made with `::: {.question-box}` and similar
lines. Open `projects/potato-late-blight/index.qmd` to see them and copy what you like.

---

## 4. Add a blog post

1. **Copy** the folder `_templates/blog-post-template` into `blog/` and rename it to
   `blog/YYYY-MM-DD-short-title`, e.g. `blog/2026-11-15-my-first-kaggle`.
2. Open `index.qmd` inside it and update the top block:

   ```yaml
   ---
   title: "What I learned from my first Kaggle competition"
   description: "A one-line summary shown on the Blog page."
   date: 2026-11-15
   categories: [learning, kaggle]
   ---
   ```

3. Write your post below the second `---`. Markdown quick reference:

   | You type                 | You get              |
   |--------------------------|----------------------|
   | `## Heading`             | a section heading    |
   | `**bold**`, `*italic*`   | **bold**, *italic*   |
   | `[text](https://…)`      | a link               |
   | `- item`                 | a bullet point       |
   | `![caption](photo.jpg)`  | an image             |

4. **Drafts:** add `draft: true` to the top block and the post won't be
   published until you remove that line.
5. Preview, then publish (section 6).

---

## 5. Add an image

**Image for one page** (most common):

1. Put the file in the **same folder** as that page's `index.qmd`,
   e.g. `blog/2026-11-15-my-first-kaggle/leaderboard.png`.
2. In `index.qmd`, write:

   ```markdown
   ![My final position on the leaderboard](leaderboard.png)
   ```

   The text in `[ ]` becomes the caption.

**Image used across the site** (e.g. your photo): put it in `images/` and
refer to it from the page, e.g. `![My photo](images/me.jpg)` on a top-level page.
Your photo on the home page: save it as `images/me.jpg` (a square crop works best,
about 600×600 px). It appears automatically; if the file is missing, the space is hidden.

Optional extras:

```markdown
![Caption](photo.jpg){width=60%}                       <!-- make it smaller -->
![Caption](photo.jpg){fig-alt="Description for screen readers"}
![Caption](chart.png){#fig-chart}   …then write  @fig-chart  to refer to it as "Figure 1"
```

Tips: file names lowercase with no spaces (`my-chart.png`, not `My Chart.PNG`);
keep photos under ~1 MB.

---

## 5b. Add photos to the Gallery

1. Copy your photos into the `gallery/photos/` folder (jpg, png or webp).
2. Name each file as the caption you want, with hyphens instead of spaces, and
   start with a date so they sort newest first:
   `2024-06-hydroponics-setup-at-northumbria.jpg`
3. In a terminal in the website folder, run:

   ```bash
   python3 gallery/make_gallery.py
   ```

   This rewrites `gallery/index.qmd` with every photo in the folder. Clicking a
   photo on the site opens it full size.
4. Keep photos under about 1 MB each (export at ~1600 px wide). Only add photos
   you have permission to publish, especially ones with other people in them.

## 5c. Add a publication

Open `publications.qmd`, copy one of the existing `::: {.tl-item}` blocks and change
the year, title, authors and link.

## 6. Publish your changes

After previewing, in a terminal in this folder:

```bash
git add .
```
```bash
git commit -m "Add house prices project"
```
```bash
git push
```

Then watch the **Actions** tab on GitHub. Green tick = live in a minute or two.
(Your browser may cache the old page — refresh with Cmd + Shift + R.)

**Red cross?** Click the failed run, open the step marked ❌, and read the
error near the bottom. The usual causes are a typo in the `---` block at the
top of a page (check indentation and colons) or an image name that doesn't
match the file. Fix it, check with `quarto preview`, and push again.

---

## 7. Other common edits

- **Your name / site title / menu:** `_quarto.yml` → `title:` and `navbar:`.
- **Home page text and buttons:** `index.qmd`. It's written in HTML, so change the
  words between the `>` and `<` and leave the tags alone. The three "Featured work"
  cards and the three "Latest writing" links are also here; update them when you add
  a new project or post you want on the home page.
- **Your story, journey and skills:** `about.qmd` (normal Markdown).
- **CV:** save your CV as `cv/Halireena_Rushdiha_CV.pdf` (exact name). The Download
  button on the CV page points to it. To update your CV, just replace that file and push.
- **Contact form:** it sends messages through Formspree (free). Sign up at
  https://formspree.io, create a form that delivers to your email, copy its ID
  (looks like `xabcdefg`), and paste it in `contact.qmd` on the line
  `const FORMSPREE_ID = "";` between the quotes. Until then the form is disabled and
  visitors are pointed to your email address instead.
- **Colours and fonts:** the top of `theme.scss` (e.g. `$rose: #D9837B;`).

## 8. (Later) Running code inside pages

The project pages make their figures with separate scripts, so GitHub
never needs Python. If you'd rather put live ```` ```{python} ```` code chunks
in a page, add this to `_quarto.yml`:

```yaml
execute:
  freeze: auto
```

then run `quarto render` on your computer and commit the `_freeze/` folder it
creates. GitHub will reuse those saved results instead of running your code.
