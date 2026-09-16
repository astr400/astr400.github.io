# uv Astrophysics Project Template

This repository is intended as a lightweight, reproducible environment for astrophysics coursework, scientific notebooks, and analysis scripts. It follows the same model as the existing non-package project in [src/pyproject.toml](src/pyproject.toml): use Python 3.12+, keep the project as an environment instead of a library, and rely on `uv` for dependency management and execution.

## Overview

The template is designed for:

- Jupyter notebooks and exploratory analysis
- scientific computing with `astropy`, `scipy`, `numpy`, `sympy`, and `pandas`
- plotting and visualization with `matplotlib`
- reproducible workflows using `uv sync` and `uv run`
- simple course or research repositories without packaging overhead

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
uv init astro-template --python 3.12 --bare --no-readme
cd astro-template
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
uv run python -m ipykernel install --user --name astro-template
```

Then in VS Code:

1. Open a notebook.
2. Click the kernel selector in the top-right corner.
3. Choose `astro-template` or select the project interpreter at `.venv/bin/python`.
4. Verify the kernel is correct with:

```python
import sys
print(sys.executable)
```

This should point to the project-local environment, typically under `.venv/bin/python`.

## Project configuration pattern

The reference project uses:

```toml
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

This ensures the project behaves like a managed environment and not an installable package.

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
- Use this template for coursework, labs, and data-analysis workflows rather than for publishing a library.
- If a project needs more packages later, add them with `uv add package-name` and lock them with `uv sync`.

## Related references

- [src/pyproject.toml](src/pyproject.toml)
- [src/README.md](src/README.md)
- [src/.gitignore](src/.gitignore)
