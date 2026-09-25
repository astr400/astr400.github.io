---
title: Configuring Git on the SFSU virtual machine
short_title: Git on the SFSU VM
nav: VM Git
pill: Remote host
description: Set your Git identity and a GitHub SSH key on the SFSU VM account.
branch: main
order: 8
step: 6
step_title: Git on the SFSU VM
summary: On jmbrewer, set your name, email, and a GitHub key that stays on that machine.
link_text: Configure Git on the VM
note: The next step, Docker, is optional. You do not need it to log in to the VM or to run MESA there.
---

[Git](/setup/git/) configures your computer. This page configures the account on `jmbrewer` after [the VM login](/setup/sfsu-vm/) works. The laptop's `git config` and GitHub key are not on that machine.

Everyday Git commands stay on the [Git](/setup/git/) page.

## 1. Identity on that account

While logged in to the virtual machine:

```bash
git config --global user.name "YOUR_FIRSTNAME YOUR_LASTNAME"
git config --global user.email "YOUR_EMAIL_ADDRESS"
git config --global init.defaultBranch main
git config --global core.editor pico
```

`pico` is the editor the other VM steps use. Do not point `core.editor` at VS Code. That program is not installed on the VM.

## 2. A key that lives on the VM

This is a different computer from your laptop, so it gets its own key. Do not copy the laptop private key onto the server.

On the virtual machine:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept `~/.ssh/id_ed25519` on the VM, and choose a passphrase.

Show the public key and add it in GitHub under **Settings** → **SSH and GPG keys** → **New SSH key**:

```bash
cat ~/.ssh/id_ed25519.pub
```

From the VM, test the connection:

```bash
ssh -T git@github.com
```
