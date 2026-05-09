#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "jinja2>=3.0",
#   "pyyaml>=6.0",
# ]
# ///
"""
Build script for CV assets.

Run with:
  uv run cv/build.py               # generate cv.tex + experience .md files
  uv run cv/build.py --pdf         # also compile cv.tex → public/cv.pdf via pdflatex
  uv run cv/build.py --content-only  # only generate experience .md files (skip tex)
"""

import argparse
import datetime
import shutil
import subprocess
import sys
from pathlib import Path

import jinja2
import yaml

ROOT = Path(__file__).parent.parent
CV_DIR = ROOT / "cv"
EXPERIENCE_DIR = ROOT / "src" / "content" / "experience"


def load_yaml() -> dict:
    with open(CV_DIR / "cv.yaml") as f:
        return yaml.safe_load(f)


def format_date_str(iso: str | None, fallback: str = "Present") -> str:
    """Convert YYYY-MM-DD string to 'Mon. YYYY' display string."""
    if iso is None:
        return fallback
    try:
        d = datetime.date.fromisoformat(str(iso))
        return d.strftime("%b. %Y")
    except ValueError:
        return str(iso)


def build_tex(data: dict) -> None:
    """Render cv.tex.j2 → cv/cv.tex using custom Jinja2 delimiters."""
    env = jinja2.Environment(
        block_start_string="<%",
        block_end_string="%>",
        variable_start_string="<<",
        variable_end_string=">>",
        comment_start_string="<#",
        comment_end_string="#>",
        trim_blocks=True,
        lstrip_blocks=True,
        loader=jinja2.FileSystemLoader(str(CV_DIR)),
        undefined=jinja2.Undefined,
    )

    # Augment experience entries with formatted date strings
    for exp in data["experience"]:
        exp["start_str"] = format_date_str(exp.get("start"))
        exp["end_str"] = format_date_str(exp.get("end"))

    template = env.get_template("cv.tex.j2")
    rendered = template.render(**data)

    out = CV_DIR / "cv.tex"
    out.write_text(rendered)
    print(f"[cv] Generated {out.relative_to(ROOT)}")


def build_pdf() -> None:
    """Compile cv/cv.tex → public/cv.pdf via pdflatex."""
    tex = CV_DIR / "cv.tex"
    if not tex.exists():
        print("[cv] cv.tex not found — run without --pdf flag first to generate it.")
        sys.exit(1)

    pdflatex = shutil.which("pdflatex")
    if not pdflatex:
        print("[cv] pdflatex not found in PATH — skipping PDF generation.")
        return

    print("[cv] Running pdflatex...")
    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "cv.tex"],
        cwd=CV_DIR,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("[cv] pdflatex failed:")
        print(result.stdout[-2000:])
        sys.exit(1)

    pdf_src = CV_DIR / "cv.pdf"
    pdf_dst = ROOT / "public" / "cv.pdf"
    shutil.copy(pdf_src, pdf_dst)
    print(f"[cv] PDF written to {pdf_dst.relative_to(ROOT)}")


def build_experience_md(data: dict) -> None:
    """Generate src/content/experience/*.md from cv.yaml experience entries."""
    EXPERIENCE_DIR.mkdir(parents=True, exist_ok=True)

    # Remove previously generated files
    for f in EXPERIENCE_DIR.glob("*.md"):
        f.unlink()

    for exp in data["experience"]:
        # Skip entries without an org (e.g. "Additional Experience" in the LaTeX CV)
        if not exp.get("org"):
            continue

        slug = exp["id"]
        role = exp["role"]
        org = exp["org"]
        location = exp.get("location") or ""
        start = exp.get("start") or ""
        end_raw = exp.get("end")
        summary = (exp.get("summary") or "").strip().replace("\n", " ")
        tags = exp.get("tags") or []

        # Build frontmatter
        lines = ["---"]
        lines.append(f'role: "{role}"')
        lines.append(f'org: "{org}"')
        if location:
            lines.append(f'location: "{location}"')
        lines.append(f"start: {start}")
        if end_raw:
            lines.append(f"end: {end_raw}")
        lines.append(f'summary: "{summary}"')
        if tags:
            tag_str = ", ".join(tags)
            lines.append(f"tags: [{tag_str}]")
        lines.append("---")
        lines.append("")

        # Body: bullet points as a Markdown list
        bullets = exp.get("bullets") or []
        if bullets:
            for b in bullets:
                text = (b.get("text") or "").strip().replace("\n", " ")
                link = b.get("link")
                pub = b.get("publication")
                prefix = f"**Published in *{pub}***: " if pub else ""
                suffix = f" ([GitHub]({link}))" if link else ""
                lines.append(f"- {prefix}{text}{suffix}")
            lines.append("")

        md_path = EXPERIENCE_DIR / f"{slug}.md"
        md_path.write_text("\n".join(lines))
        print(f"[cv] Generated {md_path.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build CV assets from cv.yaml")
    parser.add_argument("--pdf", action="store_true", help="Compile cv.tex → public/cv.pdf")
    parser.add_argument(
        "--content-only",
        action="store_true",
        help="Only generate experience .md files, skip tex/pdf",
    )
    args = parser.parse_args()

    data = load_yaml()

    if not args.content_only:
        build_tex(data)

    build_experience_md(data)

    if args.pdf:
        build_pdf()


if __name__ == "__main__":
    main()
