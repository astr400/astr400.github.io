---
title: Using Jupyter and a text editor
short_title: Editor and Jupyter
nav: Editor
pill: Editor and notebooks
description: Guide to setting up Jupyter notebooks and a text editor for astrophysics work.
branch: main
order: 4
step: 3
step_title: Editor and Jupyter
summary: Use notebooks for exploration and VS Code for scripts and larger projects.
link_text: Jupyter and VS Code
note: Coming from uv? The previous step is [uv setup](/setup/uv/).
redirect_from:
  - /editor_setup.html
---

Most astrophysics work is easiest in a notebook for exploration and a text editor for scripts, modules, and larger projects. A common setup is VS Code with the Python extension plus Jupyter support.

## 1. Install a text editor

Visual Studio Code is a strong choice for scientific work: [code.visualstudio.com](https://code.visualstudio.com/).

After installation, open VS Code and install the Python extension and the Jupyter extension.

## 2. Install Jupyter

Install Jupyter in the environment you already created.

### Conda

```bash
conda install -c conda-forge jupyterlab
```

Launch notebooks:

```bash
jupyter lab
```

### uv

```bash
uv add jupyterlab
```

Launch notebooks through uv so they use the project environment:

```bash
uv run jupyter lab
```

## 3. Use the environment in VS Code

Select the right interpreter in VS Code:

- Open the Command Palette
- Choose Python: Select Interpreter
- Select the environment for your project

For a Jupyter kernel created by uv:

```bash
uv run python -m ipykernel install --user --name astro-template
```

## 4. Good workflow habits

- Use notebooks for exploration and quick visualization
- Move reusable code to scripts or modules
- Keep notes and figure generation in version control
- Use a consistent Python environment across notebooks and scripts
