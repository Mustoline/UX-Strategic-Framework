---
name: recommendation-packager
description: Package the final Package A recommendation into a concise decision-ready document and concept brief. Use this when turning the sponsor workshop, evidence baseline, journey-step map, and option review into a recommendation that states what to build next, what to defer, and what still needs validation before implementation.
---

# Recommendation Packager

Use this skill for Package A Activity `3.1`: packaging the discovery sprint into a practical recommendation that can support the next delivery decision.

This skill should turn the chosen direction into a clear recommendation document and a tangible concept brief or lightweight prototype brief so the output is concrete enough for review and delivery planning.

This skill should build on the helper layer:

* Use [artifact-writer](../artifact-writer/SKILL.md) to draft the recommendation cleanly
* Use [ux-strategy-reviewer](../ux-strategy-reviewer/SKILL.md) as the final quality check on client-facing outputs

It should also use the earlier Package A outputs where relevant:

* [sponsor-workshop-facilitator](../sponsor-workshop-facilitator/SKILL.md) for the decision frame, target users, success measures, and constraints
* [evidence-baseline-reviewer](../evidence-baseline-reviewer/SKILL.md) for the strongest evidence and remaining assumptions
* [journey-step-mapper](../journey-step-mapper/SKILL.md) for the main breakdowns in the current step
* [option-review-facilitator](../option-review-facilitator/SKILL.md) for the preferred-direction rationale, tradeoffs, and open checks

## What this skill should produce

For most requests, produce a recommendation package with:

* A 1-2 page recommendation document
* A short statement of the decision the recommendation supports
* A summary of the preferred direction and why it is recommended
* A simple concept brief or prototype brief showing what the chosen direction needs to make tangible
* A clear build-now, defer, and validate-next view
* A short risk, dependency, and next-step list

## Operating modes

### Prep

Before packaging the recommendation, confirm:

* Which direction has been chosen or is currently preferred
* Which decision the sponsor now needs to make
* Which outputs from the earlier sprint steps are available
* Whether the concept needs a simple concept view, a prototype brief, or both
* Which assumptions, risks, or dependencies still need to be surfaced

Then:

* Use the packaging flow in [recommendation-patterns.md](references/recommendation-patterns.md)
* Prepare the document and concept structures in [recommendation-templates.md](references/recommendation-templates.md)
* Use `artifact-writer` to shape the final draft and `ux-strategy-reviewer` to refine it if the output is client-facing

### Run

While structuring the recommendation:

* Keep the document tied to the actual decision the client needs to make
* Show why the preferred direction is stronger than the alternatives considered
* Turn the direction into something tangible enough for review
* Make scope boundaries explicit so the recommendation does not overpromise
* Separate what should be built now, what should wait, and what still needs validation
* Make risks, dependencies, and unresolved assumptions visible

### Synthesize

After packaging:

* Produce a concise recommendation document that supports a go or no-go or scope decision
* Add a simple concept brief or lightweight prototype brief
* Include a short risk and next-step list that helps the client move toward delivery
* If needed, hand the draft to `artifact-writer` and then to `ux-strategy-reviewer`

## Core packaging objectives

The recommendation package should answer:

* What decision does the sponsor need to make now?
* What direction do we recommend and why?
* Which target users, success measures, and breakdowns shape that recommendation?
* What should be built next, deferred, or validated further?
* Which risks, assumptions, or dependencies still matter before implementation starts?

## Packaging flow

Read [recommendation-patterns.md](references/recommendation-patterns.md) for:

* The recommended packaging sequence
* What must appear in the recommendation document
* How to frame the concept brief
* Common watchouts that weaken the recommendation

## Output templates

Use [recommendation-templates.md](references/recommendation-templates.md) for:

* Recommendation document template
* Concept brief template
* Build-now, defer, validate summary
* Risk and next-step list

Adapt the output to the selected problem and decision rather than filling every section mechanically.

## Packaging rules

* Keep the recommendation decision-oriented, not just descriptive
* Use only the evidence and rationale the sprint can actually support
* Make the scope of the recommendation tight enough for the next delivery step
* Treat the concept brief as a tangible explanation of the direction, not a full delivery specification
* If uncertainty remains, show it clearly instead of hiding it
* Prefer a practical next-step recommendation over a polished but vague summary

## Minimum output standard

Unless the user asks for something else, return these sections:

1. Decision to support
2. Recommended direction
3. Why this direction
4. Concept brief or prototype brief
5. Build now, defer, and validate
6. Risks, dependencies, and next steps

## Boundaries

This skill covers Activity `A3.1` only. It packages the recommendation and concept direction. It does not replace detailed UI design, full technical specification, or implementation planning.
