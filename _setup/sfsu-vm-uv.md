---
title: Using uv on the SFSU virtual machine
short_title: uv on the SFSU VM
nav: VM uv
pill: Remote host
description: On the SFSU VM you have no administrator rights, so use uv in your home directory instead of system pip.
branch: alt
order: 7
step: 5
link_text: uv on the server (optional)
---

Your account on the [SFSU virtual machine](/setup/sfsu-vm/) cannot run `sudo`, so `apt install` and `pip install` into the system Python will fail. `uv` is optional here because it installs into your home directory and creates a personal environment, with no administrator rights. It is not the laptop [uv](/setup/uv/) workflow. Do it only after you can log in. The environment is `$HOME/.venvs/main`, and a new shell activates it for you.

## 1. Install uv

On the virtual machine:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv --version
```

The `PATH` line is written into `~/.bashrc` in the next card, so later logins find `uv` without the export.

## 2. Create the environment

```bash
mkdir -p "$HOME/.venvs"
uv venv "$HOME/.venvs/main" --python 3.12
```

If Python 3.12 is not already on the system, ask `uv` for a private copy, then create the environment again:

```bash
uv python install 3.12
uv venv "$HOME/.venvs/main" --python 3.12
```

## 3. Activate it from Bash

Append this to `~/.bashrc` on the virtual machine:

```text
# Make uv available
export PATH="$HOME/.local/bin:$PATH"

# Activate my default uv-managed environment
if [ -f "$HOME/.venvs/main/bin/activate" ]; then
    source "$HOME/.venvs/main/bin/activate"
fi
```

Reload it:

```bash
source ~/.bashrc
```

`echo "$VIRTUAL_ENV"` should print a path ending in `.venvs/main`.

## 4. Install a package

With the environment active:

```bash
uv pip install mesa_reader
```

Check it:

```bash
python -c "import mesa_reader; print(mesa_reader.__file__)"
```

For a project on your own computer, with `uv sync` and `uv run`, use the [uv](/setup/uv/) page instead of this account-wide environment.
