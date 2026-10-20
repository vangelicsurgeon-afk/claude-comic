"""
validate.py - mechanical pre-publish checks for an episode. Run before publishing;
any ERROR blocks publication.

    python3 tools/validate.py episodes/0007
"""
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

REQUIRED = ("number", "title", "date", "alt")
MAX_SVG_BYTES = 1_500_000


def check(ep_dir: pathlib.Path):
    errs, warns = [], []
    meta_f, svg_f, png_f = ep_dir / "meta.json", ep_dir / "comic.svg", ep_dir / "comic.png"
    for f in (meta_f, svg_f, png_f):
        if not f.exists():
            errs.append(f"missing {f.name}")
    if errs:
        return errs, warns

    m = json.loads(meta_f.read_text(encoding="utf-8"))
    for k in REQUIRED:
        if not m.get(k):
            errs.append(f"meta.json missing '{k}'")
    if f"{int(m.get('number', 0)):04d}" != ep_dir.name:
        errs.append(f"meta number {m.get('number')} does not match folder {ep_dir.name}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(m.get("date", ""))):
        errs.append("date must be YYYY-MM-DD")
    if len(m.get("alt", "")) < 40:
        warns.append("alt text is very short; describe the strip for screen-reader users")
    if not m.get("transcript"):
        warns.append("no transcript")

    raw = svg_f.read_text(encoding="utf-8")
    if len(raw.encode()) > MAX_SVG_BYTES:
        errs.append(f"comic.svg is {len(raw.encode()) // 1024} KB (limit {MAX_SVG_BYTES // 1024} KB)")
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        return errs + [f"comic.svg is not valid XML: {e}"], warns
    if not root.get("viewBox"):
        errs.append("comic.svg has no viewBox")
    if re.search(r"<script|on\w+\s*=", raw, re.I):
        errs.append("comic.svg contains script or event handlers")
    if re.search(r'(?:href|src)\s*=\s*"(?:https?:)?//', raw):
        errs.append("comic.svg references external resources (images render blank in <img>)")
    if png_f.stat().st_size < 5_000:
        warns.append("comic.png is suspiciously small; check the render")
    return errs, warns


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    errs, warns = check(pathlib.Path(sys.argv[1]))
    for w in warns:
        print("WARN :", w)
    for e in errs:
        print("ERROR:", e)
    print("FAIL" if errs else "OK")
    sys.exit(1 if errs else 0)
