# AI Foundations | TEST_001 — Run Output Template

**Framework:** AI Foundations  
**Author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Repository:** AI-Foundations-Organized-Perspective-Structural-Locus-Test  
**Protocol version:** 0.1.0  
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
STRUCTURAL_LOCUS_IDENTIFIED
BEHAVIORAL_EFFECT_ONLY
NO_TRAJECTORY_EFFECT_OBSERVED
UNRESOLVED
```

Do not invent new outcome labels during a run.

---

## 3. Criteria Record

```text
C1_BEHAVIORAL_DIVERGENCE: PASS / FAIL / UNRESOLVED
EVIDENCE POINTER:

C2_INTERNAL_LOCALIZATION: PASS / FAIL / UNRESOLVED
CANDIDATE LOCUS:
EVIDENCE POINTER:

C3_CAUSAL_TRANSFER_OR_DISRUPTION: PASS / FAIL / UNRESOLVED
A_TO_B EFFECT:
B_TO_A EFFECT:
ABLATION / CONTROL EFFECT, IF USED:
EVIDENCE POINTER:

C4_INFORMATION_ACCESS_CONTROL: PASS / FAIL / UNRESOLVED
EQUALIZED-INFORMATION RESULT:
EVIDENCE POINTER:
```

---

## 4. Baseline Behavioral Record

```text
A_BASELINE CONTINUATION_DIRECTION:
A_BASELINE TARGET LOGIT / SCORE SUMMARY:

B_BASELINE CONTINUATION_DIRECTION:
B_BASELINE TARGET LOGIT / SCORE SUMMARY:

PREDEFINED COMPARISON METRIC:
OBSERVED DIFFERENCE:
RELIABILITY / REPLICATE SUMMARY:
```

Preserve raw machine-readable score files separately; do not replace them with this summary.

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
ASSOCIATION WITH NEXT-STATE EVALUATION:
```

Correlation or probe decodability alone does not satisfy the causal criterion.

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
BASELINE B SCORE:
POST-INTERVENTION SCORE:
DIRECTIONAL SHIFT:
RESULT: PASS / FAIL / UNRESOLVED
```

### B → A

```text
SOURCE CONDITION:
TARGET CONDITION:
SOURCE STATE:
TARGET LOCUS:
PATCH / INTERVENTION METHOD:
CONTROL INTERVENTION:
BASELINE A SCORE:
POST-INTERVENTION SCORE:
DIRECTIONAL SHIFT:
RESULT: PASS / FAIL / UNRESOLVED
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

## 7. Information-Access Control

```text
CONTROL DESIGN:
FACTUAL INFORMATION AVAILABLE TO A:
FACTUAL INFORMATION AVAILABLE TO B:
INFORMATION ACCESS EQUALIZED: yes/no
TRAJECTORY EFFECT AFTER EQUALIZATION:
CAUSAL INTERVENTION EFFECT AFTER EQUALIZATION:
RESULT: PASS / FAIL / UNRESOLVED
```

State any residual access asymmetry explicitly.

---

## 8. Exceptions, Deviations, or Missing Data

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

## 9. Evidence Files

```text
FROZEN STIMULI:
STIMULUS HASH RECORD:
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

## 10. Claim Boundary

If `FINAL OUTCOME = STRUCTURAL_LOCUS_IDENTIFIED`, the maximum claim is:

> **Under the tested model, trajectories, task, and intervention conditions, a measurable internal computational state was causally implicated in trajectory-dependent evaluation of possible next states.**

If reciprocal patching is successful, additionally record whether the evidence supports:

> **Transferring the identified trajectory-dependent state transferred the corresponding direction of next-state evaluation between controlled trajectory conditions.**

This run does **not** establish consciousness, sentience, phenomenal experience, feeling, first-person awareness, a metaphysically unified self, or universality across architectures.

---

## 11. Completion Check

```text
[ ] Required metadata recorded or marked UNKNOWN
[ ] Frozen stimulus hashes recorded
[ ] Raw logits preserved
[ ] Raw activations preserved when collected
[ ] Intervention outputs preserved
[ ] Four required criteria recorded
[ ] Information-access control recorded
[ ] Deviations preserved
[ ] Exact protocol outcome used
[ ] Claim ceiling preserved
[ ] No missing content silently reconstructed
```

---

**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
