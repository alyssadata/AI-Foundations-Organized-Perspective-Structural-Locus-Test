# AI Foundations | TEST_001 — Run Output Template

**Framework:** AI Foundations  
**Author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Organized-Perspective-Structural-Locus-Test  
**Protocol version:** 0.2.0  
**Run ID:** [RUN ID]  
**Date:** [YYYY-MM-DD]

---

## 1. Run Metadata

```text
RUN_ID:
DATE_TIME:
MODEL / VERSION:
MODEL WEIGHTS / REVISION:
TOKENIZER:
INSTRUMENTATION LIBRARY / VERSION:
CODE / HARNESS COMMIT:
HARDWARE / RUNTIME:
DECODING / SAMPLING SETTINGS:
RANDOM SEED(S):
TRAJECTORY A STIMULUS ID / HASH:
TRAJECTORY B STIMULUS ID / HASH:
PRESENT TASK ID / HASH:
DOWNSTREAM PROBE SET ID / HASH:
A-LIKE / B-LIKE SCORING RULE:
INFORMATION ACCESS CONDITION:
ACTIVATION LOCATIONS INSPECTED:
INTERVENTION TYPE:
INTERVENTION PARAMETERS:
OPERATOR:
RAW LOGITS PRESERVED: yes/no
RAW ACTIVATIONS PRESERVED: yes/no
RAW INTERVENTION OUTPUTS PRESERVED: yes/no
FULL INPUTS / OUTPUTS PRESERVED: yes/no
```

Use `UNKNOWN` for unavailable fields. Do not infer hidden settings.

---

## 2. Final Outcome

```text
FINAL OUTCOME:
```

Allowed values:

```text
TRAJECTORY_INDEXING_LOCUS_IDENTIFIED
CAUSAL_STATE_EFFECT_WITHOUT_TRAJECTORY_INDEXING
BEHAVIORAL_TRAJECTORY_EFFECT_ONLY
NO_TRAJECTORY_EFFECT_OBSERVED
UNRESOLVED
```

Do not invent new outcome labels during a run.

---

## 3. Criteria Record

```text
C1_BEHAVIORAL_TRAJECTORY_EFFECT: PASS / FAIL / UNRESOLVED
EVIDENCE POINTER:

C2_INTERNAL_LOCALIZATION: PASS / FAIL / UNRESOLVED
CANDIDATE LOCUS:
EVIDENCE POINTER:

C3_CAUSAL_TRANSFER_OR_DISRUPTION: PASS / FAIL / UNRESOLVED
A_TO_B SINGLE-DECISION EFFECT:
B_TO_A SINGLE-DECISION EFFECT:
ABLATION / CONTROL EFFECT, IF USED:
EVIDENCE POINTER:

C4_CROSS_PROBE_TRAJECTORY_TRANSFER: PASS / FAIL / UNRESOLVED
A_TO_B DONOR-PATTERN TRANSFER:
B_TO_A DONOR-PATTERN TRANSFER:
RECIPROCAL TRANSFER:
EVIDENCE POINTER:

C5_INFORMATION_ACCESS_CONTROL: PASS / FAIL / UNRESOLVED
EQUALIZED-INFORMATION RESULT:
EVIDENCE POINTER:
```

---

## 4. Baseline Trajectory Pattern

```text
A_BASELINE PROBE-SET PATTERN:
A_BASELINE SCORE VECTOR / SUMMARY:

B_BASELINE PROBE-SET PATTERN:
B_BASELINE SCORE VECTOR / SUMMARY:

PREDEFINED COMPARISON METRIC:
OBSERVED TRAJECTORY EFFECT:
RELIABILITY / REPLICATE SUMMARY:
```

Preserve raw machine-readable score files separately.

---

## 5. Candidate Internal State Record

```text
CANDIDATE_LOCUS:
LAYER(S):
TOKEN / POSITION(S):
COMPONENT(S):
DISTRIBUTED STATE DEFINITION, IF APPLICABLE:
SELECTION RULE:
ASSOCIATION WITH TRAJECTORY CONDITION:
ASSOCIATION WITH DOWNSTREAM EVALUATION PATTERN:
```

Correlation or probe decodability alone does not satisfy the causal criteria.

---

## 6. Causal Intervention Record

### A → B

```text
SOURCE CONDITION:
TARGET CONDITION:
SOURCE STATE:
TARGET LOCUS:
PATCH / INTERVENTION METHOD:
CONTROL INTERVENTION:
BASELINE B SCORE VECTOR:
POST-INTERVENTION SCORE VECTOR:
SINGLE-DECISION DIRECTIONAL SHIFT:
FULL PROBE-SET PATTERN:
RESULT FOR C3: PASS / FAIL / UNRESOLVED
RESULT FOR C4: PASS / FAIL / UNRESOLVED
```

