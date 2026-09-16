# Background source (locked)

Upstream Markdown that the published setup pages were distilled from. Kept as the source of record so the provenance of the guide text is not lost.

This directory is frozen. See [`LOCKED.md`](LOCKED.md) and [`AGENTS.md`](../AGENTS.md).

| File | Role |
| --- | --- |
| `setup.md` | Condensed setup guide, MyST flavoured, the direct ancestor of the `_setup/` pages |
| `setup_original.md` | The longer original draft it was cut down from |
| `uv_setup.md` | Source for the uv page |

These files are excluded from the built site in [`_config.yml`](../_config.yml). They are not published and are not part of the Markdown dialect described in [`MARKDOWN.md`](../MARKDOWN.md) — `setup.md` still contains MyST `{admonition}` directives that Jekyll does not render.
