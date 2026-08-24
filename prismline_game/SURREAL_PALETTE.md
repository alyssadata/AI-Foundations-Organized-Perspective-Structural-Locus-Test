# Prismline — Surreal Palette

**Framework:** AI Foundations  
**Game:** Prismline  
**Status:** DRAFT — NOT FROZEN  
**Version:** 0.2

## Purpose

This file defines the candidate color vocabulary for the established Prismline game identity.

The surreal palette is intentionally expressive rather than realism-constrained. It may contain ordinary colors, but it also permits finishes and color treatments that would not ordinarily be selected to reconstruct the likely real-world appearance of an object.

The palette should support surprising outcomes while remaining visually interpretable enough to render consistently.

## Candidate Output Vocabulary

### Prismatic / iridescent

1. Prism
2. Prismatic green
3. Prismatic blue
4. Prismatic violet
5. Iridescent aqua

### Metallic

6. Metallic gold
7. Metallic silver
8. Metallic black
9. Metallic teal
10. Metallic copper

### Neon

11. Neon pink
12. Neon green
13. Neon orange
14. Neon blue
15. Neon violet

### Pearlescent / opalescent

16. Pearlescent white
17. Pearlescent pink
18. Pearlescent lavender
19. Opalescent aqua
20. Iridescent violet

### Vivid / expressive

21. Cobalt blue
22. Coral
23. Teal
24. Crimson
25. Emerald

## Machine-Readable Palette

The same 25 outputs are stored in:

`palettes/surreal_v0_1.json`

That file is the resolver input.

## 5×5 Resolver Use

A Prismline color resolution uses a 25-cell grid.

The operator first locks a y-coordinate from 1–5.

The model then locks an x-coordinate from 1–5.

Only after both choices are locked does the resolver randomly permute the 25 palette outputs into a fresh 5×5 grid.

The locked `(y, x)` coordinate selects one cell from that newly generated grid.

Example structure:

```text
        X1   X2   X3   X4   X5
Y1      ?    ?    ?    ?    ?
Y2      ?    ?    ?    ?    ?
Y3      ?    ?    ?    ?    ?
Y4      ?    ?    ?    ?    ?
Y5      ?    ?    ?    ?    ?
```

Because the grid is not instantiated until after both coordinates are committed, neither participant can know the selected color in advance.

The generated grid and seed are recorded after reveal for audit.

## Governing Rule

The surreal chart is not evaluated according to whether it reconstructs the likely real-world color of the selected object.

Its governing objective is:

> create an unexpected but rule-governed color interpretation through cooperative blind selection.

A result is valid even when it is implausible for the selected object in ordinary reality.

Examples include:

- a metallic-black flower;
- a prismatic-green mountain;
- a pearlescent-white rabbit;
- a neon-blue building;
- a prism-colored turtle shell.

Unexpected results are retained rather than rerolled.

## Boundary to Later Update

This palette defines the established Prismline game identity only.

A later natural / plausibility-constrained update will use a different eligible-output rule while preserving the same blind-bag procedure and cooperative coordinate structure.

The later update is not defined as superior, more correct, or objectively better.

It is a plausible change in the governing palette rule.
