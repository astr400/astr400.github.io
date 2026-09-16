---
title: Installing Docker Desktop on Windows with WSL
short_title: Docker on Windows
nav: Docker Windows
pill: Containers
description: Install WSL 2 with Ubuntu and Docker Desktop, then run docker from the Ubuntu terminal.
branch: alt
order: 9
step: 5
link_text: Docker Desktop on Windows (WSL)
---

On Windows, install **Docker Desktop** with the WSL 2 backend. Run `docker` from a **WSL Ubuntu** terminal, not from PowerShell, so paths and line endings match Linux images. Do not also install Docker Engine inside that Ubuntu distro while Desktop is running; the two stacks conflict. Official references: [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/), [WSL integration](https://docs.docker.com/desktop/features/wsl/), [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

## 1. Install WSL 2 and Ubuntu

In Windows PowerShell or Terminal **as Administrator**:

```bash
wsl --install
```

Reboot when Windows asks. The default distro is Ubuntu. Open **Ubuntu** from the Start menu once, and create your Linux username and password.

If WSL is already installed, update it, then confirm the distro is version 2:

```bash
wsl --update
wsl -l -v
```

## 2. Install Docker Desktop

Download and run [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/). Keep **Use WSL 2 instead of Hyper-V** selected. Start Docker Desktop from the Start menu and wait until it reports that the engine is running.

## 3. Enable Ubuntu integration

In Docker Desktop, open **Settings** → **Resources** → **WSL integration**. Enable integration for your Ubuntu distro, then **Apply & Restart**.

Leave the `docker-desktop` distros that Docker creates alone; they are not your working environment.

## 4. Confirm from Ubuntu

Open the Ubuntu terminal (Windows Terminal is fine if the profile is Ubuntu):

```bash
docker version
docker run --rm hello-world
```

You should see Client and Server details, then the hello-world message. Continue with [running images](/use/docker/).
