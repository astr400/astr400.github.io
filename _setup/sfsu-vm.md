---
title: Connecting to the SFSU virtual machine
short_title: SFSU VM
nav: SFSU VM
pill: Remote host
description: Reach the SFSU course VM over the campus VPN and SSH, then point your account at the shared MESA install.
branch: main
order: 6
step: 5
step_title: SFSU virtual machine
summary: On jmbrewer, the remote host where MESA runs. VPN, SSH, and the shared install.
link_text: Connect to the VM
---

MESA for this course runs on an SFSU virtual machine, `jmbrewer.rcc.at.sfsu.edu`, not on your laptop. Do this once from your own computer, then once while logged in. You do not need [Docker](/setup/docker/). Replace `userid` with your SFSU id.

Compile and run (`./mk`, `./rn`) are in the [MESA running guide](https://docs.mesastar.org/en/latest/using_mesa/running.html). After the account steps below, `~/star_tmpl` is the directory you copy for each new model.

## 1. VPN

Skip this if you are already on campus.

Download GlobalProtect from [gp-students.sfsu.edu](https://gp-students.sfsu.edu). Sign in with your SF State ID and password, then run the installer for your system from your downloads folder.

Launch GlobalProtect. Set the portal address to `gp-students.sfsu.edu` and connect. Sign in again with your SF State ID and password. The globe icon shows a checkmark when the tunnel is up.

## 2. SSH client

Linux and macOS already have an SSH client in the terminal.

On Windows, two common installs are [Cygwin](https://www.cygwin.com/) and the [Windows Subsystem for Linux](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux). WSL is the one that also includes X11, which the next card needs.

## 3. X11

X11 is what lets a plot window on the VM open on your computer.

Linux already has it. WSL includes it. On macOS, install the latest [XQuartz](https://www.xquartz.org/).

## 4. Connect

Be on campus, or on the VPN. Log in with X11 forwarding:

```bash
ssh -X userid@jmbrewer.rcc.at.sfsu.edu
```

Reuse the Ed25519 key from [Git](/setup/git/). Install that public key on the VM once. This login still asks for your account password:

```bash
ssh-copy-id userid@jmbrewer.rcc.at.sfsu.edu
```

Do not generate another key at `~/.ssh/id_ed25519` on your computer, and do not leave the passphrase empty to avoid a prompt. That file is already your GitHub key.

After `ssh-copy-id`, you can shorten later logins. On your computer, add this to `~/.ssh/config`, with your id in place of `userid`:

```text
Host jmbrewer
    HostName jmbrewer.rcc.at.sfsu.edu
    User userid
    Port 22
    IdentityFile ~/.ssh/id_ed25519
    ForwardX11 yes
    ForwardX11Trusted yes
```

Then:

```bash
ssh jmbrewer
```

## 5. Shared MESA install

The account does not know where MESA is until you source it from the Bash startup file. On the virtual machine:

```bash
pico ~/.bashrc
```

Add this line:

```bash
source /opt/mesa/setup/mesa.sh
```

Load it in the current session, or log out and back in:

```bash
source ~/.bashrc
```

MESA downloads data into a cache. The default cache sits inside the shared MESA directory, so each account needs its own. On the virtual machine:

```bash
mkdir -p ~/mesa_caches/eosDT_cache \
  ~/mesa_caches/kap_cache \
  ~/mesa_caches/rates_cache
```

Copy the MESA star template into your home directory and point it at those caches:

```bash
cp -R $MESA_DIR/star/work ~/star_tmpl
pico ~/star_tmpl/inlist_project
```

Under the `&star_job` heading, add these lines. Use your id in place of `userid`:

```text
    eosDT_cache_dir = '/home/userid/mesa_caches/eosDT_cache'
    kap_cache_dir = '/home/userid/mesa_caches/kap_cache'
    rates_cache_dir = '/home/userid/mesa_caches/rates_cache'
```

Copy `~/star_tmpl` when you start a model. Editing that inlist further, and `./mk` / `./rn`, are in the [MESA running guide](https://docs.mesastar.org/en/latest/using_mesa/running.html).
