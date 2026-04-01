---
name: journey-step-mapper
description: Map one selected journey step for Package A and identify where users or staff lose time, confidence, or momentum. Use this when preparing, running, or synthesizing a 60-90 minute mapping session focused on a bounded feature area, workflow, or journey moment in a discovery sprint.
---

# Journey Step Mapper

Use this skill for Package A Activity `1.3`: the current-state mapping session that makes the selected journey step visible enough to guide later option review and recommendation work.

This skill should help the team map the people, touchpoints, and dependencies shaping the problem area and identify the main breakdowns causing delay, confusion, or internal effort.

This skill should build on the helper layer:

* Use [map-structure-generator](../map-structure-generator/SKILL.md) to create the mapping scaffold, labels, and prompts
* Use [workshop-design-kit](../workshop-design-kit/SKILL.md) if the mapping is run as a live session
* Use [artifact-writer](../artifact-writer/SKILL.md) to draft the final one-page readout
* Use [ux-strategy-reviewer](../ux-strategy-reviewer/SKILL.md) as the final quality check on client-facing outputs

It should also use the earlier Package A outputs where relevant:

* [sponsor-workshop-facilitator](../sponsor-workshop-facilitator/SKILL.md) for the decision frame and target users
* [evidence-baseline-reviewer](../evidence-baseline-reviewer/SKILL.md) for the strongest evidence and known assumptions

## What this skill should produce

For most requests, produce a journey-step mapping pack with:

* A mapping objective tied to the selected decision and problem area
* A clear journey-step map scaffold for the current state
* Prompts for actors, touchpoints, dependencies, and friction points
* A short list of the 3-5 biggest breakdowns
* A concise readout of why those breakdowns matter to the sprint

## Operating modes

### Prep

Before mapping, confirm:

* The selected journey step, workflow, or feature area in scope
* Which target users or staff groups matter most
* Which evidence or sponsor-workshop outputs already exist
* Whether the session will be live or based on existing notes
* What decision the map must help support

Then:

* Use `map-structure-generator` to create the current-state journey-step scaffold
* Use `workshop-design-kit` if a live mapping session needs agenda and facilitation structure
* Use the prompts in [journey-step-patterns.md](references/journey-step-patterns.md)
* Prepare the output structure in [journey-step-templates.md](references/journey-step-templates.md)

### Run

During the mapping work:

* Keep the map bounded to the selected step rather than expanding into the full journey
* Capture what actually happens today, not what should happen
* Make actors, touchpoints, handoffs, and dependencies visible
* Identify where users or staff lose time, confidence, or momentum
* Push for concrete examples of friction instead of generic complaints
* Distinguish between core breakdowns and secondary irritants

### Synthesize

After mapping:

* Produce a one-page map or readout of the selected journey step
* Highlight the 3-5 biggest breakdowns causing delay, confusion, or internal effort
* Link each breakdown back to the selected decision or problem area
* If needed, hand the draft to `artifact-writer` and then to `ux-strategy-reviewer`

## Core mapping objectives

The journey-step map should answer:

* What happens in this part of the experience today?
* Which people, touchpoints, and dependencies shape it?
* Where do users or staff lose time, confidence, or momentum?
* Which breakdowns matter most to the next delivery decision?
* What should the sprint keep in focus as it moves into option review?

## Mapping flow

Read [journey-step-patterns.md](references/journey-step-patterns.md) for:

* The recommended mapping sequence
* What to capture in each section
* Prompts for identifying breakdowns and implications
* Common watchouts that weaken the map

## Output templates

Use [journey-step-templates.md](references/journey-step-templates.md) for:

* Mapping objective
* Journey-step map scaffold
* Breakdown summary
* Friction and dependency notes
* Journey-step readout

Adapt the output to the selected problem and decision rather than filling every section mechanically.

## Mapping rules

* Keep the scope bounded to one selected step or workflow slice
* Prefer observable current-state detail over abstract commentary
* Make it easy to see why the main breakdowns matter to the next decision
* Capture internal effort and dependency problems as well as visible user friction
* If evidence is partial, mark what still needs validation instead of implying certainty
* Focus on the few breakdowns that matter most rather than listing every issue

## Minimum output standard

Unless the user asks for something else, return these sections:

1. Mapping objective
2. Current-state structure
3. Actors, touchpoints, and dependencies
4. Main breakdowns
5. Why those breakdowns matter
6. Watchouts or validation gaps

## Boundaries

This skill covers Activity `A1.3` only. It creates the current-state view for the selected journey step. It does not replace the later option review or recommendation work.
