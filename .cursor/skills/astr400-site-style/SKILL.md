---
name: astr400-site-style
description: House style for the astr400.github.io Jekyll gateway, covering the frontmatter contract, the order versus step sequencing, section and URL policy, and the rule that content is Markdown while all HTML stays in _layouts. Use when adding or editing a page under _setup or _use, changing the topbar or pager, adding a section, or reviewing whether a change belongs in content, frontmatter, or a layout. Do not use for MESA-in-container usage (that is mesa-docker-docs on Read the Docs) or for publishing astro-study notebooks.
---

# Site style

Follow [`STYLE.md`](../../../STYLE.md). That file is the house style for this repo (section layout, frontmatter contract, URL policy). Markdown dialect: [`MARKDOWN.md`](../../../MARKDOWN.md). Scope and environment: [`AGENTS.md`](../../../AGENTS.md).

## The one rule

Content is Markdown, chrome is frontmatter, HTML exists only in [`_layouts/`](../../../_layouts/) and [`_includes/`](../../../_includes/). A content file with a tag in it is a bug. If Markdown cannot express what you need, change the layout or add a frontmatter key.

## Protocol

1. Scaffold, never hand-create: `python3 scripts/new_page.py setup <slug>` or `python3 scripts/new_page.py use <slug>`.
2. Fill the frontmatter contract from [`STYLE.md`](../../../STYLE.md). `order` is unique per collection; `step` may repeat for alternative paths.
3. Write the body as one intro paragraph with no heading, then `##` per card.
4. Cross-link with published paths (`/setup/uv/`, `/use/docker/`), never filenames.
5. Run `python3 scripts/check_site.py` before a pull request.

## Do not

- Add a `permalink` to a page; the collection or hub path default in [`_config.yml`](../../../_config.yml) sets it.
- Remove a `redirect_from` entry, or a legacy URL breaks.
- Restyle [`assets/site.css`](../../../assets/site.css) as part of a content change.
- Put leaf pages in [`_data/nav.yml`](../../../_data/nav.yml); that file is section hubs only.
- Create a `_study` collection before that content and a math decision exist ([publishing map](../../../AGENTS.md)).
- Host MESA-in-container usage on this site, or migrate the gateway to Read the Docs.
- Add always-on `.cursor/rules`.
