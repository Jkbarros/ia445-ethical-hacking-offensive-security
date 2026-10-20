#!/usr/bin/env python3
"""Extract PDF images and build docs/<slug>-pdf.md for each PDF."""

from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive" / "canvas-submissions"
SHOTS = ROOT / "docs" / "screenshots"
DOCS = ROOT / "docs"


def slugify(stem: str) -> str:
    s = stem.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:72] or "document"


def extract_images() -> None:
    SHOTS.mkdir(parents=True, exist_ok=True)
    for pdf in sorted(ARCHIVE.glob("*.pdf")):
        reader = PdfReader(pdf)
        base = slugify(pdf.stem)
        for pi, page in enumerate(reader.pages, start=1):
            for ii, img in enumerate(page.images, start=1):
                ext = ".png" if img.name.lower().endswith(".png") else ".jpg"
                (SHOTS / f"{base}-p{pi}-img{ii}{ext}").write_bytes(img.data)


def images_for_page(base: str, page: int) -> list[str]:
    return sorted(p.name for p in SHOTS.glob(f"{base}-p{page}-img*"))


def build_pdf(pdf: Path) -> None:
    reader = PdfReader(pdf)
    base = slugify(pdf.stem)
    rel = pdf.relative_to(ROOT).as_posix().replace(" ", "%20")
    title = pdf.stem
    lines: list[str] = [
        f"# {title}",
        "",
        f"**Source:** [`{pdf.name}`](../{rel})  ",
        "**Course:** IA 445 - Ethical Hacking and Offensive Security (EMU)  ",
        "**Author:** Julio Barros",
        "",
    ]
    for pi, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        imgs = images_for_page(base, pi)
        if text or imgs:
            lines.extend([f"## Page {pi}", ""])
        if text:
            lines.append(text)
            lines.append("")
        for img in imgs:
            lines.append(f"![{title} p{pi}](screenshots/{img})")
            lines.append("")
    out = DOCS / f"{base}-pdf.md"
    out.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}")


def main() -> None:
    extract_images()
    for pdf in sorted(ARCHIVE.glob("*.pdf")):
        build_pdf(pdf)


if __name__ == "__main__":
    main()
