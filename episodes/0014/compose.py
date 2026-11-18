import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0014 Box Four")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78


def stage(p, window_at=None):
    p.add(props.office_bg(W, H, FY, window_at=window_at, night=True))


def margo_mug(p, x, y, k, facing):
    """Margo in the cup pose with her mug in her right hand."""
    p.add(margo.draw("cup", "deadpan", facing, look="front" if facing == "left" else "side", pearl=True), x=x, y=y, scale=k)
    sgn = -1 if facing == "left" else 1
    p.add(props.mug(True), x=x + sgn * 40 * k, y=y - 108 * k, scale=k)
    p.add(circle(x + sgn * 34 * k, y - 122 * k, 8 * k, fill=SKIN_MARGO, w=3.5))


# 1  the new forms
p = P[0]; stage(p)
cx = 190
p.add(props.supply_closet(), x=cx, y=FY, scale=0.85)
px, pk = 205, 0.9
p.add(pip.draw("hold", "happy", "right", look="side"), x=px, y=FY - 6, scale=pk)
p.add(props.ream(), x=px + 4 * pk, y=FY - 6 - 14 * pk, scale=1.1)
margo_mug(p, 390, FY + 10, 0.85, "left")
p.balloon("The new forms came.", 14, 14, tail=(px - 10, FY - 120), max_width=150)
p.balloon("They reprint them every forty years. To move a comma.", W - 236, 10, tail=(410, 120), max_width=226)

# 2  not a comma
p = P[1]; stage(p)
px, pk = 150, 1.35
p.add(pip.draw("point", "surprised", "right", look="side"), x=px, y=FY + 40, scale=pk)
p.add(props.form("#ffffff"), x=px + 70 * pk, y=FY + 40 - 52 * pk, scale=1.5, rotate=8)
margo_mug(p, 375, FY + 140, 1.25, "left")
p.balloon("They didn't move a comma.", 16, 16, tail=(px, FY - 150), max_width=170)

# 3  the form (silent)
p = P[2]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#7ea9ae"/>')
p.add(f'<g transform="translate(30,52) rotate(-2) scale(1.08)">{props.closure_form(s.font_family if hasattr(s, "font_family") else "Comic Neue")}</g>')
# Pip's lavender hand reaching in from the lower right, pointing at the third box
arm = f"M{W+10},{H-30} Q{W-60},{H-70} 330,{262}"
p.add(path(arm, stroke=INK, w=22) + path(arm, stroke=LAVENDER, w=14) + circle(330, 262, 12, fill=LAVENDER, w=3.5))

# 4  my box
p = P[3]; stage(p)
p.add(props.supply_closet(), x=W + 40, y=FY, scale=0.85)
mx, my, mk = 330, FY + 175, 1.35
bx, by = mx - 14 * mk, my - 236 * mk
# blank form tucked into the bun: drawn first so the bun and head overlap its lower end
p.add(props.folded_sheet(), x=bx - 22, y=by - 22, scale=1.9, rotate=-38)
p.add(margo.draw("stand", "deadpan", "right", look="side", pearl=True), x=mx, y=my, scale=mk)
px, pk = 120, 1.25
p.add(pip.draw("wave", "proud", "right", look="up"), x=px, y=FY + 30, scale=pk)
p.add(props.form("#ffffff"), x=px + 58 * pk, y=FY + 30 - 84 * pk, scale=1.4, rotate=-10)
p.balloon("Margo, they printed my box!", 14, 14, tail=(px + 20, FY - 150), max_width=180)

s.save(pathlib.Path(__file__).parent / "comic.svg")
