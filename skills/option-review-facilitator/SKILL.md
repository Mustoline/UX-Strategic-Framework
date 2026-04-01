---
name: option-review-facilitator
description: Facilitate the Package A option review that compares 1-2 solution directions against agreed business, user, and delivery criteria. Use this when preparing, running, or synthesizing a 2-hour option review that needs to narrow the recommendation to one preferred direction in a discovery sprint.
---

# Option Review Facilitator

Use this skill for Package A Activity `2.1`: the option review that turns the sprint's earlier findings into a grounded direction choice.

This skill should help the team compare 1-2 solution directions against shared business, user, and delivery criteria and identify which direction is most likely to improve the journey without creating avoidable delivery risk.

This skill should build on the helper layer:

* Use [workshop-design-kit](../workshop-design-kit/SKILL.md) for agenda, facilitation structure, and playback logic
* Use [artifact-writer](../artifact-writer/SKILL.md) to draft the option review output cleanly
* Use [ux-strategy-reviewer](../ux-strategy-reviewer/SKILL.md) as the final quality check on client-facing outputs

It should also use the earlier Package A outputs where relevant:

* [sponsor-workshop-facilitator](../sponsor-workshop-facilitator/SKILL.md) for the decision frame, target users, and success measures
* [evidence-baseline-reviewer](../evidence-baseline-reviewer/SKILL.md) for the strongest evidence and remaining assumptions
* [journey-step-mapper](../journey-step-mapper/SKILL.md) for the main breakdowns and dependencies in the current step

## What this skill should produce

For most requests, produce an option review pack with:

* A review objective tied to the decision the sprint must support
* A clear set of comparison criteria
* A structured comparison of 1-2 directions
* A short tradeoff summary
* A preferred-direction rationale and list of unresolved risks or checks

## Operating modes

### Prep

Before the option review, confirm:

* Which 1-2 directions are actually being compared
* Which decision the sponsor needs to make
* Which business, user, and delivery criteria matter most
* Which constraints, risks, or dependencies are already known
* Which earlier sprint outputs should shape the comparison

Then:

* Use `workshop-design-kit` to shape the 2-hour review structure if the session is live
* Use the comparison flow in [option-review-patterns.md](references/option-review-patterns.md)
* Prepare the scorecard and summary structure in [option-review-templates.md](references/option-review-templates.md)

### Run

During the option review:

* Keep the discussion tied to the agreed decision and criteria
* Compare the directions against the same criteria rather than different personal preferences
* Push participants to name tradeoffs explicitly
* Distinguish evidence-backed judgments from assumptions or optimism
* Make delivery implications visible alongside user and business value
* End with a clear playback of the preferred direction, the reasons, and the open checks

### Synthesize

After the review:

* Produce a concise option comparison summary
* Show the preferred direction and why it is stronger
* Capture risks, dependencies, and unresolved questions that still matter before recommendation work
* If needed, hand the draft to `artifact-writer` and then to `ux-strategy-reviewer`

## Core review objectives

The option review should answer:

* Which direction best addresses the selected problem?
* Which direction best fits the target users and success measures?
* Which direction creates the least avoidable delivery risk?
* What tradeoffs are we accepting if we choose this path?
* What still needs validation before the final recommendation is written?

## Comparison flow

Read [option-review-patterns.md](references/option-review-patterns.md) for:

* The recommended review sequence
* Criteria categories to use
* Prompts for surfacing tradeoffs
* Common watchouts that weaken the decision

## Output templates

Use [option-review-templates.md](references/option-review-templates.md) for:

* Option review objective
* Decision-criteria template
* Option comparison scorecard
* Tradeoff summary
* Preferred-direction rationale
* Risk and dependency list

Adapt the output to the selected problem and decision rather than filling every section mechanically.

## Review rules

* Keep the comparison limited to the directions that can actually be chosen
* Use the same criteria across all directions
* Treat user value, business value, and delivery implications as parallel decision lenses
* Make tradeoffs explicit rather than hiding them in vague consensus
* If the evidence is too weak to prefer a direction confidently, say so and define the next validation step
* Prefer a usable decision over a false sense of certainty

## Minimum output standard

Unless the user asks for something else, return these sections:

1. Review objective
2. Comparison criteria
3. Option comparison
4. Tradeoffs
5. Preferred direction
6. Risks, dependencies, and open checks

## Boundaries

This skill covers Activity `A2.1` only. It helps the team narrow to a preferred direction. It does not replace the later recommendation and concept-packaging work.
