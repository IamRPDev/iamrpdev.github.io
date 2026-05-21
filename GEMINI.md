# GEMINI.md

## Project Overview
This repository manages the multi-engine infrastructure for `iamrpdev.github.io`. The site is a professional developer portfolio utilizing a decoupled, dual-engine architecture to serve a primary landing experience and a comprehensive technical knowledge base.

- **Primary Portfolio Engine:** Hugo (Extended)
- **Technical Documentation Engine:** Material for MkDocs
- **Integration Layer:** GitHub Actions CI/CD pipeline building to the root `main` branch.

## Building and Running
The site is built automatically via GitHub Actions on every push to the `main` branch.

### Local Development
To build the site locally before pushing:
1. **Hugo (Portfolio):**
   ```bash
   hugo -s hugo_main.iamrpdev.github.io -d public
   ```
2. **MkDocs (Wiki):**
   ```bash
   # Ensure dependencies are installed via venv
   source venv/bin/activate
   mkdocs build -f mkdocs_wiki.iamrpdev.github.io/mkdocs.yml -d public/wiki
   ```

### CI/CD Pipeline
The orchestration is defined in `.github/workflows/deploy.yml`. It handles:
- Dependency installation (Hugo, MkDocs, Material)
- Sequential builds of Hugo and MkDocs
- Artifact consolidation into a unified `public/` directory
- Automated deployment to GitHub Pages (served from the root of `main`)

## Development Conventions
- **Source of Truth:** The root directory contains the landing page (`index.html`) and orchestration files.
- **Engine Isolation:** Hugo source files reside in `hugo_main.iamrpdev.github.io/`, and MkDocs source files in `mkdocs_wiki.iamrpdev.github.io/`.
- **Security-First:** The pipeline includes a `Trivy` security scan for all built assets prior to deployment.
- **Infrastructure-as-Code:** All changes to deployment or routing MUST be updated in `.github/workflows/deploy.yml`.

## Key Files
- `index.html`: The primary root landing page (Intelligence Matrix).
- `.github/workflows/deploy.yml`: The central CI/CD orchestration pipeline.
- `hugo_main.iamrpdev.github.io/`: Portfolio engine directory.
- `mkdocs_wiki.iamrpdev.github.io/`: Wiki engine directory.
- `data/skills.yaml`: Centralized competence matrix for portfolio cards.
