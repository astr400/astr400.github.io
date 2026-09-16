---
name: mesa-docker-docs
description: Protocol for MESA-in-container documentation in the MESA Docker repository on Read the Docs, including versioning with image tags and linking back to the astr400.github.io gateway. Use when creating that Docker repo, adding Sphinx or MkDocs docs, configuring Read the Docs, or when a request would put MESA usage on the Jekyll gateway.
---

# MESA Docker docs

The gateway ([`AGENTS.md`](../../../AGENTS.md) publishing map) stays on GitHub Pages. **MESA usage** is software docs: author it next to the Dockerfiles and publish on Read the Docs.

## Protocol

1. Create the docs in the **MESA Docker repo**, not under `_setup/` on astr400.github.io.
2. Pick **one** engine: Sphinx with [MyST](https://mystmd.org/) Markdown, or MkDocs. Do not also invent a Jekyll site in that repo.
3. Add a Read the Docs config (`.readthedocs.yaml`) that installs the docs dependencies and builds HTML. Enable **versioning from git tags** that match image tags.
4. Document image pull, work directories, `docker run` mounts, and MESA commands there.
5. Link **back** to the gateway for prerequisites: [Docker install](https://astr400.github.io/setup/docker/), [generic docker run](https://astr400.github.io/use/docker/), [Python](https://astr400.github.io/setup/conda/), [Git](https://astr400.github.io/setup/git/). Do not copy those pages.
6. When the RTD URL exists, add it to the gateway [`_data/resources.yml`](../../../_data/resources.yml) and replace the placeholder on [`_setup/docker.md`](../../../_setup/docker.md).

## Do not

- Migrate astr400.github.io to Read the Docs to get a version switcher.
- Put inlists, `mesa_star` walkthroughs, or tag matrices on the gateway.
- Duplicate the gateway night-sky theme; RTD project docs may use a default Sphinx or MkDocs theme.
- Publish astro-study notebooks through this RTD project unless they are MESA tutorials that belong with the image.
