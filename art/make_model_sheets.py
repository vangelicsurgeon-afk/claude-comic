"""Regenerates art/model-sheets/*.svg. Run: python3 art/make_model_sheets.py then tools/render.py."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art.palette import PAPER, INK

OUT = ROOT / "art" / "model-sheets"


def label(p, text, x, y, size=16):
    p.raw(f'<text x="{x}" y="{y}" font-family="Comic Neue" font-size="{size}" '
          f'font-weight="700" fill="{INK}" text-anchor="middle">{text}</text>')


def sheet(name, mod, poses, exprs, head_pose, scale, foot, cell_h, head_crop):
    cols = max(len(poses), len(exprs))
    W = 190 * cols + 40
    H = 60 + cell_h + 60 + 60 + 250 + 20
    s = Strip(width=W, height=H, cols=1, rows=1, margin=0, gutter=0, title=f"{name} model sheet")
    p = s.panels[0]; p.border_width = 0; p.background(PAPER)
    label(p, f"{name.upper()} – poses (neutral face)", W / 2, 32, 22)
    for i, po in enumerate(poses):
        x = 20 + 95 + i * 190
        p.add(mod.draw(po, "neutral"), x=x, y=60 + cell_h, scale=scale)
        label(p, po, x, 60 + cell_h + 26)
    y0 = 60 + cell_h + 60
    label(p, "expressions", W / 2, y0 - 6, 22)
    for i, ex in enumerate(exprs):
        x = 20 + 95 + i * 190
        p.add(mod.draw("stand", ex), x=x, y=y0 + 60 + head_crop[0], scale=head_crop[1])
        label(p, ex, x, y0 + 60 + 240)
    s.save(OUT / f"{name}.svg")


sheet("margo", margo, ["stand", "point", "shrug", "hold", "arms_up", "sit_desk"],
      ["neutral", "deadpan", "happy", "worried", "surprised", "smug", "annoyed"],
      "stand", 0.8, 0, 200, (190, 1.0))
sheet("pip", pip, ["stand", "point", "wave", "hold", "arms_up", "slump"],
      ["neutral", "happy", "worried", "surprised", "proud", "sad", "flustered"],
      "stand", 1.2, 0, 150, (150, 1.35))
