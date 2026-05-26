# Package A facilitator guide

## Purpose

Use this guide to prepare and run the real-world Package A activities with the client.

The goal is to make sure you collect the right material, in the right sequence, so the AI can process each activity cleanly and turn it into a validated output before the next step begins.

Use this guide together with:

* [Package_A_core_activities.md](Package_A_core_activities.md) for the package summary
* [Package_A_ai_process.md](Package_A_ai_process.md) for the AI handoff and stage-gated workflow
* [prototype_prompt_pack_template.md](prototype_prompt_pack_template.md) for the prompt structure used to generate the prototype

## Shared live-delivery prep assets

Use these shared files when you need to prepare the real-world session itself:

* [../../Projects/Templates/English/Shared/workshop_invite_template.md](../../Projects/Templates/English/Shared/workshop_invite_template.md)
* [../../Projects/Templates/English/Shared/session_brief_template.md](../../Projects/Templates/English/Shared/session_brief_template.md)

## How the workflow should run

1. Use this guide to prepare and run one Package A activity with the client.
2. Capture the required notes in the seeded project input file for that activity.
3. Bring that input into the AI process.
4. Review the processed output with the client and confirm any changes.
5. Only then move to the next activity.

Do not move ahead if the previous output is not yet accepted. The value of Package A depends on each step being grounded in validated input.

## Lean capture rule

Package A should not feel like a long repeated questionnaire.

Use these rules while facilitating:

* Start each activity from the validated output of the previous stage
* Treat confirmed client, scope, decision, target users, and constraints as carried-forward context unless the client explicitly changes them
* Capture only the genuinely new input needed for the current activity
* If a point only needs confirmation, confirm it quickly instead of re-documenting it in full
* Keep the live activity focused on the next decision, not on rebuilding earlier notes

When the activity is later simulated in chat, the AI should mirror the same logic by using a short step-based sequence and asking only for the minimum new input needed.

Use the seeded project input file in `01-inputs/` and [../../Projects/Templates/English/Package_A/package_a_template_library.md](../../Projects/Templates/English/Package_A/package_a_template_library.md) as the source of truth for the exact step-based handoff structure. The short lean capture structures later in this guide only summarize the sequence for each activity and should not be expanded back into full duplicate templates.

## AI handoff into the next live activity

When the previous stage has been validated and the next step is a real-world activity:

* The AI should explicitly say that the next step is now a live activity
* The AI should link to the seeded project input file for that activity
* The AI should link to the relevant part of this facilitator guide and any relevant template, question guide, or tool file
* The AI should summarize the objective, estimated time, and who should attend or what material should be gathered
* The AI should wait for the completed activity notes before resuming synthesis unless the user explicitly asks to simulate or prepare the activity in chat
* The AI should use the canonical handoff structure in [../../Projects/Templates/English/Shared/live_activity_handoff_message_template.md](../../Projects/Templates/English/Shared/live_activity_handoff_message_template.md)

## Final deliverables to leave the sprint with

By the end of Package A, you should be able to deliver:

* A recommendation document
* A map of the key breakdowns in the selected journey step
* A 1-2 screen clickable prototype illustrating the recommended improvement
* A short list of risks and next steps

To make the prototype reliably producible, the final synthesis should also generate:

* A prototype prompt pack file with:
  * A canonical prototype brief
  * Fresh-generation prompts
  * Refinement prompts
* A separate prototype record file that captures the approved screenshots, prototype link, iteration notes, and approval status

The prompt pack is a production-support artifact that helps create the clickable prototype. It should not replace the prototype itself, and it should not make the main final deliverable longer than it needs to be.

## Project setup before the sprint starts

Before Activity 1.1, create the project workspace for the engagement.

### Project setup checklist

* Ask for the project name and normalize it into a folder-safe format
* Create `../../Projects/<Project-Name>/`
* Create `../../Projects/<Project-Name>/00-project-setup/`
* Create `../../Projects/<Project-Name>/01-inputs/`
* Create `../../Projects/<Project-Name>/02-working/`
* Create `../../Projects/<Project-Name>/03-reviews/`
* Create `../../Projects/<Project-Name>/04-final/`
* Create `../../Projects/<Project-Name>/project_index.md` as the project control center
* Create `../../Projects/<Project-Name>/00-project-setup/project_setup.md`
* Seed the relevant Stage 0 and activity-input files in `01-inputs/`
* Seed the relevant activity-output files in `02-working/`
* Seed the relevant stage-review files in `03-reviews/`
* Seed the package final-deliverable file in `04-final/`
* Seed the separate prototype prompt-pack file in `04-final/`
* Seed the separate prototype record file in `04-final/`
* Record the original project name, folder name, package type, working language, created date, and current status in the setup note
* If the folder already exists, stop and confirm whether it should be reused before storing any files
* Store raw client inputs in `01-inputs/`, in-progress synthesis in `02-working/`, review versions in `03-reviews/`, and approved outputs in `04-final/`

