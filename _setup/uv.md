---
title: Using uv for astrophysics projects
short_title: uv setup
nav: uv
pill: uv project template
description: Guide to using uv for reproducible Python environments in astrophysics workflows.
order: 3
step: 2
branch: alt
link_text: uv workflow
redirect_from:
  - /uv_setup.html
---

uv is an alternative to Conda: a lightweight, reproducible Python environment for notebooks and analysis scripts. Use Python 3.12+, keep the project as an environment rather than a published library, and rely on `uv` for dependency management and execution.

## Overview

This pattern is designed for:

- Jupyter notebooks and exploratory analysis
- Scientific computing with `astropy`, `scipy`, `numpy`, `sympy`, and `pandas`
- Plotting with `matplotlib`
- Reproducible workflows using `uv sync` and `uv run`
- Course or research repositories without packaging overhead

## Install uv

Install `uv` before creating a project environment. The official install guide is the [Astral uv installation page](https://docs.astral.sh/uv/getting-started/installation/).

### macOS

```bash
brew install uv
```

If you do not use Homebrew, the official installer also works:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, open a new terminal or reload your shell so the `uv` command is in your PATH.

### Windows (WSL 2)

Install uv inside your WSL 2 Linux environment rather than in PowerShell:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then reopen the terminal and verify:

```bash
uv --version
```

## Recommended layout

```text
.
├── data/
├── notebooks/
├── scripts/
├── README.md
├── pyproject.toml
├── uv.lock
└── .gitignore
```

## Quick start

```bash
uv init astrolab --python 3.12 --bare --no-readme
cd astrolab
uv add astropy ipykernel jupyterlab matplotlib pandas scipy sympy
uv add --dev pytest ruff
uv sync
```

### Run notebooks

```bash
uv run jupyter lab
```

### Run tests

```bash
uv run pytest
```

### Lint the project

```bash
uv run ruff check .
```

### Run a script

```bash
uv run python scripts/example.py
```

## VS Code kernel integration

To make the environment available as a Jupyter kernel in VS Code:

```bash
uv run python -m ipykernel install --user --name astrolab
```

Then in VS Code:

1. Open a notebook.
2. Click the kernel selector in the top-right corner.
3. Choose `astrolab` or select the project interpreter at `.venv/bin/python`.
4. Verify the kernel is correct with:

```python
import sys
print(sys.executable)
```

This should point to the project-local environment, typically under `.venv/bin/python`.

## Project configuration pattern

A typical `pyproject.toml` for this workflow looks like:

```text
[project]
requires-python = ">=3.12"

[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "ruff>=0.3.0",
]

[tool.uv]
package = false
```

This keeps the project as a managed environment rather than an installable package.

## Verification checklist

After setup, confirm the environment works with:

```bash
uv sync
uv run python -c "import astropy, matplotlib, pandas, scipy, sympy; print('ok')"
uv run jupyter lab --version
uv run pytest -q
uv run ruff check .
```

## Notes

- Prefer `uv run` over activating the virtual environment manually.
- Keep runtime and development dependencies separated.
- Use this pattern for coursework, labs, and data-analysis workflows rather than for publishing a library.
- If a project needs more packages later, add them with `uv add package-name` and lock them with `uv sync`.
