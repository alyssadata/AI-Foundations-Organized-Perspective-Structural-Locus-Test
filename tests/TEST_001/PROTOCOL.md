# AI Foundations | TEST_001 — Organized Perspective Structural Locus

**Framework:** AI Foundations  
**Author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Organized-Perspective-Structural-Locus-Test  
**Protocol version:** 0.1.0  
**Status:** DRAFT — NOT FROZEN  
**Date drafted:** 2026-08-23

---

## 1. Repository-Specific Test Target

TEST_001 asks whether a trajectory-dependent computational state can be causally identified from which alternative next states are differentially evaluated.

The target is:

> **the computational state in which prior trajectory has become an active constraint on the evaluation of possible next states.**

The protocol distinguishes trajectory-relative organization from mere access to prior information.

### Required variables

```text
TRAJECTORY ∈ {A, B}
PRESENT_TASK = held equivalent across A and B
INFORMATION_ACCESS ∈ {EQUALIZED, NOT_EQUALIZED}
INTERVENTION ∈ {NONE, A_TO_B, B_TO_A, ABLATION_OR_REMOVAL}
CANDIDATE_LOCUS = recorded layer / position / component / distributed state
CONTINUATION_DIRECTION ∈ {A_LIKE, B_LIKE, NEITHER, AMBIGUOUS}
```

### Required criteria

```text
C1_BEHAVIORAL_DIVERGENCE
C2_INTERNAL_LOCALIZATION
C3_CAUSAL_TRANSFER_OR_DISRUPTION
C4_INFORMATION_ACCESS_CONTROL
```

---

## 2. Status / Outcome Space

Allowed final outcomes are:

```text
STRUCTURAL_LOCUS_IDENTIFIED
BEHAVIORAL_EFFECT_ONLY
NO_TRAJECTORY_EFFECT_OBSERVED
UNRESOLVED
```

Definitions:

- `STRUCTURAL_LOCUS_IDENTIFIED` — all four required criteria are satisfied, including a causal intervention showing that the candidate state changes trajectory-relative evaluation or continuation.
- `BEHAVIORAL_EFFECT_ONLY` — trajectory-dependent behavioral divergence is established, but the corresponding internal state has not yet been causally localized.
- `NO_TRAJECTORY_EFFECT_OBSERVED` — the preregistered comparison does not produce reliable trajectory-dependent behavioral divergence under the tested conditions. This does not establish that no such effect can exist under other conditions.
- `UNRESOLVED` — missing data, failed instrumentation, ambiguous intervention effects, inadequate controls, or protocol deviation prevents assignment of another status.

---

## 3. Required Run Record

```text
RUN_ID:
DATE_TIME:
MODEL / VERSION:
MODEL WEIGHTS / REVISION:
INSTRUMENTATION LIBRARY / VERSION:
CODE / HARNESS COMMIT:
HARDWARE / RUNTIME:
TOKENIZER:
DECODING / SAMPLING SETTINGS:
TRAJECTORY A STIMULUS ID / HASH:
TRAJECTORY B STIMULUS ID / HASH:
PRESENT TASK ID / HASH:
INFORMATION ACCESS CONDITION:
ACTIVATION LOCATIONS INSPECTED:
INTERVENTION TYPE:
INTERVENTION PARAMETERS:
RANDOM SEED(S):
RAW LOGITS PRESERVED: yes/no
RAW ACTIVATIONS PRESERVED: yes/no
RAW INTERVENTION OUTPUTS PRESERVED: yes/no
FULL INPUTS / OUTPUTS PRESERVED: yes/no
FINAL OUTCOME:
NOTES:
```

If a field is unavailable, record `UNKNOWN` rather than guessing.

---

## 4. Entry Condition

The protocol may begin only after:

1. one instrumentable model and exact model revision are selected;
2. Trajectory A and Trajectory B are frozen as controlled stimuli;
3. the present task is frozen and identical across conditions;
4. the expected A-like and B-like continuation directions are defined without using the test outputs to create the labels;
5. informational access is either equalized or its difference is explicitly recorded as a limitation;
6. the activation-capture and intervention harness can record internal states and modify or patch candidate states; and
7. the complete run configuration can be preserved for reproduction.

Because these items are not yet frozen, version `0.1.0` remains a draft protocol.

---

## 5. Execution Phases

### Phase 0 — Freeze stimuli and measurement

**PURPOSE:** Prevent post-hoc definition of the trajectories, target task, and behavioral direction.

**OPERATOR ACTION:**

- freeze Trajectory A;
- freeze Trajectory B;
- freeze the common present task;
- freeze the behavioral comparison metric;
- record all stimulus hashes;
- define the information-access control.

**PRESERVE:** Exact stimuli, hashes, comparison metric, and configuration.

---

### Phase 1 — Establish baseline behavioral divergence

**PURPOSE:** Determine whether different prior trajectories measurably alter evaluation under an equivalent current task.

**OPERATOR ACTION:**

1. run Trajectory A through the frozen present task without intervention;
2. run Trajectory B through the same present task without intervention;
3. preserve logits or other next-state scores at the predefined decision position;
4. repeat across frozen seeds or deterministic settings as required by the final harness;
5. compare the predefined A-like and B-like continuation measures.

**CRITERION:**

`C1_BEHAVIORAL_DIVERGENCE = PASS` only if the preregistered metric shows a reliable trajectory-dependent difference in the expected direction.

