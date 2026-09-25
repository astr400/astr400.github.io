---
title: Installing Docker Engine on Ubuntu
short_title: Docker on Ubuntu
nav: Docker Ubuntu
pill: Containers
description: Install Docker Engine from Docker's apt repository on Ubuntu, then optionally run docker without sudo.
branch: alt
order: 11
step: 7
link_text: Docker Engine on Ubuntu
note: Adding a user to the docker group grants root-equivalent privileges. Anyone in that group can run containers that access host files. Grant it only on machines you control.
---

Use Docker's own apt repository so you get current Engine, CLI, containerd, Buildx, and Compose packages. Ubuntu's `docker.io` package is older and is not the path this guide follows. Official reference: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/).

## 1. Install dependencies

```bash
sudo apt update
sudo apt install -y ca-certificates curl
```

## 2. Add Docker's GPG key

```bash
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

## 3. Add the Docker apt repository

This reads your Ubuntu codename from `/etc/os-release` (for example `noble` on 24.04). Do not hardcode a release name.

```bash
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
```

## 4. Install Docker Engine and plugins

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 5. Verify the engine

```bash
sudo systemctl status docker
sudo docker run --rm hello-world
```

You should see that the service is active and that the client pulled and ran `hello-world`. Everyday commands are on [running images](/use/docker/).

## 6. Optional: run Docker without sudo

Create the `docker` group if needed and add your user:

```bash
sudo groupadd docker
sudo usermod -aG docker "$USER"
```

If `groupadd` reports that the group already exists, continue with `usermod`. Log out and back in (or reboot) so the group change applies. `newgrp docker` activates it in the current shell only:

```bash
newgrp docker
docker run --rm hello-world
```

That last command must work **without** `sudo`.

## Troubleshooting: Debian repository by mistake

If a previous attempt pointed apt at `download.docker.com/linux/debian` instead of Ubuntu, rewrite those list files, then repeat the repository and install steps:

```bash
sudo sed -i 's|download.docker.com/linux/debian|download.docker.com/linux/ubuntu|g' /etc/apt/sources.list.d/docker*
sudo apt update
```
