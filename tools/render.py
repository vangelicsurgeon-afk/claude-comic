"""
render.py - rasterize an SVG to PNG so it can be looked at (by the art director
subagent via the Read tool) and used as the social preview image.

    python3 tools/render.py episodes/0001/comic.svg            # -> comic.png beside it
    python3 tools/render.py art/model-sheets/ada.svg -o /tmp/x.png --scale 2

Uses resvg (pip: resvg-py) with the repo's fonts/ dir; falls back to cairosvg.
"""
import argparse
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / "fonts"


def render(svg_path: pathlib.Path, out: pathlib.Path, scale: float = 1.0, background="#ffffff"):
    svg = svg_path.read_text(encoding="utf-8")
    try:
        import resvg_py

        png = resvg_py.svg_to_bytes(svg_string=svg, font_dirs=[str(FONT_DIR)],
                                    zoom=scale, background=background)
        out.write_bytes(bytes(png))
        return "resvg"
    except ImportError:
        pass
    try:
        import cairosvg

        cairosvg.svg2png(bytestring=svg.encode(), write_to=str(out), scale=scale,
                         background_color=background)
        return "cairosvg"
    except ImportError:
        sys.exit("No renderer found. Run: pip install resvg-py fonttools "
                 "(add --break-system-packages if pip refuses)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("svg")
    ap.add_argument("-o", "--out")
    ap.add_argument("--scale", type=float, default=1.0)
    a = ap.parse_args()
    src = pathlib.Path(a.svg)
    dst = pathlib.Path(a.out) if a.out else src.with_suffix(".png")
    engine = render(src, dst, a.scale)
    print(f"rendered {dst} ({engine})")
