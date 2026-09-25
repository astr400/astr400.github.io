#!/usr/bin/env python3
"""Validate site content before a pull request.

Guards the invariants that the layouts depend on and that hand-written HTML used
to get wrong: the frontmatter contract, a single consistent page order, no raw
HTML in content, resolvable internal links, and preserved legacy URLs.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from sitelib import REPO_ROOT, Page, load_pages, parse_frontmatter, section_names, split_fences

REQUIRED_KEYS = (
    "title",
    "nav",
    "pill",
    "description",
    "branch",
    "order",
    "step",
    "link_text",
)

VALID_BRANCHES = ("main", "alt")

# `layout` comes from _config.yml defaults and `permalink` from the collection
# or hub path defaults. A page setting either is drifting from the contract.
FORBIDDEN_KEYS = ("permalink", "layout")

# URLs the site published as hand-written HTML. Each must stay reachable.
LEGACY_URLS = (
    "/toolchain_setup.html",
    "/conda_setup.html",
    "/uv_setup.html",
    "/editor_setup.html",
    "/git_setup.html",
    "/project_workflow.html",
)

HTML_TAG_RE = re.compile(r"</?[A-Za-z][A-Za-z0-9]*(?:\s[^>]*)?/?>")
LINK_RE = re.compile(r"\]\((/[^)\s]*)\)")
H1_RE = re.compile(r"^#\s", re.MULTILINE)
TODO_RE = re.compile(r"\bTODO\b")
COLLECTION_RE = re.compile(r"(?m)^[ \t]*collection:[ \t]*([A-Za-z0-9_-]+)[ \t]*$")


def hub_entries(root: Path) -> list[tuple[str, str]]:
    """Hub files implied by section directories: `setup.md` at `/setup/`."""
    return [(f"{name}.md", f"/{name}/") for name in section_names(root)]


class Report:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []
        self.failed = False

    def add(self, check: str, ok: bool, detail: str = "") -> None:
        self.rows.append((check, "pass" if ok else "fail", detail))
        if not ok:
            self.failed = True

    def render(self) -> str:
        width = max(len(row[0]) for row in self.rows)
        lines = []
        for check, result, detail in self.rows:
            suffix = f"  {detail}" if detail else ""
            lines.append(f"  {check.ljust(width)}  {result}{suffix}")
        return "\n".join(lines)


def _redirects(page: Page) -> list[str]:
    entries = page.front.get("redirect_from") or []
    if isinstance(entries, str):
        return [entries]
    return list(entries)


def known_urls(pages: list[Page], root: Path) -> set[str]:
    known = {"/"}
    known.update(url for _name, url in hub_entries(root))
    for page in pages:
        known.add(page.url)
        known.update(_redirects(page))
    return known


def check_frontmatter(pages: list[Page], report: Report) -> None:
    problems = []
    warnings = []
    for page in pages:
        title = page.front.get("title") or ""
        if len(title.split()) > 5 and not page.front.get("short_title"):
            warnings.append(f"{page.rel}: long title without short_title")
        missing = [key for key in REQUIRED_KEYS if page.front.get(key) in (None, "")]
        # An alternative path shares its step's catalog row, so it omits
        # step_title and summary. It still requires link_text.
        if page.front.get("branch") == "alt":
            missing = [key for key in missing if key not in ("step_title", "summary")]
        if missing:
            problems.append(f"{page.rel}: missing {', '.join(missing)}")
        present = [key for key in FORBIDDEN_KEYS if key in page.front]
        if present:
            problems.append(f"{page.rel}: must not set {', '.join(present)}")
        branch = page.front.get("branch")
        if branch is not None and branch not in VALID_BRANCHES:
            problems.append(f"{page.rel}: branch must be main or alt, got {branch!r}")
        if TODO_RE.search(str(page.front)):
            problems.append(f"{page.rel}: unfilled TODO in frontmatter")
    report.add("frontmatter contract", not problems, "; ".join(problems))
    report.add("titles fit a tab", not warnings, "; ".join(warnings))


def check_order(pages: list[Page], report: Report) -> None:
    problems = []
    seen: dict[int, str] = {}
    for page in pages:
        order = page.front.get("order")
        if order in seen:
            problems.append(f"order {order} used by both {seen[order]} and {page.rel}")
        else:
            seen[order] = page.rel
    report.add("unique order", not problems, "; ".join(problems))


def check_steps(pages: list[Page], report: Report) -> None:
    problems = []
    steps: dict[int, list[Page]] = {}
    for page in pages:
        steps.setdefault(page.front.get("step"), []).append(page)

    for step, group in sorted(steps.items(), key=lambda item: item[0] or 0):
        primaries = [p for p in group if p.front.get("step_title")]
        if len(primaries) != 1:
            names = ", ".join(p.rel for p in group)
            problems.append(
                f"step {step} needs exactly one page with step_title, found "
                f"{len(primaries)} among {names}"
            )
        for page in group:
            if page.front.get("step_title") and not page.front.get("summary"):
                problems.append(f"{page.rel}: step_title without summary")
            if not page.front.get("step_title") and page.front.get("branch") != "alt":
                problems.append(f"{page.rel}: shares a step but is not branch: alt")
    report.add("step grouping", not problems, "; ".join(problems))


def check_no_raw_html(pages: list[Page], report: Report) -> None:
    problems = []
    for page in pages:
        prose, _ = split_fences(page.body)
        tags = sorted(set(HTML_TAG_RE.findall(prose)))
        if tags:
            problems.append(f"{page.rel}: raw HTML {', '.join(tags)}")
    report.add("no raw HTML in content", not problems, "; ".join(problems))


def check_headings(pages: list[Page], report: Report) -> None:
    problems = []
    for page in pages:
        prose, _ = split_fences(page.body)
        if H1_RE.search(prose):
            problems.append(f"{page.rel}: uses '#' in the body; the h1 comes from title")
    report.add("heading levels", not problems, "; ".join(problems))


def check_fences(pages: list[Page], report: Report) -> None:
    problems = []
    for page in pages:
        _, fenced = split_fences(page.body)
        for line in fenced:
            if "<h2" in line:
                problems.append(f"{page.rel}: literal '<h2' in a code fence")
                break
    report.add("no <h2 in fences", not problems, "; ".join(problems))


def check_links(pages: list[Page], report: Report, root: Path, known: set[str]) -> None:
    problems = []
    docs: list[tuple[str, dict, str]] = [
        (page.rel, page.front, page.body) for page in pages
    ]
    for name, _url in hub_entries(root):
        path = root / name
        if path.exists():
            front, body = parse_frontmatter(path.read_text(encoding="utf-8"))
            docs.append((name, front, body))

    for rel, front, body in docs:
        targets = LINK_RE.findall(body)
        note = front.get("note")
        if isinstance(note, str):
            targets += LINK_RE.findall(note)
        for target in targets:
            if target in known:
                continue
            if target.startswith("/assets/"):
                if not (root / target.lstrip("/")).exists():
                    problems.append(f"{rel}: missing asset {target}")
                continue
            problems.append(f"{rel}: unresolved internal link {target}")
    report.add("internal links resolve", not problems, "; ".join(problems))


def check_redirects(pages: list[Page], report: Report) -> None:
    covered: dict[str, list[str]] = {}
    for page in pages:
        for entry in _redirects(page):
            covered.setdefault(entry, []).append(page.rel)

    problems = []
    for legacy in LEGACY_URLS:
        owners = covered.get(legacy, [])
        if not owners:
            problems.append(f"{legacy} has no redirect_from")
        elif len(owners) > 1:
            problems.append(f"{legacy} claimed by {', '.join(owners)}")
    report.add("legacy URLs redirect", not problems, "; ".join(problems))


def check_home(report: Report, root: Path) -> None:
    path = root / "index.md"
    if not path.exists():
        report.add("landing page", False, "index.md is missing")
        return
    front, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    problems = []
    if front.get("home") is not True or not front.get("title"):
        problems.append("index.md needs home: true and a title")
    prose, _ = split_fences(body)
    if H1_RE.search(prose):
        problems.append("index.md: uses '#' in the body; the h1 comes from title")
    report.add("landing page", not problems, "; ".join(problems))


def check_nav(report: Report, root: Path) -> None:
    path = root / "_data" / "nav.yml"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    declared = COLLECTION_RE.findall(text)
    sections = section_names(root)
    problems = []
    if not path.exists():
        problems.append("_data/nav.yml is missing")
    for section in sections:
        count = declared.count(section)
        if count == 0:
            problems.append(f"{section}: no collection line in _data/nav.yml")
        elif count > 1:
            problems.append(f"{section}: collection listed {count} times in _data/nav.yml")
    for name in declared:
        if name not in sections:
            problems.append(f"_data/nav.yml: collection {name} has no section directory")
    report.add("nav collections", not problems, "; ".join(problems))


def check_hubs(report: Report, root: Path) -> None:
    problems = []
    for name, _url in hub_entries(root):
        path = root / name
        if not path.exists():
            problems.append(f"{name} is missing")
            continue
        front, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not front.get("title"):
            problems.append(f"{name}: missing title")
        if not front.get("description"):
            problems.append(f"{name}: missing description")
        present = [key for key in FORBIDDEN_KEYS if key in front]
        if present:
            problems.append(f"{name}: must not set {', '.join(present)}")
        prose, _ = split_fences(body)
        if H1_RE.search(prose):
            problems.append(f"{name}: uses '#' in the body; the h1 comes from title")
        tags = sorted(set(HTML_TAG_RE.findall(prose)))
        if tags:
            problems.append(f"{name}: raw HTML {', '.join(tags)}")
    report.add("hub pages", not problems, "; ".join(problems))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("section", nargs="?", help="Check one section only")
    args = parser.parse_args(argv)

    root = REPO_ROOT
    all_sections = section_names(root)
    if not all_sections:
        print("No section directories found.", file=sys.stderr)
        return 1

    all_pages: list[Page] = []
    for section in all_sections:
        all_pages.extend(load_pages(section, root))
    known = known_urls(all_pages, root)

    sections = [args.section] if args.section else all_sections
    if args.section and args.section not in all_sections:
        print(f"unknown section {args.section!r}.", file=sys.stderr)
        return 1

    report = Report()
    check_home(report, root)
    check_hubs(report, root)
    check_nav(report, root)

    for section in sections:
        pages = load_pages(section, root)
        if not pages:
            report.add(f"{section}: pages found", False, "no Markdown pages")
            continue
        report.add(f"{section}: pages found", True, f"{len(pages)} pages")
        check_frontmatter(pages, report)
        check_order(pages, report)
        check_steps(pages, report)
        check_no_raw_html(pages, report)
        check_headings(pages, report)
        check_fences(pages, report)
        check_links(pages, report, root, known)

    check_redirects(all_pages, report)

    print(report.render())
    if report.failed:
        print("\ncheck_site: FAILED", file=sys.stderr)
        return 1
    print("\ncheck_site: all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
