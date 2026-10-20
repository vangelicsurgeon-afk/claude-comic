"""
comic.py - layout and lettering toolkit for the strip.

This is infrastructure, not style. It handles the mechanical parts that are
easy to get wrong when hand-writing SVG: panel geometry, clipping, accurate
text wrapping (measured with the real font metrics), speech/thought/caption
balloons with tails, and embedding the lettering font so the SVG looks the
same in every browser and in the PNG render.

All creative drawing (characters, props, settings) lives in art/ and is passed
in as raw SVG fragments.

Typical use (inside episodes/NNNN/compose.py):

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
    from comic import Strip

    strip = Strip(width=1200, height=420, cols=3, rows=1)
    p = strip.panels[0]
    p.background("#f4efe6")
    p.add(some_character_svg, x=120, y=330, scale=1.0)      # local panel coords
    p.balloon("Is it Tuesday again?", x=40, y=30, tail=(150, 200))
    p.caption("Meanwhile...", corner="top-left")
    strip.save(pathlib.Path(__file__).parent / "comic.svg")
"""
from __future__ import annotations

import base64
import html
import math
import pathlib
from dataclasses import dataclass, field
from functools import lru_cache

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / "fonts"

# Lettering defaults. A genesis/style run may change these in bible/style.md and
# pass different values per strip; the toolkit just needs a TTF in fonts/.
DEFAULT_FONT_FAMILY = "Comic Neue"
DEFAULT_FONT_FILES = {"normal": "ComicNeue-Regular.ttf", "bold": "ComicNeue-Bold.ttf"}


def esc(s: str) -> str:
    return html.escape(s, quote=True)


