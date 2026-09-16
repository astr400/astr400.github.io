---
title: Installing Docker Desktop on macOS
short_title: Docker on macOS
nav: Docker macOS
pill: Containers
description: Install Docker Desktop on macOS with Homebrew or the official installer, then confirm the engine is running.
branch: alt
order: 7
step: 5
link_text: Docker Desktop on macOS
---

Docker Desktop is the usual choice on a Mac. It provides the engine, the `docker` CLI, and Compose. Apple Silicon and Intel Macs both work; pick the installer that matches your chip if you download from Docker rather than Homebrew.

## 1. Install Docker Desktop

If you use Homebrew:

```bash
brew install --cask docker
```

Otherwise download Docker Desktop from the [macOS install guide](https://docs.docker.com/desktop/setup/install/mac-install/) and complete the installer.

## 2. Start the engine

Open **Docker** from Applications. Wait until the menu-bar whale shows that Docker Desktop is running. The CLI does not work until that engine is up.

## 3. Confirm the install

In a terminal:

```bash
docker version
```

You should see both Client and Server sections. Then continue with [running images](/use/docker/).
