# Repository guide

This repository is a Jekyll/GitHub Pages personal academic site. Keep changes small, preserve existing URLs, and verify the specific surface you touch.

## Site structure

- `about.md` is the homepage (`/`).
- `_config.yml` owns site metadata, author details, navigation, plugins, and global defaults.
- `_posts/` contains archived long-form tech posts; the site currently has no public tech-blog index or navigation entry.
- `_layouts/` and `_includes/` contain Liquid templates. Shared styling enters through `assets/css/main.scss`; local overrides live in `_sass/layout/` and theme variables in `_sass/theme/`.
- `_data/tech_log.yml` and `_data/tech_concepts.yml` retain curated tech-log data.
- `images/` contains site images. `assets/` contains public PDFs, video, fonts, and the published CV. `CV_Latex/` contains CV source and build artifacts.
- `blog.md` is a planning document without Jekyll front matter; it is not the published blog index.

## Generated learning-log content

`Renyuan_Log.md` is the source of truth for dated learning-log text.

- `python3 scripts/generate_tech_log_archive.py` regenerates `tech-log-full.md`, `_data/tech_log_blocks.yml`, and `_data/tech_log_artifacts.yml`.
- `python3 scripts/update_post_source_coverage.py` regenerates `_data/post_source_coverage.yml` and the sections between `<!-- source-log-coverage:start -->` and `<!-- source-log-coverage:end -->` in every tech post.
- Do not hand-edit generated files or generated coverage blocks. Edit the source log, the assignment map in `update_post_source_coverage.py`, or the curated post content above the marker, then regenerate.
- `_data/tech_log.yml` and `_data/tech_concepts.yml` are curated inputs, not outputs of the current scripts.

## Generated GitHub activity

`scripts/update_github_contributions.py` fetches the public contribution calendar for the configured GitHub user and regenerates `images/github-contributions.svg` plus `_data/github_contributions.json`. The daily `.github/workflows/update-github-contributions.yml` workflow commits these two outputs when they change. Do not hand-edit either generated file.

When the learning log or its mappings change, run the generators in this order:

```bash
python3 scripts/generate_tech_log_archive.py
python3 scripts/update_post_source_coverage.py
python3 scripts/verify_post_source_coverage.py
```

## Verification

For every change, run:

```bash
git diff --check
python3 scripts/verify_post_source_coverage.py
```

The repository currently has no `Gemfile` and does not pin a Jekyll toolchain. Do not claim a successful full-site build unless a working Jekyll environment has been added or supplied. Once one exists, also run the repository's Jekyll build command and inspect `/`, a post page, and `/404.html` at desktop and mobile widths.

## Editing conventions

- Preserve front matter, permalinks, heading anchors, and source-coverage markers unless the requested change explicitly migrates them.
- Use Liquid URL filters such as `relative_url` or the existing `base_path` pattern for internal links and assets.
- Reuse the existing Sass variables, theme custom properties, and breakpoints so light/dark and responsive behavior remain consistent.
- Keep accessible labels, alt text, keyboard interaction, and reduced-motion behavior in mind when changing navigation, modals, or media.
- Avoid unrelated formatting churn and do not rewrite binary assets unless the task requires it.
