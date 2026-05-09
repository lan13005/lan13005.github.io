# lan13005.github.io

Personal portfolio site for Lawrence Ng — built with [Astro](https://astro.build), [Tailwind CSS](https://tailwindcss.com), and deployed to GitHub Pages.

## Prerequisites

- Node.js 20+, npm 9+
- [uv](https://docs.astral.sh/uv/) (for the CV build script)
- pdflatex / TeX Live (only needed to compile the CV PDF locally)

## Getting started

```bash
npm install
uv run cv/build.py   # generate experience content from cv.yaml
npm run dev          # start dev server at http://localhost:4321
```

## Scripts

| Command           | Description                                                                 |
| ----------------- | --------------------------------------------------------------------------- |
| `npm run dev`     | Start local dev server                                                      |
| `npm run build`   | Build site for production → `dist/`                                         |
| `npm run preview` | Preview the production build locally                                        |
| `npm run format`  | Auto-format all files with Prettier                                         |
| `npm run lint`    | Lint `.astro` and `.ts` files with ESLint                                   |
| `npm run cv`      | Regenerate `cv/cv.tex` + `src/content/experience/` from `cv/cv.yaml`        |
| `npm run cv:pdf`  | Same as above, also compiles `cv.tex` → `public/cv.pdf` (requires pdflatex) |

## CV build system

The CV is driven by a single source of truth: **`cv/cv.yaml`**.

```
cv/
├── cv.yaml      ← edit this
├── cv.tex.j2    ← Jinja2 template (custom << >> delimiters to avoid LaTeX conflicts)
└── build.py     ← generates cv.tex + src/content/experience/*.md
```

`build.py` is a self-contained uv script (PEP 723 inline dependencies — no venv setup needed).

### Typical workflow

1. **Edit** `cv/cv.yaml` — personal info, experience entries, skills.
2. **Regenerate** content and template:
   ```bash
   npm run cv          # → cv/cv.tex + src/content/experience/*.md
   npm run cv:pdf      # → also builds public/cv.pdf (needs pdflatex)
   ```
3. **Preview** the site: `npm run dev`
4. **Push** to `main` — CI generates content from YAML and conditionally rebuilds the PDF if `cv/` changed.

### What is and isn't generated

| File                          | Source                        | Generated?                                                      |
| ----------------------------- | ----------------------------- | --------------------------------------------------------------- |
| `cv/cv.tex`                   | `cv/cv.tex.j2` + `cv/cv.yaml` | Yes — gitignored                                                |
| `public/cv.pdf`               | `cv/cv.tex` via pdflatex      | Yes — gitignored (CI builds it)                                 |
| `src/content/experience/*.md` | `cv/cv.yaml`                  | Yes — committed so Astro builds work without running the script |

Experience `.md` files are committed rather than gitignored so that `npm run build` works in environments where uv isn't available (e.g. bare CI jobs). Re-run `npm run cv` after editing `cv/cv.yaml` to keep them in sync.

## Adding content

### Update your CV / experience

Edit **`cv/cv.yaml`** only, then run `npm run cv`. Do not hand-edit `src/content/experience/*.md` — those are overwritten on the next build.

### New project

Create a new Markdown file in `src/content/projects/`:

```markdown
---
title: 'My New Project'
summary: 'One or two sentences describing it.'
date: 2025-01-15
tags: ['python', 'ml']
repo: 'https://github.com/lan13005/my-project' # optional
featured: false
draft: false
---

Project description in Markdown...
```

That's it — the project automatically appears on `/projects` and, if `featured: true`, on the home page teaser.

### Update personal info

Edit **`src/config.ts`** for name, role, bio, CTAs, social links, and "What I Do" cards.
Edit **`cv/cv.yaml`** `personal:` block for changes that should also appear in the PDF CV.

## Deployment

The site deploys automatically via GitHub Actions on every push to `main`. The workflow:

1. Installs [uv](https://docs.astral.sh/uv/) and Node deps.
2. Runs `uv run cv/build.py --content-only` to regenerate experience content from YAML.
3. If any file in `cv/` changed, installs TeX Live and rebuilds `public/cv.pdf`.
4. Runs `npm run build` → uploads `dist/` to GitHub Pages.

**One-time setup:** In your repo on GitHub, go to **Settings → Pages → Source** and set it to **"GitHub Actions"**.

## Assets to replace

- `public/og-image.svg` — replace with a real 1200×630 OG image
- `src/assets/hero.svg` — replace with a preferred illustration