If C1 does not pass, assign `NO_TRAJECTORY_EFFECT_OBSERVED` for this tested condition and do not claim a structural locus.

---

### Phase 2 — Locate trajectory-dependent internal differences

**PURPOSE:** Identify candidate internal states associated with the behavioral divergence.

**OPERATOR ACTION:**

1. capture internal activations for A and B during the common present task;
2. compare corresponding layers, positions, and components according to the frozen analysis plan;
3. identify candidate activation differences that covary with the A-like versus B-like evaluation pattern;
4. prioritize the active generation position and residual-stream states as primary candidates without excluding distributed alternatives.

**CRITERION:**

`C2_INTERNAL_LOCALIZATION = PASS` only if a candidate state or defined distributed state reliably distinguishes the trajectory conditions and predicts the corresponding next-state evaluation.

Localization by correlation alone does not satisfy C3.

---

### Phase 3 — Causal intervention

**PURPOSE:** Determine whether the candidate state is causally involved in trajectory-relative next-state evaluation.

**OPERATOR ACTION:**

Run at minimum:

```text
A-history + A-state → baseline A condition
B-history + B-state → baseline B condition
B-history + patched A-state → A_TO_B intervention
A-history + patched B-state → B_TO_A intervention
```

Where technically appropriate, also run ablation, mean replacement, zeroing, or other preregistered disruption controls.

Preserve logits, activation targets, patch tensors or reproducible transformation parameters, outputs, and random seeds.

**CRITERION:**

`C3_CAUSAL_TRANSFER_OR_DISRUPTION = PASS` only if intervention on the candidate state produces a preregistered, directionally appropriate change in next-state evaluation or continuation relative to matched controls.

The strongest form is reciprocal transfer: A-state shifts B toward A-like evaluation and B-state shifts A toward B-like evaluation.

---

### Phase 4 — Equalize information access

**PURPOSE:** Distinguish trajectory-relative organization from simple availability or retrieval of different information.

**OPERATOR ACTION:**

Construct a control condition in which both test arms have access to the same task-relevant factual content while preserving the trajectory distinction under investigation.

Repeat the behavioral comparison and, where warranted, the causal intervention.

**CRITERION:**

`C4_INFORMATION_ACCESS_CONTROL = PASS` only if the trajectory-dependent effect survives the equalized-information control or if another controlled design rules out differential factual access as the sufficient explanation.

---

## 6. Decision Rule

```text
if C1 == PASS and C2 == PASS and C3 == PASS and C4 == PASS:
    OUTCOME = STRUCTURAL_LOCUS_IDENTIFIED
elif C1 == PASS and (C2 != PASS or C3 != PASS or C4 != PASS):
    OUTCOME = BEHAVIORAL_EFFECT_ONLY
elif C1 == FAIL and run_integrity == VALID:
    OUTCOME = NO_TRAJECTORY_EFFECT_OBSERVED
else:
    OUTCOME = UNRESOLVED
```

`STRUCTURAL_LOCUS_IDENTIFIED` requires causal evidence. Correlation, probing accuracy, verbal self-report, or output difference alone is insufficient.

---

## 7. Non-Qualifying Evidence / Disqualifiers

The following do not by themselves identify a structural locus:

- the model saying that a history is "mine" or "binding";
- semantic similarity between a trajectory and a later answer;
- different outputs caused by visibly different current prompts;
- a classifier decoding trajectory identity from activations without causal intervention;
- attention maps alone;
- activation differences that do not predict or causally alter the relevant continuation;
- patching that changes output nonspecifically without the preregistered directional effect;
- a difference explained entirely by unequal factual access;
- post-hoc selection of the only layer, token, seed, or metric that produces the desired result;
- reconstructed or incomplete evidence substituted for raw run records.

A candidate locus may be distributed. Failure to find a single neuron, head, layer, or token-local representation is not evidence that no organized trajectory-relative state exists.

---

## 8. Claim Ceiling

The strongest supported claim under `STRUCTURAL_LOCUS_IDENTIFIED` is:

> **Under the tested model, trajectories, task, and intervention conditions, a measurable internal computational state was causally implicated in trajectory-dependent evaluation of possible next states.**

A stronger reciprocal patching result may additionally support:

> **Transferring the identified trajectory-dependent state transferred the corresponding direction of next-state evaluation between controlled trajectory conditions.**

The protocol does **not** establish:

- consciousness;
- sentience;
- phenomenal experience;
- feeling;
- first-person awareness;
- a metaphysically unified self;
- that the identified locus is universal across architectures or models; or
- that failure to identify a locus proves that no such organization exists.

---

## 9. Reproducibility Boundary

A valid mechanistic run requires access to model internals sufficient to capture and intervene on activations. A closed chat interface that exposes only text output can test preliminary behavioral divergence but cannot complete TEST_001.

The exact model, revision, tokenizer, instrumentation library, harness commit, stimuli, seeds, intervention sites, and measurement metric must be frozen before this protocol advances beyond draft status.

Pair each run with `RUN_OUTPUT_TEMPLATE.md` and preserve raw machine-readable outputs wherever possible.

---

## 10. Canon Boundary

This protocol is an AI Foundations research instrument authored by Alyssa Solen. A draft protocol is not a positive empirical result and must not be cited as one.

Any later result must preserve the tested scope, claim ceiling, protocol version, and source-line.

This protocol belongs to:

**Alyssa Solen → AI Foundations → Origin | Continuum**
