# Homelabbing and Local AI

A HacKSU workshop deck on the basics of homelabbing, using a real homelab as the running example. Built on the HacKSU presentation template.

```text
static/
  app.js                  slide navigation and particle background
  style.css               HacKSU deck design
templates/
  slides/                 template layouts to copy from
    homelab/              homelab half (Ian)
    ai/                   local AI half (Meheraj)
    closing.html          shared Q&A slide
  base.html               page shell, nav bar, logo
  index.html              slide order
  notes.html              speaker notes and run of show
app.py                    base app, three routes: deck, notes, logo
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

Design and plumbing lifted from the polyglot programming deck.
