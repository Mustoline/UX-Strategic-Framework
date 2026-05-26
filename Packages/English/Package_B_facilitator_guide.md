# Package B facilitator guide

## Purpose

Use this guide to prepare and run the real-world Package B activities with the client.

The goal is to make sure you collect the right material, in the right sequence, so the AI can process each activity cleanly and turn it into a validated output before the next step begins.

Use this guide together with:

* [Package_B_core_activities.md](Package_B_core_activities.md) for the package summary
* [Package_B_ai_process.md](Package_B_ai_process.md) for the AI handoff and stage-gated workflow
* [prototype_prompt_pack_template.md](prototype_prompt_pack_template.md) for the prompt structure used to generate the prototype

## Shared live-delivery prep assets

Use these shared files when you need to prepare the real-world session itself:

* [../../Projects/Templates/English/Shared/workshop_invite_template.md](../../Projects/Templates/English/Shared/workshop_invite_template.md)
* [../../Projects/Templates/English/Shared/interview_invite_and_consent_template.md](../../Projects/Templates/English/Shared/interview_invite_and_consent_template.md)
* [../../Projects/Templates/English/Shared/session_brief_template.md](../../Projects/Templates/English/Shared/session_brief_template.md)

## How the workflow should run

1. Use this guide to prepare and run one Package B activity with the client.
2. Capture the required notes in the seeded project input file for that activity.
3. Bring that input into the AI process.
4. Review the processed output with the client and confirm any changes.
5. Only then move to the next activity.

Do not move ahead if the previous output is not yet accepted. The value of Package B depends on each step being grounded in validated input.

## Lean capture rule

Package B should not feel like a long repeated questionnaire.

Use these rules while facilitating:

* Start each activity from the validated output of the previous stage
* Treat confirmed client, opportunity area, journey in scope, target users, key stakeholders, and constraints as carried-forward context unless the client explicitly changes them
* Capture only the genuinely new input needed for the current activity
* If a point only needs confirmation, confirm it quickly instead of re-documenting it in full
* Keep the live activity focused on the next decision, not on rebuilding earlier notes

When the activity is later simulated in chat, the AI should mirror the same logic by using a short step-based sequence and asking only for the minimum new input needed.

Use the seeded project input file in `01-inputs/` and [../../Projects/Templates/English/Package_B/package_b_template_library.md](../../Projects/Templates/English/Package_B/package_b_template_library.md) as the source of truth for the exact step-based handoff structure. The short lean capture structures later in this guide only summarize the sequence for each activity and should not be expanded back into full duplicate templates.

## AI handoff into the next live activity

When the previous stage has been validated and the next step is a real-world activity:

* The AI should explicitly say that the next step is now a live activity
* The AI should link to the seeded project input file for that activity
* The AI should link to the relevant part of this facilitator guide and any relevant template, question guide, or tool file
* The AI should summarize the objective, estimated time, and who should attend or what material should be gathered
* The AI should wait for the completed activity notes before resuming synthesis unless the user explicitly asks to simulate or prepare the activity in chat
* The AI should use the canonical handoff structure in [../../Projects/Templates/English/Shared/live_activity_handoff_message_template.md](../../Projects/Templates/English/Shared/live_activity_handoff_message_template.md)

## Final deliverables to leave the package with

By the end of Package B, you should be able to deliver:

* A concise insight summary from 4-6 interviews
* A current-state and future-state journey map
* A list of required service changes across process, content, ownership, and data
* A clickable prototype of the core flow
* A prioritized delivery recommendation

To make the prototype reliably producible, the final synthesis should also generate:

* A prototype prompt pack file with:
  * A canonical prototype brief
  * Fresh-generation prompts
  * Refinement prompts
* A separate prototype record file that captures approved screenshots, the prototype link, iteration notes, and approval status

The prompt pack is a production-support artifact that helps create the clickable prototype. It should not replace the prototype itself, and it should not make the main final deliverable longer than it needs to be.

## Project setup before the package starts

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

## Before the package starts

### Minimum intake checklist

Collect this before Activity 1.1:

* The opportunity area, product, portal, or service journey in scope
* The decisions the package needs to support
* Why this matters now in business terms
* The evidence already available and who owns it
* The target user groups to recruit or represent
* The relevant stakeholders, teams, and systems
* The known constraints, assumptions, and out-of-scope items

### Pre-package preparation checklist

Before running the first activity:

