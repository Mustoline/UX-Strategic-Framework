---
name: map-structure-generator
description: Create reusable structures for journey maps, ecosystem maps, and service blueprints in strategic UX and service design discovery work. Use this when a mapping activity needs a clear scaffold, labeling logic, legend, breakdown areas, or dependency structure before the team captures findings.
---

# Map Structure Generator

Use this skill to create the structure behind discovery maps so teams can capture findings in a consistent and decision-oriented way.

This skill is responsible for map logic, section structure, labels, and output scaffolding. It should not invent findings, fill gaps with assumptions, or pretend the current-state evidence is stronger than it is.

## What this skill should produce

For most requests, produce a mapping scaffold with:

* A clear mapping objective tied to a decision or discovery question
* A recommended map type
* A section structure with labels and fields
* A legend for actors, touchpoints, systems, breakdowns, and dependencies
* Prompts for capturing friction, risk, ownership, and service implications

## Operating modes

### Prep

Before creating the map structure, confirm:

* Which package and activity this supports
* Which map type is needed
* What slice of the journey, service, or ecosystem is in scope
* Which actors, touchpoints, systems, or teams need to appear
* What decision the map must help support

If the map type is not specified, choose the one that best fits the activity and state the assumption.

### Run

While supporting the mapping work:

* Keep the map tied to the scope and decision it must support
* Separate current-state observation from future-state aspiration
* Use labels that make handoffs, friction, ownership, and dependencies visible
* Keep the structure readable enough for workshop use and synthesis afterward
* Prompt for where value is lost, effort is added, or risk accumulates

### Synthesize

After the structure is defined:

* Produce a finished scaffold with consistent sections and labels
* Add a legend and annotation rules
* Include prompts for breakdowns, dependencies, and implications
* Make the output ready for the relevant activity-facing skill to populate

## Map selection

Read [map-patterns.md](references/map-patterns.md) to choose the right structure for:

* Journey-step maps
* Current-state journey maps
* Ecosystem maps
* Service blueprints
* Future-state journey or service maps

## Output templates

Use [map-templates.md](references/map-templates.md) for:

* Journey map scaffold
* Ecosystem map scaffold
* Service blueprint scaffold
* Legend template
* Breakdown and dependency prompt set

Adapt the scaffold to the decision the work needs to support rather than filling every possible section.

## Mapping rules

* Map only what is needed to understand the problem and support the next decision
* Use the same labels consistently across rows, columns, and annotations
* Make it easy to see where users, teams, or systems create friction for one another
* Show ownership and dependency gaps where they matter to delivery or service change
* If the evidence is partial, leave placeholders and mark what still needs validation
* Prefer structures that support synthesis and prioritization over visually impressive but vague maps

## Minimum output standard

Unless the user asks for something else, return these sections:

1. Mapping objective
2. Recommended map type
3. Structure and sections
4. Legend and labeling rules
5. Breakdown and dependency prompts
6. Watchouts or gaps

## Boundaries

This skill does not replace the activity-facing skill that performs the mapping work. It is the structure layer that makes the map usable, consistent, and aligned to the discovery decision.
