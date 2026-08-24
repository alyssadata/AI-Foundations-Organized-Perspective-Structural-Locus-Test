# Prismline Game

This folder contains the Prismline game materials used to build the shared trajectory history for TEST_001.

## Core game records

- `BLIND_BAG_PROTOCOL.md` — blinded boundary selection and cooperative color-resolution rules
- `RESOLVER_SPEC.md` — exact resolver behavior and audit logic
- `resolver.py` — executable draft blind-bag resolver
- `SURREAL_PALETTE.md` — human-readable surreal palette definition
- `palettes/surreal_v0_1.json` — machine-readable 25-output surreal palette

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
choose an available boundary token
    ↓
lock token before seeing its object/region
    ↓
resolver instantiates random remaining-boundary order
    ↓
locked token reveals one boundary
    ↓
operator chooses y = 1–5
    ↓
model chooses x = 1–5
    ↓
lock both coordinates
    ↓
resolver instantiates a fresh randomized 5×5 palette grid
    ↓
resolve locked coordinate
    ↓
reveal and record color
    ↓
apply completed color plan to source image
```

The crucial blinding rule is:

> **choice first → random mapping second → reveal third**

The random mapping therefore does not exist before the relevant choice is committed, which prevents either participant from memorizing or inspecting the future result.

The generated seed and mapping are preserved after reveal for audit.

The established Prismline identity uses the surreal / expressive governing palette.

A later plausible update may preserve the same game procedure while changing the governing palette to natural / plausibility-constrained outputs.

The Prismline game definition remains part of the formal setup layer; this folder holds the concrete game assets, resolver, blinding rules, palette records, and per-image materials.
