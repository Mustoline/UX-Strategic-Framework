# Package C facilitator guide

## Purpose

Use this guide to prepare and run the real-world Package C activities with the client.

The goal is to make sure you collect the right material, in the right sequence, so the AI can process each activity cleanly and turn it into a validated output before the next step begins.

Use this guide together with:

* [Package_C_core_activities.md](Package_C_core_activities.md) for the package summary
* [Package_C_ai_process.md](Package_C_ai_process.md) for the AI handoff and stage-gated workflow
* [prototype_prompt_pack_template.md](prototype_prompt_pack_template.md) if one selected high-risk journey slice needs a supporting prototype

## Shared live-delivery prep assets

Use these shared files when you need to prepare the real-world session itself:

* [../../Projects/Templates/English/Shared/workshop_invite_template.md](../../Projects/Templates/English/Shared/workshop_invite_template.md)
* [../../Projects/Templates/English/Shared/interview_invite_and_consent_template.md](../../Projects/Templates/English/Shared/interview_invite_and_consent_template.md)
* [../../Projects/Templates/English/Shared/session_brief_template.md](../../Projects/Templates/English/Shared/session_brief_template.md)

## How the workflow should run

1. Use this guide to prepare and run one Package C activity with the client.
2. Capture the required notes in the seeded project input file for that activity.
3. Bring that input into the AI process.
4. Review the processed output with the client and confirm any changes.
5. Only then move to the next activity.

Do not move ahead if the previous output is not yet accepted. The value of Package C depends on each step being grounded in validated input.

## Lean capture rule

Package C should feel structured, but not bureaucratic.

Use these rules while facilitating:

* Start each activity from the validated output of the previous stage
* Treat confirmed service scope, strategic decision frame, stakeholder picture, and known constraints as carried-forward context unless the client explicitly changes them
* Capture only the genuinely new input needed for the current activity
* If a point only needs confirmation, confirm it quickly instead of re-documenting it in full
* Keep the live activity focused on the next strategic decision, not on rebuilding earlier notes

When the activity is later simulated in chat, the AI should mirror the same logic by using a short step-based sequence and asking only for the minimum new input needed.

Use the seeded project input file in `01-inputs/` and [../../Projects/Templates/English/Package_C/package_c_template_library.md](../../Projects/Templates/English/Package_C/package_c_template_library.md) as the source of truth for the exact step-based handoff structure. The short lean capture structures later in this guide only summarize the sequence for each activity and should not be expanded back into full duplicate templates.

## AI handoff into the next live activity

When the previous stage has been validated and the next step is a real-world activity:

* The AI should explicitly say that the next step is now a live activity
* The AI should link to the seeded project input file for that activity
* The AI should link to the relevant part of this facilitator guide and any relevant template, question guide, or tool file
* The AI should summarize the objective, estimated time, and who should attend or what material should be gathered
* The AI should wait for the completed activity notes before resuming synthesis unless the user explicitly asks to simulate or prepare the activity in chat
* The AI should use the canonical handoff structure in [../../Projects/Templates/English/Shared/live_activity_handoff_message_template.md](../../Projects/Templates/English/Shared/live_activity_handoff_message_template.md)

## Final deliverables to leave the package with

By the end of Package C, you should be able to deliver:

* An executive brief
* A current-state service blueprint
* A tested future-state service model
* A phased roadmap across teams and systems
* A change and business case summary

Where the future-state service model needs a more tangible validation aid, the final synthesis may also generate:

* A prototype prompt pack file for one selected high-risk journey slice, containing:
  * A canonical prototype brief
  * Fresh-generation prompts
  * Refinement prompts
* A separate prototype record file for that selected slice, capturing approved screenshots, the prototype link, iteration notes, and approval status

This prototype prompt pack is optional support for the tested service model. It should only be used for one selected high-risk journey slice and should not replace the core Package C deliverables.

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
* Seed the optional prototype prompt-pack file in `04-final/`
* Seed the optional prototype record file in `04-final/`
* Record the original project name, folder name, package type, working language, created date, and current status in the setup note
* If the folder already exists, stop and confirm whether it should be reused before storing any files
* Store raw client inputs in `01-inputs/`, in-progress synthesis in `02-working/`, review versions in `03-reviews/`, and approved outputs in `04-final/`

## Before the package starts

### Minimum intake checklist

Collect this before Activity 1.1:

* The service, proposition, or cross-functional initiative in scope
* The strategic and investment decisions the package needs to support
* Why this matters now in business and service terms
* The evidence already available and who owns it
* The executive, service-owner, operational, and frontline participants needed
* The known constraints, assumptions, and out-of-scope areas

