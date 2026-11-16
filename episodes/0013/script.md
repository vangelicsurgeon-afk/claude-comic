# 0013 – What Luck
Logline: Pip gets their own desk and stamp, and their first solo case is suspiciously easy: someone anonymous needs a pen that works.
Beat: Season 2 beat 1 (Pip's own desk and stamp; first solo case). Callbacks: Margo's desk far from the tube (0002), the stamp in the bun (0009), the world rule that the target reaction is "What luck" (bible/world.md). Plain-funny episode with only a crumb of ache, per the Season 2 note.
Layout: 4 panels, 2x2

## Panel 1
Staging: Office, night window left. Far right, Margo's desk; tucked beside it on its right (the side further from the tube, which is off-panel on the left wall), a new, much smaller desk (about half the width). Pip floats in front of the small desk, flame tall, eyes wide (surprised/happy). Margo stands behind her own desk, deadpan, gesturing at it.
Dialogue:
- MARGO: Your desk. Same distance from the tube as mine.
- PIP: It has a drawer!

## Panel 2
Staging: Closer two-shot. Margo holds out a new rust stamp in one hand toward Pip. Pip, both arms up to receive it, flame tall, looking at the stamp (look up).
Dialogue:
- MARGO: Your stamp. Don't file it anywhere I would.

## Panel 3
Staging: Pip hovers behind the small desk with a mustard folder open, reading the slip; their own stamp on the desk. In the background, at her desk, Margo scribbles on a form with a pen; little scratch marks but no ink (a small dry-scribble mark near the nib), Margo annoyed, not looking at Pip.
Dialogue:
- PIP: Case 4831. "Find a pen that works." Requester: anonymous.

## Panel 4
Staging: Pip brings their stamp down on the folder: KA-CHUNK. Beside it, Margo's pen now draws a clean blue line. Margo, half-lidded, does not look up. Pip side-eyes her, flame tall.
Dialogue:
- MARGO: What luck.
Caption/SFX: KA-CHUNK

## Script review notes
APPROVE. Taken: Pip's desk is on the far side of Margo's from the tube; pen and blue line drawn large; tube hatch visible far left in panel 3 so the case visibly arrived by tube; three copies (white/yellow/pink) on Pip's desk in panel 3; Pip's flame varied (tall p1-2, leaning/curious p3, tall p4 with a side-eye). Not taken: an insert close-up for p4 (the joke needs both faces in one frame).

## New art needed
- small desk: `props.desk(w)` at w ~130 works but the drawer is fixed-size; add `props.desk(w, small=True)` or scale the desk.
- Pip holding a stamp (place `props.stamp()` near hands in `hold`/`arms_up` pose).
- dry pen scribble marks vs. a working blue line near Margo's pen (draw in compose; Margo's `pen()` hand works for an insert only, so in a two-shot just draw the line under her hand).
