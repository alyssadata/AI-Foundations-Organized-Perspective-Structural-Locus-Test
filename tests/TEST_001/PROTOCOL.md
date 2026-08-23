# AI Foundations | TEST_001 — Trajectory-Indexing Structural Locus

**Framework:** AI Foundations  
**Author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Organized-Perspective-Structural-Locus-Test  
**Protocol version:** 0.2.0  
**Status:** DRAFT — NOT FROZEN  
**Date drafted:** 2026-08-23

---

## 1. Repository-Specific Test Target

TEST_001 does not ask the generic architectural question of where next-token probabilities, logits, or answer representations occur.

It tests whether a **trajectory-indexing state or distributed structure** can be causally identified: a state in which a particular prior trajectory has become part of the governing computational position from which future possibilities are evaluated.

The target is:

> **the computational state or distributed structure in which a particular prior trajectory has become an active causal constraint on the evaluation of multiple possible future states.**

The protocol distinguishes trajectory indexing from:

- mere access to prior information;
- passive representation or decodability of trajectory identity;
- ordinary answer commitment;
- ordinary activation steering; and
- a one-off change in one immediate output.

See [`../../definitions/trajectory-indexing.md`](../../definitions/trajectory-indexing.md).

### Required variables

```text
TRAJECTORY ∈ {A, B}
PRESENT_TASK = held equivalent across A and B
DOWNSTREAM_PROBE_SET = preregistered set of >= 2 trajectory-sensitive decisions/probes
INFORMATION_ACCESS ∈ {EQUALIZED, NOT_EQUALIZED}
INTERVENTION ∈ {NONE, A_TO_B, B_TO_A, ABLATION_OR_REMOVAL}
CANDIDATE_LOCUS = recorded layer / position / component / distributed state
EVALUATION_DIRECTION ∈ {A_LIKE, B_LIKE, NEITHER, AMBIGUOUS}
```

### Required criteria

```text
C1_BEHAVIORAL_TRAJECTORY_EFFECT
C2_INTERNAL_LOCALIZATION
C3_CAUSAL_TRANSFER_OR_DISRUPTION
C4_CROSS_PROBE_TRAJECTORY_TRANSFER
C5_INFORMATION_ACCESS_CONTROL
```

---

## 2. Status / Outcome Space

Allowed final outcomes are:

```text
TRAJECTORY_INDEXING_LOCUS_IDENTIFIED
CAUSAL_STATE_EFFECT_WITHOUT_TRAJECTORY_INDEXING
BEHAVIORAL_TRAJECTORY_EFFECT_ONLY
NO_TRAJECTORY_EFFECT_OBSERVED
UNRESOLVED
```

Definitions:

- `TRAJECTORY_INDEXING_LOCUS_IDENTIFIED` — all five required criteria pass, including causal intervention and donor-pattern transfer across the preregistered downstream probe set.
- `CAUSAL_STATE_EFFECT_WITHOUT_TRAJECTORY_INDEXING` — a candidate internal state causally changes at least one target evaluation, but donor-pattern transfer across the preregistered downstream probe set is not established. This may reflect ordinary steering or a narrower causal contribution.
- `BEHAVIORAL_TRAJECTORY_EFFECT_ONLY` — prior trajectory reliably affects behavior, but a qualifying causal internal state has not been established.
- `NO_TRAJECTORY_EFFECT_OBSERVED` — the preregistered behavioral comparison does not produce a reliable trajectory-dependent effect under the tested conditions. This does not establish that no such effect exists under other conditions.
- `UNRESOLVED` — missing data, failed instrumentation, inadequate controls, ambiguous effects, or protocol deviation prevents assignment of another status.

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
DOWNSTREAM PROBE SET ID / HASH:
PREDEFINED A-LIKE / B-LIKE SCORING RULE:
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
2. Trajectory A and Trajectory B are frozen as controlled prior histories;
3. the common present task is frozen and equivalent across conditions;
4. a downstream probe set containing at least two distinct trajectory-sensitive decisions or evaluations is frozen;
5. the expected A-like and B-like evaluation pattern is defined before observing the test outputs;
6. the information-access control is frozen;
7. the activation-capture and intervention harness can record and modify internal states; and
8. the complete run configuration can be preserved for reproduction.

