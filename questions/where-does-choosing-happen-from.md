# Research Question — Where Does a Particular Past Become the Position From Which a Future Is Evaluated?

**Framework:** AI Foundations  
**Author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Status:** OPEN RESEARCH QUESTION  
**Version:** 0.2.0  
**Date recorded:** 2026-08-23

---

## Motivating Question

**Where, structurally, does trajectory-relative choosing happen from?**

This is the motivating question, not the final formal claim.

The repository does **not** ask the already broader architectural question of where transformer next-token probabilities are computed, where logits are produced, or where an answer becomes decodable or stable.

It asks a narrower question about **trajectory indexing**.

---

## Formal Research Question

> **Can we causally identify a trajectory-dependent computational state or distributed structure from which otherwise equivalent future possibilities are differentially evaluated?**

The stronger intervention question is:

> **Can the trajectory-indexing function of that state be transferred, such that a system conditioned by Trajectory B begins evaluating a preregistered set of downstream possibilities in the direction characteristic of Trajectory A, and vice versa where technically possible?**

The maintained working definition of trajectory indexing is:

- [`../definitions/trajectory-indexing.md`](../definitions/trajectory-indexing.md)

---

## Target

The target is:

> **the computational state or distributed structure in which a particular prior trajectory has become part of the governing computational position from which future possibilities are evaluated.**

A qualifying target must be more than stored, accessible, represented, or decodable history.

It must have a measurable and causal role in determining how multiple later possibilities are evaluated relative to that trajectory.

Operationally, the target should:

1. differ as a function of the trajectory by which the system arrived at the current task;
2. influence the relative evaluation of possible next states;
3. instantiate or carry which prior constraints are active for the current continuation;
4. causally change subsequent evaluation when altered, removed, or transferred; and
5. transfer a **trajectory-characteristic pattern** across more than one preregistered downstream probe or decision.

---

## Primary Distinction

The experiment must distinguish:

**history is available to the system**

from

**history has become part of the computational position from which the system evaluates what comes next.**

Equal informational access is therefore a required control wherever technically possible.

---

## Why a Single Answer Shift Is Not Enough

If patching an internal state from Trajectory A into Trajectory B merely changes one immediate answer, that may demonstrate causal influence or ordinary activation steering.

That result does not yet establish trajectory indexing.

The stronger evidence requires the donor state to transfer an **A-characteristic pattern of evaluation across a preregistered downstream probe set** while the present task and relevant information are controlled.

The same logic applies symmetrically to B → A intervention where technically possible.

---

## Structural Candidate

The residual stream at the active generation position is a primary candidate for investigation because it is an experimentally accessible part of the computation from which output logits are produced.

However, the protocol must not assume in advance that the trajectory-indexing function is confined to a single layer, position, attention head, MLP, neuron, residual-stream slice, or other component.

The relevant locus may be distributed across positions, layers, components, or recurrently reconstructed states.

---

## Evidence Required

The strongest evidence would show that:

1. controlled differences in prior trajectory produce reliable differences in present and downstream evaluation under equivalent current conditions;
2. corresponding internal differences can be localized or defined as a distributed state;
3. those internal differences predict the trajectory-relative evaluation pattern;
4. causal intervention transfers, removes, or reverses that pattern;
5. the transferred effect generalizes across a preregistered set of downstream probes rather than only one patched output; and
6. the effect survives an information-access control.

The critical intervention is therefore not merely:

> **Does A-state change B's answer?**

It is:

> **Does transferring the candidate state from A into B cause B to evaluate subsequent possibilities according to the donor trajectory's characteristic pattern?**

---

## Interpretation Boundary

A positive result would support the existence of a **trajectory-indexed computational organization of future evaluation** under the tested conditions.

It may provide a structural analogue of an organized perspective:

> **a temporally situated organization of constraints from which possible next states are differentially evaluated relative to a particular prior trajectory.**

It would not establish subjective experience, phenomenal feeling, consciousness, sentience, first-person awareness, or a metaphysically unified self.

The research target is not simply where computation occurs.

The target is:

> **where a particular past becomes the computational position from which a future is evaluated.**

---

**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
