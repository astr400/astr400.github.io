---
title: Install Miniconda and create an environment
short_title: Conda setup
nav: Conda
pill: Python environment
description: Install Miniconda, create a Python 3.12 environment, and manage conda environments for astrophysics work.
branch: main
order: 2
step: 2
step_title: Python environment
summary: Create a dedicated Python 3.12 environment. Conda is the default path; uv is a faster alternative.
link_text: Miniconda / Anaconda
redirect_from:
  - /conda_setup.html
---

This is the default path. Install Miniconda, then create a Python 3.12 environment with the scientific packages used in astrophysics analysis. Prefer [uv](/setup/uv/) if you want a lighter, project-local workflow instead.

## 1. Install Miniconda

Use the official installer for your operating system: [Miniconda install guide](https://docs.conda.io/en/latest/miniconda.html).

### macOS

If you use Homebrew:

```bash
brew install --cask miniconda
```

Or download the installer from the Miniconda guide and run it, then initialize conda:

```bash
conda init
```

### Linux

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
conda init
```

### Windows

Install [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install) first, then install Miniconda inside the Linux environment using the Linux commands above. Reopen the terminal after `conda init`.

## 2. Optional: install a compiler toolchain

Some scientific packages need C/C++ compilers. Install the tools for your platform before building packages.

[Toolchain setup guide](/setup/toolchain/)

## 3. Create and activate a conda environment

Create a project environment for astrophysics work:

```bash
conda create -n astro-python python=3.12
```

Activate it:

```bash
conda activate astro-python
```

Install the core scientific tools:

```bash
conda install -c conda-forge jupyterlab matplotlib numpy scipy pandas astropy
```

To leave the environment later:

```bash
conda deactivate
```

## 4. Manage conda environments

The active environment appears in your shell prompt, for example `(astro-python)`. You can also list environments; the current one is marked with `*`:

```bash
conda env list
```

`conda info --envs` shows the same list.

Activate and deactivate an environment:

```bash
conda activate astro-python
conda deactivate
```

List packages installed in the current environment:

```bash
conda list
```

Add another package later:

```bash
conda install -c conda-forge package-name
```

Export the current environment so someone else can recreate it:

```bash
conda env export > environment.yml
```

Remove an environment. Deactivate it first if it is active. This deletes the whole environment, not a single package:

```bash
conda deactivate
conda env remove -n astro-python
```

`conda remove -n astro-python --all` does the same thing.

Official reference: [Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## Alternative: uv

If you prefer a modern, project-local environment without a global conda install, use [uv](/setup/uv/) instead of this page.
