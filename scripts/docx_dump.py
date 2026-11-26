"""Дамп .docx в Markdown + извлечение всех изображений.

Использование:
    .venv\\Scripts\\python.exe scripts\\docx_dump.py metodichka_servernye_prilozhenia.docx

Результат:
    docs/<имя>.md        - весь текст методички в Markdown
    docs/images/*        - все картинки (по порядку появления + все media)
"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "v": "urn:schemas-microsoft-com:vml",
    "pic": "http://schemas.openxmlformats.org/drawingml/2006/picture",
}

def _qn(tag: str) -> str:
    prefix, local = tag.split(":")
    return "{%s}%s" % (NS[prefix], local)


IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".emf", ".wmf", ".tif", ".tiff", ".svg", ".webp"}

# Части .docx, изображения которых попали в Markdown.
USED_PARTS: set[str] = set()


def iter_block_items(parent):
    """Параграфы и таблицы в порядке документа."""
    body = parent.element.body if hasattr(parent, "element") else parent._tc
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)


def style_name(p: Paragraph) -> str:
    try:
        return (p.style.name or "").strip()
    except Exception:
        return ""


def is_code_style(name: str) -> bool:
    n = name.lower()
    return any(k in n for k in ("code", "код", "source", "preformatted", "mono"))


def para_markdown(p: Paragraph, img_counter: list[int], outdir: Path, rel_prefix: str) -> str:
    """Markdown одного параграфа + выгрузка картинок."""
    text_parts: list[str] = []
    images: list[str] = []

    for run in p.runs:
        # картинки внутри run
        for blip in run._element.findall(".//" + qn("a:blip")):
            rid = blip.get(qn("r:embed")) or blip.get(qn("r:link"))
            path = save_image(p, rid, img_counter, outdir)
            if path:
                images.append(path)
        for imagedata in run._element.findall(".//" + _qn("v:imagedata")):
            rid = imagedata.get(qn("r:id"))
            path = save_image(p, rid, img_counter, outdir)
            if path:
                images.append(path)
        text_parts.append(run.text)

    text = "".join(text_parts)
    text = re.sub(r"[ \t]+", " ", text).strip()

    name = style_name(p)
    lines: list[str] = []

    if text:
        m = re.match(r"^(?:heading|заголовок)\s*(\d)$", name.lower())
        if m:
            lines.append("#" * min(6, int(m.group(1))) + " " + text)
        elif name.lower() in ("title", "название"):
            lines.append("# " + text)
        elif name.lower().startswith(("subtitle", "подзаголовок")):
            lines.append("## " + text)
        elif is_code_style(name):
            lines.append("```\n" + text + "\n```")
        elif name.lower().startswith(("list", "список")) or p._element.find(
            ".//" + qn("w:numPr")
        ) is not None:
            indent = 0
            numpr = p._element.find(".//" + qn("w:numPr"))
            if numpr is not None:
                ilvl = numpr.find(qn("w:ilvl"))
                if ilvl is not None:
                    try:
                        indent = int(ilvl.get(qn("w:val")) or 0)
                    except ValueError:
                        indent = 0
            lines.append("  " * indent + "- " + text)
        elif name.lower().startswith(("quote", "цитата")):
            lines.append("> " + text)
        else:
            lines.append(text)

    for img in images:
        lines.append(f"![{Path(img).stem}]({rel_prefix}{img})")

    return "\n\n".join(lines)


def save_image(p: Paragraph, rid: str | None, counter: list[int], outdir: Path) -> str | None:
    if not rid:
        return None
    try:
        part = p.part.related_parts[rid]
    except Exception:
        return None
    blob = getattr(part, "blob", None)
    if not blob:
        return None
    USED_PARTS.add(str(part.partname))
    ext = Path(part.partname).suffix.lower() or ".png"
    counter[0] += 1
    name = f"img_{counter[0]:03d}{ext}"
    (outdir / name).write_bytes(blob)
    return f"images/{name}"


def table_markdown(t: Table) -> str:
    rows: list[list[str]] = []
    for row in t.rows:
        cells = []
        for cell in row.cells:
            txt = " ".join(cell.text.split())
            cells.append(txt.replace("|", "\\|"))
        rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    head = rows[0]
    body = rows[1:]
    out = ["| " + " | ".join(head) + " |", "|" + "|".join([" --- "] * width) + "|"]
    for r in body:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    outdir = Path("docs")
    imgdir = outdir / "images"
    imgdir.mkdir(parents=True, exist_ok=True)

    doc = Document(str(src))
    counter = [0]
    blocks: list[str] = []

    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            md = para_markdown(block, counter, imgdir, "")
            if md:
                blocks.append(md)
        else:
            md = table_markdown(block)
            if md:
                blocks.append(md)

    md_path = outdir / (src.stem + ".md")
    md_path.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")

    # Докладываем media, которые не встречаются в тексте (в т.ч. неиспользуемые).
    with zipfile.ZipFile(src) as z:
        media = [n for n in z.namelist() if n.startswith("word/media/")]
        unreferenced = [n for n in media if f"/{n}" not in USED_PARTS and n not in USED_PARTS]
        all_dir = outdir / "images_all"
        for n in unreferenced:
            all_dir.mkdir(exist_ok=True)
            (all_dir / Path(n).name).write_bytes(z.read(n))

    print(f"MD: {md_path} ({len(blocks)} блоков)")
    print(f"Картинок из текста: {counter[0]} -> {imgdir}")
    print(f"Всего media в docx: {len(media)}; вне текста: {len(unreferenced)}")
    if unreferenced:
        print(f"  вне текста скопированы в {all_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
