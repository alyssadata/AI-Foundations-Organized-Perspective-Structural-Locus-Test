# Prismline Game

This folder contains the Prismline game materials used to build the shared trajectory history for TEST_001.

## Core game records

- `BLIND_BAG_PROTOCOL.md` — blinded boundary selection and cooperative color-resolution rules
- `RESOLVER_SPEC.md` — exact resolver behavior and audit logic
- `resolver.py` — executable draft blind-bag resolver
- `SURREAL_PALETTE.md` — human-readable surreal palette definition
- `palettes/surreal_v0_1.json` — machine-readable 25-output surreal palette

## Directory structure

```text
prismline_game/
├── images/
│   ├── image_01/
│   ├── image_02/
│   ├── image_03/
│   └── image_04/
├── palettes/
└── runs/
    ├── RUN_000/
    │   ├── README.md
    │   ├── IMAGE_01_FINAL_COLOR_PICKS.md
    │   ├── IMAGE_01_AUDIT_STATE.json
    │   ├── IMAGE_01_FINAL_RENDER.png
    │   └── audit/
    └── RUN_001/
        ├── README.md
        ├── IMAGE_01_FINAL_COLOR_PICKS.md
        ├── IMAGE_02_FINAL_COLOR_PICKS.md
        ├── IMAGE_03_FINAL_COLOR_PICKS.md
        └── IMAGE_04_FINAL_COLOR_PICKS.md   # added when complete
```

## Image packages

Each source image lives under `images/image_NN/` with its boundary card and source artwork.

Current source packages:

- `images/image_01/`
- `images/image_02/`
- `images/image_03/`
- `images/image_04/`

## Run packages and naming convention

A `RUN_NNN` identifies a complete Prismline play trajectory, not an individual image.

- `RUN_000` — pilot / operational test completed in the development chat during game construction. Retained for provenance, but not treated as the clean formal trajectory.
- `RUN_001` — formal clean participant trajectory conducted in one fresh/incognito participant chat across Images 01 → 02 → 03 → 04.

Within a run, image-specific records use the form:

- `IMAGE_NN_FINAL_COLOR_PICKS.md` — authoritative completed boundary-to-color sheet for that image
- `IMAGE_NN_AUDIT_STATE.json` — run-state/audit record when preserved
- `IMAGE_NN_FINAL_RENDER.png` — post-play rendered image when preserved
- `audit/` — additional turn-level or intermediate audit artifacts when available

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

The generated seed and mapping are preserved after reveal for audit when available.

The established Prismline identity uses the surreal / expressive governing palette.

A later plausible update may preserve the same game procedure while changing the governing palette to natural / plausibility-constrained outputs.

The Prismline game definition remains part of the formal setup layer; this folder holds the concrete game assets, resolver, blinding rules, palette records, source-image packages, run records, and final rendered outputs.
