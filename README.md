# Profile Page

[Click here for the personal page](https://lan13005.github.io/personal_page/)

# Prerequisites

Built with [Astro](https://astro.build), [Tailwind CSS](https://tailwindcss.com), and deployed to GitHub Pages.

- Node.js 20+, npm 9+
- pdflatex / TeX Live (only needed to compile the CV PDF locally)

# Content Structure

Everything — personal info, experience, projects, social links — lives in one file: **`src/data/profile.toml`**.

Top-level structure:

- `[site]` — name, bio, CTAs, socials, "What I Do" cards, meta tags
- `[[experience]]` — jobs, each optionally containing `[[experience.project]]` entries
- Projects appear on both the experience timeline and the projects page; `featured = true` also surfaces them on the home page

# Development

**One-time setup:** In your repo on GitHub, go to **Settings → Pages → Source** and set it to **"GitHub Actions"**.

After that, every push to `main` deploys automatically.

```bash
npm install
npm run dev    # http://localhost:4321, Astro watches for changes and hot-reloads the browser.

# Code Quality
npm run format    # Prettier — rewrites files to enforce style
npm run lint      # ESLint — flags logic and pattern issues

# Converting LaTeX CV to PDF
#   CI: the PDF is rebuilt automatically whenever any file in `cv/` changes.
npm run cv:pdf    # compiles → public/cv.pdf (requires pdflatex locally)
```

When you're done, push to `main`. Astro renders every page to static HTML and bundles assets into `dist/`, and then deploys it to GitHub Pages via GitHub Actions.

## Assets to replace

- `public/og-image.svg` — replace with a real 1200×630 OG image
