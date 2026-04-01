---
name: evidence-baseline-reviewer
description: Review existing evidence for Package A and turn it into a practical evidence baseline that separates known signals from assumption. Use this when synthesizing analytics, support issues, sales input, and prior research relevant to one selected problem area before mapping and option review begin.
---

# Evidence Baseline Reviewer

Use this skill for Package A Activity `1.2`: reviewing existing evidence relevant to the selected problem so the sprint starts from the strongest available signals instead of internal debate.

This skill should help the team identify what appears well supported, what is still assumption, and which questions the sprint must validate next.

This skill should build on the helper layer:

* Use [evidence-ingest](../evidence-ingest/SKILL.md) to normalize the raw sources first
* Use [artifact-writer](../artifact-writer/SKILL.md) to draft a concise evidence baseline summary
* Use [ux-strategy-reviewer](../ux-strategy-reviewer/SKILL.md) as the final quality check on client-facing outputs

## What this skill should produce

For most requests, produce an evidence baseline pack with:

* A short evidence objective tied to the selected problem and decision
* A summary of the strongest available signals
* A known-versus-assumed view
* A short interpretation of what the evidence implies for the sprint
* A list of evidence gaps and validation priorities

## Operating modes

### Prep

Before reviewing the evidence, confirm:

* The selected problem area, feature area, workflow, or journey step
* The decision the sprint needs to support
* What evidence sources are available
* Which outputs from the sponsor workshop are already agreed
* Whether the team already suspects key unknowns or disagreements

Then:

* Use `evidence-ingest` to normalize the raw material if it has not already been structured
* Use the review flow in [evidence-baseline-patterns.md](references/evidence-baseline-patterns.md)
* Prepare the output structure in [evidence-baseline-templates.md](references/evidence-baseline-templates.md)

### Run

During the review:

* Keep the evidence tied to the selected problem and decision
* Pull out the strongest patterns across analytics, support, sales input, and prior research
* Separate direct evidence from interpretation
* Identify where different sources reinforce each other and where they conflict
* Flag where the evidence is too weak or too broad to guide the next step confidently

### Synthesize

After the review:

* Produce a concise evidence baseline summary
* Show what appears known, what remains assumption, and what the sprint should clarify next
* Link the evidence back to the business question and target users from the sponsor workshop
* If needed, hand the draft to `artifact-writer` and then to `ux-strategy-reviewer`

## Core review objectives

The evidence baseline should answer:

* What do we already know that is relevant to this decision?
* Which signals appear strongest across the available sources?
* What still rests on assumption rather than evidence?
* Which questions are most important for the sprint to clarify next?
* Which source gaps or conflicts could weaken the later recommendation?

## Review flow

Read [evidence-baseline-patterns.md](references/evidence-baseline-patterns.md) for:

* The recommended review sequence
* What to emphasize by source type
* How to frame known versus assumed
* Common watchouts that weaken the baseline

## Output templates

Use [evidence-baseline-templates.md](references/evidence-baseline-templates.md) for:

* Evidence review objective
* Strongest-signals summary
* Known-versus-assumed matrix
* Evidence gap list
* Evidence baseline summary

Adapt the output to the decision the sprint must support rather than filling every section mechanically.

## Review rules

* Stay focused on the selected problem rather than summarizing everything the client knows
* Prefer cross-source patterns over isolated facts
* Make the limits of the evidence visible
* Name the commercial, service, or delivery implications where the evidence supports them
* Preserve conflicts between sources rather than smoothing them away
* Treat weak evidence as a cue for validation, not a cue for overconfidence

## Minimum output standard

Unless the user asks for something else, return these sections:

1. Evidence objective
2. Sources reviewed
3. Strongest signals
4. Known versus assumed
5. Gaps, conflicts, and watchouts
6. Questions to validate next

## Boundaries

This skill covers Activity `A1.2` only. It prepares the evidence baseline for the rest of the sprint. It does not replace the later mapping, option review, or recommendation work.
