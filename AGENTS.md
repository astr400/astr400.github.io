# Agent notes

Human setup and commands: [`README.md`](README.md). House style: [`STYLE.md`](STYLE.md) ([astr400-site-style](.cursor/skills/astr400-site-style/SKILL.md)). Markdown: [`MARKDOWN.md`](MARKDOWN.md) ([markdown-style](.cursor/skills/markdown-style/SKILL.md)). MESA Docker docs (other repo): [mesa-docker-docs](.cursor/skills/mesa-docker-docs/SKILL.md). Do not add always-on `.cursor/rules`; use project skills in [`.cursor/skills/`](.cursor/skills/).

This repository is **astr400.github.io** ([github.com/astr400/astr400.github.io](https://github.com/astr400/astr400.github.io)): the published **gateway** for the astr400 org (environment setup, Docker-the-tool, day-to-day use, and discovery). It is not the host for MESA-in-container usage docs or for study notebooks.

## Publishing map

Three surfaces, three engines. Do not merge them onto Read the Docs or into this Jekyll site.

| Surface | Repo | Engine | Host |
| --- | --- | --- | --- |
| Gateway: setup, installing Docker, using environments, discovery | **this** | Jekyll 3.10, Markdown collections | GitHub Pages (`astr400.github.io`) |
| MESA in a container (image tags, `mesa_star`, volumes) | the MESA Docker repo, when it exists | Sphinx with MyST, or MkDocs | Read the Docs, versioned with image tags |
| Study guides and astropy notebooks | **astro-study** ([github.com/astr400/astro-study](https://github.com/astr400/astro-study)) | Jupyter Book / MyST | not this site until a math engine and a Markdown-versus-notebook source of truth exist |

- Do **not** migrate this gateway to [readthedocs.io](https://readthedocs.io). Read the Docs is a build-and-version host for the Docker **software**, not a replacement for the guide chrome (`order` / `step` / `branch`, cards, chassis theme).
- Do **not** write MESA run commands, inlists, or image-tag matrices on this site. Link out. Generic Docker **install** belongs at [`/setup/docker/`](_setup/docker.md). Generic `docker run` belongs at [`/use/docker/`](_use/docker.md).
- When the MESA Docker repo exists: author its docs next to the Dockerfiles; enable RTD versioning aligned with image tags; link **back** to this gateway for Git, Python, and [installing Docker](/setup/docker/). Do not duplicate those setup guides in the Docker repo.
- Study notebooks stay in **astro-study**. Do not invent a `_study` collection, and do not treat Read the Docs as a reason to publish `.ipynb` here.

## Content is Markdown

Authoring happens in `.md` and `.yml` only. All HTML lives in [`_layouts/`](_layouts/) and [`_includes/`](_includes/). If a change seems to need HTML in a content file, the layout is missing a feature; fix the layout instead.

## Environment

- No Node, no npm, no package manager for content work. Editing and reviewing pages needs nothing installed.
- The scripts are standard-library Python 3: `python3 scripts/new_page.py`, `python3 scripts/check_site.py`.
- Local preview is optional and needs Ruby with bundler as your user (never `sudo`): `gem install --user-install bundler` then `bundle install && bundle exec jekyll serve`.
- CI installs nothing. `actions/jekyll-build-pages` is a container with the `github-pages` gem preinstalled, which pins **Jekyll 3.10**. Do not use Jekyll 4 syntax.

## Roles

| Role | Path |
| --- | --- |
| Published content | [`_setup/`](_setup/), [`_use/`](_use/), [`setup.md`](setup.md), [`use.md`](use.md), [`index.md`](index.md) |
| The only HTML | [`_layouts/`](_layouts/), [`_includes/guide_grid.html`](_includes/guide_grid.html) |
| Site config and sections | [`_config.yml`](_config.yml) |
| Topbar and home bands | [`_data/nav.yml`](_data/nav.yml) |
| Landing-page link list | [`_data/resources.yml`](_data/resources.yml) |
| Design | [`assets/site.css`](assets/site.css), [`assets/site.js`](assets/site.js), [`assets/logo.png`](assets/logo.png), [`assets/milky-way.jpg`](assets/milky-way.jpg) |
| Tooling | [`scripts/`](scripts/) |

## Source of truth

Skills auto-load in isolation: keep a **one-line** reminder plus a link, not a second copy of STYLE or MARKDOWN.

| Layer | Owns |
| --- | --- |
| This file | Map, env, write trees |
| [`STYLE.md`](STYLE.md) | Frontmatter contract, section and URL policy, page anatomy |
| [`MARKDOWN.md`](MARKDOWN.md) | Markdown dialect, code fences, link form |
| [`_config.yml`](_config.yml) | Which sections exist |
| [`_data/nav.yml`](_data/nav.yml) | Topbar hubs, and home bands when `collection` is set |
| Process skills | Protocol unique to that job (not a second STYLE) |

Content **pages** live under `_setup/` and `_use/`. Hub indexes are `setup.md` and `use.md` at the repo root. House **rules** and tooling may change in [`STYLE.md`](STYLE.md), [`MARKDOWN.md`](MARKDOWN.md), [`.cursor/skills/`](.cursor/skills/), [`_layouts/`](_layouts/), and [`scripts/`](scripts/) when the task is rules or tooling.

## Sections

The site is organised into sections, one Jekyll collection each. **setup** is install and configure. **use** is day-to-day environment commands. Docker-the-tool install is `/setup/docker/`. Generic `docker run` is `/use/docker/`. MESA-in-container is not a section.

- Add a page: `python3 scripts/new_page.py setup <slug>` or `python3 scripts/new_page.py use <slug>` ([new-page skill](.cursor/skills/new-page/SKILL.md)).
- Add a section: add a `collections` entry plus a `defaults` scope in `_config.yml`, a hub file, and a [`_data/nav.yml`](_data/nav.yml) item with `collection`, then a directory of Markdown. Home bands follow that key; the layout does not change.
- Study guides from **astro-study** are notebooks with LaTeX math. Publishing them needs a math engine and a decision on hand-authored Markdown versus notebooks as the source of truth (typically Jupyter Book / MyST, not Sphinx on Read the Docs unless the notebooks are MESA tutorials). Neither is set up. Do not invent a `_study` collection until that content and decision exist. The gateway may **link** to published study pages; it must not host the notebooks.

## Checks

Before a pull request, run `python3 scripts/check_site.py` ([site-review skill](.cursor/skills/site-review/SKILL.md)). It fails on missing or duplicated frontmatter, broken internal links, raw HTML in content, a missing legacy redirect, and a `<h2` inside a code fence. That last one matters: [`_layouts/guide.html`](_layouts/guide.html) builds the cards by splitting rendered HTML on `<h2`, so a literal `<h2` in a fenced block would corrupt the page.

## Git vs GitHub

Remote: `git@github.com:astr400/astr400.github.io`. Push with the shared SSH key. `gh` (PRs) needs `gh auth login` as that same GitHub user. Never commit tokens or `GH_TOKEN`.

Deployment is the Pages Actions workflow in [`.github/workflows/pages.yml`](.github/workflows/pages.yml). The Pages source must be set to **GitHub Actions**, not a branch.