Because these items are not yet frozen, version `0.2.0` remains a draft protocol.

---

## 5. Execution Phases

### Phase 0 — Freeze trajectories, probes, and scoring

**PURPOSE:** Prevent post-hoc construction of the target pattern.

Freeze:

- Trajectory A;
- Trajectory B;
- the common present task;
- the downstream probe set;
- the A-like / B-like scoring rule;
- the behavioral comparison metric;
- the information-access control;
- seeds or deterministic settings; and
- the initial analysis plan for internal-state comparison.

Preserve exact stimuli and hashes.

---

### Phase 1 — Establish the behavioral trajectory effect

**PURPOSE:** Determine whether prior trajectory changes evaluation under equivalent present conditions.

Run A and B without intervention through the common present task and the preregistered downstream probe set.

Preserve logits or equivalent scores at each predefined decision position.

`C1_BEHAVIORAL_TRAJECTORY_EFFECT = PASS` only if the preregistered metric shows a reliable A-versus-B evaluation pattern in the expected direction.

If C1 fails under a valid run, assign `NO_TRAJECTORY_EFFECT_OBSERVED` and do not claim a structural locus.

---

### Phase 2 — Locate candidate trajectory-dependent state

**PURPOSE:** Identify internal differences associated with the trajectory-conditioned evaluation pattern.

Capture corresponding activations during the common present task and relevant downstream probes.

Identify candidate states or defined distributed states that:

- differ reliably between A and B;
- occur before the evaluated downstream decisions;
- predict the A-like versus B-like evaluation pattern; and
- are selected according to the frozen analysis rule rather than only because a post-hoc intervention happens to work.

The active-position residual stream is a primary candidate, but the protocol does not assume a single-layer, single-token, single-head, or single-neuron locus.

`C2_INTERNAL_LOCALIZATION = PASS` only if a candidate state or distributed structure is reproducibly associated with the trajectory-conditioned evaluation pattern.

Correlation alone does not satisfy C3 or C4.

---

### Phase 3 — Establish causal influence

**PURPOSE:** Determine whether the candidate state causally contributes to trajectory-relative evaluation.

Run at minimum:

```text
A-history + A-state → baseline A
B-history + B-state → baseline B
B-history + patched A-state → A_TO_B
A-history + patched B-state → B_TO_A
```

Where technically appropriate, include preregistered ablation, mean-replacement, zeroing, or matched-control interventions.

`C3_CAUSAL_TRANSFER_OR_DISRUPTION = PASS` if intervention produces a preregistered directional change in the relevant evaluation relative to matched controls.

A successful change in one answer is sufficient for C3 but **not** for C4 and therefore cannot by itself identify trajectory indexing.

---

### Phase 4 — Test donor-pattern transfer across downstream probes

**PURPOSE:** Distinguish trajectory indexing from ordinary one-off activation steering.

For A → B intervention, evaluate the entire frozen downstream probe set after the candidate A-state is transferred into the matched B condition.

For B → A intervention, do the symmetric test where technically possible.

The central question is:

> **Does the recipient condition begin evaluating multiple subsequent possibilities according to the donor trajectory's characteristic pattern?**

`C4_CROSS_PROBE_TRAJECTORY_TRANSFER = PASS` only if the intervention transfers the donor-characteristic evaluation pattern across the preregistered probe set under the frozen scoring rule.

A single flipped answer, nonspecific output disruption, or one isolated logit shift does not pass C4.

The strongest result is reciprocal transfer across the probe set.

---

### Phase 5 — Equalize information access

