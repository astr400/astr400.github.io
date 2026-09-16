# Agent notes

Human setup and commands: [`README.md`](README.md). House style: [`STYLE.md`](STYLE.md) ([astr400-site-style](.cursor/skills/astr400-site-style/SKILL.md)). Markdown: [`MARKDOWN.md`](MARKDOWN.md) ([markdown-style](.cursor/skills/markdown-style/SKILL.md)). Do not add always-on `.cursor/rules`; use project skills in [`.cursor/skills/`](.cursor/skills/).

This repository is **astr400.github.io** ([github.com/astr400/astr400.github.io](https://github.com/astr400/astr400.github.io)): the published site for the astr400 org. Weekly study guides live in the sibling repo **astro-study** ([github.com/astr400/astro-study](https://github.com/astr400/astro-study)) and are not published here yet.

## Content is Markdown

Authoring happens in `.md` and `.yml` only. All HTML lives in [`_layouts/`](_layouts/) — two files. If a change seems to need HTML in a content file, the layout is missing a feature; fix the layout instead.

## Environment

- No Node, no npm, no package manager for content work. Editing and reviewing pages needs nothing installed.
- The scripts are standard-library Python 3: `python3 scripts/new_page.py`, `python3 scripts/check_site.py`.
- Local preview is optional and needs Ruby with bundler as your user (never `sudo`): `gem install --user-install bundler` then `bundle install && bundle exec jekyll serve`.
- CI installs nothing. `actions/jekyll-build-pages` is a container with the `github-pages` gem preinstalled, which pins **Jekyll 3.10**. Do not use Jekyll 4 syntax.

## Roles

| Role | Path |
| --- | --- |
| Published content | [`_setup/`](_setup/) and [`index.md`](index.md) |
| The only HTML | [`_layouts/default.html`](_layouts/default.html), [`_layouts/guide.html`](_layouts/guide.html) |
| Site config and sections | [`_config.yml`](_config.yml) |
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
| Process skills | Protocol unique to that job (not a second STYLE) |

Content **pages** live only under `_setup/` (and future section directories). House **rules** and tooling may change in [`STYLE.md`](STYLE.md), [`MARKDOWN.md`](MARKDOWN.md), [`.cursor/skills/`](.cursor/skills/), [`_layouts/`](_layouts/), and [`scripts/`](scripts/) when the task is rules or tooling.

## Sections

The site is organised into sections, one Jekyll collection each. Only **setup** exists today.

- Add a page: `python3 scripts/new_page.py setup <slug>` ([new-page skill](.cursor/skills/new-page/SKILL.md)).
- Add a section: add a `collections` entry plus a `defaults` scope in `_config.yml`, then a directory of Markdown. No layout or content file changes.
- Study guides from **astro-study** are notebooks with LaTeX math. Publishing them needs a math engine and a decision on hand-authored Markdown versus `nbconvert`. Neither is set up. Do not invent a `_study` collection until that content and decision exist.

## Checks

Before a pull request, run `python3 scripts/check_site.py` ([site-review skill](.cursor/skills/site-review/SKILL.md)). It fails on missing or duplicated frontmatter, broken internal links, raw HTML in content, a missing legacy redirect, and a `<h2` inside a code fence. That last one matters: [`_layouts/guide.html`](_layouts/guide.html) builds the cards by splitting rendered HTML on `<h2`, so a literal `<h2` in a fenced block would corrupt the page.

## Git vs GitHub

Remote: `git@github.com:astr400/astr400.github.io`. Push with the shared SSH key. `gh` (PRs) needs `gh auth login` as that same GitHub user. Never commit tokens or `GH_TOKEN`.

Deployment is the Pages Actions workflow in [`.github/workflows/pages.yml`](.github/workflows/pages.yml). The Pages source must be set to **GitHub Actions**, not a branch.
