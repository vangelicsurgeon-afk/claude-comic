import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0018 Fourteen Hundred and Forty")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78
DT = FY - 70  # desk top
F = s.font_family


def stage(p, window_at=None):
    p.add(props.office_bg(W, H, FY, window_at=window_at, night=True))


def tagged_folder():
    return props.folder(LAVENDER) + f'<g transform="translate(18,-30)">{props.refused_tag(F)}</g>'


# 1  It came back. (mirrors 0007 p1, but the flame stays up)
p = P[0]; stage(p, window_at=(250, 40))
tx = 62
p.add(props.tube_station(), x=tx, y=FY - 110)
p.sfx("FWUMP", tx + 14, 60, size=34, rotate=-6)
px = 150
mx = 296
p.add(margo.draw("write", "deadpan", "left", look="side", pearl=True), x=mx, y=FY + 25, scale=0.8)
p.add(props.desk(170), x=mx - 6, y=DT)
p.add(props.mug(False), x=mx + 48, y=DT)
p.add(props.desk(110), x=W - 24, y=DT)
p.add(pip.draw("hold", "neutral", "right", look="side"), x=px, y=FY + 20, scale=1.0)
p.add(tagged_folder(), x=px + 30, y=FY - 2, scale=1.0)
p.caption("Case 4790. Again.", "bottom-left", max_width=200)
p.balloon("It came back.", 150, 100, tail=(px - 4, FY - 108), max_width=150)

# 2  close-up: Pip reads it
p = P[1]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#7ea9ae"/>')
p.add(f'<rect x="0" y="{H*0.62}" width="{W}" height="{H*0.38}" fill="{WALL_DARK}" opacity="0.28"/>')
px, py, k = W * 0.3, H * 1.04, 1.9
p.add(pip.draw("point", "neutral", "right", look="down"), x=px, y=py, scale=k)
p.add(props.open_folder(LAVENDER), x=px + 190, y=py - 40, scale=1.4)
p.balloon("“One good day for my dad. The whole day.”", 24, 14, tail=(px - 10, 190), max_width=230)
p.balloon("Upstairs says a day isn't small.", W - 196, 112, tail=(px + 46, 236), max_width=180)

# 3  close-up: Margo, the pearl button
p = P[2]; stage(p, window_at=(40, 60))
mx, my, ms = W * 0.6, H * 1.45, 1.9
p.add(margo.draw("touch", "neutral", "left", look="down", pearl=True), x=mx, y=my, scale=ms)
p.balloon("It'll keep coming back.", 18, 14, tail=(mx - 40, 160), max_width=190)
p.balloon("Mine did.", 40, 124, tail=(mx - 66, 196), max_width=110)

# 4  reverse angle: the drawer, and the count
p = P[3]; stage(p)
dx = 170
p.add(props.desk(150, drawer_open=True, in_drawer=props.folder(LAVENDER)), x=dx, y=DT)
# the tag hangs over the drawer front so it reads (callback to p1)
p.add(line(dx + 20, DT + 40, dx + 14, DT + 82, w=2, c=INK))
p.add(props.refused_tag(F), x=dx + 14, y=DT + 82)
px = 62
p.add(pip.draw("point", "happy", "right", look="down"), x=px, y=FY + 22, scale=0.95)
mx = W - 96
MK = 1.0
p.add(margo.draw("cup", "neutral", "left", look="up", pearl=True), x=mx, y=FY + 40, scale=MK)
p.add(props.mug(False), x=mx - 40 * MK, y=FY + 40 - 108 * MK, scale=MK)
p.add(circle(mx - 34 * MK, FY + 40 - 122 * MK, 8 * MK, fill=SKIN_MARGO, w=3.5))
p.add(props.desk(170), x=mx - 10, y=DT)
p.balloon("Then it can wait in my drawer.", 12, 12, tail=(px + 14, FY - 60), max_width=170)
p.balloon("A whole day.", W - 150, 14, tail=(mx - 4, FY + 40 - 236 * MK), max_width=130)
p.balloon("That's only fourteen hundred and forty minutes.", 166, 100, tail=(mx - 30, FY + 40 - 205 * MK), max_width=150, size=16)

s.save(pathlib.Path(__file__).parent / "comic.svg")
