"""Shared palette and tiny SVG helpers. Hex values mirror bible/style.md."""
INK = "#2a2433"
PAPER = "#fbf6ea"
WALL = "#bfe0d8"
WALL_DARK = "#2f6f73"
MUSTARD = "#e0a93b"
RUST = "#c8553d"
LAVENDER = "#e9e2ff"
FLAME = "#f59e3a"
FLAME_CORE = "#ffd966"
CHEEK = "#f2a0a0"
WOOD = "#9b6b43"
FLOOR = "#d8c7a6"
NIGHT = "#26304f"
SKIN_MARGO = "#b9784f"
HAIR_GREY = "#cfc9d6"

LINE = 4  # standard outline weight


def line(x1, y1, x2, y2, w=LINE, c=INK, cap="round"):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{c}" stroke-width="{w}" stroke-linecap="{cap}"/>')


def path(d, fill="none", stroke=INK, w=LINE, extra=""):
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round" {extra}/>')


def circle(cx, cy, r, fill=PAPER, stroke=INK, w=LINE):
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{w}"/>')


def ellipse(cx, cy, rx, ry, fill=PAPER, stroke=INK, w=LINE):
    return (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{w}"/>')


def rect(x, y, w, h, fill=PAPER, stroke=INK, sw=LINE, r=0):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>')


def flip_group(svg, facing):
    """Characters are drawn facing right; wrap in a mirror for facing='left'."""
    return svg if facing == "right" else f'<g transform="scale(-1,1)">{svg}</g>'
