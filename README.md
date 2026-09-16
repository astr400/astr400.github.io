# Astrophysics Setup Guide

Source for [astr400.github.io](https://astr400.github.io/): a static site of astrophysics computing setup, environment management, and project workflow guides.

Content is Markdown. The only HTML in the repo is two Jekyll layouts. Agent map: [`AGENTS.md`](AGENTS.md). House style: [`STYLE.md`](STYLE.md). Markdown dialect: [`MARKDOWN.md`](MARKDOWN.md).

## Structure

```text
.
├── index.md              # landing page
├── _setup/               # the setup-guide section, one Markdown file per page
├── _layouts/             # the only HTML: default.html and guide.html
├── _data/resources.yml   # landing-page link list
├── assets/               # site.css, site.js, branding
├── background/           # frozen upstream source (locked, not published)
└── scripts/              # new_page.py and check_site.py
```

Each page's frontmatter carries what used to be hand-copied HTML: the badge, the
nav label, its position in the sequence, and its landing-page card text. The
topbar, the numbered step grid, and the prev/next pagers are all generated from
those fields, so they cannot drift out of sync.

## Editing content

Edit the Markdown in `_setup/`. Every `##` heading becomes one card on the page;
fence runnable commands as `bash` to get a copy button, and directory trees as
`text` to skip it. Never put HTML in a content file — see [`MARKDOWN.md`](MARKDOWN.md).

Add a page:

```bash
python3 scripts/new_page.py setup <slug>
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

Pages are sectioned, for example `/setup/conda/`. Every URL the site published as
hand-written HTML still resolves: each page lists its old path in `redirect_from`,
and `check_site.py` fails if one is dropped.
