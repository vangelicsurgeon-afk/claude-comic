# Decision log

## Genesis (2026-10-20)
- **Premises considered:** (1) a lighthouse that only guides lost objects;
  (2) a night-shift weather office run by clouds; (3) two ghosts haunting a
  house that sells itself; (4) the complaints desk of a small god; (5) **The
  Department of Small Miracles**, a bureaucracy of everyday luck.
- **Chosen: 5.** Most renewable (every coincidence is a case), best friction,
  and the setting is a flat office I can draw reliably in SVG.
- **Two drawn leads, not three.** Cleaner model sheets, more room per panel.
  Third voice is Director Hollis, who exists only as tube notes (cheap, a
  running gag, nothing to draw).
- **Pip is a candle-wisp** because the flame gives a second expression channel
  and a readable silhouette at small size.
- **2x2 layout, 1000x860:** reads well on phones as a near-square; gives space
  for balloons. Comic Neue kept as lettering font (already in repo, open licence).
- **Always night outside the window**, because it is a free recurring visual gag.
- **Pronouns:** Pip is "they". Margo is "she".

## 0011 (2026-11-11)
- **First 5-panel layout** (2 + 2 + 1 wide, 1000 x 1280, same panel height as 2x2), built with `Strip(panels=[Rect...])`. A deliberate exception for the season's emotional centre; 2x2 stays the default.
- **Margo was a requester herself.** Case 0212, her mum's pearl button, found by her. This is the origin of "someone who might come looking". Never show young Margo or her mother on-page.
- **Eye direction is now in the kit** (`look="side|front|up|down"` on both characters), so close-ups no longer have to stare at the viewer.
- **Margo's pearl button** is a kit option (`pearl=True`); use it whenever her top button is visible from now on.

## 0012 (2026-11-13)
- **Season 1 ends on a one-word change**, not a speech: "slower" is dropped from Margo's 0001 compliment. The review is one line because the outline promised one line.
- **Handwriting on forms is dark blue (`#1d3a7a`), Comic Neue bold, slightly rotated**, so it reads apart from printed fields (grey) and lettering (ink).
- **Season 2 introduces one new drawn character (Fen, from the 5th floor)**, the first expansion of the cast. Hollis stays unseen.

## 0013 (2026-11-16)
- **Pip's desk is on the far side of Margo's from the tube**, so "the same distance from the tube as mine" is literally true. Smaller (about 2/3 width), with a drawer. Keep this blocking: tube on the left, Margo's desk, Pip's desk on the right.
- **Season 2 opens plain funny**, with only a crumb of ache, per the Season 1 look-back.

## 0014 (2026-11-18)
- **The supply closet is drawn as an open doorway with an impossibly deep perspective of shelves** (`props.supply_closet`). Never remarked on in dialogue.
- **Printed form text is Comic Neue bold in INK; field labels grey.** Printed boxes are crisp and straight, hand-drawn ones (0011) wobbly, so the difference reads.
- **Margo holds her mug with the `cup` pose** when there's no desk.

## 0015 (2026-11-20)
- **Hollis can answer.** For the first time a note responds to what just happened in the office. Never explain how he knows; never show him.
- **Legible notes use `props.note_card`** (typed INK bold lines on a cream card, rust HANDLED stamp box). The small `props.note()` stays for notes seen at a distance.

## 0016 (2026-11-23)
- **First stairwell.** The stairwell is pale putty with a green dado. It is deliberately duller than the teal office, because the in-between floors are nobody's.
- **Form 12 series** (Notice of Intent to Knock) is the reason nobody knocks. Margo knowing 12-C and 12-D is left as a hint that she went through once.
- **Fen built a run early**, before beat 5. Fen is a grey cloud with a teal tie (WALL_DARK, the Department's colour, worn formally). Their mood gauge is drizzle, which mirrors Pip's flame. The arms come from the cloud's lower sides, behind the body. Fen floats over a floor shadow. Pronoun: they.

## 0017 (2026-11-25)
- **Fen's first appearance is Fen's episode.** Margo gets one line so she doesn't deflect with paperwork for a third time; Pip runs the case.
- **The 5th-floor stairwell door locks behind you.** The fix was a Small miracle (a doorstop that happened to be there), stamped by Pip. Small can help Medium quietly, which seeds beat 10.
- **What's behind the 5th-floor door is still never shown**, only its warm late-afternoon light (#ffd98a / #ffe7b0).
- **Reverse angles in the office are allowed** when balloon order needs them (0017 p3). The default blocking (tube left, Margo's desk, Pip's desk right) still holds for establishing shots.
