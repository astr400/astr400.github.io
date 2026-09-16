---
name: markdown-style
description: Markdown dialect for the astr400.github.io repo, covering the no-raw-HTML rule, ATX headings that map to cards, language-labelled code fences that control copy buttons, and internal link form. Use when writing or editing any .md file in this repo, including published pages, repo docs, and skills.
---

# Markdown style

Follow [`MARKDOWN.md`](../../../MARKDOWN.md). That file is the Markdown guide for this repo (published pages, repo docs, and skills). Page structure and frontmatter: [`STYLE.md`](../../../STYLE.md).

If [`background/`](../../../background/) is locked, do not edit it (see [`AGENTS.md`](../../../AGENTS.md)).

## Highest-value rules

1. **No raw HTML in content.** No `<section>`, `<div>`, `<a>`, `<pre>`, no `markdown="1"`. The layouts own all markup.
2. **No `#` in a page body.** The `<h1>` comes from the `title` frontmatter key; `##` starts a card.
3. **Label every fence.** `bash` and `python` get a copy button; `text` does not. Use `text` for directory trees and file samples.
4. **Write `<` and `>` literally.** Markdown needs no HTML entities.
5. **Internal links are published paths** with a trailing slash: `[uv](/setup/uv/)`.

Never put a literal `<h2` inside a code fence; [`_layouts/guide.html`](../../../_layouts/guide.html) splits rendered HTML on it.

The renderer is kramdown with GFM input, pinned to Jekyll 3.10. Do not rely on Jekyll 4 behaviour.

## Skills (`SKILL.md`)

- YAML frontmatter: `name` (lowercase hyphens) and third-person `description` with WHAT + WHEN.
- Keep the body under 500 lines: protocol, not a second copy of `STYLE.md` or `MARKDOWN.md`.
