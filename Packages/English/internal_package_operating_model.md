# Internal package operating model

Internal note: This document describes how the package portfolio is delivered behind the scenes. It is not client-facing and should not be quoted or referenced in proposals, sales material, or executive summaries.

## Purpose

The package portfolio now runs on a consistent internal structure so the offer language, the facilitated activities, and the stage-gated synthesis process all support the same outcomes.

The goal is to make each package:

* Easier to sell because the package logic is clear and repeatable
* Easier to facilitate because the real-world activities are prepared in a consistent way
* Easier to run with AI support because each activity has a defined handoff, output, and validation gate
* Easier to maintain because package changes can be traced across summary, facilitation, and synthesis documents

## The three-layer model

Each package is maintained in three linked layers:

### 1. Summary layer

This is the package logic and commercial description.

It defines:

* What the package is for
* When to use it
* The activities, timeline, and estimated effort
* The concrete outcomes and decisions supported

Primary files:

* `./strategic_ux_packages.md`
* `./Package_A_core_activities.md`
* `./Package_B_core_activities.md`
* `./Package_C_core_activities.md`
* `../../Sales materials/English/executive_offer_one_pager.md`
* `../../Sales materials/English/upstream_discovery_positioning.md`

### 2. Facilitator layer

This is the real-world delivery guide for the consultant or facilitator.

It defines:

* How to prepare and run the activity
* Who needs to participate
* What evidence or material must be collected
* What must be captured in the handoff back into synthesis
* What the client must validate before the next activity begins

Primary files:

* `./Package_A_facilitator_guide.md`
* `./Package_B_facilitator_guide.md`
* `./Package_C_facilitator_guide.md`

### 3. Internal synthesis layer

This is the stage-gated internal workflow that turns captured input into decision-ready outputs.

It defines:

* Required input format for each activity handoff
* Analysis and synthesis steps
* Expected output format
* Validation states and stop or go rules
* What carries forward into the next activity
* Prototype prompt-pack production where relevant

Primary files:

* `./Package_A_ai_process.md`
* `./Package_B_ai_process.md`
* `./Package_C_ai_process.md`
* `./prototype_prompt_pack_template.md`

## Supporting execution library

The three-layer model is still the operating backbone.

The `/skills` folder is a supporting execution library behind that model, not a parallel package system.

It should be used to:

* Power activity-specific synthesis, facilitation support, and review
* Keep specialist logic reusable across packages
* Support optional specialist agents where a bounded activity clearly benefits from them

It should not be used to:

* Replace the package stage gates
* Create a second user-visible workflow
* Drift away from the package files and project templates

Primary files:

* `./internal_activity_skill_mapping.md`
* `../../skills/`

## Project storage convention

Every real Package A, Package B, or Package C engagement should start with a project setup step before intake begins.

At the start of a live package:

* Ask the user for the project name
* Normalize the name into a folder-safe format and stop for confirmation if that normalized folder already exists
* Create `../../Projects/<Project-Name>/`
* Create `../../Projects/<Project-Name>/00-project-setup/`
* Create `../../Projects/<Project-Name>/00-project-setup/shared-prep/`
* Create `../../Projects/<Project-Name>/01-inputs/`
* Create `../../Projects/<Project-Name>/02-working/`
* Create `../../Projects/<Project-Name>/03-reviews/`
* Create `../../Projects/<Project-Name>/04-final/`
* Create `../../Projects/<Project-Name>/project_index.md` as the project control center
* Create `../../Projects/<Project-Name>/00-project-setup/project_setup.md`
* Seed the shared prep assets in `00-project-setup/shared-prep/`
* Seed a package-specific ready-to-edit draft for the first live activity in `00-project-setup/shared-prep/`
* Refresh the generated `next_activity_*.md` prep files in `00-project-setup/shared-prep/` after each review sync
* Seed the relevant Stage 0 and activity-input files in `01-inputs/`
* Seed the relevant activity-output files in `02-working/`
* Seed the relevant stage-review files in `03-reviews/`
* Seed the final-deliverable file in `04-final/`
* Where prototype work is part of the package, separate the main final deliverable, the prototype prompt pack, and the prototype record into distinct files in `04-final/`
* Keep all project-generated files for that engagement inside this folder structure
* After a review file is updated with a validation decision, run `python3 Projects/sync_project_status.py --project-name "<Project name>"` so the project control files reflect the current workflow state and the next live activity prep pack is refreshed
* When the work is being run through this tool, the assistant should do that automatically in the same turn as the validation update

Use [../../Projects/README.md](../../Projects/README.md) as the shared storage convention. Keep `../../Projects/Dry runs/` separate for scenario tests rather than live client work.

Use [../../Projects/Templates/English/Shared/activity_readiness_checklist.md](../../Projects/Templates/English/Shared/activity_readiness_checklist.md) when a live activity needs a pre-flight readiness check, and use [../../Projects/Templates/English/Shared/pilot_retrospective_template.md](../../Projects/Templates/English/Shared/pilot_retrospective_template.md) after pilots or dry runs to capture improvements for the next iteration.

Use [../../Projects/Templates/English/Shared/evidence_request_template.md](../../Projects/Templates/English/Shared/evidence_request_template.md) when an activity depends on client-side evidence, access, exports, or supporting material.

Use [../../Projects/Templates/English/Shared/workshop_invite_template.md](../../Projects/Templates/English/Shared/workshop_invite_template.md), [../../Projects/Templates/English/Shared/interview_invite_and_consent_template.md](../../Projects/Templates/English/Shared/interview_invite_and_consent_template.md), and [../../Projects/Templates/English/Shared/session_brief_template.md](../../Projects/Templates/English/Shared/session_brief_template.md) when the next step needs practical live-session preparation. New projects should also start with the seeded `00-project-setup/shared-prep/first_live_activity_example_draft.md` as a ready-to-edit first pass for the first live activity, and then rely on the auto-refreshed `next_activity_*.md` files after each validated stage.

