# Repository Guidelines

## Project Structure & Module Organization
This repository is a Jekyll-based personal academic site. Core site settings live in `_config.yml` and `_config_docker.yml`. Author-facing content is organized by collection: `_pages/`, `_posts/`, `_publications/`, `_talks/`, `_teaching/`, and `_portfolio/`. Shared templates and styling live in `_layouts/`, `_includes/`, and `_sass/`. Static assets and downloadable files are stored under `assets/`, `images/`, and `files/`. Structured site data such as navigation and CV JSON lives in `_data/`. Utility scripts in `scripts/` and `markdown_generator/` are maintenance helpers, not part of the default page build.

## Build, Test, and Development Commands
Run `bundle install` to install Jekyll and plugin gems. Use `bundle exec jekyll serve` for local development at `http://127.0.0.1:4000`, and restart it after editing `_config.yml`. Use `bundle exec jekyll build` as the main validation pass before submitting changes. Run `npm install` once to install the JavaScript toolchain, then `npm run build:js` after editing `assets/js/_main.js` or files in `assets/js/plugins/`; this regenerates `assets/js/main.min.js`. If you prefer containers, `docker compose up --build` starts the same site through the repo Docker setup.

## Coding Style & Naming Conventions
Use 2-space indentation in YAML, Markdown front matter, JavaScript, and shell snippets. Match the surrounding style in touched files and keep front matter keys lowercase, for example `title`, `collection`, `date`, and `permalink`. Preserve the repository’s date-prefixed filenames such as `2025-03-31-IJCNN.md` for publications and `2015-08-14-blog-post-4.md` for posts. No ESLint, Prettier, or RuboCop configuration is present, so keep diffs minimal and regenerate minified JS when source files change.

## Testing Guidelines
There is no automated unit-test or coverage gate in this repository. Before opening a PR, run `bundle exec jekyll build`; if you changed theme JavaScript, also run `npm run build:js`. Manually verify the affected pages in the local site, especially navigation, publication links, PDFs, and image assets.

## Commit & Pull Request Guidelines
Recent commits use short imperative summaries such as `Update about.md`; keep that style, but make subjects more descriptive when possible, for example `Update about page news items`. Keep each commit focused on one content or theme change. Pull requests should include a brief summary, note which pages or collections changed, link any related issue, and attach screenshots for layout or CSS changes. Call out regenerated or replaced binary assets in `assets/`, `images/`, or `files/` so reviewers can focus on intentional diffs.
