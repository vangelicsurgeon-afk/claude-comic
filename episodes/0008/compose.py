import sys, pathlib, random
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
from comic import Strip
from art.characters import margo, pip
from art import props
from art.palette import *

s = Strip(width=1000, height=860, cols=2, rows=2, margin=20, gutter=16, title="0008 Fourth Row")
P = s.panels
W, H = P[0].rect.w, P[0].rect.h
FY = H * 0.78
fam = s.font_family


def stage(p):
    p.add(props.office_bg(W, H, FY, night=True))


# 1  case 4811
p = P[0]; stage(p)
p.add(margo.draw("stand", "deadpan", "left"), x=W - 110, y=FY + 25, scale=0.85)
p.add(props.desk(250), x=W - 130, y=FY - 70)
p.add(props.tin(), x=W - 190, y=FY - 70, scale=1.3)
p.add(pip.draw("hold", "neutral", "right"), x=150, y=FY + 40, scale=1.2)
p.add(props.folder(MUSTARD), x=205, y=FY - 30, scale=0.9, rotate=-10)
p.balloon("Case 4811. Navy coat, one button missing, four holes.", 20, 20, tail=(140, 190), max_width=250)
p.balloon("Check the tin.", 290, 125, tail=(W - 130, 185), max_width=150)

# 2  peering in
p = P[1]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WALL}"/>')
p.add(f'<rect x="0" y="{H*0.8}" width="{W}" height="{H*0.2}" fill="{FLOOR}"/>')
p.add(pip.draw("stand", "surprised", "right"), x=W / 2 - 40, y=H * 0.98, scale=2.2)
p.balloon("There are hundreds.", 20, 20, tail=(W / 2 - 60, 160), max_width=190)
p.balloon("Two hundred and eleven.", W - 230, 215, tail=(W - 4, 300), max_width=200)

# 3  tin from above
p = P[2]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WOOD}"/>')
cx, cy, R = W / 2, H / 2 + 30, 175
p.add(circle(cx, cy, R + 14, fill=MUSTARD, w=4) + circle(cx, cy, R, fill=RUST, w=4) + circle(cx, cy, R - 10, fill="#7a2f20", w=0))
rnd = random.Random(8)
cols = ["#7ea58a", "#a9743c", "#8a8f9a", "#d9d3c3", "#b7576a", "#e0a93b", "#f2eadb"]
navy = (cx + 60, cy + 20)
pts = []
for row in range(-3, 4):
    for col in range(-3, 4):
        x, y = cx + col * 44, cy + row * 42
        if (x - cx) ** 2 + (y - cy) ** 2 < (R - 32) ** 2:
            pts.append((x + rnd.randint(-4, 4), y + rnd.randint(-4, 4)))
navy = min(pts, key=lambda q: (q[0]-navy[0])**2 + (q[1]-navy[1])**2)
for (x, y) in pts:
    c = "#26304f" if (x, y) == navy else rnd.choice(cols)
    p.add(circle(x, y, 15, fill=c, w=3) + circle(x - 4, y - 3, 2, fill=INK, w=0) + circle(x + 4, y + 3, 2, fill=INK, w=0))
    p.add(line(x + 12, y + 10, x + 24, y + 22, w=2) + rect(x + 20, y + 18, 14, 9, fill="#fff5c8", sw=2))
p.add(circle(navy[0], navy[1], 24, fill="none", stroke=RUST, w=4))
bx, by = pts[0]
p.balloon("\"Green. Bus seat.\" \"Brown. Laughed.\"", 10, 12, tail=(120, 150), max_width=210)
p.balloon("Navy. Fourth row.", W - 200, 12, tail=(W - 150, 130), max_width=170)
p.sfx("clink", W - 120, H - 20, size=34, rotate=-6)

# 4  top button
p = P[3]
p.add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WALL}"/>')
p.add(f'<rect x="0" y="{H*0.85}" width="{W}" height="{H*0.15}" fill="{FLOOR}"/>')
p.add(margo.draw("stand", "deadpan", "left"), x=W * 0.62, y=H * 1.45, scale=1.9)
bx, by = W * 0.62 - 7 * 1.9, H * 1.45 - 132 * 1.9
p.add(circle(bx, by, 11, fill="#f6f1e6", w=3.5) + circle(bx, by, 5, fill="none", stroke=INK, w=2))
p.add(pip.draw("stand", "neutral", "right"), x=90, y=H * 1.02, scale=1.3)
p.balloon("Your top button doesn't match.", 14, 14, tail=(100, 200), max_width=200)
p.balloon("It's very well documented.", 250, 20, tail=(W * 0.62 - 20, 130), max_width=200)

s.save(pathlib.Path(__file__).parent / "comic.svg")