### Pre-package preparation checklist

Before running the first activity:

* Confirm the sponsor and the named owner who can validate outputs
* Confirm who must take part in executive interviews, ecosystem mapping, fieldwork, validation, and roadmap work
* Request service, support, operational, and analytics material early
* Confirm what permissions or confidentiality limits affect fieldwork
* Book the live sessions and review points in sequence
* Tell the client that each activity ends with a review checkpoint before the next step starts

## Activity 1.1: Executive and service-owner interviews

### Objective

Clarify the business case, strategic priorities, service pressures, and investment questions that should shape the redesign.

### Estimated activity time

1-2 days across 5-7 interviews of 45-60 minutes each, plus first synthesis

### Who should be interviewed

* Senior sponsors
* Service owners
* Leaders responsible for operations, channels, or core systems

### Prep before interviews

* Confirm which decisions or investments the package must inform
* Prepare an interview guide around service pressure, business consequences, and investment questions
* Collect any strategy, operating-model, or performance material already available

### What you must capture

* Strategic priorities
* Service pressures and failure points
* Business and operational consequences
* Risks and tensions
* Investment questions
* Areas of stakeholder alignment and conflict

### Lean capture structure

Use the seeded `01-inputs/package_c_activity_1_1_input.md` file for this activity.

Capture only:

* the strategic framing that emerged from the interviews
* the pressures, consequences, and investment questions that matter next

Short sequence:

1. Interviews and strategic framing
2. Service pressures and consequences
3. Tensions and investment questions

### Validation checkpoint

The client should confirm:

* The strategic framing reflects the real service problem
* The main investment questions are visible
* The rest of the package is focused on the right strategic tensions

## Activity 1.2: Ecosystem workshop and service scope

### Objective

Agree the service scope across departments, touchpoints, systems, and operational actors.

### Estimated activity time

Half day

### Who should attend

* Senior sponsors
* Service owners
* Operational stakeholders
* People who understand channels, systems, dependencies, and handoffs

### Suggested workshop flow

* Strategic playback and objective: 20 minutes
* Departments, touchpoints, systems, and actors: 60 minutes
* Critical service moments and scope boundary: 60 minutes
* Playback of service scope and fieldwork focus: 30 minutes

### What you must capture

* Service scope
* Departments and operational actors
* Channels and touchpoints
* Systems and dependencies
* Critical service moments
* In-scope and out-of-scope areas

### Lean capture structure

Use the seeded `01-inputs/package_c_activity_1_2_input.md` file for this activity.

Capture only:

* the service boundary the group actually agreed
* the actors, dependencies, and critical moments needed to guide fieldwork

Short sequence:

1. Strategic question and service scope
2. Departments, channels, and systems
3. Critical moments and fieldwork focus

### Validation checkpoint

The client should confirm:

* The service boundary is clear enough to guide fieldwork
* The critical service moments are the right ones to study
* The package has not expanded beyond the agreed service scope

## Activity 2.1: Contextual fieldwork and data review

### Objective

Study how the service works in practice and reveal workarounds, delays, hidden effort, and ownership gaps.

### Estimated activity time

3-5 days across 5-8 sessions of 60-90 minutes each, plus evidence review and first synthesis

### Evidence and access to request

* Operational data and service performance signals
* Support patterns and case types
* Analytics or service volume data
* Access to relevant users, customers, frontline teams, or internal roles
* Permission for observation or shadowing where possible

Use [../../Projects/Templates/English/Shared/evidence_request_template.md](../../Projects/Templates/English/Shared/evidence_request_template.md) if you need to request this evidence or access from the client team in a structured way.

### How to run this step

* Focus on what happens in practice, not only what process owners say should happen
* Capture cross-channel movement, delays, rework, escalation, and hidden supporting work
* Distinguish direct observation from inference

### What you must capture

* Service moments observed
* Workarounds
* Delays and hidden effort
* Ownership gaps
* Breakdowns across teams, systems, and channels
* Questions for blueprinting

### Lean capture structure

Use the seeded `01-inputs/package_c_activity_2_1_input.md` file for this activity.

Capture only:

* the operational evidence and observations that really change the picture
* the breakdowns and blueprinting questions that need carrying forward

Short sequence:

1. Observation coverage
2. Operational friction and hidden effort
3. Breakdowns and blueprinting questions

### Validation checkpoint

The client should confirm:

