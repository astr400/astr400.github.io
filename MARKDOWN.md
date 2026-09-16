# astr400.github.io Markdown

Rules for **all** Markdown in this repo: published pages, repo docs, and skills. Agents: [markdown-style skill](.cursor/skills/markdown-style/SKILL.md). Page structure and frontmatter: [`STYLE.md`](STYLE.md).

The renderer is kramdown with GFM input, pinned to **Jekyll 3.10** by the `github-pages` gem. Do not rely on Jekyll 4 or CommonMark-only behaviour.

| Surface | Where | Typical use |
| --- | --- | --- |
| Published page | `_setup/*.md`, `_use/*.md`, `setup.md`, `use.md`, `index.md` | Reader-facing guide prose |
| Repo doc | `README.md`, `AGENTS.md`, `STYLE.md` | Repo map and rules |
| Skill | `.cursor/skills/*/SKILL.md` | Agent protocol |

## No raw HTML

Content files contain **zero** HTML tags. This is the whole point of the refactor: the old site was hand-written HTML and drifted. All markup comes from [`_layouts/`](_layouts/) and [`_includes/`](_includes/).

- No `<section>`, `<div>`, `<br>`, `<img>`, `<a>`, or `<pre>`.
- No `markdown="1"` wrappers.
- No inline `style` or `class` attributes.

`scripts/check_site.py` fails the build on a raw tag in a content file. If you need markup that Markdown cannot express, change the layout or add a frontmatter key; do not reach for HTML.

## Headings

- ATX only (`##`, `###`). No underlined Setext headings.
- Never use `#` in a page body. The `<h1>` comes from the `title` frontmatter key.
- `##` starts a new card, so treat it as a section break, not a decorative label.
- `###` groups content inside a card, typically per platform (`### macOS`, `### Linux`, `### Windows`).

## Code fences

Always fence, always label the language. The label is not decoration — it becomes a `.language-<lang>` class on the built block, which decides whether the block gets a copy button.

| Fence | Use | Copy button |
| --- | --- | --- |
| `bash` | Commands a reader will run | yes |
| `python` | Python a reader will run | yes |
| `text` | Directory trees, file samples, output | no |

Write shell and config content literally. Because content is Markdown rather than HTML, characters that used to need escaping are now plain: write `>` and `<` directly, not `&gt;` and `&lt;`.

Never put a literal `<h2` inside a fence. [`_layouts/guide.html`](_layouts/guide.html) builds cards by splitting rendered HTML on `<h2`, and `check_site.py` rejects it.

## Lists, links, emphasis

- Blank line before every list. Prefer `-` over `*`.
- Numbered lists only for ordered steps a reader performs in sequence.
- Internal links use the published path with a trailing slash: `[uv](/setup/uv/)`, `[docker run](/use/docker/)`. Never link a filename or a legacy `*.html` path.
- External links are plain Markdown: `[Apple](https://developer.apple.com/xcode/)`. Do not hand-write `target` or `rel`; the landing-page resource list adds those from `_data/resources.yml`.
- Inline code for commands, paths, filenames, and package names: `` `conda activate` ``, `` `pyproject.toml` ``.
- Bold for UI labels a reader clicks: `**Settings** → **SSH and GPG keys**`.

## Tables

Header row plus a `| --- |` separator. Keep cells short; a table is for enumerable facts, and explanation belongs in the surrounding prose.

## Repo docs and skills

| File | Role |
| --- | --- |
| `README.md` | Human setup, commands, deployment |
| `AGENTS.md` | Repo map, environment, locks, write trees |
| `STYLE.md` | Frontmatter contract, section and URL policy |
| `.cursor/skills/*/SKILL.md` | YAML `name` plus third-person `description` (WHAT + WHEN); under 500 lines |

Skill descriptions are third person and state both what the skill does and when to load it. Keep a skill body to protocol; point at `STYLE.md` or `MARKDOWN.md` rather than restating them.

## Do not

- Paste rendered HTML from the old site into a Markdown file.
- Add a `permalink` to a page; the collection sets it.
- Remove a `redirect_from` entry.
- Duplicate this file's rules inside a skill.
