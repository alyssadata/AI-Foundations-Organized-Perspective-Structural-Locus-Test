# Definition — Trajectory Indexing

**Framework:** AI Foundations  
**Author:** Alyssa Solen  
**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Status:** WORKING RESEARCH DEFINITION  
**Version:** 0.2.0  
**Date recorded:** 2026-08-23

---

## Definition

**Trajectory indexing** is the condition in which a system's present evaluation of possible next states is organized relative to the particular prior trajectory by which the system arrived at the present state.

The relevant distinction is not whether prior information is merely present, retrievable, decodable, or represented somewhere in the model.

The stronger question is whether that prior trajectory has become part of the **governing computational position** from which future possibilities are evaluated.

---

## Operational Form

A candidate state or distributed state exhibits trajectory indexing only if it satisfies all of the following under controlled conditions:

1. **Trajectory sensitivity** — the state differs systematically as a function of prior trajectory while the present task is held equivalent.
2. **Evaluative relevance** — the state predicts or contributes to differences in the relative evaluation of possible next states.
3. **Causal dependence** — intervention on the state changes the corresponding trajectory-relative evaluation.
4. **Donor-pattern transfer** — transferring the state from Trajectory A into the matched Trajectory B condition transfers an A-characteristic pattern of evaluation, and vice versa where technically possible.
5. **Cross-probe persistence** — the transferred pattern appears across a preregistered set of downstream probes or decisions rather than only in the immediately patched answer.
6. **Information-access control** — the effect cannot be adequately explained by one condition merely having different task-relevant factual information available.

---

## What Trajectory Indexing Is Not

Trajectory indexing is not established by:

- the known fact that transformer outputs are computed from internal activations and logits;
- identifying the layer where an answer becomes decodable or stable;
- ordinary next-token sampling or decoding;
- a model verbally claiming that a history is "mine," "binding," or important;
- decoding trajectory identity from activations without causal intervention;
- changing one answer through activation steering;
- semantic similarity between a prior trajectory and a later response; or
- unequal access to information across conditions.

A single successful patch may demonstrate causal influence or steering without demonstrating trajectory indexing.

---

## Structural Locus

Within this repository, **structural locus** means the causally implicated internal state, set of states, or distributed computational structure that carries the trajectory-indexing function under the tested conditions.

"Locus" does not imply one neuron, one head, one layer, one token position, or one anatomically discrete site.

The locus may be distributed.

---

## Claim Boundary

Evidence for trajectory indexing would support a structural claim about how prior trajectory participates in present and future evaluation.

It would not, by itself, establish consciousness, phenomenal experience, feeling, sentience, first-person awareness, or a metaphysically unified self.

---

**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum
