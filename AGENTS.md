# Repository Guidelines

## Project Structure & Module Organization
This repository is a Jekyll-based personal site. Core site settings live in `_config.yml`. Page content is currently flat at the repo root, mainly [`about.md`](about.md) and [`404.md`](404.md). Reusable Liquid partials are in `_includes/`, page shells are in `_layouts/`, and styling is split between the entry stylesheet `assets/css/main.scss` and partials under `_sass/`. Static files such as PDFs, icons, fonts, and images belong in `assets/` or `images/`.

## Build, Test, and Development Commands
Use Jekyll locally after installing the required Ruby gems in your environment:

- `jekyll serve -l -H localhost` starts a local preview server with live reload.
- `jekyll build` generates the production site into `_site/` and is the main validation step before opening a PR.

There is no dedicated test suite in this repo. A clean `jekyll build` plus a manual check of the affected page(s) in the local preview is the expected verification workflow.

## Coding Style & Naming Conventions
Follow the existing Jekyll/Liquid conventions:

- Use YAML front matter on pages.
- Keep indentation at 2 spaces in HTML, Liquid, and YAML.
- Use lowercase, hyphen-free filenames only when matching existing top-level pages (`about.md`, `404.md`); otherwise prefer lowercase kebab-case for new assets and content files.
- Edit `assets/css/main.scss` only to adjust import order; place most style changes in `_sass/theme/` or `_sass/layout/`.
- Avoid modifying vendored files under `_sass/vendor/` unless the change is unavoidable and documented in the PR.

## Testing Guidelines
Because there is no automated coverage setup, test changes by building locally and checking navigation, sidebar content, images, and linked PDFs. For content-heavy edits, verify anchor links from `_config.yml` still resolve on the homepage.

## Commit & Pull Request Guidelines
Recent history favors short, direct subjects such as `chore/...`, `refactor/...`, and `Update about.md`. Keep commits narrowly scoped and descriptive. Pull requests should include:

- a brief summary of user-visible changes,
- linked issue/context when applicable,
- screenshots for layout or styling updates,
- confirmation that `jekyll build` completed successfully.