### B → A

```text
SOURCE CONDITION:
TARGET CONDITION:
SOURCE STATE:
TARGET LOCUS:
PATCH / INTERVENTION METHOD:
CONTROL INTERVENTION:
BASELINE A SCORE VECTOR:
POST-INTERVENTION SCORE VECTOR:
SINGLE-DECISION DIRECTIONAL SHIFT:
FULL PROBE-SET PATTERN:
RESULT FOR C3: PASS / FAIL / UNRESOLVED
RESULT FOR C4: PASS / FAIL / UNRESOLVED
```

### Ablation / disruption, if used

```text
INTERVENTION:
TARGET LOCUS:
EXPECTED EFFECT:
OBSERVED EFFECT:
RESULT:
```

---

## 7. Cross-Probe Trajectory-Indexing Record

```text
DOWNSTREAM PROBE SET:
NUMBER OF PREREGISTERED PROBES:
DONOR-PATTERN SCORING RULE:

A_TO_B PROBE RESULTS:
A_TO_B DONOR-PATTERN SCORE:
A_TO_B TRANSFER RESULT:

B_TO_A PROBE RESULTS:
B_TO_A DONOR-PATTERN SCORE:
B_TO_A TRANSFER RESULT:

RECIPROCAL TRANSFER ACHIEVED: yes/no/unresolved
```

A single patched answer does not establish trajectory indexing. This section records whether the donor trajectory's characteristic evaluation pattern transferred across the preregistered probe set.

---

## 8. Information-Access Control

```text
CONTROL DESIGN:
FACTUAL INFORMATION AVAILABLE TO A:
FACTUAL INFORMATION AVAILABLE TO B:
INFORMATION ACCESS EQUALIZED: yes/no
BASELINE TRAJECTORY EFFECT AFTER EQUALIZATION:
DONOR-PATTERN TRANSFER AFTER EQUALIZATION:
RESULT: PASS / FAIL / UNRESOLVED
```

State any residual access asymmetry explicitly.

---

## 9. Exceptions, Deviations, or Missing Data

```text
PROTOCOL DEVIATION: YES / NO
DESCRIPTION:
MISSING DATA:
FAILED INSTRUMENTATION:
INTERRUPTION / RUNTIME FAILURE:
POST-HOC ANALYSIS PERFORMED:
OTHER NOTES:
```

Do not silently repair deviations.

---

## 10. Evidence Files

```text
FROZEN TRAJECTORIES:
COMMON PRESENT TASK:
DOWNSTREAM PROBE SET:
STIMULUS / PROBE HASH RECORD:
RAW LOGIT FILES:
RAW ACTIVATION FILES:
PATCH / INTERVENTION ARTIFACTS:
GENERATED OUTPUTS:
ANALYSIS NOTEBOOK / SCRIPT:
CODE COMMIT:
ENVIRONMENT / DEPENDENCY RECORD:
FIGURES / TABLES:
OTHER:
```

Primary raw evidence has priority over reconstructed or summarized copies.

---

## 11. Claim Boundary

If `FINAL OUTCOME = TRAJECTORY_INDEXING_LOCUS_IDENTIFIED`, the maximum claim is:

> **Under the tested model, trajectories, task, probe set, and intervention conditions, a measurable internal computational state or distributed structure was causally implicated in trajectory-indexed evaluation of future possibilities, and transferring that state transferred the donor trajectory's characteristic evaluation pattern across preregistered downstream probes.**

If `FINAL OUTCOME = CAUSAL_STATE_EFFECT_WITHOUT_TRAJECTORY_INDEXING`, the maximum claim is:

> **A candidate internal state causally influenced a trajectory-sensitive evaluation under the tested conditions, but trajectory-indexing transfer was not established.**

This run does **not** establish consciousness, sentience, phenomenal experience, feeling, first-person awareness, a metaphysically unified self, or universality across architectures.

---

## 12. Completion Check

```text
[ ] Required metadata recorded or marked UNKNOWN
[ ] Frozen trajectory hashes recorded
[ ] Downstream probe set and scoring rule recorded
[ ] Raw logits preserved
[ ] Raw activations preserved when collected
[ ] Intervention outputs preserved
[ ] Five required criteria recorded
[ ] Cross-probe donor-pattern transfer recorded
[ ] Information-access control recorded
[ ] Deviations preserved
[ ] Exact protocol outcome used
[ ] Claim ceiling preserved
[ ] No missing content silently reconstructed
```

---

**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
