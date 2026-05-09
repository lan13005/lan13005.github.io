# lan13005.github.io

Personal portfolio site for Lawrence Ng — built with [Astro](https://astro.build), [Tailwind CSS](https://tailwindcss.com), and deployed to GitHub Pages.

## Prerequisites

- Node.js 20+, npm 9+
- pdflatex / TeX Live (only needed to compile the CV PDF locally)

## Getting started

```bash
npm install
npm run dev    # start dev server at http://localhost:4321
```

## Scripts

| Command           | Description                                               |
| ----------------- | --------------------------------------------------------- |
| `npm run dev`     | Start local dev server                                    |
| `npm run build`   | Build site for production → `dist/`                       |
| `npm run preview` | Preview the production build locally                      |
| `npm run format`  | Auto-format all files with Prettier                       |
| `npm run lint`    | Lint `.astro` and `.ts` files with ESLint                 |
| `npm run cv:pdf`  | Compile `cv/cv.tex` → `public/cv.pdf` (requires pdflatex) |

## Adding content

### New experience entry

Edit `src/content/experience/` directly — create or update a `.md` file:

```markdown
---
role: 'Job Title'
org: 'Organization'
location: 'City, ST' # optional
start: 2024-01-01
end: 2024-12-31 # omit for "Present"
summary: 'One sentence shown on the experience page.'
tags: [python, ml]
---

- Optional bullet point details (rendered on the experience page)
```

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

If `featured: true`, the project also appears on the home page teaser.

### Update personal info

Edit `src/config.ts` — name, role, bio, CTAs, social links, and "What I Do" cards.

### CV PDF

Edit `cv/cv.tex` directly, then:

```bash
npm run cv:pdf    # compiles → public/cv.pdf (requires pdflatex locally)
```

In CI, the PDF is rebuilt automatically whenever any file in `cv/` changes.

## Deployment

The site deploys automatically via GitHub Actions on every push to `main`.

**One-time setup:** In your repo on GitHub, go to **Settings → Pages → Source** and set it to **"GitHub Actions"**.

## Assets to replace

- `public/og-image.svg` — replace with a real 1200×630 OG image
- `src/assets/hero.svg` — replace with a preferred illustration