## Before the sprint starts

### Minimum intake checklist

Collect this before Activity 1.1:

* The problem area, workflow, feature area, or journey step in scope
* The decision the sprint needs to support
* Why this matters now in business terms
* The evidence already available and who owns it
* The relevant stakeholders and teams
* The known constraints, assumptions, and out-of-scope items

### Pre-sprint preparation checklist

Before running the first activity:

* Confirm the sponsor and the named owner who can validate outputs
* Confirm which stakeholders should attend each live session
* Request the existing evidence early so Activity 1.2 is not delayed
* Book the live sessions in sequence so the sprint can keep momentum
* Tell the client that each activity ends with a review checkpoint before the next step starts

## Activity 1.1: Sponsor workshop and decision frame

### Objective

Agree the business question, target users, success measures, scope boundary, and main constraints for the sprint.

### Estimated activity time

90 minutes

### Who should attend

* Sponsor or budget owner
* Product, service, or business owner
* Relevant operational, commercial, or delivery stakeholders
* Avoid inviting observers who cannot contribute to the decision

### Prep before the session

* Confirm the decision the sprint must support
* Confirm what is already believed about the problem
* Prepare the out-of-scope boundary so the discussion stays focused
* Ask for any baseline metrics already known

### Suggested agenda

* Opening and objective framing: 10 minutes
* Problem framing and business context: 20 minutes
* Target users and journey focus: 20 minutes
* Success measures and constraints: 20 minutes
* Open questions and sprint priorities: 15 minutes
* Playback and close: 5 minutes

### Critical questions to ask

* What decision must be made before delivery starts?
* Why is this problem worth addressing now?
* Which users or staff groups matter most to that decision?
* What part of the journey is in scope, and what is not?
* What would success look like in business, user, and operational terms?
* Which constraints are fixed, and which are still assumptions?

### What you must capture

* Business question
* Decision to support
* Why this matters now
* Target users
* Scope and out-of-scope boundary
* Success measures, including baseline and target where possible
* Constraints
* Open sprint questions

### Lean capture structure

Use the seeded `01-inputs/package_a_activity_1_1_input.md` file for this activity.

Capture only:

* carried-forward context that changed
* genuinely new input from the workshop

Short sequence:

1. Workshop setup and business question
2. Users and scope
3. Measures and constraints
4. Tensions and open sprint questions

### Validation checkpoint

The client should confirm:

* The sprint is focused on the right problem
* The scope boundary is clear
* The success measures are good enough to guide the rest of the sprint
* Unknown constraints are logged as unknown, not hidden

## Activity 1.2: Evidence baseline review

### Objective

Turn the available evidence into a practical baseline that separates supported signals from assumptions.

### Estimated activity time

2-4 hours, depending on evidence quality and availability

### Evidence to request

* Analytics for the selected journey step
* Segmented performance data by device, traffic source, new versus returning visitor, or relevant customer segment where possible
* Support issues or complaint themes
* Sales or commercial input
* Prior research or usability findings
* Session recordings, heatmaps, or behavioral evidence if available

Use [../../Projects/Templates/English/Shared/evidence_request_template.md](../../Projects/Templates/English/Shared/evidence_request_template.md) if you need to request this material from the client team in a structured way.

### How to run this step

* Review the strongest sources first, not every possible source
* Keep the review tightly bounded to the selected problem
* Mark what is evidence, what is interpretation, and what is still assumption
* Pay attention to missing segmentation, because broad averages often hide where the problem is strongest

### What you must capture

* Sources reviewed
* Strongest signals
* Well-supported findings
* Directional but not yet proven findings
* Remaining assumptions
* Conflicts or gaps in the evidence
* Questions the sprint still needs to validate

### Lean capture structure

Use the seeded `01-inputs/package_a_activity_1_2_input.md` file for this activity.

Capture only:

* carried-forward context that changed
* genuinely new evidence findings and gaps

Short sequence:

1. Evidence sources and coverage
2. Strongest signals and supported findings
3. Remaining uncertainty and next validation questions

### Validation checkpoint

The client should confirm:

* The baseline reflects the strongest available evidence
* The difference between known and assumed is clear
* The remaining gaps are visible enough to guide the mapping and option review

## Activity 1.3: Journey-step mapping session

### Objective

Create a shared current-state view of the selected journey step and isolate the few breakdowns that matter most to the decision.

### Estimated activity time

60-90 minutes

### Who should attend

* Stakeholders close to the selected step
* People who understand the current workflow, content, systems, or service handoffs
* Avoid turning this into a full-journey workshop

### Suggested session flow

