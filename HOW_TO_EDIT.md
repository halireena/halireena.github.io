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
_quarto.yml              Site settings: title, menu bar, theme
index.qmd                About page (the home page)
projects.qmd             Projects page – lists everything in projects/ automatically
projects/                One folder per project
blog.qmd                 Blog page – lists everything in blog/ automatically
blog/                    One folder per blog post
cv.qmd                   CV page;  cv/cv.pdf is the downloadable PDF
images/                  Images used across the site (e.g. profile.png)
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

1. **Copy** the folder `projects/example-project` and give the copy a short
   name with no spaces, e.g. `projects/house-prices`.
   (The folder name becomes the web address:
   `halireena.github.io/projects/house-prices/`.)
2. Open `projects/house-prices/index.qmd`.
3. Edit the settings block between the `---` lines at the top:

   ```yaml
   ---
   title: "Predicting house prices in Colombo"
   description: "One sentence that appears on the Projects page."
   date: 2026-11-01
   categories: [R, machine learning]
   image: fig1.png
   ---
   ```

   - `date` must be `YYYY-MM-DD`. Projects are sorted newest first.
   - `image` is the thumbnail on the Projects page.
4. Replace the text under each heading: **The question → The data → Methods →
   Results (2 figures) → What I learned → Code**.
5. Replace `fig1.png` and `fig2.png` with your own figures (see section 5),
   and change the GitHub link at the bottom to your project's repository.
6. Delete files you don't need (`data.csv`, `make_figures.py`) and remove them
   from the `resources:` line at the top (or delete that line).
7. Run `quarto preview`, click **Projects** — your new card should be there.

To hide the example project from your site, delete the
`projects/example-project` folder (keep a copy somewhere if you like it as a
template).

---

## 4. Add a blog post

1. **Copy** the folder `blog/2026-10-03-welcome` and rename it to
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
refer to it from the top-level page, e.g. in `index.qmd`:
`image: images/profile.png`. To change your profile photo, just replace
`images/profile.png` with your own (same name), or change that line.

Optional extras:

```markdown
![Caption](photo.jpg){width=60%}                       <!-- make it smaller -->
![Caption](photo.jpg){fig-alt="Description for screen readers"}
![Caption](chart.png){#fig-chart}   …then write  @fig-chart  to refer to it as "Figure 1"
```

Tips: file names lowercase with no spaces (`my-chart.png`, not `My Chart.PNG`);
keep photos under ~1 MB.

---

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
- **Social links on the About page:** the `links:` list at the top of `index.qmd`.
- **CV:** edit `cv.qmd`, and replace `cv/cv.pdf` with your own PDF (same name).
- **Colours / theme:** change `cosmo` in `_quarto.yml` to another
  [Bootswatch theme](https://quarto.org/docs/output-formats/html-themes.html),
  e.g. `flatly`, `litera`, `minty`.

## 8. (Later) Running code inside pages

The example project makes its figures with a separate script, so GitHub
never needs Python. If you'd rather put live ```` ```{python} ```` code chunks
in a page, add this to `_quarto.yml`:

```yaml
execute:
  freeze: auto
```

then run `quarto render` on your computer and commit the `_freeze/` folder it
creates. GitHub will reuse those saved results instead of running your code.
