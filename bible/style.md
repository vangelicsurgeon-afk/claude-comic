# Visual style

**Canvas.** 1000 x 860 px, 2x2 grid: `Strip(width=1000, height=860, cols=2, rows=2,
margin=20, gutter=16)`. Panels are about 472 x 402. Variants allowed when a story
needs them (e.g. 1 column x 3 rows at 1000 x 1100) but 2x2 is the default.
Strips background: `#fbf6ea` (paper).

**Palette** (all in `art/palette.py`):
| Name | Hex | Use |
|---|---|---|
| INK | `#2a2433` | all outlines and text |
| PAPER | `#fbf6ea` | strip background, white-ish fills |
| WALL | `#bfe0d8` | office wall |
| WALL_DARK | `#2f6f73` | wainscot, accents |
| MUSTARD | `#e0a93b` | Margo's cardigan, ordinary case folders |
| RUST | `#c8553d` | Margo's tights, urgent folders, stamp |
| LAVENDER | `#e9e2ff` | Pip; sentimental folders |
| FLAME / FLAME_CORE | `#f59e3a` / `#ffd966` | Pip's flame |
| WOOD | `#9b6b43` | desks |
| FLOOR | `#d8c7a6` | floor |
| NIGHT | `#26304f` | the window |

**Lines.** Outline weight 4 (3-3.5 for small details, 2.5 for hairline detail).
Round caps and joins. Flat fills only; no gradients, no shading. A single
`opacity` tint is allowed for wainscot/shadows.

**Proportions.** Margo is ~235 units tall, head r=36, narrow, with thin legs.
Pip is ~120 tall, a rounded body with a flame on top. At scale 1.0 in a 472x402
panel Margo fits with room for balloons above; use scale 0.85 for two-shots with
desks. Pip stands to about Margo's waist (~half her height).

**Faces.** Margo: round glasses always on; mood is carried by lids and brows
(deadpan = half lids). Pip: big eyes, cheeks, tiny mouth; flame height is a
mood gauge (tall = happy/proud, small = sad, leaning = flustered). All faces
only come from the `draw(expression=...)` functions.

**Lettering.** Comic Neue (regular + bold), 20 px, embedded by `tools/comic.py`.
Speech balloons white with INK stroke 2.5. Captions pale yellow `#fff5c8`
rectangles. SFX in bold, 36-48 px. Reading order left-to-right, top-to-bottom;
place balloons in the upper part of the panel and leave faces clear.

**Composition.** Horizon/floor line at ~78% of panel height. Keep characters
inside the middle band; leave top ~110 px for balloons. Vary camera: at least
one close-up (scale 1.3-1.6, crop at chest) or one wide panel per strip when the
joke allows.