* Confirm the selected step and decision to support: 10 minutes
* Map the actors, current actions, and touchpoints: 20 minutes
* Map systems, dependencies, and handoffs: 15 minutes
* Identify the main friction points and internal implications: 20 minutes
* Prioritize the 3-5 most important breakdowns: 15 minutes

### What you must capture

* Selected step in scope
* Actors
* Current actions
* Touchpoints and channels
* Systems and dependencies
* Friction points
* Internal implications
* The 3-5 biggest breakdowns and why they matter

### Lean capture structure

Use the seeded `01-inputs/package_a_activity_1_3_input.md` file for this activity.

Capture only:

* the selected step and current-state mapping inputs
* the few breakdowns that matter to the decision

Short sequence:

1. Step in scope and current flow
2. Touchpoints and dependencies
3. Breakdown pattern

### Validation checkpoint

The client should confirm:

* The map reflects what happens today, not an idealized version
* The main breakdowns are the ones most relevant to the decision
* The scope has stayed bounded to one step or workflow slice

## Activity 2.1: Option review and preferred direction

### Objective

Compare a small number of realistic directions and identify the preferred route with clear tradeoffs.

### Estimated activity time

2 hours

### Prep before the session

* Bring the validated outputs from Activities 1.1 to 1.3
* Prepare 1-2 realistic directions
* If the client has not proposed options, collect enough material for the AI to generate them before the review
* Prepare shared criteria across user, business, and delivery lenses

### Suggested session flow

* Confirm objective and criteria: 15 minutes
* Review Option A: 25 minutes
* Review Option B: 25 minutes
* Compare tradeoffs and dependencies: 25 minutes
* Playback of preferred direction and open checks: 30 minutes

### What you must capture

* Options compared
* Comparison criteria
* Judgments for each option against the criteria
* Tradeoffs
* Risks and dependencies
* Preferred direction
* Open checks before recommendation work

### Lean capture structure

Use the seeded `01-inputs/package_a_activity_2_1_input.md` file for this activity.

Capture only:

* the options actually compared
* the criteria, tradeoffs, and preferred direction that emerged

Short sequence:

1. Decision and options
2. Comparison criteria
3. Option notes and tradeoffs
4. Preferred direction and open checks

### Validation checkpoint

The client should confirm:

* The same criteria were used across all options
* The tradeoffs are explicit
* The preferred direction is clear enough to package into a recommendation

## Activity 3.1: Recommendation package and concept brief

### Objective

Turn the validated sprint outputs into a decision-ready recommendation and a concept that is tangible enough for sponsor review.

### Estimated activity time

4-8 hours of synthesis and packaging, plus a 30-45 minute sponsor review checkpoint

### Prep before AI handoff

* Bring the validated preferred direction
* Confirm the intended scope boundary for the near-term delivery step
* Confirm any final constraints or dependencies that affect the recommendation
* Confirm how success should be measured after release
* Confirm which 1-2 screens or moments the prototype should show
* Confirm whether the user can share screenshots or links from the client's existing solution if the prototype should stay close to the current visual design
* Confirm whether the prototype should be built first in Figma Make or Google Stitch

### What you must capture

* Recommended direction
* Why this direction is stronger
* Target users
* Success measures
* What to build now
* What to defer
* What to validate next
* Risks and dependencies
* Immediate next steps
* The exact screens, moments, and interactions the prototype should include
* Any content, brand, or layout constraints that should shape the prototype prompt

### Lean capture structure

Use the seeded `01-inputs/package_a_activity_3_1_input.md` file for this activity.

Capture only:

* the final recommendation logic that still needs confirmation
* the prototype brief details needed to generate the prompt pack

Short sequence:

1. Recommendation lock and sponsor notes
2. Scope and measures
3. Risks, validation, and next steps
4. Prototype brief

### Validation checkpoint

The client should confirm:

* The recommendation supports the original decision
* The scope is tight enough for the next delivery step
* The build-now, defer, and validate-next split is credible
* The risks and measurement logic are explicit enough to move forward

### Prototype production step

After the AI has produced the recommendation package and prototype prompt pack:

1. Use the canonical brief and the tool-specific prompt in the selected design tool.
2. Generate the first prototype draft.
3. Review the draft against the validated recommendation and the prototype review checklist in [prototype_prompt_pack_template.md](prototype_prompt_pack_template.md).
4. If screenshots or links from the client's current solution were provided, check that the draft stays close to the existing visual language unless the brief explicitly asks for change.
5. Refine the prompt if the prototype drifts away from the agreed direction.
6. Include the final clickable prototype alongside the recommendation package.

## Practical facilitation rules

* Keep Package A bounded to one problem area, workflow, or journey step
* Treat unknown constraints as a risk to surface early
* Do not let the sprint become a redesign discussion
* Keep the language commercial and decision-oriented
* Push for baseline and target measures when stakeholders talk about success
* Only move forward when the previous output has been reviewed and accepted
