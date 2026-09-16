---
title: Toolchain setup for scientific Python
short_title: Toolchain setup
nav: Toolchain
pill: Compiler setup
description: Install the system compiler tools needed for scientific Python and astrophysics work on macOS, Linux, and Windows.
branch: main
order: 1
step: 1
step_title: Toolchain (optional)
summary: Install compilers if you will build scientific packages with native extensions.
link_text: Toolchain setup
note: Choosing uv instead of Conda? Continue to [uv setup](/setup/uv/) after this page.
redirect_from:
  - /toolchain_setup.html
---

Some scientific Python packages, especially those with compiled extensions, need a working C/C++ toolchain. Install the compiler tools for your operating system before building packages. Skip this page if you only install pre-built wheels and never compile extensions.

## macOS

Install Xcode Command Line Tools, or the full Xcode developer environment from [Apple](https://developer.apple.com/xcode/):

```bash
xcode-select --install
```

## Linux

On Ubuntu or Debian-based systems, install the base build tools:

```bash
sudo apt update
sudo apt install build-essential
```

## Windows

Use WSL 2 with Ubuntu or another supported Linux distribution, then install the Linux build tools inside the WSL terminal. See the [WSL installation guide](https://learn.microsoft.com/en-us/windows/wsl/install).

```bash
sudo apt update
sudo apt install build-essential
```

## Why this matters

- Some Python packages compile native code for speed or numerical performance.
- Compilers are often required for data analysis and scientific computing libraries.
- Installing the toolchain early avoids later build errors.
