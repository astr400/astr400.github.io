---
title: Installing Docker
short_title: Docker setup
nav: Docker
pill: Containers
description: Choose your operating system and install Docker Engine or Docker Desktop, without MESA-specific usage.
branch: main
order: 6
step: 5
step_title: Docker (optional)
summary: Install Docker for macOS, Ubuntu, or Windows with WSL. Everyday docker run commands live under Use.
link_text: Choose your operating system
note: MESA run commands, inlists, and image tags belong in the MESA Docker repository on Read the Docs, once that repo is published. This page only covers installing Docker itself.
---

Docker packages an application and its dependencies as an image you can run the same way on macOS, Linux, and Windows. Use it when software is hard to compile locally. Finish [Git](/setup/git/) and a [Python environment](/setup/conda/) first if you also work in notebooks; you do not need Docker for ordinary scientific Python.

## Pick your operating system

Follow the install page for the machine in front of you, then come back here for what to do next.

- [Docker Desktop on macOS](/setup/docker-macos/)
- [Docker Engine on Ubuntu](/setup/docker-ubuntu/)
- [Docker Desktop on Windows with WSL](/setup/docker-windows/)

On a campus Linux lab machine that is not Ubuntu, use the matching [Docker Engine install guide](https://docs.docker.com/engine/install/) for that distribution.

## After it runs

Confirm the client can talk to the engine, then learn the few commands you will reuse for any image:

- [Run an image and mount a folder](/use/docker/)

Keep MESA-in-container walkthroughs on Read the Docs when that repository is published. The same `docker run` pattern works for any image; only the image name and mounts change.
