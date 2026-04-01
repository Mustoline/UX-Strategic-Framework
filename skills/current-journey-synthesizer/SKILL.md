---
name: current-journey-synthesizer
description: Synthesize the Package B current-state journey by combining interview evidence with service and system context. Use this when turning the scoping output and 4-6 interview findings into a current-state journey map that shows where the experience and service break down across users, teams, and systems.
---

# Current Journey Synthesizer

Use this skill for Package B Activity `2.1`: the current-state journey work that turns research into a shared view of how the experience works today and where it breaks down across users, teams, and systems.

This skill should help the team map the end-to-end journey around the selected product or service area, make visible where users, internal teams, and systems create friction for one another, and distill the findings into opportunity areas, user priorities, and decision criteria.

This skill should build on the helper layer:

* Use [map-structure-generator](../map-structure-generator/SKILL.md) to create the current-state journey scaffold, labels, and prompts
* Use [artifact-writer](../artifact-writer/SKILL.md) to draft the map readout and summary cleanly
* Use [ux-strategy-reviewer](../ux-strategy-reviewer/SKILL.md) as the final quality check on client-facing outputs

It should also use earlier Package B outputs where relevant:

* Use [scoping-workshop-facilitator](../scoping-workshop-facilitator/SKILL.md) for the journey in scope, business case, success measures, and discovery questions
* Use [user-research-runner](../user-research-runner/SKILL.md) for the interview summaries, top needs, barriers, and decision points
* Use [evidence-ingest](../evidence-ingest/SKILL.md) if additional evidence needs to be normalized into the current-state view

## What this skill should produce

For most requests, produce a current-journey pack with:

* A mapping objective tied to the journey in scope and the decisions ahead
* A current-state journey map scaffold and populated synthesis view
* A clear view of where users, teams, and systems create friction for one another
* A short list of opportunity areas, user priorities, and decision criteria
* A concise readout of what the future-state work must respond to

## Operating modes

### Prep

Before synthesizing the current journey, confirm:

* Which journey, product, or service area is in scope
* Which interview summaries and evidence inputs are available
* Which users, teams, systems, and channels must appear in the map
* Which decisions the current-state view must support
* Whether a live synthesis session is needed or whether the work is based on existing notes

Then:

* Use `map-structure-generator` to create the current-state journey scaffold
* Use the synthesis flow in [current-journey-patterns.md](references/current-journey-patterns.md)
* Prepare the output structure in [current-journey-templates.md](references/current-journey-templates.md)

### Run

During synthesis:

* Keep the map tied to the journey in scope rather than drifting into unrelated adjacent journeys
* Combine user evidence with service, system, and team context
* Make visible where friction sits between users, touchpoints, teams, and systems
* Distinguish repeated breakdowns from isolated issues
* Pull out the moments that matter most to later concept definition and prioritization
* Preserve uncertainty or evidence gaps where the current-state picture is still incomplete

### Synthesize

After the journey work:

* Produce a current-state journey map or structured readout
* Highlight the main breakdowns across users, teams, and systems
* Distill the work into opportunity areas, user priorities, and decision criteria
* Show what the future-state concept work should solve first
* If needed, hand the draft to `artifact-writer` and then to `ux-strategy-reviewer`

## Core synthesis objectives

The current-state journey should answer:

* How does the selected journey work today from the user and service perspective?
* Where do users hesitate, struggle, or lose momentum?
* Where do teams, systems, or handoffs create friction for one another?
* Which opportunity areas and user priorities matter most?
* Which decision criteria should shape the later future-state concept work?

## Synthesis flow

Read [current-journey-patterns.md](references/current-journey-patterns.md) for:

* The recommended synthesis sequence
* What to capture in each journey stage
* How to frame opportunity areas and decision criteria
* Common watchouts that weaken the current-state view

## Output templates

Use [current-journey-templates.md](references/current-journey-templates.md) for:

* Mapping objective
* Current-state journey scaffold
* Breakdown summary
* Opportunity-area summary
* Decision-criteria summary
* Current-journey readout

Adapt the output to the journey and decision in scope rather than filling every section mechanically.

## Synthesis rules

* Keep the map focused on the agreed journey in scope
* Show both visible user friction and less visible service or system friction
* Prefer repeated evidence-backed patterns over isolated anecdotes
* Turn findings into usable opportunity areas and decision criteria, not just pain-point lists
* If the current-state picture is partial, mark that clearly rather than implying a complete model
* Keep the output usable for later concept definition rather than overloaded with detail

## Minimum output standard

Unless the user asks for something else, return these sections:

1. Mapping objective
2. Current-state journey structure
3. Main breakdowns across users, teams, and systems
4. Opportunity areas and user priorities
5. Decision criteria for future-state work
6. Watchouts or gaps

## Boundaries

This skill covers Activity `B2.1` only. It creates the shared current-state view and synthesis layer for Package B. It does not replace the later future-state concept session or prioritization work.
