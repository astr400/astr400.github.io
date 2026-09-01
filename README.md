# Astrophysics Setup Guide

This repository hosts a static site for astrophysics computing setup, environment management, and project workflows.

## GitHub Pages deployment

To publish the site with a GitHub Pages repository:

1. Create a repository named `your-username.github.io` for a personal page or `your-org.github.io` for an organization page.
2. Push the contents of this repository to the main branch.
3. Open the repository settings, then go to Pages.
4. Set the source to the root of the `main` branch, or to the `docs/` folder if you copy the site there.
5. Save the settings. GitHub will publish the site at:
   - `https://your-username.github.io/`
   - or `https://your-org.github.io/`

## Local preview

From the project root, run:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/`.

## Site structure

- `index.html` — landing page and recommended setup order
- `toolchain_setup.html` — optional compiler toolchain
- `conda_setup.html` — Miniconda / Anaconda environment
- `uv_setup.html` — uv workflow (alternative to Conda)
- `editor_setup.html` — Jupyter and VS Code
- `git_setup.html` — Git and GitHub
- `project_workflow.html` — project layout and habits
- `assets/` — shared CSS, JavaScript, and branding

## Notes

- This site is intentionally static and easy to deploy as a simple GitHub Pages project.
- All page assets are local to the repository so the site remains self-contained and link-safe.
- The repository does not depend on any missing legacy templates or external branding.
