---
title: Running images and mounting files
short_title: Use Docker
nav: Docker
pill: Containers
description: Run container images, mount a work directory, and clean up unused images after Docker is installed.
branch: main
order: 2
step: 2
step_title: Docker
summary: Pull an image, run a container, and persist files with a bind mount. MESA-in-container usage lives with the image docs, not here.
link_text: Run an image and mount a folder
note: MESA run commands, inlists, and image tags belong in the MESA Docker repository on Read the Docs, once that repo is published. This page only covers Docker itself. Install the engine first at [Docker setup](/setup/docker/).
---

An **image** is the immutable snapshot (`docker pull`). A **container** is a running (or stopped) instance (`docker run`). A **volume** or bind mount is how you persist files when the container exits. Install Docker for your OS first: [Docker setup](/setup/docker/).

## 1. Verify the engine

Pull a tiny image and run it once. `--rm` deletes the container when it exits, so it does not clutter `docker ps -a`:

```bash
docker run --rm hello-world
```

You should see a message that the client reached the Docker daemon and pulled the `hello-world` image. On Linux Engine installs that still require `sudo`, prefix the command with `sudo` until you are in the `docker` group.

## 2. List images and containers

```bash
docker images
docker ps -a
```

Run an image interactively and destroy it on exit:

```bash
docker run --rm -it ubuntu:24.04 bash
```

## 3. Mount a host directory

Mount a directory you own so work survives the container. Replace `/path/on/host` with that path:

```bash
docker run --rm -it -v /path/on/host:/work ubuntu:24.04 bash
```

Inside the container, files under `/work` are the same files as on the host. On Docker Desktop for Mac and Windows, prefer a path inside your home directory; bind mounts outside it can fail or be slow.

## 4. Stop and clean up

Stop a runaway container from another terminal with `docker ps` to get the ID, then `docker stop` with that ID. Remove unused images when disk fills:

```bash
docker image prune
```

Official command reference: [docker run](https://docs.docker.com/reference/cli/docker/container/run/).

## MESA and other research images

This site is the gateway: it teaches Docker, Python, Git, and workflow. It does **not** document how to run MESA.

When the astr400 MESA Docker repository is published, its usage docs will live **in that repo** and on **Read the Docs**, versioned with image tags. Link there for `docker pull` of the MESA image, work directories, and MESA commands. Link back here for [installing Docker](/setup/docker/) and for this generic `docker run` pattern.

Until that URL exists, use the [MESA documentation](https://docs.mesastar.org/) for the code itself, and watch [astr400 on GitHub](https://github.com/astr400) for the image repository.
