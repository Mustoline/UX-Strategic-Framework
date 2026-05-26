# Prototype prompt pack template

## Purpose

Use this template to turn validated package outputs into a prompt pack that can be used in tools such as Figma Make or Google Stitch.

This is a production-support artifact. It helps generate a prototype that reflects the decisions, constraints, and learnings from the package. It does not replace the underlying recommendation, map, roadmap, or other core deliverables.

## How to use this template

Complete the canonical prototype brief first.

Then adapt that brief into:

* A fresh-generation Figma Make prompt
* A refinement Figma Make prompt
* A fresh-generation Google Stitch prompt
* A refinement Google Stitch prompt

Finally, use the review checklist and prototype record template to judge whether the generated prototype still matches the validated package outputs and whether the approved artifact is captured cleanly.

## Canonical prototype brief

```md
# Canonical prototype brief

## Package
[Package A / Package B / Package C]

## Prototype purpose
[Why this prototype needs to exist and what decision or review it should support]

## Decision this prototype should support
[Text]

## Users in focus
* [Group]
* [Group]

## Journey or flow in scope
[Bounded flow, step, or selected high-risk journey slice]

## What the prototype must show
* [Screen, step, or moment]
* [Screen, step, or moment]
* [Screen, step, or moment]

## What decisions or learnings must be reflected
* [Decision or learning]
* [Decision or learning]
* [Decision or learning]

## What the prototype should help validate
* [Question]
* [Question]

## Content priorities
* [Content priority]
* [Content priority]

## Interaction notes
* [Interaction note]
* [Interaction note]

## Constraints to respect
* [Constraint]
* [Constraint]

## Existing visual references if available
* [Screenshot, URL, or note]
* [Screenshot, URL, or note]

## Visual alignment instruction
[If visual references are provided, keep the prototype aligned with the client's existing visual design unless a deliberate visual change is part of the brief]

## What to avoid
* [Item]
* [Item]

## Tone or brand cues
* [Cue]
* [Cue]

## Device or layout expectation
[Desktop / mobile / responsive / specific device focus]

## Output expectation
[For example: 1-2 clickable screens, core flow only, low-fidelity, mid-fidelity]
```

## Figma Make fresh-generation prompt

```md
Create a clickable prototype based on the following validated brief.

Important: treat the instructions below as generation guidance, not as visible UI copy. Do not render internal rationale, prototype labels, or explanatory strategy text inside the interface unless the brief explicitly asks for that content.

Goal:
[Prototype purpose]

Decision this prototype should support:
[Decision]

Users in focus:
* [Group]
* [Group]

Flow in scope:
[Flow or journey slice]

Create:
* [Screen or moment]
* [Screen or moment]
* [Screen or moment]

The prototype must reflect these validated decisions and learnings:
* [Decision or learning]
* [Decision or learning]
* [Decision or learning]

The prototype should help validate:
* [Question]
* [Question]

Content priorities:
* [Priority]
* [Priority]

Interaction notes:
* [Interaction note]
* [Interaction note]

Constraints to respect:
* [Constraint]
* [Constraint]

Existing visual references if available:
* [Screenshot, URL, or note]
* [Screenshot, URL, or note]

Visual alignment instruction:
[Text]

Avoid:
* [Item]
* [Item]

Tone and brand cues:
* [Cue]
* [Cue]

Device or layout expectation:
[Text]

Output expectation:
[Text]
```

## Figma Make refinement prompt

