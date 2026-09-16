#!/usr/bin/env python3
"""Scaffold a new page in a section with a valid frontmatter contract."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from sitelib import REPO_ROOT, load_pages, section_names

SLUG_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")

TEMPLATE = """\
---
title: TODO full descriptive phrase for the page heading
short_title: TODO short label for the browser tab
nav: TODO
pill: TODO
description: TODO one sentence for search results and link previews.
branch: main
order: {order}
step: {step}
step_title: TODO heading of the landing-page card
summary: TODO body text of the landing-page card.
link_text: TODO link label inside the landing-page card
---

TODO one intro paragraph with no heading. The layout pairs this with the title
and pill in the first card.

## TODO first section

TODO. Each `##` heading becomes one card. Fence runnable commands as `bash` so
they get a copy button, and directory trees as `text` so they do not.
"""


def validate_slug(slug: str) -> None:
    if not SLUG_RE.fullmatch(slug):
        raise ValueError(
            "slug must be lowercase words joined by hyphens "
            f"(for example 'spectral-lines'), got {slug!r}."
        )


def create_page(section: str, slug: str, root: Path | None = None) -> Path:
    base = root or REPO_ROOT
    validate_slug(slug)

    available = section_names(base)
    if section not in available:
        raise ValueError(
            f"unknown section {section!r}. Available: {', '.join(available) or 'none'}. "
            "Add a collections entry in _config.yml before creating a new section."
        )

    path = base / f"_{section}" / f"{slug}.md"
    if path.exists():
        raise FileExistsError(f"page already exists: {path.relative_to(base)}")

    pages = load_pages(section, base)
    orders = [page.front.get("order") or 0 for page in pages]
    steps = [page.front.get("step") or 0 for page in pages]
    next_order = max(orders, default=0) + 1
    next_step = max(steps, default=0) + 1

    path.write_text(
        TEMPLATE.format(order=next_order, step=next_step),
        encoding="utf-8",
    )
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("section", help="Section name, e.g. setup")
    parser.add_argument("slug", help="Page slug, e.g. spectral-lines")
    args = parser.parse_args(argv)

    try:
        created = create_page(args.section, args.slug)
    except (ValueError, FileExistsError, FileNotFoundError) as exc:
        print(exc, file=sys.stderr)
        return 1

    relative = created.relative_to(REPO_ROOT)
    print(f"Created {relative}")
    print("Next: replace the TODO placeholders, then run scripts/check_site.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
