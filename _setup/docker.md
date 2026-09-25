---
title: Installing Docker
short_title: Docker setup
nav: Docker
pill: Containers
description: Choose your operating system and install Docker Engine or Docker Desktop, without MESA-specific usage.
branch: main
order: 9
step: 7
step_title: Docker (optional)
summary: Optional demo of a container workflow. Not required on your computer or on the SFSU VM.
link_text: Choose your operating system
note: MESA run commands, inlists, and image tags belong in the MESA Docker repository on Read the Docs, once that repo is published. This page only covers installing Docker itself.
---

Docker is optional. It shows what a container-based scientific workflow looks like: an application and its dependencies packed as an image that runs the same way on macOS, Linux, and Windows. You do not need it for ordinary scientific Python, and you do not need it for the [SFSU virtual machine](/setup/sfsu-vm/). Finish [Git](/setup/git/) and a [Python environment](/setup/conda/) first if you choose to try it.

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
