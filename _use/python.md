---
title: Using a Python environment
short_title: Use Python
nav: Python
pill: Environments
description: Activate Conda or uv environments, launch Jupyter, and install packages after the tools are on your machine.
branch: main
order: 1
step: 1
step_title: Python environment
summary: Activate the environment you installed, launch Jupyter, and add packages as the project grows.
link_text: Activate Conda or uv
---

This page is daily use after install. For Miniconda itself see [Conda setup](/setup/conda/). For a project-local manager see [uv](/setup/uv/). Pick one manager and stay with it in a given project.

## 1. Activate the environment

### Conda

```bash
conda activate astro-python
```

The active environment appears in your shell prompt, for example `(astro-python)`. List environments with `conda env list`; the current one is marked with `*`.

To leave it:

```bash
conda deactivate
```

### uv

Prefer `uv run` over activating by hand. From the project directory:

```bash
uv sync
uv run python -c "import astropy; print('ok')"
```

If you do need a shell inside the project environment:

```bash
uv run bash
```

## 2. Launch Jupyter

### Conda

With the environment active:

```bash
jupyter lab
```

### uv

```bash
uv run jupyter lab
```

In VS Code, choose **Python: Select Interpreter** and pick the Conda env or the project `.venv`. For a named Jupyter kernel with uv:

```bash
uv run python -m ipykernel install --user --name astrolab
```

Then select that kernel in the notebook.

## 3. Install another package

### Conda

```bash
conda install -c conda-forge package-name
```

Export the environment so someone else can recreate it:

```bash
conda env export > environment.yml
```

### uv

```bash
uv add package-name
uv sync
```

## 4. Editor and notebooks

Install VS Code and the Jupyter extension on the [Editor](/setup/editor/) page. Use notebooks for exploration, then move reusable code into scripts as described in [project workflow](/use/workflow/).