# --------------------------------------------------------------------------- #
# Text measurement
# --------------------------------------------------------------------------- #
@lru_cache(maxsize=None)
def _font_metrics(filename: str):
    from fontTools.ttLib import TTFont  # pip install fonttools

    f = TTFont(str(FONT_DIR / filename))
    cmap = f.getBestCmap()
    hmtx = f["hmtx"].metrics
    upem = f["head"].unitsPerEm
    fallback = hmtx.get(cmap.get(ord("n"), ".notdef"), (upem // 2, 0))[0]
    return cmap, hmtx, upem, fallback


def text_width(text: str, size: float, font_file: str) -> float:
    cmap, hmtx, upem, fallback = _font_metrics(font_file)
    units = 0
    for ch in text:
        g = cmap.get(ord(ch))
        units += hmtx[g][0] if g in hmtx else fallback
    return units * size / upem


def wrap(text: str, size: float, max_width: float, font_file: str) -> list[str]:
    """Greedy word wrap using real glyph advances. Respects explicit newlines."""
    lines: list[str] = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for w in words[1:]:
            trial = f"{cur} {w}"
            if text_width(trial, size, font_file) <= max_width:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


# --------------------------------------------------------------------------- #
# Geometry helpers
# --------------------------------------------------------------------------- #
@dataclass
class Rect:
    x: float
    y: float
    w: float
    h: float

    @property
    def cx(self):
        return self.x + self.w / 2

    @property
    def cy(self):
        return self.y + self.h / 2


def grid(width, height, cols, rows, margin=24, gutter=18):
    """Evenly spaced panel rects, row-major order."""
    pw = (width - 2 * margin - (cols - 1) * gutter) / cols
    ph = (height - 2 * margin - (rows - 1) * gutter) / rows
    return [
        Rect(margin + c * (pw + gutter), margin + r * (ph + gutter), pw, ph)
        for r in range(rows)
        for c in range(cols)
    ]


# --------------------------------------------------------------------------- #
# Panel
# --------------------------------------------------------------------------- #
@dataclass
class Panel:
    index: int
    rect: Rect
    strip: "Strip"
    layers: list[str] = field(default_factory=list)  # art, drawn first
    lettering: list[str] = field(default_factory=list)  # balloons, drawn last
    border_width: float = 3
    border_color: str = "#111"
    fill: str = "#ffffff"

    # ---- art -------------------------------------------------------------- #
    def background(self, color: str):
        self.fill = color
        return self

    def add(self, svg: str, x: float = 0, y: float = 0, scale: float = 1.0,
            flip: bool = False, rotate: float = 0):
        """Place an SVG fragment at local panel coords (x, y)."""
        t = f"translate({x:.2f},{y:.2f})"
        if rotate:
            t += f" rotate({rotate:.2f})"
        sx = -scale if flip else scale
        if sx != 1 or scale != 1:
            t += f" scale({sx:.4f},{scale:.4f})"
        self.layers.append(f'<g transform="{t}">{svg}</g>')
        return self

    def raw(self, svg: str):
        """Add raw SVG in local panel coords with no transform."""
        self.layers.append(svg)
        return self

    # ---- lettering ---------------------------------------------------------- #
    def _text_block(self, lines, x, y, size, line_h, anchor="middle", bold=False,
                    color="#111"):
        weight = "700" if bold else "400"
        out = [f'<text font-family="{esc(self.strip.font_family)}" font-size="{size}" '
               f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}">']
        for i, ln in enumerate(lines):
            out.append(f'<tspan x="{x:.1f}" y="{y + i * line_h:.1f}">{esc(ln)}</tspan>')
        out.append("</text>")
        return "".join(out)

    def balloon(self, text: str, x: float, y: float, tail: tuple | None = None,
                kind: str = "speech", max_width: float | None = None,
                size: float | None = None, bold: bool = False, pad: float = 14,
                fill: str = "#fff", stroke: str = "#111", stroke_width: float = 2.5):
        """
        Speech/thought/whisper/shout balloon whose top-left is at (x, y), local coords.
        tail: (tx, ty) point the tail aims at (usually a mouth), local coords.
        kind: "speech" | "thought" | "whisper" | "shout"
        Returns the balloon Rect (local coords) so callers can stack balloons.
        """
        size = size or self.strip.font_size
        max_width = max_width or min(self.rect.w * 0.62, 340)
        font_file = self.strip.font_files["bold" if (bold or kind == "shout") else "normal"]
        lines = wrap(text, size, max_width - 2 * pad, font_file)
        line_h = size * 1.18
        tw = max(text_width(ln, size, font_file) for ln in lines) if lines else 0
        bw = tw + 2 * pad
        bh = len(lines) * line_h + 2 * pad - (line_h - size)
        rx, ry = bw / 2, bh / 2
        cx, cy = x + rx, y + ry
        self._check_bounds(Rect(x, y, bw, bh), f"balloon '{text[:24]}'")

        parts = []
        dash = ' stroke-dasharray="7 5"' if kind == "whisper" else ""
        common = f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"{dash}'

        if tail and kind != "thought":
            parts.append(self._tail(cx, cy, rx, ry, tail, fill, stroke, stroke_width, dash))
        if kind == "thought" and tail:
            tx, ty = tail
            dist = math.hypot(tx - cx, ty - cy) or 1
            ux, uy = (tx - cx) / dist, (ty - cy) / dist
            # distance from centre to the cloud edge along the tail direction
            edge = 1 / math.sqrt((ux / (rx * 1.2)) ** 2 + (uy / (ry * 1.3)) ** 2)
            start, end = edge + 12, max(edge + 30, dist - 14)
            for i, r in enumerate((9, 6, 4)):
                d = start + (end - start) * i / 2
                parts.append(f'<circle cx="{cx + ux * d:.1f}" cy="{cy + uy * d:.1f}" r="{r}" {common}/>')

        if kind == "shout":
            parts.append(f'<path d="{_burst_path(cx, cy, rx * 1.18, ry * 1.32)}" {common}/>')
        elif kind == "thought":
            parts.append(f'<path d="{_cloud_path(cx, cy, rx * 1.12, ry * 1.2)}" {common}/>')
        else:
            parts.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx * 1.12:.1f}" '
                         f'ry="{ry * 1.14:.1f}" {common}/>')
        # Patch over the tail join so the tail looks continuous with the balloon.
        if tail and kind in ("speech", "whisper"):
            parts.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx * 1.12 - stroke_width:.1f}" '
                         f'ry="{ry * 1.14 - stroke_width:.1f}" fill="{fill}"/>')
        ty0 = cy - bh / 2 + pad + size * 0.82
        parts.append(self._text_block(lines, cx, ty0, size, line_h,
                                      bold=(bold or kind == "shout")))
        self.lettering.append("<g>" + "".join(parts) + "</g>")
        return Rect(x - rx * 0.12, y - ry * 0.14, bw * 1.12, bh * 1.14)

    def caption(self, text: str, corner: str = "top-left", max_width: float | None = None,
                size: float | None = None, fill: str = "#fff5c8", stroke: str = "#111",
                pad: float = 10, inset: float = 8):
        """Rectangular narration box pinned to a panel corner."""
        size = size or self.strip.font_size * 0.92
        max_width = max_width or self.rect.w * 0.7
        font_file = self.strip.font_files["normal"]
        lines = wrap(text, size, max_width - 2 * pad, font_file)
        line_h = size * 1.18
        tw = max(text_width(ln, size, font_file) for ln in lines)
        bw, bh = tw + 2 * pad, len(lines) * line_h + 2 * pad - (line_h - size)
        x = inset if "left" in corner else self.rect.w - inset - bw
        y = inset if "top" in corner else self.rect.h - inset - bh
        box = (f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" '
               f'fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        txt = self._text_block(lines, x + pad, y + pad + size * 0.82, size, line_h, anchor="start")
        self.lettering.append(f"<g>{box}{txt}</g>")
        return Rect(x, y, bw, bh)

    def sfx(self, text: str, x: float, y: float, size: float = 40, rotate: float = -8,
            fill: str = "#111", stroke: str | None = "#fff"):
        """Sound effect lettering."""
        s = f' stroke="{stroke}" stroke-width="{size / 9:.1f}" paint-order="stroke"' if stroke else ""
        self.lettering.append(
            f'<text x="{x:.1f}" y="{y:.1f}" transform="rotate({rotate} {x:.1f} {y:.1f})" '
            f'font-family="{esc(self.strip.font_family)}" font-weight="700" font-size="{size}" '
            f'fill="{fill}"{s}>{esc(text)}</text>')
        return self

    # ---- internals ---------------------------------------------------------- #
    def _tail(self, cx, cy, rx, ry, tail, fill, stroke, sw, dash):
        tx, ty = tail
        ang = math.atan2(ty - cy, tx - cx)
        spread = 0.22
        # base points on the ellipse edge either side of the tail direction
        b1 = (cx + rx * 0.95 * math.cos(ang - spread), cy + ry * 0.95 * math.sin(ang - spread))
        b2 = (cx + rx * 0.95 * math.cos(ang + spread), cy + ry * 0.95 * math.sin(ang + spread))
        return (f'<path d="M{b1[0]:.1f},{b1[1]:.1f} Q{(b1[0] + tx) / 2:.1f},{(b1[1] + ty) / 2:.1f} '
                f'{tx:.1f},{ty:.1f} Q{(b2[0] + tx) / 2:.1f},{(b2[1] + ty) / 2:.1f} {b2[0]:.1f},{b2[1]:.1f} Z" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"{dash}/>')

    def _check_bounds(self, r: Rect, what: str):
        if r.x < 0 or r.y < 0 or r.x + r.w > self.rect.w or r.y + r.h > self.rect.h:
            self.strip.warnings.append(
                f"panel {self.index + 1}: {what} extends outside the panel "
                f"({r.x:.0f},{r.y:.0f},{r.w:.0f}x{r.h:.0f} vs {self.rect.w:.0f}x{self.rect.h:.0f})")

    def render(self) -> str:
        r = self.rect
        cid = f"panel-clip-{self.index}"
        return (
            f'<clipPath id="{cid}"><rect x="0" y="0" width="{r.w:.1f}" height="{r.h:.1f}"/></clipPath>'
            f'<g class="panel" transform="translate({r.x:.1f},{r.y:.1f})">'
            f'<g clip-path="url(#{cid})">'
            f'<rect x="0" y="0" width="{r.w:.1f}" height="{r.h:.1f}" fill="{self.fill}"/>'
            + "".join(self.layers) + "".join(self.lettering) +
            "</g>"
            f'<rect x="0" y="0" width="{r.w:.1f}" height="{r.h:.1f}" fill="none" '
            f'stroke="{self.border_color}" stroke-width="{self.border_width}"/>'
            "</g>"
        )


def _burst_path(cx, cy, rx, ry, spikes=14):
    pts = []
    for i in range(spikes * 2):
        a = math.pi * i / spikes
        k = 1.0 if i % 2 == 0 else 0.8
        pts.append(f"{cx + rx * k * math.cos(a):.1f},{cy + ry * k * math.sin(a):.1f}")
    return "M" + " L".join(pts) + " Z"


def _cloud_path(cx, cy, rx, ry, bumps=10):
    d = []
    for i in range(bumps + 1):
        a = 2 * math.pi * i / bumps
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        if i == 0:
            d.append(f"M{x:.1f},{y:.1f}")
        else:
            am = 2 * math.pi * (i - 0.5) / bumps
            qx, qy = cx + rx * 1.25 * math.cos(am), cy + ry * 1.25 * math.sin(am)
            d.append(f"Q{qx:.1f},{qy:.1f} {x:.1f},{y:.1f}")
    return " ".join(d) + " Z"


# --------------------------------------------------------------------------- #
# Strip
# --------------------------------------------------------------------------- #
class Strip:
    def __init__(self, width=1200, height=420, cols=3, rows=1, margin=24, gutter=18,
                 panels: list[Rect] | None = None, background="#ffffff",
                 font_family=DEFAULT_FONT_FAMILY, font_files=None, font_size=20,
                 title: str | None = None):
        self.width, self.height = width, height
        self.background = background
        self.font_family = font_family
        self.font_files = font_files or dict(DEFAULT_FONT_FILES)
        self.font_size = font_size
        self.title = title
        self.defs: list[str] = []
        self.overlay: list[str] = []
        self.warnings: list[str] = []
        rects = panels or grid(width, height, cols, rows, margin, gutter)
        self.panels = [Panel(i, r, self) for i, r in enumerate(rects)]

    def add_def(self, svg: str):
        """Gradients, patterns, filters, <symbol>s shared by all panels."""
        self.defs.append(svg)

    def add_overlay(self, svg: str):
        """Strip-level SVG drawn on top of everything (e.g. elements breaking panel borders)."""
        self.overlay.append(svg)

    def _font_face_css(self) -> str:
        css = []
        for weight, fn in (("400", self.font_files["normal"]), ("700", self.font_files["bold"])):
            data = base64.b64encode((FONT_DIR / fn).read_bytes()).decode()
            css.append(f"@font-face{{font-family:'{self.font_family}';font-weight:{weight};"
                       f"src:url(data:font/ttf;base64,{data}) format('truetype');}}")
        return "".join(css)

    def to_svg(self, embed_font=True) -> str:
        style = f"<style>{self._font_face_css()}</style>" if embed_font else ""
        title = f"<title>{esc(self.title)}</title>" if self.title else ""
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'width="{self.width}" height="{self.height}">{title}'
            f"<defs>{style}{''.join(self.defs)}</defs>"
            f'<rect width="100%" height="100%" fill="{self.background}"/>'
            + "".join(p.render() for p in self.panels)
            + "".join(self.overlay)
            + "</svg>"
        )

    def save(self, path, embed_font=True):
        path = pathlib.Path(path)
        path.write_text(self.to_svg(embed_font=embed_font), encoding="utf-8")
        for w in self.warnings:
            print("WARNING:", w)
        return path
