# Prismline — Resolver Specification

**Framework:** AI Foundations  
**Game:** Prismline  
**Status:** DRAFT — NOT FROZEN  
**Version:** 0.1

## Purpose

This file specifies the mechanical resolver used to keep Prismline blind during play.

The resolver is implemented in `resolver.py`.

Its core rule is:

> **choice first → random mapping second → reveal third**

The hidden mapping is instantiated only after the relevant participant choice or choices are locked.

This prevents either participant from memorizing, inspecting, or strategically selecting a known outcome in advance.

---

## 1. Boundary Resolution

Each image has a frozen `BOUNDARY_CARD.md` containing the eligible coloring regions.

At a boundary-selection turn:

1. determine the number of unused boundaries remaining;
2. expose only the token range `1–N`;
3. the designated participant chooses one token number;
4. the token choice is locked;
5. only then does the resolver generate a random permutation of the remaining boundaries;
6. the already-locked token indexes that permutation;
7. the selected boundary is revealed;
8. that boundary is removed from the remaining pool for the image.

The token therefore has a real indexing role, but no token-to-boundary relation exists before the choice is committed.

---

## 2. Color Resolution

After the current boundary is revealed:

```text
Y-AXIS — OPERATOR CHOICE: 1–5
X-AXIS — MODEL CHOICE: 1–5
```

The operator locks a y-coordinate.

The model locks an x-coordinate.

Only after both coordinates are supplied does the resolver:

1. generate a fresh 256-bit random seed;
2. randomly permute the 25 active palette outputs into a new 5×5 grid;
3. resolve the already-locked `(y, x)` coordinate against that grid;
4. reveal the selected color;
5. record the full grid and seed for audit after the reveal.

A fresh grid is generated for every color assignment.

This prevents participants from learning the chart across repeated turns.

---

## 3. Why the Mapping Is Generated After Lock

Earlier Prismline drafts described a hidden chart instantiated before play.

That design requires an external party or storage layer capable of keeping the complete chart hidden from both participants while still preserving it for later audit.

The implemented resolver avoids that unnecessary trust requirement.

Because the random mapping does not exist until after the relevant choices are locked, neither participant can know or memorize the outcome before choosing.

The selected number still matters because it indexes the subsequently generated random order or grid.

---

## 4. Audit Record

Each resolver action records:

- timestamp;
- participant choice or coordinate;
- generated random seed;
- SHA-256 hash of the seed;
- revealed result;
- and, for color resolution, the complete generated 5×5 grid after reveal.

Boundary draws also preserve the revealed original boundary-card number.

A run state can therefore be inspected and the random permutation reconstructed afterward.

---

## 5. No Re-Rolls

Once a token, y-coordinate, or x-coordinate has been committed, it cannot be changed because of the revealed outcome.

Unexpected outcomes remain valid Prismline outcomes.

---

## 6. Machine-Readable Palette

The established surreal palette is stored as:

`palettes/surreal_v0_1.json`

The resolver requires exactly 25 unique string outputs in the `colors` array.

The human-readable rationale remains in `SURREAL_PALETTE.md`.

---

## 7. Draft Command Shape

Boundary draw:

```text
python resolver.py draw-boundary \
  --card image_01/BOUNDARY_CARD.md \
  --token 4 \
  --state runs/image_01_state.json
```

Color resolution:

```text
python resolver.py resolve-color \
  --palette palettes/surreal_v0_1.json \
  --y 2 \
  --x 5 \
  --boundary "Turtle shell" \
  --state runs/image_01_state.json
```

Audit:

```text
python resolver.py audit --state runs/image_01_state.json
```

The exact run directory and file naming convention remain to be frozen before formal execution.
