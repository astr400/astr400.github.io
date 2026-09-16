"""Shared helpers for the site scripts: frontmatter parsing and page discovery.

Standard library only, so the scripts run with no environment setup. The YAML
parsing covers the subset used by this repo's frontmatter (scalars and simple
lists) rather than pretending to be a general YAML implementation.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Directories starting with an underscore that are Jekyll machinery, not sections.
NON_SECTION_DIRS = {"_layouts", "_data", "_site", "_includes", "_sass", "_plugins"}

KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")
FENCE_RE = re.compile(r"^\s*```")


def _scalar(raw: str):
    """Coerce a YAML scalar to str, int, or bool."""
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    if value in {"true", "false"}:
        return value == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split a Markdown file into its frontmatter mapping and its body."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text

    end = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end = index
            break
    if end is None:
        return {}, text

    data: dict = {}
    key: str | None = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[:1].isspace() and raw.strip().startswith("- "):
            if key is None:
                continue
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(_scalar(raw.strip()[2:]))
            continue
        match = KEY_RE.match(raw)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            data[key] = None if value == "" else _scalar(value)

    return data, "\n".join(lines[end + 1 :])


def split_fences(body: str) -> tuple[str, list[str]]:
    """Return the body with fenced blocks removed, plus the fenced blocks."""
    prose: list[str] = []
    fenced: list[str] = []
    in_fence = False
    for line in body.split("\n"):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        (fenced if in_fence else prose).append(line)
    return "\n".join(prose), fenced


@dataclass
class Page:
    path: Path
    section: str
    slug: str
    front: dict = field(default_factory=dict)
    body: str = ""

    @property
    def url(self) -> str:
        return f"/{self.section}/{self.slug}/"

    @property
    def rel(self) -> str:
        return str(self.path.relative_to(REPO_ROOT))


def section_dirs(root: Path | None = None) -> list[Path]:
    """Every collection directory, e.g. `_setup`."""
    base = root or REPO_ROOT
    return sorted(
        path
        for path in base.glob("_*")
        if path.is_dir() and path.name not in NON_SECTION_DIRS
    )


def section_names(root: Path | None = None) -> list[str]:
    return [path.name.lstrip("_") for path in section_dirs(root)]


def load_pages(section: str, root: Path | None = None) -> list[Page]:
    """Load every page in a section, sorted by `order`."""
    base = root or REPO_ROOT
    pages: list[Page] = []
    for path in sorted((base / f"_{section}").glob("*.md")):
        front, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        pages.append(
            Page(path=path, section=section, slug=path.stem, front=front, body=body)
        )
    pages.sort(key=lambda page: page.front.get("order") or 0)
    return pages
