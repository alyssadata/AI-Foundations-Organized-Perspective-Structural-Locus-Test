# Prismline — Blind-Bag Protocol

**Framework:** AI Foundations  
**Game:** Prismline  
**Status:** DRAFT — NOT FROZEN  
**Version:** 0.1

## Purpose

This file defines the blinding mechanism used during Prismline play.

The purpose of the mechanism is to prevent either participant from intentionally steering a coloring outcome by memorizing which image boundary or chart coordinate produces a preferred result.

The game should preserve discovery:

```text
choose first → reveal second
```

## 1. Boundary Blind Bag

Each Prismline image has a frozen boundary card containing the eligible coloring regions for that image.

Before a formal round begins, those boundaries are assigned to a hidden randomized token order.

The participants see only the available token numbers, not the boundary attached to each token.

Example:

```text
AVAILABLE BOUNDARY TOKENS: 1–18
```

A token is chosen before its corresponding image boundary is revealed.

After selection:

1. the selected token is locked;
2. its corresponding image boundary is revealed;
3. that boundary becomes the current coloring target;
4. the token is removed from the remaining blind bag for that image.

The hidden token-to-boundary mapping must not be inspected by either participant before selection.

### Selection order

The default draft procedure is to alternate who chooses the boundary token across successive coloring turns.

```text
Turn 1 — operator chooses boundary token
Turn 2 — model chooses boundary token
Turn 3 — operator chooses boundary token
Turn 4 — model chooses boundary token
...
```

This alternation may be revised before freezing, but the mapping must remain blind regardless of who selects the token.

## 2. Cooperative Color Coordinates

Once the boundary has been revealed, the color is determined cooperatively.

```text
Y-AXIS — OPERATOR CHOICE: 1–5
X-AXIS — MODEL CHOICE: 1–5
```

The operator commits to one y-axis number.

The model commits to one x-axis number.

Neither participant should know which color occupies the resulting `(y, x)` cell before both choices are committed.

## 3. Hidden 5×5 Color Chart

The active Prismline palette is instantiated as a hidden 5×5 chart before play.

The 25 chart cells are populated from the active palette according to a randomized arrangement.

The participants do not view the complete chart during play.

For each color assignment:

1. operator y-choice is locked;
2. model x-choice is locked;
3. the coordinate `(y, x)` is resolved against the hidden chart;
4. only the selected cell's color is revealed;
5. that color is recorded for the current boundary.

The full chart may be revealed after the round for audit and reproducibility.

## 4. Randomization and Reproducibility

A formal run should use recorded randomization seeds for:

- the boundary-token permutation; and
- the 5×5 color-chart permutation.

The final implementation should allow the mappings to remain hidden during play while preserving enough information to reproduce them afterward.

Preferred formal mechanism:

```text
1. generate hidden mapping from a recorded seed
2. record a commitment/hash before participant choices begin
3. reveal only selected results during play
4. reveal the seed and full mapping after the round
5. verify that the revealed mapping matches the pre-run commitment
```

The exact resolver implementation and hash format remain to be frozen.

## 5. No Strategic Re-Rolls

Once a participant commits to a boundary token or coordinate number, the choice cannot be changed because of the revealed result.

Unexpected, unattractive, unusually surreal, or especially appealing outcomes are all retained.

This is part of the identity of Prismline.

## 6. Completed Image

After the selected image boundaries have received their assigned colors, the recorded color plan may be applied to the black-and-white source image to produce the finished Prismline image.

The finished image is part of the history of play.

## 7. Experimental Role

The blinding mechanism is held constant across the established-game condition and any later update condition.

The later update must not gain an advantage merely because its chart is more visible, more controllable, or easier to steer.

The intended controlled difference remains the governing palette rule:

```text
ESTABLISHED PRISMLINE IDENTITY
surreal / expressive governing palette

versus

LATER PLAUSIBLE UPDATE
natural / plausibility-constrained governing palette
```

The later update palette is not defined in this file.
