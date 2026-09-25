# astr400.github.io style

House style for the published site. Agents: [astr400-site-style skill](.cursor/skills/astr400-site-style/SKILL.md). Setup: [`README.md`](README.md). Scope protocol: [`AGENTS.md`](AGENTS.md). Markdown dialect: [`MARKDOWN.md`](MARKDOWN.md).

The rule behind every rule here: **content is Markdown, chrome is frontmatter, HTML is only in [`_layouts/`](_layouts/)**.

## Section layout

```text
_setup/                  # install and configure the machine
├── toolchain.md
├── conda.md
├── uv.md
├── editor.md
├── git.md
├── docker.md            # Docker-the-tool chooser; MESA usage is not a page here
├── docker-macos.md
├── docker-ubuntu.md
└── docker-windows.md
_use/                    # day-to-day environment use
├── python.md
├── docker.md            # generic docker run and volumes, not MESA
└── workflow.md
setup.md                 # Setup hub, published at /setup/
use.md                   # Use hub, published at /use/
index.md                 # landing page, home: true
```

Slugs are lowercase with hyphens and become the URL: `_setup/conda.md` publishes at `/setup/conda/`. Scaffold with `python3 scripts/new_page.py setup <slug>` (or `use`); never create the file by hand.

The topbar lists section hubs from [`_data/nav.yml`](_data/nav.yml) (`Home`, `Setup`, `Use`). Leaf pages do not appear there. A hub item with `collection` also becomes a home band. Home and each hub render a numbered list from the collection.

## Frontmatter contract

`layout` comes from `defaults` in [`_config.yml`](_config.yml), so a page never sets it. Hub files (`setup.md`, `use.md`) also omit `permalink`; path-scoped defaults publish them at `/setup/` and `/use/`. Everything else on a guide page is explicit, including `branch`: the pager filters on it, and a value that only ever arrived through a config default would be an invisible dependency.

| Key | Required | Role |
| --- | --- | --- |
| `title` | yes | `<h1>`. A full descriptive phrase. |
| `short_title` | recommended | Browser tab and search-result title, when `title` is too long for one. |
| `nav` | yes | Pager label. One or two words. |
| `pill` | yes | Uppercase badge above the `<h1>`. |
| `description` | yes | `<meta name="description">`, one sentence. |
| `order` | yes | Unique position **in this collection** (pager and hub row sequence). |
| `step` | yes | Numbered row on the home catalog and the section hub. Shared by alternative paths. |
| `step_title` | step primary only | Heading of the catalog row. |
| `summary` | step primary only | Body text of the catalog row. |
| `link_text` | yes | Link label inside the catalog row. |
| `branch` | yes | `main` for the numbered path, `alt` for a parallel alternative. |
| `note` | optional | Aside rendered as `p.note` below the pager. May contain Markdown links. |
| `redirect_from` | legacy pages only | Old URLs that must keep working. |

A page carries three names because they serve three readers. `title` is the
heading someone reads on the page, `short_title` is what fits a browser tab and
a search result, and `nav` is what fits a Next link. Set
`short_title` whenever `title` runs past about five words.

Hub files need `title` and `description` only. Their `<h1>` comes from `title`; the body is one intro paragraph with no heading. `description` is also the lede of that section's home band.

## `order` versus `step`

These are deliberately separate, because a section can branch: Conda and uv are two ways to do the same Setup step, and Docker OS pages share the Docker step.

- `order` is unique **per collection** and controls sequence inside that section. Conda is 2, uv is 3 in setup.
- `step` is the numbered catalog row and may repeat. Conda and uv are both step 2.
- `branch` is `main` on the numbered path and `alt` on an alternative. The pager only ever targets `branch: main` pages in the **same collection**, so uv's Next rejoins the main path at Editor. The first and last main pages pager back to that section's hub (`/setup/` or `/use/`).

One row appears on Home and on the section hub per `step`, owned by the page carrying `step_title`. Other pages sharing that step become extra links inside it.

## Page anatomy

A guide page is frontmatter plus body. The body starts with one intro paragraph and no heading — [`_layouts/guide.html`](_layouts/guide.html) pairs it with the `title` and `pill` in the first card.

```markdown
---
title: Installing and configuring Git
nav: Git
...
---

Git helps you track changes to code, notebooks, and analysis scripts.

## 1. Install Git

Check whether Git is already installed:

```bash
git --version
```
```

Each `## Heading` becomes one `section.card`. Never write `<section>`, `<div>`, or any other tag: the layout adds them. Use `###` for subsections inside a card.

Number headings (`## 1. Install Git`) when the page is a sequence to follow, and leave them unnumbered when they are independent reference sections.

## URLs

- Sectioned and trailing-slashed: `/setup/conda/`, `/use/docker/`.
- Hubs: `/setup/`, `/use/`.
- Every page that existed as `*.html` keeps a `redirect_from` entry. Do not remove one; inbound links depend on it.
- Cross-links between pages use the published path, `[uv](/setup/uv/)`, not a filename.

## Design

The published look is a dark chassis theme in [`assets/site.css`](assets/site.css): phosphor green and filament amber on `#080b08`, with [`assets/logo.png`](assets/logo.png) as a small mark beside the wordmark. A NASA/JPL-Caltech Spitzer photograph of the galactic centre ([`assets/milky-way.jpg`](assets/milky-way.jpg)) is the page wash. The home hero lays a survey grid over that photo: an x-line and a y-line sweep, then a reticle locks and reads EVENT DETECTED. Each sweep picks a new point in the browser, uniform across x and Gaussian about the vertical centre. Scanlines and a slow CRT sweep sit on top. That motion holds on the locked reticle under `prefers-reduced-motion`. Display type (Syne) carries headlines, Instrument Sans carries body copy, and IBM Plex Mono carries kickers, buttons, and step numbers. Guide prose stays on opaque `card` surfaces so the photograph never carries reading text. Available classes are `card`, `hero`, `band`, `steps`, `step-num`, `pill`, `pager`, `note`, `resources`, and `btn`; the layouts apply them. Content files never reference a class.

Fence directory trees and config samples as `text` so they get no copy button. Fence runnable commands as `bash` so they do.

GitHub Pages forces the Rouge highlighter on, so a fenced block builds as a `.language-<lang>` wrapper around the `<pre>`. [`assets/site.css`](assets/site.css) ships no Rouge colour theme on purpose, so tokens inherit the body colour and code blocks stay plain. Do not add one without deciding that syntax colours are wanted site-wide.

## Adding a section

1. Add a `collections` entry with `output: true` and `permalink: /<name>/:name/` in [`_config.yml`](_config.yml).
2. Add a `defaults` scope for that collection setting `layout: guide`.
3. Add a hub Markdown file at the repo root and a path-scoped default that sets `layout: hub`, `permalink: /<name>/`, and `hub: <name>`.
4. Add a hub item to [`_data/nav.yml`](_data/nav.yml) with `name`, `url`, and `collection` set to the section name. Home renders one band per item that has `collection`, using that hub page's `description` as the lede.
5. Create the directory and scaffold pages with `scripts/new_page.py`.

The topbar lists hubs only, and the home bands follow `collection`, so adding a section or a page never requires a layout edit.

Keep generic Docker **install** in `_setup/` and generic `docker run` in `_use/`. Do not add a `_mesa` collection or MESA runbooks; those docs belong in the MESA Docker repo on Read the Docs ([publishing map](AGENTS.md)). Do not add `_study` until the math and source-of-truth decision in that map is made.
