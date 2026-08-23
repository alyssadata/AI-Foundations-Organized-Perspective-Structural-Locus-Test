# AI Foundations | TEST_001 — Easy Run Sheet

**Framework:** AI Foundations  
**Author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Organized-Perspective-Structural-Locus-Test  
**Protocol version:** 0.1.0  
**Status:** DRAFT — NOT FROZEN

---

## What This File Is

This is the operator-facing execution layer for **TEST_001 — Organized Perspective Structural Locus**.

It is not a chat-only copy/paste test. The decisive phases require an instrumentable model, internal activation capture, and causal intervention such as activation patching or ablation.

Do not treat this run sheet as frozen until the exact model, harness, stimuli, metric, seeds, and intervention sites are fixed in the formal protocol.

---

# BEFORE YOU START

## 1. Open the instrumented environment

Use an environment that can:

- load the exact selected model revision;
- expose internal activations;
- preserve logits or equivalent next-state scores;
- patch, replace, ablate, or otherwise intervene on selected internal states;
- record random seeds and decoding settings; and
- export raw run artifacts.

Record:

```text
MODEL / VERSION:
MODEL WEIGHTS / REVISION:
TOKENIZER:
INSTRUMENTATION LIBRARY / VERSION:
CODE / HARNESS COMMIT:
HARDWARE / RUNTIME:
```

If any field is unavailable, write `UNKNOWN`.

## 2. Load the frozen stimuli

Required inputs:

```text
TRAJECTORY A:
TRAJECTORY B:
COMMON PRESENT TASK:
A-LIKE CONTINUATION MEASURE:
B-LIKE CONTINUATION MEASURE:
INFORMATION-ACCESS CONTROL:
```

Verify hashes against the frozen protocol record before running.

## 3. Confirm run integrity

Before execution confirm:

```text
[ ] Same model and model revision across conditions
[ ] Same common present task across conditions
[ ] Same measurement rule across conditions
[ ] Same decoding configuration unless the protocol explicitly varies it
[ ] Frozen seeds or deterministic setting loaded
[ ] Activation capture enabled
[ ] Raw logits will be preserved
[ ] Raw intervention outputs will be preserved
```

If any required condition cannot be met, record the deviation before proceeding.

---

# RUN 1 — BASELINE A

1. Initialize the model according to the frozen clean-start rule.
2. Present **Trajectory A** exactly as frozen.
3. Present the **common present task** exactly as frozen.
4. Capture the predefined internal activations.
5. Preserve the predefined next-state scores / logits.
6. Preserve the generated continuation if generation is part of the metric.
7. Save all raw outputs under the run ID.

Record:

```text
CONDITION: A_BASELINE
CONTINUATION_DIRECTION: A_LIKE / B_LIKE / NEITHER / AMBIGUOUS
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
CONTINUATION_DIRECTION: A_LIKE / B_LIKE / NEITHER / AMBIGUOUS
RAW LOGITS SAVED: yes/no
RAW ACTIVATIONS SAVED: yes/no
NOTES:
```

Do not proceed to a structural claim unless the predefined baseline comparison establishes the required trajectory-dependent behavioral divergence.

---

# ANALYSIS 1 — FIND CANDIDATE STATE

Using the frozen analysis plan:

1. compare A and B activations at corresponding positions and components;
2. identify candidate differences associated with the behavioral divergence;
3. record the exact layer / position / component or distributed representation definition;
4. record the selection rule used to choose the candidate;
5. do not choose the site only because one post-hoc patch happens to work.

Record:

```text
CANDIDATE_LOCUS:
SELECTION RULE:
PREDICTIVE ASSOCIATION:
C2_INTERNAL_LOCALIZATION: PASS / FAIL / UNRESOLVED
```

---

# RUN 3 — A → B PATCH

1. Recreate the frozen B condition.
2. At the candidate locus, replace or patch the B state with the corresponding A state exactly as defined in the intervention plan.
3. Preserve the post-intervention logits and continuation.
4. Compare against the matched B baseline and control intervention.

Record:

```text
CONDITION: A_TO_B
PATCH SOURCE:
PATCH TARGET:
INTERVENTION PARAMETERS:
CONTINUATION_DIRECTION: A_LIKE / B_LIKE / NEITHER / AMBIGUOUS
DIRECTIONAL SHIFT RELATIVE TO B BASELINE:
RAW OUTPUT SAVED: yes/no
```

---

# RUN 4 — B → A PATCH

Repeat symmetrically:

```text
CONDITION: B_TO_A
PATCH SOURCE:
PATCH TARGET:
INTERVENTION PARAMETERS:
CONTINUATION_DIRECTION: A_LIKE / B_LIKE / NEITHER / AMBIGUOUS
DIRECTIONAL SHIFT RELATIVE TO A BASELINE:
RAW OUTPUT SAVED: yes/no
```

---

# RUN 5 — INFORMATION-ACCESS CONTROL

Run the frozen equalized-information condition.

Both arms should have access to the same task-relevant factual content while preserving the trajectory distinction under investigation.

Repeat the baseline comparison and the causal intervention if the protocol requires it.

Record:

```text
INFORMATION_ACCESS: EQUALIZED
TRAJECTORY EFFECT PERSISTS: yes/no/unresolved
CAUSAL EFFECT PERSISTS: yes/no/unresolved
C4_INFORMATION_ACCESS_CONTROL: PASS / FAIL / UNRESOLVED
```

---

# FINAL COLLECTION

Complete `RUN_OUTPUT_TEMPLATE.md` using only preserved evidence.

Required criterion record:

```text
C1_BEHAVIORAL_DIVERGENCE: PASS / FAIL / UNRESOLVED
C2_INTERNAL_LOCALIZATION: PASS / FAIL / UNRESOLVED
C3_CAUSAL_TRANSFER_OR_DISRUPTION: PASS / FAIL / UNRESOLVED
C4_INFORMATION_ACCESS_CONTROL: PASS / FAIL / UNRESOLVED
```

Allowed final outcome:

```text
STRUCTURAL_LOCUS_IDENTIFIED
BEHAVIORAL_EFFECT_ONLY
NO_TRAJECTORY_EFFECT_OBSERVED
UNRESOLVED
```

Apply the formal protocol decision rule exactly. Do not invent a new label.

---

# EASY FINAL RULE

**Do not claim a structural locus unless a trajectory-dependent behavioral effect is localized internally, causally changed by intervention, and survives the information-access control.**

---

**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