```md
Use this as a follow-up refinement prompt for the prototype that has already been generated.

Important:
* Do not start over with a new concept unless the brief explicitly says the previous direction was rejected.
* Keep the current generated prototype as the base and make targeted refinements only.
* Treat everything below as hidden generation guidance, not visible UI copy.
* Do not render internal rationale, prototype labels, or explanatory strategy text inside the interface unless the brief explicitly asks for that content.

Use these references together:
* The original client visual references or screenshots
* The current generated prototype that now needs refinement

Goal:
[What should improve in the next iteration without changing the overall concept]

Keep these parts from the current draft:
* [What already works]
* [What already works]

Change these things in the current draft:
1. [Correction]
* [Specific refinement]
* [Specific refinement]
2. [Correction]
* [Specific refinement]
* [Specific refinement]

Refine these existing screens or moments:
* [Screen or moment]
* [Screen or moment]

Interaction expectations:
* [Interaction note]
* [Interaction note]

Constraints to respect:
* [Constraint]
* [Constraint]

Visible UI copy should remain:
* concise
* product-like
* aligned with the language and tone in the brief

Avoid:
* [Item]
* [Item]

Output:
* an updated version of the current prototype
* [What should be clearer or better after refinement]
* [What visual or interaction quality should now align better]
```

## Google Stitch fresh-generation prompt

```md
Design a prototype that expresses the following validated product or service direction.

Important: treat the instructions below as generation guidance, not as visible UI copy. Do not render internal rationale, prototype labels, or explanatory strategy text inside the interface unless the brief explicitly asks for that content.

Prototype purpose:
[Prototype purpose]

Decision this prototype should support:
[Decision]

Primary users:
* [Group]
* [Group]

Flow or journey slice in scope:
[Text]

Show these key moments:
* [Screen or moment]
* [Screen or moment]
* [Screen or moment]

Build the prototype so it reflects these agreed decisions and learnings:
* [Decision or learning]
* [Decision or learning]
* [Decision or learning]

Use the prototype to help validate:
* [Question]
* [Question]

Content priorities:
* [Priority]
* [Priority]

Interaction notes:
* [Interaction note]
* [Interaction note]

Constraints:
* [Constraint]
* [Constraint]

Existing visual references if available:
* [Screenshot, URL, or note]
* [Screenshot, URL, or note]

Visual alignment instruction:
[Text]

Do not include:
* [Item]
* [Item]

Tone or brand cues:
* [Cue]
* [Cue]

Layout or device expectation:
[Text]

Output expectation:
[Text]
```

## Google Stitch refinement prompt

```md
Use this as a follow-up refinement prompt for the prototype that has already been generated.

Important:
* Do not replace the concept unless the validated brief changed.
* Refine the current generated prototype rather than starting from scratch.
* Treat the instructions below as hidden generation guidance, not visible interface copy.
* Do not render internal rationale, prototype labels, or explanatory strategy text inside the interface unless the brief explicitly asks for that content.

Use these references together:
* The original client visual references or screenshots
* The current generated prototype that needs iteration

Goal:
[What should improve in the next iteration]

Keep these parts from the current draft:
* [What already works]
* [What already works]

Refine the prototype with these corrections:
1. [Correction]
* [Specific refinement]
* [Specific refinement]
2. [Correction]
* [Specific refinement]
* [Specific refinement]

Keep the same screens or flow unless the brief explicitly changes scope:
* [Screen or moment]
* [Screen or moment]

Constraints:
* [Constraint]
* [Constraint]

Do not include:
* [Item]
* [Item]

Desired outcome:
* [What should feel clearer or stronger]
* [What should stay aligned with the client's visual language]
```

## Prototype approval record template

Use this after a prototype has been generated and reviewed.

```md
# Prototype record

## Tool used
[Figma Make / Google Stitch / other]

## Prototype link or working file
[Text]

## Approved screenshots or references
* [Screenshot, URL, or note]
* [Screenshot, URL, or note]

## Iteration history
1. [Fresh generation or revision]
2. [Refinement round]

## Review outcome
[What was approved, rejected, or still needs work]

## Remaining polish notes
* [Note]
* [Note]

## Approval status
[Draft / Ready for review / Approved]
```

## Prototype review checklist

Use this after generating the prototype:

* Does the prototype reflect the validated decision from the package?
* Does it stay within the agreed scope boundary?
* Does it show the right users, flow, and moments?
* Does it express the most important learnings from the package rather than inventing a new direction?
* Does it respect the stated constraints and avoid the excluded items?
* If visual references were provided, does it stay recognizably aligned with the client's existing visual design unless change was explicitly requested?
* Is it strong enough to support the review or decision it was meant for?
