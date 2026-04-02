# Repository Guidelines

## Project Structure & Module Organization
This repository is a Jekyll-based personal academic site centered on [`_pages/about.md`](/home/ryan/CUHKSZ/ryannnice.github.io/_pages/about.md). The main runtime shell lives in `_layouts/`, `_includes/`, `_sass/`, and `_data/navigation.yml`. Downloadable PDFs and evidence files are stored in `assets/`, while images used by the homepage and sidebar live in `images/`. Most site content is intentionally concentrated in the homepage; [`_pages/404.md`](/home/ryan/CUHKSZ/ryannnice.github.io/_pages/404.md) is the only secondary page kept in the repo.

## Build, Test, and Development Commands
Run `bundle install` to install Jekyll and plugin gems. Use `bundle exec jekyll serve` for local development at `http://127.0.0.1:4000`, and restart it after editing `_config.yml`. Use `bundle exec jekyll build` as the main validation pass before submitting changes. Run `npm install` once to install the JavaScript toolchain, then `npm run build:js` after editing `assets/js/_main.js` or files in `assets/js/plugins/`; this regenerates `assets/js/main.min.js`. If you prefer containers, `docker compose up --build` starts the same site through the repo Docker setup.

## Coding Style & Naming Conventions
Use 2-space indentation in YAML, Markdown front matter, JavaScript, and shell snippets. Match the surrounding style in touched files and keep front matter keys lowercase, for example `title`, `permalink`, and `author_profile`. Prefer editing the homepage sections in [`_pages/about.md`](/home/ryan/CUHKSZ/ryannnice.github.io/_pages/about.md) instead of introducing new content collections unless there is a clear structural need. No ESLint, Prettier, or RuboCop configuration is present, so keep diffs minimal and regenerate minified JS when source files change.

## Testing Guidelines
There is no automated unit-test or coverage gate in this repository. Before opening a PR, run `bundle exec jekyll build`; if you changed theme JavaScript, also run `npm run build:js`. Manually verify the homepage sections, anchor navigation, sidebar links, PDF embeds, downloadable assets, and visitor/analytics widgets.

## Commit & Pull Request Guidelines
Recent commits use short imperative summaries such as `Update about.md`; keep that style, but make subjects more descriptive when possible, for example `Update about page news items`. Keep each commit focused on one homepage, asset, or theme change. Pull requests should include a brief summary, note any changed PDFs or images, and attach screenshots for layout or CSS changes.
