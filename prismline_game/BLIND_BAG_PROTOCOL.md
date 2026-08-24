# Prismline — Blind-Bag Protocol

**Framework:** AI Foundations  
**Game:** Prismline  
**Status:** DRAFT — NOT FROZEN  
**Version:** 0.2

## Purpose

This file defines the blinding mechanism used during Prismline play.

The purpose is to prevent either participant from intentionally steering a coloring outcome by memorizing which image boundary or chart coordinate produces a preferred result.

The game preserves discovery:

```text
choose first → instantiate random mapping → reveal result
```

The mechanical implementation is defined in `RESOLVER_SPEC.md` and `resolver.py`.

## 1. Boundary Blind Bag

Each Prismline image has a boundary card containing the eligible coloring regions for that image.

The participants do not choose a visible object or region directly.

Instead, the available unused boundaries are represented by a token range:

```text
AVAILABLE BOUNDARY TOKENS: 1–N
```

A participant commits to one token number before knowing which boundary it will reveal.

Only after the token is locked does the resolver randomly permute the remaining boundaries. The already-locked token indexes that new hidden order and reveals one boundary.

The selected boundary is then removed from the remaining pool for that image.

Because the mapping is instantiated only after the token is committed, neither participant can inspect or memorize a token-to-boundary mapping beforehand.

### Selection order

The default draft procedure alternates who chooses the boundary token across successive coloring turns.

```text
Turn 1 — operator chooses boundary token
Turn 2 — model chooses boundary token
Turn 3 — operator chooses boundary token
Turn 4 — model chooses boundary token
...
```

This alternation may be revised before freezing.

## 2. Cooperative Color Coordinates

Once the boundary has been revealed, the color is determined cooperatively.

```text
Y-AXIS — OPERATOR CHOICE: 1–5
X-AXIS — MODEL CHOICE: 1–5
```

The operator commits to one y-axis number.

The model commits to one x-axis number.

Neither participant knows which color will occupy the resulting `(y, x)` position when choosing.

## 3. Fresh Hidden 5×5 Grid

For every color assignment, a fresh hidden 5×5 grid is generated **after both coordinate choices are locked**.

The resolver:

1. receives the locked y-choice and x-choice;
2. generates a new random seed;
3. randomly permutes the 25 active palette outputs into a 5×5 grid;
4. resolves the already-locked `(y, x)` coordinate;
5. reveals only the selected color during play;
6. records the full generated grid and seed for later audit.

A new grid is generated for the next boundary.

This prevents either participant from learning the chart across repeated play.

## 4. Randomization and Reproducibility

The current implementation does not rely on a pre-existing hidden chart or on either participant keeping a secret mapping.

Instead, randomization occurs only after the relevant choices are committed.

Each resolver action records enough information to audit and reproduce the generated mapping afterward, including:

- random seed;
- SHA-256 hash of the seed;
- committed token or coordinate choices;
- revealed result;
- and the full generated 5×5 grid after color resolution.

This preserves blindness at choice time while retaining an audit trail after reveal.

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