* Confirm the sponsor and the named owner who can validate outputs
* Confirm who must attend each live session
* Confirm what evidence can be shared before research starts
* Confirm recruitment feasibility and who can help access users
* Book the live sessions and review points in sequence
* Tell the client that each activity ends with a review checkpoint before the next step starts

## Activity 1.1: Scoping workshop and research frame

### Objective

Agree the journey in scope, business case, success measures, scope boundaries, and the questions the package must answer.

### Estimated activity time

2 hours

### Who should attend

* Sponsor or budget owner
* Product, service, or business owner
* Commercial, operational, content, or delivery stakeholders with relevant authority

### Prep before the session

* Confirm the opportunity area under discussion
* Collect any known business case inputs and outcome expectations
* Prepare a first view of in-scope and out-of-scope areas
* Confirm what evidence already exists

### Suggested agenda

* Objective and decision framing: 15 minutes
* Opportunity area and business case: 30 minutes
* Journey in scope and scope boundaries: 30 minutes
* Success measures and discovery questions: 30 minutes
* Playback and next steps: 15 minutes

### Critical questions to ask

* Which journey or service area is actually in scope?
* What business case or commercial logic makes this work worth doing now?
* Which outcomes should this package influence?
* What should be explicitly out of scope?
* What would count as success for this package?
* Which research questions must be answered before delivery scope can be set with confidence?

### What you must capture

* Business case
* Journey in scope
* Scope boundaries
* Target users
* Success measures
* Discovery questions
* Risks or disagreements

### Lean capture structure

Use the seeded `01-inputs/package_b_activity_1_1_input.md` file for this activity.

Capture only:

* carried-forward context that changed
* genuinely new framing input from the workshop

Short sequence:

1. Workshop setup and business case
2. Journey, users, and scope
3. Measures and discovery focus
4. Constraints, tensions, and open questions

### Validation checkpoint

The client should confirm:

* The journey in scope is clear
* The business case is specific enough to guide the research
* The success measures and discovery questions are good enough to drive the rest of the package

## Activity 1.2: Evidence review, recruitment, and user interviews

### Objective

Build a grounded picture of user needs, barriers, workarounds, and decision points before the work moves into journey and concept definition.

### Estimated activity time

1-2 days across evidence prep, recruitment coordination, 4-6 interviews, and first synthesis

### Evidence and access to request

* Analytics and behavioral evidence relevant to the journey
* Customer feedback, support themes, and sales input
* Prior research or usability findings
* Access to the user groups that matter to the journey in scope
* Any constraints affecting recruitment, confidentiality, or interview format

Use [../../Projects/Templates/English/Shared/evidence_request_template.md](../../Projects/Templates/English/Shared/evidence_request_template.md) if you need to request this evidence or access from the client team in a structured way.

### How to run this step

* Review the strongest evidence before interviews start
* Recruit for relevance to the journey, not demographic spread for its own sake
* Use the interviews to understand real goals, barriers, decision points, and workarounds
* Separate participant quotes, team inference, and remaining assumptions

### What you must capture

* Research objective
* Participant profile or recruitment logic
* Evidence reviewed
* Top user needs
* Main barriers
* Decision points and comparison logic
* Open questions for journey and concept work

### Lean capture structure

Use the seeded `01-inputs/package_b_activity_1_2_input.md` file for this activity.

Capture only:

* the strongest evidence and interview findings
* the new needs, barriers, and decision logic that matter to the package

Short sequence:

1. Evidence and research coverage
2. Needs and barriers
3. Decision criteria and workarounds
4. Conflicts, surprises, and next questions

### Validation checkpoint

The client should confirm:

* The insight summary reflects the right users
* The needs, barriers, and decision points feel credible
* The most important questions for the journey work are visible

## Activity 2.1: Current-state journey map and opportunity framing

### Objective

Create a shared current-state view of the journey and identify the most important opportunity areas for the future-state concept.

### Estimated activity time

4-6 hours of synthesis and mapping, plus a 45-60 minute stakeholder review checkpoint

### Who should attend the review

* Stakeholders who understand the journey today
* Teams that influence the service, content, process, or systems shaping the journey

### How to run this step

* Map the journey end to end across users, teams, and systems
* Show where users hesitate, where handoffs fail, and where service logic creates friction
* Distill the few opportunity areas that matter most to the concept phase

### What you must capture

* Current-state journey stages
* User needs and barriers by stage
* Teams, systems, and handoffs involved
* Main breakdowns
* Opportunity areas
* Decision criteria the future-state concept must satisfy

### Lean capture structure

