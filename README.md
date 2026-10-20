# Homelabbing and Local AI

A HacKSU workshop deck on the basics of homelabbing, using a real homelab as the running example. Built on the HacKSU presentation template.

```text
.github/workflows/
  pages.yml               builds and deploys to GitHub Pages
static/
  app.js                  slide navigation and particle background
  style.css               HacKSU deck design
  HacKSU.png              logo
  images/                 slide images
templates/
  slides/                 template layouts to copy from
    homelab/              homelab half (Ian)
    ai/                   local AI half (Meheraj)
    closing.html          shared Q&A slide
  base.html               page shell, nav bar, logo
  index.html              slide order
  notes.html              speaker notes and run of show
app.py                    base app, two routes: deck, notes
build.py                  renders the deck to static HTML in dist/
OUTLINE.md                slide-by-slide content outline
pyproject.toml            project metadata and dependencies (uv)
README.md                 documentation
```

A Flask app on port 5174, managed with [uv](https://docs.astral.sh/uv/).

Run the commands below from a Linux shell (WSL on Windows, or macOS/Linux). If uv isn't installed yet:

`curl -LsSf https://astral.sh/uv/install.sh | sh`

Install dependencies:

`uv sync`

To run the app:

`uv run app.py`

`/` is the deck, navigated with arrows, space, or the dots.

`/notes` is the speaker notes with a minute-by-minute run of show.

To add a dependency, use `uv add <package>` rather than editing `pyproject.toml` by hand, so `uv.lock` stays in sync.

To change the order of slides, navigate to `templates/index.html`, and reorder using `{% include %}`

Use relative paths (`static/...`, no leading slash) for images and other files, so the deck also works on GitHub Pages.

## GitHub Pages

Every push to the default branch builds the deck and publishes it to GitHub Pages. After forking, do this once:

1. **Actions** tab: enable workflows (GitHub disables them on forks).
2. **Settings → Pages**: set Source to **GitHub Actions**.
3. **Actions** tab: run **Deploy to GitHub Pages** manually, or push a commit.

The deck is published at `https://<username>.github.io/<repo-name>/` and the notes at `.../notes.html`.

To build locally: `uv run build.py`, then open `dist/index.html`.

Design and plumbing lifted from the polyglot programming deck.
