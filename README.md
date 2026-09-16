# Astrophysics Setup Guide

Source for [astr400.github.io](https://astr400.github.io/): the org **gateway** for astrophysics computing setup (Python, Git, Docker-the-tool), day-to-day environment use, and project workflow. MESA-in-container usage will live with the Docker image on Read the Docs; study notebooks live in **astro-study**. Publishing map: [`AGENTS.md`](AGENTS.md).

Content is Markdown. HTML lives only in [`_layouts/`](_layouts/) and [`_includes/`](_includes/). Agent map: [`AGENTS.md`](AGENTS.md). House style: [`STYLE.md`](STYLE.md). Markdown dialect: [`MARKDOWN.md`](MARKDOWN.md).

## Structure

```text
.
├── index.md              # landing page
├── setup.md              # Setup hub (/setup/)
├── use.md                # Use hub (/use/)
├── _setup/               # install guides (Python, Git, Docker-the-tool; not MESA usage)
├── _use/                 # day-to-day environment use
├── _layouts/             # default.html, guide.html, hub.html
├── _includes/            # shared catalog grid
├── _data/nav.yml         # topbar hubs
├── _data/resources.yml   # landing-page link list
├── assets/               # site.css, site.js, branding
└── scripts/              # new_page.py and check_site.py
```

Each page's frontmatter carries what used to be hand-copied HTML: the badge, the
nav label, its position in the section, and its catalog card text. The home and
hub grids and the prev/next pagers are generated from those fields. The topbar
is the short hub list in `_data/nav.yml`.

## Editing content

Edit the Markdown in `_setup/` and `_use/`. Every `##` heading becomes one card on the page;
fence runnable commands as `bash` to get a copy button, and directory trees as
`text` to skip it. Never put HTML in a content file — see [`MARKDOWN.md`](MARKDOWN.md).

Add a page:

```bash
python3 scripts/new_page.py setup <slug>
python3 scripts/new_page.py use <slug>
```

Check content before opening a pull request:

```bash
python3 scripts/check_site.py
```

Both scripts use only the Python standard library, so they need no setup.

## Local preview

Optional; CI builds the site regardless. Needs Ruby with a user-local bundler,
never `sudo`:

```bash
gem install --user-install bundler
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000/`. The [`Gemfile`](Gemfile) pins the same
`github-pages` gem the deployment uses, so local output matches production.

## Deployment

Pushing to `main` runs [`.github/workflows/pages.yml`](.github/workflows/pages.yml),
which checks content, builds with `actions/jekyll-build-pages`, and deploys the
artifact. Pull requests build and check without publishing.

The repository's Pages source must be set to **GitHub Actions** under
Settings then Pages. No generated HTML is committed.

## URLs

Pages are sectioned, for example `/setup/conda/` and `/use/docker/`. Hubs are
`/setup/` and `/use/`. Every URL the site published as hand-written HTML still
resolves: each page lists its old path in `redirect_from`, and `check_site.py`
fails if one is dropped.