Use the seeded `01-inputs/package_b_activity_2_1_input.md` file for this activity.
Use [../../Projects/Templates/English/Shared/current_journey_mapping_template.md](../../Projects/Templates/English/Shared/current_journey_mapping_template.md) or the generated `next_activity_mapping_canvas.md` in the project's `00-project-setup/shared-prep/` folder if you want a concrete canvas for mapping the current-state journey.

Capture only:

* the current-state structure that needs to be visible
* the few breakdowns, opportunity areas, and decision criteria that matter next

Short sequence:

1. Current-state structure
2. Breakdown pattern and dependencies
3. Opportunity areas and decision criteria

### Validation checkpoint

The client should confirm:

* The current-state journey is realistic
* The main breakdowns matter to the decisions ahead
* The opportunity areas are tight enough to guide the concept work

## Activity 3.1: Future-state concept working session

### Objective

Define the future-state journey and the required service changes behind it.

### Estimated activity time

2-3 hours for the concept session, plus 3-5 hours of synthesis

### Who should attend

* Stakeholders who can shape product, service, content, operational, ownership, and data implications

### Prep before the session

* Bring the validated current-state journey and opportunity areas
* Prepare the future-state concept scaffold
* Confirm which delivery questions the concept must make easier

### Suggested session flow

* Playback of the current-state opportunity frame: 20 minutes
* Future-state journey definition: 60-75 minutes
* Process, content, ownership, and data changes: 40-50 minutes
* Playback of concept, service changes, and open questions: 20-25 minutes

### What you must capture

* Future-state journey
* Experience principles
* Required service changes across process, content, ownership, and data
* Dependencies and open questions
* Parts of the concept that should move into the prototype

### Lean capture structure

Use the seeded `01-inputs/package_b_activity_3_1_input.md` file for this activity.

Capture only:

* the future-state direction that the group actually aligned on
* the service changes, dependencies, and prototype moments that need carrying forward

Short sequence:

1. Future-state direction and journey
2. Principles and service changes
3. Dependencies and prototype moments

### Validation checkpoint

The client should confirm:

* The future-state direction responds to the most important current-state problems
* The required service changes are visible and credible
* The concept is strong enough to move into prototype and prioritization work

## Activity 4.1: Clickable prototype, prioritization workshop, and delivery recommendation

### Objective

Make the concept tangible and turn it into a build-first recommendation.

### Estimated activity time

2 hours for the prioritization workshop, plus 1-2 days for prototype briefing, prompt generation, prototype production support, and recommendation packaging

### Prep before the session

* Confirm which parts of the future-state journey the prototype must show
* Confirm the opportunities or changes that need prioritization
* Confirm known effort signals, delivery constraints, and dependencies
* Confirm which design tool will be used first for the prototype

### Suggested session flow

* Prototype objective and scope playback: 20 minutes
* Review of key opportunities or concept elements: 30 minutes
* Prioritization against shared criteria: 45 minutes
* Playback of build-first, defer, and validate-next: 25 minutes

### What you must capture

* Prototype objective
* Core flow or moments the prototype must show
* Prioritization criteria
* Build-first recommendation
* Defer items
* Validate-next items
* Risks, dependencies, and sequencing implications

### Lean capture structure

Use the seeded `01-inputs/package_b_activity_4_1_input.md` file for this activity.

Capture only:

* the prototype scope and prioritization logic needed for the final recommendation
* the constraints, validation points, and tool choice needed for the prompt pack

Short sequence:

1. Decision and prototype objective
2. Prototype scope and interactions
3. Prioritization and sequencing
4. Risks, validation, and tool choice

### Validation checkpoint

The client should confirm:

* The prototype scope is tight enough to support a real decision
* The prioritization logic is credible
* The build-first recommendation is clear enough for the next phase

### Prototype production step

After the AI has produced the recommendation package and prototype prompt pack:

1. Use the canonical brief and the tool-specific prompt in the selected design tool.
2. Generate the first prototype draft.
3. Review the draft against the validated concept and the prototype review checklist in [prototype_prompt_pack_template.md](prototype_prompt_pack_template.md).
4. If screenshots or links from the client's current solution were provided, check that the draft stays close to the existing visual language unless the brief explicitly asks for change.
5. Refine the prompt if the prototype drifts away from the agreed direction.
6. Include the final clickable prototype alongside the recommendation package.

## Practical facilitation rules

* Keep the package tied to one journey or service area
* Treat evidence, research, journey work, concepting, and prioritization as connected steps
* Do not let prototype work reopen the validated concept from scratch
* Keep the language commercial and decision-oriented
* Only move forward when the previous output has been reviewed and accepted
