---
title: Project workflow for astrophysics analysis
short_title: Project workflow
nav: Workflow
pill: Project structure
description: Recommended project workflow for astrophysics coding and analysis with Python, notebooks, Git, and reproducible practices.
branch: main
order: 6
step: 5
step_title: Project workflow
summary: Keep data, notebooks, scripts, and results organized and reproducible.
link_text: Recommended layout and cycle
redirect_from:
  - /project_workflow.html
---

A good project workflow keeps your data, code, notebooks, and results organized while making it easier to share and reproduce work.

## Recommended layout

```text
project/
├── notebooks/
├── scripts/
├── data/
├── results/
├── README.md
├── .gitignore
├── environment.yml   # or pyproject.toml / uv.lock
└── .venv/
```

## Good habits

- Use notebooks for exploration and figures
- Move reusable code into scripts or modules
- Record dependencies and environment setup in a reproducible format
- Commit often and push to GitHub before sharing
- Document assumptions, data sources, and processing steps

## Typical cycle

1. Create or activate the project environment
2. Open the notebook or script in VS Code
3. Run analysis and generate figures
4. Move cleaned-up logic into a script or module
5. Commit the updates and push them to GitHub