## Client-facing language rule

Clients do not need to hear about agentic workflows, internal prompts, or AI process mechanics.

In client-facing material, describe the work as:

* A clear package with a defined decision to support
* Focused workshops, interviews, reviews, and evidence inputs
* Structured synthesis between activities
* Review and validation checkpoints tied to concrete outputs

Do not describe the work as:

* An AI workflow
* An agentic process
* A prompt-driven production model
* A hidden automation system

The client should experience the work as a well-run discovery process, not as an explanation of the internal machinery supporting it.

## Standard dependency pattern

The standard operating sequence is:

1. The client or facilitator generates the required input in the real-world activity.
2. The captured input is structured into the agreed handoff format.
3. The internal synthesis process turns that input into a concrete output.
4. The client reviews and validates the output.
5. The next activity starts only when the previous output has been accepted or any open risks are made explicit.

This pattern applies across Package A, Package B, and Package C.

## Real-world handoff rule

After any validated stage, first check whether the next step is a real-world activity or an internal synthesis step.

If the next step is a real-world activity:

* Stop and hand off to that activity explicitly instead of immediately asking for completed notes
* Name the activity, purpose, and estimated time
* State who should attend or what evidence or material should be gathered
* Link to the seeded project input file in `Projects/<Project-Name>/01-inputs/`
* Link to the relevant facilitator guide and any relevant template, question guide, or tool file
* Ask the user to come back with the completed notes or request help preparing the activity
* Use the exact section order defined in [../../Projects/Templates/English/Shared/live_activity_handoff_message_template.md](../../Projects/Templates/English/Shared/live_activity_handoff_message_template.md)

Only ask for the completed activity notes directly in chat when the user explicitly asks to simulate or prepare that activity inside the tool.

## Visibility rule for user prompts

Because the interface may collapse progress updates:

* Keep progress narration in commentary or status updates only
* Put direct user questions, validation prompts, and next-step requests in the main user-visible response
* Do not hide the actual prompt for the user inside commentary text
* Do not hide any part of the live-activity handoff structure inside commentary text

## Safety rule for live question sequences

When the user asks to simulate a live activity inside the tool:

* Treat the whole sequence as a temporary capture mode
* Run it as a short step-based flow rather than a long field-by-field questionnaire
* Use 2-4 steps for most activities and show visible progress such as `Activity 1.2, step 2 of 3`
* Each step can contain 1-3 tightly related questions
* Carry forward validated context from earlier stages by default and ask only for changed, missing, or still-contested input
* Switch to chat-only simulation mode for the duration of the sequence
* In chat-only simulation mode, do not run file reads, file writes, sync commands, or any other tool actions during the active question flow
* Hold the captured notes in working memory until the sequence is complete
* Persist the notes only after the last question, when the user explicitly asks to save mid-flow, or at the next validation checkpoint
* Do not let raw command or tool text leak into the visible question flow
* Keep the user-visible flow clean and uninterrupted until the sequence is complete

## Prior-answer recap rule

When a follow-up question depends on an answer the user has already given in the same flow:

* Restate the relevant earlier answer inside the new question
* Do not make the user scroll back to recover context
* Use short recap phrasing before the question itself, especially for options, constraints, chosen directions, and earlier named concepts

## Simulation fallback rule

If internal command or tool text leaks into the visible conversation during a simulated activity:

* Treat the leak as a blocker for the one-question-at-a-time mode
* Stop the live question sequence immediately
* Switch first to a grouped-step fallback mode instead of jumping straight to a full activity dump
* Give the user a short recap of what is already captured
* Ask for the remaining questions for the current step or next logical step in one grouped reply
* Keep the visible progress format so the user still knows where they are in the sequence
* Only if that grouped-step fallback also proves unstable should the process switch to a single-message fallback for the rest of the activity
* Save and synthesize only after the user returns the remaining fields
* Name the issue honestly as a workflow or platform limitation and carry it into pilot feedback

## Deliverable rule

Each package must still produce the concrete outcomes promised in the offer documents. The internal operating model supports those outcomes but does not replace them.

That means:

* Package A must still produce the recommendation document, journey-step breakdown map, clickable prototype, and risk or next-step list
* Package B must still produce the insight summary, current-state and future-state journey maps, required service-change list, clickable prototype, and prioritized delivery recommendation
* Package C must still produce the executive brief, current-state service blueprint, tested future-state service model, phased roadmap, and change or business case summary

Where a prototype is part of the deliverable, the prompt pack is an internal production-support asset. It is not the client deliverable itself.

## Maintenance rule

When a package changes, update all three layers.

Minimum update path:

* The package summary language in `./strategic_ux_packages.md`
* The package summary file in `./Package_*_core_activities.md`
* The matching facilitator guide
* The matching internal synthesis file
* Any portfolio-level doc whose wording depends on the package logic

## Portfolio-level application

Use the model like this:

* `./strategic_ux_packages.md`, `../../Sales materials/English/upstream_discovery_positioning.md`, and `../../Sales materials/English/executive_offer_one_pager.md` should describe the client experience of the model without mentioning AI
* `../../Sales materials/English/discovery_sales_playbook.md` should help explain the staged delivery model in commercial conversations without exposing internal mechanics
* `../../Sales materials/English/discovery_phase_proposal_template.md` should translate the model into proposal-safe language and client commitments
* The package facilitator guides and internal synthesis files should carry the operational detail needed to run the work consistently