* The fieldwork reflects how the service really behaves
* The main breakdown patterns are visible
* The blueprinting step has enough evidence to move forward

## Activity 2.2: Current-state service blueprint

### Objective

Create a current-state service blueprint that exposes delay, duplication, cost, and ownership gaps across front-stage and back-stage delivery.

### Estimated activity time

1-2 days of blueprinting and synthesis, plus a 60-90 minute stakeholder review checkpoint

### What you must capture

* Front-stage interactions
* Back-stage processes
* Systems and dependencies
* Delays and duplication
* Ownership gaps
* Cost, effort, or lost-value hotspots

### Lean capture structure

Use the seeded `01-inputs/package_c_activity_2_2_input.md` file for this activity.

Capture only:

* the blueprint structure that must be visible
* the hotspots and implications that matter to future-state work

Short sequence:

1. Blueprint structure
2. Delays, duplication, and hotspots
3. Implications and carry-forward logic

### Validation checkpoint

The client should confirm:

* The blueprint reflects current service reality
* The main hotspots are the right ones for the future-state work to tackle
* The operating-model implications are visible enough for the next step

## Activity 3.1: Future-state service model workshop and concept validation

### Objective

Define a future-state service model and validate whether it holds up with the people who need to live with it.

### Estimated activity time

Half-day workshop plus 1-2 days for validation sessions, synthesis, and refinement

### Who should attend

* Cross-functional stakeholders who shape the future service model
* Validation participants who can expose real friction, adoption risk, or feasibility issues

### Prep before the workshop

* Bring the validated current-state blueprint and hotspots
* Confirm which breakdowns the future-state model must address first
* Confirm who should take part in validation

### What you must capture

* Target-state service logic
* Main changes across channels, teams, systems, and ownership
* Validation feedback
* Feasibility signals
* Refinements made after validation
* Open questions for roadmap and business-case work

### Lean capture structure

Use the seeded `01-inputs/package_c_activity_3_1_input.md` file for this activity.

Capture only:

* the future-state direction that survived validation
* the refinement points and any selected high-risk slice that need carrying forward

Short sequence:

1. Future-state direction
2. Change model
3. Validation and refinement
4. Optional prototype slice

### Validation checkpoint

The client should confirm:

* The future-state model addresses the right current-state problems
* The model has been tested enough to support roadmap work
* If a high-risk journey slice needs a prototype, the slice is clearly selected and bounded

## Activity 4.1: Roadmap and business case session

### Objective

Turn the validated future-state service model into a phased roadmap, a change implication summary, and a credible ROI hypothesis.

### Estimated activity time

Half-day session plus 4-6 hours of synthesis and packaging

### Prep before the session

* Bring the validated future-state service model
* Confirm the strategic or investment decision this step must support
* Confirm which dependencies, non-negotiables, and value areas matter most

### What you must capture

* What should happen now, next, and later
* Dependencies and decision points
* Operating-model, governance, and ownership changes
* ROI hypothesis or value logic
* Risks and assumptions that still matter

### Lean capture structure

Use the seeded `01-inputs/package_c_activity_4_1_input.md` file for this activity.

Capture only:

* the sequencing, change implications, and value logic leadership needs
* the optional prototype support details only if one selected high-risk slice still needs them

Short sequence:

1. Strategic sequencing
2. Dependencies and change implications
3. Value logic and risk
4. Optional prototype support

### Validation checkpoint

The client should confirm:

* The roadmap is practical enough to guide next steps
* The change implications are visible enough for leadership discussion
* The ROI hypothesis is credible enough for this stage

### Optional prototype production step

Only use this if the validated future-state service model needs a more tangible validation aid for one selected high-risk journey slice.

After the AI has produced the service-model package and optional prototype prompt pack:

1. Use the canonical brief and the tool-specific prompt in the selected design tool.
2. Generate the prototype only for the selected high-risk journey slice.
3. Review the draft against the validated future-state model and the prototype review checklist in [prototype_prompt_pack_template.md](prototype_prompt_pack_template.md).
4. If screenshots or links from the client's current solution were provided, check that the draft stays close to the existing visual language unless the brief explicitly asks for change.
5. Refine the prompt if the prototype drifts away from the agreed service direction.

## Practical facilitation rules

* Keep the package tied to a real cross-functional service problem
* Preserve strategic and operational tension rather than smoothing it away
* Keep the current-state and future-state work anchored in evidence
* Do not let optional prototype support take over the service-model and roadmap work
* Only move forward when the previous output has been reviewed and accepted