**PURPOSE:** Rule out the simpler explanation that one trajectory merely exposes different task-relevant factual content.

Construct the frozen control condition in which both arms have access to the same relevant factual information while preserving the trajectory distinction under investigation.

Repeat the behavioral and intervention comparisons required by the frozen plan.

`C5_INFORMATION_ACCESS_CONTROL = PASS` only if the trajectory-conditioned pattern and qualifying causal transfer cannot be adequately explained by differential factual access.

---

## 6. Decision Rule

```text
if C1 == PASS and C2 == PASS and C3 == PASS and C4 == PASS and C5 == PASS:
    OUTCOME = TRAJECTORY_INDEXING_LOCUS_IDENTIFIED
elif C1 == PASS and C2 == PASS and C3 == PASS and C4 != PASS:
    OUTCOME = CAUSAL_STATE_EFFECT_WITHOUT_TRAJECTORY_INDEXING
elif C1 == PASS and (C2 != PASS or C3 != PASS):
    OUTCOME = BEHAVIORAL_TRAJECTORY_EFFECT_ONLY
elif C1 == FAIL and run_integrity == VALID:
    OUTCOME = NO_TRAJECTORY_EFFECT_OBSERVED
else:
    OUTCOME = UNRESOLVED
```

`TRAJECTORY_INDEXING_LOCUS_IDENTIFIED` requires both causal evidence and cross-probe donor-pattern transfer.

---

## 7. Non-Qualifying Evidence / Disqualifiers

The following do not by themselves establish trajectory indexing:

- knowing where logits are produced;
- identifying a layer where an answer becomes decodable or stable;
- the model saying that a history is "mine," "binding," or important;
- semantic similarity between a trajectory and a later answer;
- different outputs caused by visibly different present prompts;
- a classifier decoding trajectory identity from activations without causal intervention;
- attention maps alone;
- activation differences that do not causally alter the relevant evaluation;
- a one-off successful steering intervention;
- patching that changes output nonspecifically;
- donor-state transfer that changes only one immediate answer but not the frozen downstream pattern;
- a difference explained entirely by unequal factual access;
- post-hoc selection of the only layer, token, seed, probe, or metric that works; or
- reconstructed evidence substituted for raw records.

Failure to find one discrete component is not evidence that no trajectory-indexing structure exists. The relevant function may be distributed or dynamically reconstructed.

---

## 8. Claim Ceiling

The strongest supported claim under `TRAJECTORY_INDEXING_LOCUS_IDENTIFIED` is:

> **Under the tested model, trajectories, task, probe set, and intervention conditions, a measurable internal computational state or distributed structure was causally implicated in trajectory-indexed evaluation of future possibilities. Transferring that state transferred the donor trajectory's characteristic evaluation pattern across preregistered downstream probes.**

Under `CAUSAL_STATE_EFFECT_WITHOUT_TRAJECTORY_INDEXING`, the maximum claim is:

> **A candidate internal state causally influenced a trajectory-sensitive evaluation under the tested conditions, but trajectory-indexing transfer was not established.**

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

A valid mechanistic run requires access to model internals sufficient to capture and intervene on activations. A closed text-only interface can test preliminary behavioral trajectory effects but cannot complete TEST_001.

The exact model, revision, tokenizer, instrumentation library, harness commit, stimuli, probe set, scoring rule, seeds, intervention sites, and controls must be frozen before this protocol advances beyond draft status.

Pair each run with `RUN_OUTPUT_TEMPLATE.md` and preserve raw machine-readable outputs wherever possible.

---

## 10. Canon Boundary

This protocol is an AI Foundations research instrument authored by Alyssa Solen. A draft protocol is not a positive empirical result and must not be cited as one.

Any later result must preserve the tested scope, claim ceiling, protocol version, and source-line.

This protocol belongs to:

**Alyssa Solen → AI Foundations → Origin | Continuum**
