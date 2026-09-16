---
title: Installing and configuring Git
short_title: Git setup
nav: Git
pill: Version control
description: Guide to installing and configuring Git and GitHub for astrophysics projects.
branch: main
order: 5
step: 4
step_title: Git
summary: Install Git, set your identity, and connect to GitHub.
link_text: Git and GitHub setup
redirect_from:
  - /git_setup.html
---

Git helps you track changes to code, notebooks, papers, and data-processing scripts. It is an essential part of an organized astrophysics workflow.

## 1. Install Git

Check whether Git is already installed:

```bash
git --version
```

If it is not installed, pick one of these:

### macOS

```bash
brew install git
```

### Linux

```bash
sudo apt update
sudo apt install git
```

### Conda

```bash
conda install -c conda-forge git
```

On Windows, install Git inside WSL 2 using the Linux commands.

## 2. Set your identity

```bash
git config --global user.name "YOUR_FIRSTNAME YOUR_LASTNAME"
git config --global user.email "YOUR_EMAIL_ADDRESS"
git config --global init.defaultBranch main
```

## 3. Set VS Code as the Git editor

```bash
git config --global core.editor "code --wait"
```

## 4. Create a GitHub account and add an SSH key

Create a free account at [GitHub](https://github.com/).

For command-line access, use SSH keys instead of a password. On your machine, generate an SSH key pair:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept the default file location, and choose a secure passphrase if prompted.

Start the SSH agent and add the key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Copy the public key to your clipboard:

```bash
cat ~/.ssh/id_ed25519.pub
```

Then in GitHub, open **Settings** → **SSH and GPG keys** → **New SSH key**, paste the key, and save it.

Finally, test the connection:

```bash
ssh -T git@github.com
```

If you are on Windows, run these steps in Git Bash or inside WSL 2 so the SSH agent and key files behave correctly.

## Useful commands

```bash
git clone <repository-url>
git status
git add .
git commit -m "Add analysis notebook"
git push
```
