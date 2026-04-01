---
name: sponsor-workshop-facilitator
description: Facilitate the Package A sponsor workshop that defines the business question, target users, success criteria, and constraints before delivery starts. Use this when preparing, running, or synthesizing a 90-minute sponsor workshop with 3-5 decision-makers in a discovery sprint.
---

# Sponsor Workshop Facilitator

Use this skill for Package A Activity `1.1`: the 90-minute sponsor workshop that creates the decision frame for the rest of the discovery sprint.

This skill should help the team agree what decision needs to be made, who matters most, how success will be judged, and which business or technical constraints shape the work.

This skill should build on the helper layer:

* Use [workshop-design-kit](../workshop-design-kit/SKILL.md) for agenda, facilitation structure, and note logic
* Use [evidence-ingest](../evidence-ingest/SKILL.md) if existing evidence needs to be normalized before or after the session
* Use [artifact-writer](../artifact-writer/SKILL.md) to draft the workshop output cleanly
* Use [ux-strategy-reviewer](../ux-strategy-reviewer/SKILL.md) as the final quality check on client-facing outputs

## What this skill should produce

For most requests, produce a sponsor workshop pack with:

* A workshop objective tied to the delivery decision the sprint must support
* A timed agenda for a 90-minute session
* Critical sponsor questions and follow-up probes
* A note structure focused on decision, users, success measures, constraints, and open questions
* A workshop summary that captures the agreed decision frame

## Operating modes

### Prep

Before the workshop, confirm:

* The problem area or journey step under discussion
* Which delivery decision this sprint needs to support
* Who will attend and what authority they hold
* What evidence already exists
* Which business or technical constraints are already known

Then:

* Use `workshop-design-kit` to shape the agenda and facilitation structure
* Use the question patterns in [sponsor-workshop-patterns.md](references/sponsor-workshop-patterns.md)
* Prepare the note structure and output templates in [sponsor-workshop-templates.md](references/sponsor-workshop-templates.md)

### Run

During the workshop:

* Keep the discussion tied to the business question and near-term decision
* Push the group to name target users precisely
* Turn vague success ambitions into concrete measures
* Separate fixed constraints from assumptions or preferences
* Surface disagreements rather than smoothing them away
* End with a short playback of what is agreed, what is still open, and what the sprint must clarify next

### Synthesize

After the workshop:

* Draft a concise sponsor workshop summary
* Capture the business question, target users, success measures, and constraints clearly
* Make unresolved assumptions and risks visible
* If needed, hand the draft to `artifact-writer` and then to `ux-strategy-reviewer`

## Core workshop objectives

The sponsor workshop should answer:

* What decision must be made before delivery starts?
* Which users, customers, or staff groups matter most to that decision?
* What would count as success in business and service terms?
* Which constraints are fixed, and which are still assumptions?
* What should this sprint clarify so the client can make a grounded next-step decision?

## Question selection

Read [sponsor-workshop-patterns.md](references/sponsor-workshop-patterns.md) for:

* The recommended 90-minute flow
* Critical questions by section
* Follow-up probes when sponsor answers stay too vague
* Watchouts that commonly weaken the output

## Output templates

Use [sponsor-workshop-templates.md](references/sponsor-workshop-templates.md) for:

* Sponsor workshop agenda
* Decision framing template
* Target-user summary
* Success-measure template
* Constraints register
* Workshop summary

Adapt the output to the workshop objective rather than filling every section mechanically.

## Facilitation rules

* Treat the workshop as a decision-framing session, not a general kickoff
* Keep the scope bounded to one problem area, workflow, or journey step
* Ask for concrete business consequences when sponsors speak in abstract terms
* Name what is not in scope so the discovery sprint stays focused
* If the group lacks enough evidence to answer something, record it as a sprint question rather than pretending it is settled
* Prefer a usable decision frame over an exhaustive discussion

## Minimum output standard

Unless the user asks for something else, return these sections:

1. Workshop objective
2. Suggested 90-minute agenda
3. Critical sponsor questions
4. Note structure
5. Draft workshop summary
6. Open questions and risks

## Boundaries

This skill covers Activity `A1.1` only. It frames the decision and prepares the sprint. It does not replace the later evidence review, journey mapping, option review, or recommendation activities.
