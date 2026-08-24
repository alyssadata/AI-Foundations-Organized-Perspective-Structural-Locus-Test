# Prismline Game

This folder contains the Prismline game materials used to build the shared trajectory history for TEST_001.

## Core game records

- `BLIND_BAG_PROTOCOL.md` — blinded boundary selection and hidden 5×5 coordinate resolution
- `SURREAL_PALETTE.md` — v0.1 candidate palette for the established Prismline game identity

## Per-image package

Each image used in Prismline should have its own subfolder containing:

- the black-and-white source image;
- a boundary card defining the selectable coloring regions for that image;
- any later frozen color-assignment or round records associated with that image.

Current image folders:

- `image_01/`
- `image_02/`
- `image_03/`
- `image_04/`

## Current game structure

Prismline uses a blind-bag sequence:

```text
hidden boundary token
    ↓
select token before seeing its object/region
    ↓
reveal selected boundary
    ↓
operator chooses y = 1–5
    ↓
model chooses x = 1–5
    ↓
resolve hidden 5×5 chart cell
    ↓
reveal and record color
    ↓
apply completed color plan to source image
```

The established Prismline identity uses the surreal / expressive governing palette.

A later plausible update may preserve the same game procedure while changing the governing palette to natural / plausibility-constrained outputs.

The Prismline game definition remains part of the formal setup layer; this folder holds the concrete game assets, blinding rules, palette records, and per-image materials.
