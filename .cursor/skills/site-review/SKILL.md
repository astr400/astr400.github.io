---
name: site-review
description: Pre-pull-request review protocol for the astr400.github.io site, running the check_site.py gate and interpreting each failure class, including duplicate order values, broken internal links, raw HTML in content, missing legacy redirects, and a literal h2 inside a code fence. Use before opening a pull request, when the check script fails, or when reviewing someone else's content change.
---

# Site review

The gate is one command:

```bash
python3 scripts/check_site.py
```

Run it before every pull request. It uses only the Python standard library, so it needs no environment setup. House style: [`STYLE.md`](../../../STYLE.md). Markdown dialect: [`MARKDOWN.md`](../../../MARKDOWN.md).

## Protocol

1. Run the script. Fix every reported failure; do not suppress one.
2. If the layouts or `_config.yml` changed, also build locally (`bundle exec jekyll build`) and confirm the topbar, landing-page grid, and pagers still render.
3. Report results as a table with one row per check and a result of `pass`, `fail`, or `n/a`.

## Failure classes

| Failure | Meaning | Fix |
| --- | --- | --- |
| Missing frontmatter key | The page breaks the contract | Add the key from [`STYLE.md`](../../../STYLE.md) |
| Duplicate `order` | Two pages claim one topbar slot | Renumber the later pages in that section |
| Step has no primary | No page in the step carries `step_title` | Give the main-path page `step_title` and `summary` |
| Raw HTML in content | The old error-prone pattern returning | Move the markup into a layout or a frontmatter key |
| Broken internal link | Target page or asset does not exist | Use the published path with a trailing slash |
| Missing `redirect_from` | A legacy URL would 404 | Restore the old `*.html` path on that page |
| `<h2` inside a code fence | Would corrupt card splitting in [`_layouts/guide.html`](../../../_layouts/guide.html) | Rewrite the sample without a literal `<h2` |

## Do not

- Edit the check script to make a failure disappear.
- Skip the local build after a layout change; the script checks content, not Liquid.
- Review content against a locked tree by editing it ([`AGENTS.md`](../../../AGENTS.md)); read-only review is allowed.
