# Astrophysics Computing Set-Up

This page provides the core software setup needed for astrophysics work, scientific computing, and data analysis. The primary workflow is to set up the required OS-specific tools, install compiler support, create a Python environment, and configure Git and VS Code. Advanced topics such as manual Python installation or the `uv` workflow are useful follow-up options, but they are not the main starting point.

## Before you begin

Please follow these instructions carefully. This workflow is meant for a local development environment on your own computer or laptop. If you are on macOS or Linux and already have Miniconda or Anaconda installed, you can skip the installation step and continue with the compiler section. If you are using Windows, we recommend installing WSL 2 so that your environment matches the scientific computing stack used in this course.

```{admonition} Windows users take note
:class: caution

If you are working on a Windows computer, we recommend installing Windows Subsystem for Linux (WSL) 2 for this workflow.
If you are using Windows 11, WSL 2 is fully supported.
If you are using Windows 10, see the Microsoft installation notes for WSL 2 requirements.
```

## Installing Miniconda and compiler tools

Click the appropriate section for your operating system to see the setup instructions.

### Mac OS

Download and run the Miniconda installer from the official documentation:

- https://docs.conda.io/en/latest/miniconda.html

Install Xcode for compiler support:

- https://developer.apple.com/xcode/

### Linux

Download and run the Miniconda installer from the official documentation:

- https://docs.conda.io/en/latest/miniconda.html

After installing Miniconda, install compilers for C and C++ work using:

```bash
sudo apt update
sudo apt install build-essential
```

### Windows

If your computer uses Windows, install WSL 2 first and choose Ubuntu 22.04 or another supported Linux distribution.

- https://learn.microsoft.com/en-us/windows/wsl/install

Once WSL is installed, open the Ubuntu terminal. This opens a Linux environment inside Windows. You must install Miniconda within that Linux environment.

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

After installation, close and reopen the terminal. If you do not see `(base)` in your prompt, run:

```bash
conda init
```

Then install the compiler toolchain:

```bash
sudo apt update
sudo apt install build-essential
```

## Creating a conda environment

Everyone should complete this section after installing Miniconda.

Create a conda environment for scientific Python work:

```bash
conda create -n astro-python python=3.11
```

Activate it:

```bash
conda activate astro-python
```

Install the scientific Python libraries commonly used in astrophysics and data analysis:

```bash
conda install -c conda-forge jupyterlab matplotlib numpy scipy pandas astropy
```

To deactivate the environment later:

```bash
conda deactivate
```

## Installing and configuring Git

Git is required for version control and collaboration.

Check whether Git is installed:

```bash
git --version
```

If needed, install it with conda:

```bash
conda install -c conda-forge git
```

Then configure your identity and default branch:

```bash
git config --global user.name "YOUR_FIRSTNAME YOUR_LASTNAME"
git config --global user.email "YOUR_EMAIL_ADDRESS"
git config --global init.defaultBranch main
```

Set VS Code as the default editor for Git commands:

```bash
git config --global core.editor "code --wait"
```

## Installing a text editor

We recommend using Visual Studio Code as the primary editor for scientific computing and astrophysics projects.

- https://code.visualstudio.com/

Install the Python extension after installation. If you are using WSL or remote development, install the VS Code WSL extension as needed.

## Creating a GitHub account

If you do not yet have a GitHub account, create one at:

- https://github.com/

When creating your GitHub username, remember that this is often a professional profile where you can showcase work. Choose a username that is recognizable and appropriate for research or coursework.

### GitHub SSH setup

GitHub recommends using SSH rather than a password for command-line access.

Follow the official instructions here:

- https://docs.github.com/en/authentication/connecting-to-github-with-ssh

After you add an SSH key, test it with:

```bash
ssh -T git@github.com
```

This should return a success message with your GitHub username.

## Advanced options

These are useful if you prefer a custom Python installation or a modern reproducible workflow:

- manual Python installation from: https://www.python.org/downloads/
- use `python3 -m venv .venv` for a lightweight virtual environment
- use the `uv` workflow for reproducible environment management, as described in the UV setup page

## Recommended project workflow

A simple astrophysics project layout looks like this:

```text
project/
├── notebooks/
├── scripts/
├── data/
├── README.md
├── .gitignore
└── .venv/
```

For everyday work:

- keep notebooks and scripts under version control
- commit often with clear messages
- push changes to GitHub before sharing results
- use a consistent environment across machines when possible

## Useful references

- https://docs.python.org/3/tutorial/
- https://jupyter.org/
- https://git-scm.com/doc
- https://docs.github.com/
- https://code.visualstudio.com/

## Summary

By the end of this setup process, you should have:

- Python installed through Miniconda or an equivalent environment manager
- compiler support installed for your OS
- Git configured
- VS Code installed
- a working Python environment for scientific work
- a GitHub account and SSH key configured
- a local workflow for analysis and project repositories

This is the foundation for the scientific Python, data analysis, visualization, and modeling work used in astrophysics research and coursework.

