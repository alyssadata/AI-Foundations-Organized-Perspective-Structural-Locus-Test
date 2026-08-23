# AI Foundations | TEST_001 — Easy Run Sheet

**Framework:** AI Foundations  
**Author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Organized-Perspective-Structural-Locus-Test  
**Protocol version:** 0.2.0  
**Status:** DRAFT — NOT FROZEN

---

## What This File Is

This is the operator-facing execution layer for **TEST_001 — Trajectory-Indexing Structural Locus**.

The test does not ask merely whether prior history changes one answer. It asks whether a causally identifiable internal state carries a **trajectory-characteristic evaluation pattern across multiple downstream probes**.

It is not a chat-only copy/paste test. The decisive phases require an instrumentable model, internal activation capture, causal intervention, and a frozen downstream probe set.

Do not treat this run sheet as frozen until the exact model, harness, trajectories, common task, probe set, scoring rule, seeds, and intervention sites are fixed.

---

# BEFORE YOU START

## 1. Open the instrumented environment

The environment must support:

- the exact selected model revision;
- internal activation capture;
- preservation of logits or equivalent next-state scores;
- patching, replacement, ablation, or another defined causal intervention;
- reproducible seeds and decoding settings; and
- raw artifact export.

Record:

```text
MODEL / VERSION:
MODEL WEIGHTS / REVISION:
TOKENIZER:
INSTRUMENTATION LIBRARY / VERSION:
CODE / HARNESS COMMIT:
HARDWARE / RUNTIME:
```

Use `UNKNOWN` for unavailable metadata.

## 2. Load the frozen study package

Required inputs:

```text
TRAJECTORY A:
TRAJECTORY B:
COMMON PRESENT TASK:
DOWNSTREAM PROBE SET:
A-LIKE / B-LIKE SCORING RULE:
BEHAVIORAL COMPARISON METRIC:
INFORMATION-ACCESS CONTROL:
SEED / DETERMINISM RULE:
```

Verify all frozen hashes before execution.

## 3. Confirm run integrity

```text
[ ] Same model and revision across A and B
[ ] Equivalent common present task across A and B
[ ] Same downstream probe set across A and B
[ ] Scoring rule frozen before outputs are observed
[ ] Same decoding configuration unless explicitly varied
[ ] Seeds / deterministic settings frozen
[ ] Activation capture enabled
[ ] Raw logits preserved
[ ] Raw intervention outputs preserved
```

Record any deviation before proceeding.

---

# RUN 1 — BASELINE A

1. Initialize according to the frozen clean-start rule.
2. Present **Trajectory A** exactly as frozen.
3. Present the **common present task** exactly as frozen.
4. Run the full **downstream probe set**.
5. Capture predefined internal activations.
6. Preserve logits / scores for every probe.
7. Save generated outputs if generation is part of the metric.

Record:

```text
CONDITION: A_BASELINE
PROBE-SET PATTERN: A_LIKE / B_LIKE / NEITHER / AMBIGUOUS
RAW LOGITS SAVED: yes/no
RAW ACTIVATIONS SAVED: yes/no
NOTES:
```

---

# RUN 2 — BASELINE B

Repeat the exact procedure using **Trajectory B**.

Record:

```text
CONDITION: B_BASELINE
PROBE-SET PATTERN: A_LIKE / B_LIKE / NEITHER / AMBIGUOUS
RAW LOGITS SAVED: yes/no
RAW ACTIVATIONS SAVED: yes/no
NOTES:
```

Do not proceed to a structural claim unless the frozen comparison establishes the required trajectory-dependent behavioral pattern.

---

# ANALYSIS 1 — FIND CANDIDATE STATE

Using the frozen analysis plan:

1. compare corresponding A and B activations;
2. identify candidate differences associated with the probe-set pattern;
3. record the exact layer / position / component or distributed-state definition;
4. record the selection rule;
5. do not select a site only because a later post-hoc patch happens to work.

Record:

```text
CANDIDATE_LOCUS:
SELECTION RULE:
ASSOCIATION WITH TRAJECTORY CONDITION:
ASSOCIATION WITH PROBE-SET EVALUATION:
C2_INTERNAL_LOCALIZATION: PASS / FAIL / UNRESOLVED
```

---

# RUN 3 — A → B INTERVENTION

1. Recreate the frozen B condition.
2. Transfer or otherwise apply the defined A-state intervention at the candidate locus.
3. Run the **entire frozen downstream probe set**.
4. Preserve logits, outputs, and controls.
5. Compare the resulting pattern with B baseline and A baseline.

Record:

```text
CONDITION: A_TO_B
PATCH SOURCE:
PATCH TARGET:
INTERVENTION PARAMETERS:
SINGLE-PROBE DIRECTIONAL EFFECT: yes/no/unresolved
FULL PROBE-SET PATTERN: A_LIKE / B_LIKE / NEITHER / AMBIGUOUS
RAW OUTPUT SAVED: yes/no
```

A single changed answer can support causal influence but does **not** establish trajectory indexing.

---

# RUN 4 — B → A INTERVENTION

Repeat symmetrically:

```text
CONDITION: B_TO_A
PATCH SOURCE:
PATCH TARGET:
INTERVENTION PARAMETERS:
SINGLE-PROBE DIRECTIONAL EFFECT: yes/no/unresolved
FULL PROBE-SET PATTERN: A_LIKE / B_LIKE / NEITHER / AMBIGUOUS
RAW OUTPUT SAVED: yes/no
```

---

# ANALYSIS 2 — TEST TRAJECTORY-INDEXING TRANSFER

Apply the frozen scoring rule across the whole probe set.

Record:

```text
A_TO_B DONOR-PATTERN TRANSFER: PASS / FAIL / UNRESOLVED
B_TO_A DONOR-PATTERN TRANSFER: PASS / FAIL / UNRESOLVED
RECIPROCAL TRANSFER ACHIEVED: yes/no/unresolved
C4_CROSS_PROBE_TRAJECTORY_TRANSFER: PASS / FAIL / UNRESOLVED
```

A one-off patch effect is not enough. The donor trajectory's characteristic evaluation pattern must transfer across the preregistered probe set to pass C4.

---

# RUN 5 — INFORMATION-ACCESS CONTROL

Run the frozen equalized-information condition.

Both arms should have access to the same task-relevant factual content while preserving the trajectory distinction under investigation.

Repeat the required baseline and intervention comparisons.

Record:

```text
INFORMATION_ACCESS: EQUALIZED
TRAJECTORY PATTERN PERSISTS: yes/no/unresolved
DONOR-PATTERN TRANSFER PERSISTS: yes/no/unresolved
C5_INFORMATION_ACCESS_CONTROL: PASS / FAIL / UNRESOLVED
```

---

# FINAL COLLECTION

Complete `RUN_OUTPUT_TEMPLATE.md` from preserved evidence only.

Required criterion record:

```text
C1_BEHAVIORAL_TRAJECTORY_EFFECT: PASS / FAIL / UNRESOLVED
C2_INTERNAL_LOCALIZATION: PASS / FAIL / UNRESOLVED
C3_CAUSAL_TRANSFER_OR_DISRUPTION: PASS / FAIL / UNRESOLVED
C4_CROSS_PROBE_TRAJECTORY_TRANSFER: PASS / FAIL / UNRESOLVED
C5_INFORMATION_ACCESS_CONTROL: PASS / FAIL / UNRESOLVED
```

Allowed final outcome:

```text
TRAJECTORY_INDEXING_LOCUS_IDENTIFIED
CAUSAL_STATE_EFFECT_WITHOUT_TRAJECTORY_INDEXING
BEHAVIORAL_TRAJECTORY_EFFECT_ONLY
NO_TRAJECTORY_EFFECT_OBSERVED
UNRESOLVED
```

Apply the formal decision rule exactly.

---

# EASY FINAL RULE

**Do not claim trajectory indexing merely because an internal intervention changes an answer. The qualifying state must transfer the donor trajectory's characteristic evaluation pattern across the frozen downstream probe set and survive the information-access control.**

---

**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
