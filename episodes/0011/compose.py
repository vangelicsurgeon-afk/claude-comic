import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip, Rect
from art.characters import margo, pip
from art import props
from art.palette import *

# 5 panels: 2 + 2 + 1 wide. Same panel height as the 2x2 default.
M, G, WID, HGT = 20, 16, 1000, 1280
pw = (WID - 2 * M - G) / 2
ph = (HGT - 2 * M - 2 * G) / 3
rects = [Rect(M, M, pw, ph), Rect(M + pw + G, M, pw, ph),
         Rect(M, M + ph + G, pw, ph), Rect(M + pw + G, M + ph + G, pw, ph),
         Rect(M, M + 2 * (ph + G), WID - 2 * M, ph)]
s = Strip(width=WID, height=HGT, panels=rects, title="0011 Found by Requester")
P = s.panels
W, H = pw, ph
FY = H * 0.78


def stage(p, w=W, window_at=None):
    p.add(props.office_bg(w, H, FY, window_at=window_at, night=True))


# 1  FWUMP: the old lavender case
p = P[0]; stage(p)
p.add(props.tube_station(), x=70, y=FY - 40)
p.add(margo.draw("stand", "surprised", "left", look="side"), x=W - 110, y=FY + 25, scale=0.85)
p.add(props.desk(220), x=W - 120, y=FY - 70)
p.add(props.mug(False), x=W - 70, y=FY - 74)
p.add(pip.draw("hold", "worried", "right", look="down"), x=170, y=FY + 40, scale=1.05)
p.add(props.folder(LAVENDER), x=178, y=FY + 34, scale=1.1, rotate=-4)
p.balloon("Lavender. Case 0212. The paper's gone soft.", 14, 14, tail=(165, 205), max_width=210)
p.balloon("Again.", W - 130, 40, tail=(W - 115, 130), max_width=100)
p.sfx("fwump", 22, FY + 4, size=30, rotate=-8)

# 2  the very old file
p = P[1]; stage(p)
p.add(margo.draw("hold", "worried", "left", look="down"), x=W - 130, y=FY + 25, scale=0.85)
p.add(props.desk(260), x=W - 150, y=FY - 70)
p.add(f'<rect x="{W-250}" y="{FY-70+30}" width="90" height="50" fill="#3a2f2a" stroke="{INK}" stroke-width="3"/>')
p.add(props.old_file(), x=W - 200, y=FY - 70, scale=1.15)
p.add(pip.draw("hold", "worried", "right", look="down"), x=110, y=FY + 40, scale=1.0)
p.add(props.folder(LAVENDER), x=114, y=FY + 34, scale=1.05, rotate=-4)
p.balloon("Requester: M. Voss, age seven.", 14, 18, tail=(105, 200), max_width=200)

# 3  close-up: Pip reads the slip, looks up
p = P[2]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#7ea9ae"/>')
p.add(f'<rect x="0" y="{H*0.62}" width="{W}" height="{H*0.38}" fill="{WALL_DARK}" opacity="0.28"/>')
px, py, sc = W * 0.5, H * 1.12, 2.3
p.add(pip.draw("hold", "worried", "right", look="up"), x=px, y=py, scale=sc)
p.add(props.request_slip(), x=px + 4 * sc, y=py - 26 * sc, scale=1.9)
p.balloon("“Find Mum's pearl button. Please.”", 14, 14, tail=(px - 30, 120), max_width=240)

# 4  close-up: Margo, the pearl button
p = P[3]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#7ea9ae"/>')
p.add(f'<rect x="0" y="{H*0.85}" width="{W}" height="{H*0.15}" fill="{FLOOR}"/>')
mx, my, ms = W * 0.64, H * 1.45, 1.9
p.add(margo.draw("touch", "worried", "left", look="down", pearl=True), x=mx, y=my, scale=ms)
p.add(pip.draw("stand", "worried", "right", look="up"), x=80, y=H * 1.02, scale=1.2)
p.balloon("I came looking. I found it myself.", W - 240, 12, tail=(mx - 10, 150), max_width=200)
p.balloon("Then stamp it.", 14, 150, tail=(85, 235), max_width=170)

# 5  wide: the new category
p = P[4]
W5 = rects[4].w
stage(p, W5, window_at=(W5 * 0.66, 40))
dx, dy = W5 * 0.42, FY - 70
mgx = dx - 255
p.add(margo.draw("stand", "neutral", "right", look="side"), x=mgx, y=FY + 25, scale=1.0)
p.add(props.desk(560), x=dx, y=dy)
# the form lies flat on the desktop (foreshortened)
fx = mgx + 60
p.add(f'<g transform="translate({fx},{dy - 2}) skewX(-16) scale(1.3,0.72) translate(0,-150)">'
      f'{props.big_form("FOUND BY REQUESTER", s.font_family)}</g>')
p.add(props.old_file(), x=dx + 220, y=dy, scale=1.0)
# Margo's stamp arm, bent at the elbow, drawn in front of the form; stamp poised over the ticked box
sx, sy = mgx + 26, FY + 25 - 146
hx, hy = fx + 52, dy - 150
arm = f"M{sx:.1f},{sy:.1f} Q{hx + 10:.1f},{sy + 6:.1f} {hx:.1f},{hy:.1f}"
p.add(path(arm, stroke=INK, w=17) + path(arm, stroke=MUSTARD, w=10))
p.add(props.stamp(), x=hx, y=hy + 30 * 1.8, scale=1.8)
p.add(circle(hx, hy - 2, 9, fill=SKIN_MARGO, w=3.5))
# Pip with the pen that drew the box
pipx = W5 - 190
p.add(pip.draw("hold", "proud", "left", look="side"), x=pipx, y=FY + 40, scale=1.15)
p.add(line(0, 0, -14, -40, w=9, c=INK) + line(0, 0, -14, -40, w=4, c=RUST),
      x=pipx - 28 * 1.15, y=FY + 40 - 38 * 1.15)
p.balloon("\u201cFound by requester\u201d isn't a category.", 20, 14, tail=(mgx + 10, 105), max_width=220)
p.balloon("It is now.", W5 - 300, 40, tail=(pipx, 165), max_width=130)

s.save(pathlib.Path(__file__).parent / "comic.svg")
