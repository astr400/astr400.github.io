# astr400.github.io style

House style for the published site. Agents: [astr400-site-style skill](.cursor/skills/astr400-site-style/SKILL.md). Setup: [`README.md`](README.md). Scope protocol: [`AGENTS.md`](AGENTS.md). Markdown dialect: [`MARKDOWN.md`](MARKDOWN.md).

The rule behind every rule here: **content is Markdown, chrome is frontmatter, HTML is only in [`_layouts/`](_layouts/)**.

## Section layout

```text
_setup/                  # one directory per section, a Jekyll collection
├── toolchain.md
├── conda.md
├── uv.md
├── editor.md
├── git.md
└── workflow.md
index.md                 # landing page, home: true
```

Slugs are lowercase with hyphens and become the URL: `_setup/conda.md` publishes at `/setup/conda/`. Scaffold with `python3 scripts/new_page.py setup <slug>`; never create the file by hand.

## Frontmatter contract

`layout` comes from `defaults` in [`_config.yml`](_config.yml), so a page never sets it. Everything else is explicit, including `branch`: the pager filters on it, and a value that only ever arrived through a config default would be an invisible dependency.

| Key | Required | Role |
| --- | --- | --- |
| `title` | yes | `<h1>`. A full descriptive phrase. |
| `short_title` | recommended | Browser tab and search-result title, when `title` is too long for one. |
| `nav` | yes | Topbar label and pager label. One or two words. |
| `pill` | yes | Uppercase badge above the `<h1>`. |
| `description` | yes | `<meta name="description">`, one sentence. |
| `order` | yes | Unique position in the topbar and the page sequence. |
| `step` | yes | Numbered step on the landing page. Shared by alternative paths. |
| `step_title` | step primary only | Heading of the landing-page card. |
| `summary` | step primary only | Body text of the landing-page card. |
| `link_text` | yes | Link label inside the landing-page card. |
| `branch` | yes | `main` for the numbered path, `alt` for a parallel alternative. |
| `note` | optional | Aside rendered as `p.note` below the pager. May contain Markdown links. |
| `redirect_from` | legacy pages only | Old URLs that must keep working. |

A page carries three names because they serve three readers. `title` is the
heading someone reads on the page, `short_title` is what fits a browser tab and
a search result, and `nav` is what fits a topbar and a Next link. Set
`short_title` whenever `title` runs past about five words.

## `order` versus `step`

These are deliberately separate, because the site has a branch: Conda and uv are two ways to do the same step.

- `order` is unique and controls topbar sequence. Conda is 2, uv is 3.
- `step` is the numbered path and may repeat. Conda and uv are both step 2.
- `branch` is `main` on the numbered path and `alt` on an alternative. The pager only ever targets `branch: main` pages, so uv's Next rejoins the main path at step 3.

One card appears on the landing page per `step`, owned by the page carrying `step_title`. Other pages sharing that step become extra links inside it.

This replaced three conflicting orderings in the old hand-written HTML: the topbar listed Conda before Toolchain, the landing page numbered Toolchain first, and the pagers implied a third sequence. Everything now derives from `order` and `step`, so they cannot disagree.

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

- Sectioned and trailing-slashed: `/setup/conda/`.
- Every page that existed as `*.html` keeps a `redirect_from` entry. Do not remove one; inbound links depend on it.
- Cross-links between pages use the published path, `[uv](/setup/uv/)`, not a filename.

## Design

The published look is a dark night-sky theme in [`assets/site.css`](assets/site.css): navy and gold on `#0b1220`, with [`assets/logo.png`](assets/logo.png) as the brand mark. A NASA/JPL-Caltech Spitzer photograph of the galactic centre ([`assets/milky-way.jpg`](assets/milky-way.jpg)) appears in the home hero and as a faint page wash. Body copy, headings, lists, and code stay on opaque `card` surfaces so the photo never carries reading text. Available classes are `card`, `hero`, `grid`, `pill`, `step-num`, `pager`, `note`, and `resources`; the layouts apply them. Content files never reference a class.

Fence directory trees and config samples as `text` so they get no copy button. Fence runnable commands as `bash` so they do.

GitHub Pages forces the Rouge highlighter on, so a fenced block builds as a `.language-<lang>` wrapper around the `<pre>`. [`assets/site.css`](assets/site.css) ships no Rouge colour theme on purpose, so tokens inherit the body colour and code blocks stay plain. Do not add one without deciding that syntax colours are wanted site-wide.

## Adding a section

1. Add a `collections` entry with `output: true` and `permalink: /<name>/:name/` in [`_config.yml`](_config.yml).
2. Add a `defaults` scope for that collection setting `layout: guide`.
3. Create the directory and scaffold pages with `scripts/new_page.py`.

The topbar and pagers read from the collection, so no layout edit is needed for a single-section nav. Grouping the topbar by section is a layout change, made once, when the second section arrives.
