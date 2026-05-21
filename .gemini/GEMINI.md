# GEMINI.md (Project Context)

## Project Overview
This repository manages the unified infrastructure for `iamrpdev.github.io`. The site is a professional developer portfolio, CV, and technical knowledge base utilizing a single-engine architecture.

- **Engine:** ProperDocs (community-supported fork of MkDocs 1.x)
- **Theme:** Material for MkDocs (Custom "Bare Metal" Aesthetic)
- **Integration Layer:** GitHub Actions CI/CD pipeline building from the `main` branch.

## Building and Running
The site is built automatically via GitHub Actions on every push to the `main` branch. 

### Local Development
To serve the site locally with hot-reloading:
```bash
cd wiki
properdocs serve -f properdocs.yml -a 127.0.0.1:8181
```

### CI/CD Pipeline
The orchestration is defined in `.github/workflows/deploy.yml`. It handles:
- Dependency installation (ProperDocs, MkDocs Material)
- Building the static site
- Automated deployment directly to GitHub Pages via artifact upload (bypassing the need for a `gh-pages` branch).

## Development Conventions
- **Source of Truth:** Markdown source files reside in `wiki/docs/`.
- **Dynamic Content:** `wiki/scripts/gen_profile.py` imports `.source/USERPROFILE_RPDev.md` into the wiki dynamically at build time.
- **Design System:** The global visual language is defined in `wiki/docs/assets/css/theme.css`.
- **Privacy:** Private configuration specs are isolated in `wiki/docs/private/` and compiled to `.source/` (Git-ignored) so they are excluded from the public deployment.

## GitHub Pages Deployment Override
*Heuristic applied:* If the GitHub repository settings GUI hides the "GitHub Actions" deployment source (common in `<user>.github.io` repos), enforce the workflow via the GitHub API:
```bash
gh api -X PUT /repos/IamRPDev/iamrpdev.github.io/pages -f build_type="workflow"
```
