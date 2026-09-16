---
name: new-page
description: Scaffolds a new page in a section of the astr400.github.io site with a valid frontmatter contract, and explains how order, step, and branch place the page in the section hub, the home catalog, and the prev/next sequence. Use when adding a setup or use page, inserting a page into the middle of the sequence, or adding an alternative path alongside an existing step.
---

# New page

Scaffold with the script; do not hand-create the file.

```bash
python3 scripts/new_page.py setup <slug>
python3 scripts/new_page.py use <slug>
```

The slug is lowercase with hyphens and becomes the URL (`_setup/conda.md` publishes at `/setup/conda/`). The script validates the slug, picks the next free `order` and `step` in that section, and writes the frontmatter contract.

Field meanings and the full contract: [`STYLE.md`](../../../STYLE.md). Body dialect: [`MARKDOWN.md`](../../../MARKDOWN.md).

## Protocol

1. Run the script. It fails if the page already exists.
2. Replace every `TODO` placeholder in the frontmatter. `nav` is one or two words; `title` is a full phrase; `description` is one sentence.
3. Write the body: one intro paragraph with **no heading**, then `##` per card.
4. Run `python3 scripts/check_site.py`.

## Placing the page

- **Appended to the end** of the section is the default: the script takes the next `order` and `step`.
- **Inserted in the middle** means renumbering. Bump `order` and `step` on every later page in that section, then rerun the check script; duplicate `order` values in the same section fail it.
- **An alternative path** for an existing step (what uv is to Conda, or Docker on macOS to the Docker hub) takes a unique `order`, reuses that step's `step` number, and sets `branch: alt` instead of `main`. Omit `step_title` and `summary`, since the step's primary page owns the catalog card. The pager targets only `branch: main` pages in the same collection, so the alternative rejoins the main path automatically.

Leaf pages never go in the topbar. That list is [`_data/nav.yml`](../../../_data/nav.yml) hubs only.

## Do not

- Add a `permalink`; the collection sets it.
- Add `redirect_from` to a genuinely new page. It is only for URLs that already existed.
- Create a new section directory without first adding its `collections`, hub, and nav entries in [`_config.yml`](../../../_config.yml) and [`_data/nav.yml`](../../../_data/nav.yml).
