# AGENTS.md

## Project type

This is a strategy project, not a software delivery project. The work in this repository is about shaping, packaging, and strengthening a strategic UX and service design offer that can be sold upstream as part of a discovery phase.

## Project purpose

The core objective is to position UX, design thinking, and service design as a business-facing decision phase that helps clients:

* Define the right problem before delivery starts
* Reduce delivery risk and avoid avoidable rework
* Improve prioritization and investment decisions
* Expose the service, operational, and organizational changes required behind the interface

The emphasis should stay on business value, decision support, and practical next steps rather than on design activity for its own sake.

## Core documents

The repository is now split first by document purpose and then by language.

Primary English source documents:

* **`Packages/English/strategic_ux_packages.md`**: Main package overview covering the value proposition, package structure, core activities, concrete outcomes, and package selection logic
* **`Sales materials/English/upstream_discovery_positioning.md`**: Positioning document explaining who buys the offer, when it becomes relevant, and why it belongs upstream in a project
* **`Sales materials/English/discovery_sales_playbook.md`**: Sales-facing guide covering qualification, objections, proposal language, and discovery-to-delivery handoff
* **`Sales materials/English/executive_offer_one_pager.md`**: Compressed executive-facing version of the discovery offer for quick commercial conversations
* **`Sales materials/English/discovery_phase_proposal_template.md`**: Reusable proposal structure for turning the package logic into client-ready proposals
* **`Packages/English/Package_A_core_activities.md`**: Summary execution plan for the discovery sprint package
* **`Packages/English/Package_B_core_activities.md`**: Summary execution plan for the service concept definition package
* **`Packages/English/Package_C_core_activities.md`**: Summary execution plan for the strategic service redesign package

Matching Danish documents live in:

* **`Packages/Danish/`**
* **`Sales materials/Danish/`**

Project-specific work should be stored in:

* **`Projects/`** for real package engagements and dry runs

## Working principles

When producing or revising materials in this repository:

* Treat every output as a client-facing strategy artifact unless clearly noted otherwise
* Keep the tone direct, commercially grounded, and suited to a Danish business audience
* Anchor recommendations in business value, risk reduction, prioritization, and delivery consequences
* Use a design thinking and service design lens, not a narrow interface-design lens
* Make activities concrete by stating method, format, duration, participant type, and purpose
* Make outcomes concrete by stating the deliverable, what it contains, and what decision or next step it supports
* Avoid vague labels and consultant shorthand when a more specific description is possible
* Keep terminology aligned across the package overview and the detailed package files

## Project storage rule

When a real client project is started through this tool:

* Ask the user for the project name before any project artifact is created
* Normalize that name into a folder-safe format by replacing spaces with hyphens and removing unsafe special characters while keeping the name readable
* Create a dedicated project folder under `Projects/<Project-Name>/`
* Use this standard structure:
  * `Projects/<Project-Name>/00-project-setup/`
  * `Projects/<Project-Name>/00-project-setup/shared-prep/`
  * `Projects/<Project-Name>/01-inputs/`
  * `Projects/<Project-Name>/02-working/`
  * `Projects/<Project-Name>/03-reviews/`
  * `Projects/<Project-Name>/04-final/`
* Create `Projects/<Project-Name>/project_index.md` as the project control center
* Create `Projects/<Project-Name>/00-project-setup/project_setup.md` when the project starts
* Seed the relevant intake, activity-input, activity-output, review, and final-deliverable files automatically when the project starts instead of asking the user to copy template files manually
* Seed the relevant shared prep assets in `Projects/<Project-Name>/00-project-setup/shared-prep/` automatically when the project starts
* Seed a package-specific ready-to-edit draft for the first live activity in `Projects/<Project-Name>/00-project-setup/shared-prep/` automatically when the project starts
* Refresh the generated `next_activity_*.md` prep files in `Projects/<Project-Name>/00-project-setup/shared-prep/` automatically after each review sync
* When the package includes prototype work, separate the final outputs in `04-final/` so the main final deliverable, the prototype prompt pack, and the prototype record can live in different files
* Store all project-generated files inside that project folder rather than in the shared source-document folders
* After a review file is updated with a validation decision, run `python3 Projects/sync_project_status.py --project-name "<Project name>"` in the same turn so `project_setup.md` and `project_index.md` stay aligned with the current workflow state
* Use `--resume`, `--on-hold`, or `--close` with that command when the project state changes alongside the stage validation
* Do this automatically as part of handling the project workflow rather than asking the user to remember or run the command

When collecting the first Stage 0 intake for a new project:

* Run the intake as a sequenced dialogue by default rather than asking the user to send the full intake block in one message
* Ask one step at a time rather than one isolated field at a time
* Keep each step short and focused, usually 1-3 closely related questions
* Show progress in the main response using a format such as `Stage 0, step 2 of 4`
* Phrase each question as natural guided dialogue rather than as a raw field label
* Prefer plain prompts such as `What problem area should this package stay focused on?` over just repeating the section name
* For every question after `Client / context`, provide one short illustrative example
* Prefer examples drawn from the internal dry runs and make clear that the example is illustrative rather than expected
* If the user prefers to paste several answers at once, accept that and continue from the next missing field

## Sequence design rule

When running Stage 0 or simulating a live package activity inside the tool:

* Default to a short step-based sequence, not a long questionnaire and not one field per message
* Use 2-4 steps for most activities
* Each step may contain 1-3 tightly related questions in a single message
* Treat validated context from earlier stages as carried forward by default
* Only ask again about client, scope, decision, target users, constraints, or measures if they are missing, changed, or still contested
* When context is being carried forward, say so explicitly and ask only for updates, corrections, or the genuinely new input needed for the current step
* Prefer a `core path` with the minimum new input needed to synthesize the next output
* Ask optional follow-up questions only if the core path leaves a real gap
* Keep the visible sequence feeling more like a checkout flow than a workshop form

## Live activity handoff rule

When a live project stage is validated and the next step is a real-world activity such as a workshop, interview, evidence review, or mapping session:

* Do not immediately start asking for the activity input as if the real-world session has already happened
* Make it explicit that the next step is a real-world activity that the user or facilitator now needs to run
* State the activity name, purpose, estimated time, and the key people, evidence, or materials needed
* Link to the seeded project input file in `01-inputs/`
* Link to the matching facilitator guide and any relevant template, question guide, or tool file needed to run the activity
* Ask the user to return with the completed notes or say if they want help preparing the activity
* Only run the next activity as an in-chat question sequence if the user explicitly asks to simulate or prepare it inside the tool
* Use the canonical structure in `Projects/Templates/English/Shared/live_activity_handoff_message_template.md` or `Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md`

Use this exact section order in the main user-visible response:

1. `Next live activity`
2. `Why this step now`
3. `Estimated time`
4. `Who should be involved`
5. `What to prepare or gather`
6. `Files to use`
7. `Come back with`
8. `Optional support`

Before a real-world activity is run, use `Projects/Templates/English/Shared/activity_readiness_checklist.md` or `Projects/Templates/Danish/Shared/activity_readiness_checklist_danish.md` when a readiness check would help reduce avoidable confusion or missing prep.

When an activity depends on evidence, access, exports, or supporting material from the client team, use `Projects/Templates/English/Shared/evidence_request_template.md` or `Projects/Templates/Danish/Shared/evidence_request_template_danish.md` instead of drafting the request from scratch.

When preparing a live workshop, interview, contextual session, or validation session, use the shared prep assets instead of drafting from scratch:

* `Projects/Templates/English/Shared/workshop_invite_template.md`
* `Projects/Templates/English/Shared/interview_invite_and_consent_template.md`
* `Projects/Templates/English/Shared/session_brief_template.md`
* `Projects/Templates/Danish/Shared/workshop_invite_template_danish.md`
* `Projects/Templates/Danish/Shared/interview_invite_and_consent_template_danish.md`
* `Projects/Templates/Danish/Shared/session_brief_template_danish.md`

After a pilot, dry run, or full package test, use `Projects/Templates/English/Shared/pilot_retrospective_template.md` or `Projects/Templates/Danish/Shared/pilot_retrospective_template_danish.md` to capture friction, strengths, and concrete next improvements.

## Question visibility rule

Because commentary updates may be collapsed in the interface:

* Never place the actual user-facing question only in `commentary`
* Never place the validation question only in `commentary`
* Never place the required-input prompt only in `commentary`
* Never place any part of the live-activity handoff structure only in `commentary`
* Use `commentary` for progress updates only
* Put the actual question or next-step prompt in the main user-visible response so it stays visible

## Live question-flow safety rule

When the user explicitly asks to simulate a live activity or when a stage intake is being run as a one-question-at-a-time dialogue:

* Treat the full question sequence as a temporary capture mode
* Once the live question sequence starts, switch to chat-only simulation mode until the sequence is complete
* In chat-only simulation mode, do not run file reads, file writes, sync commands, or any other tool actions at all during the active question sequence
* Keep the captured answers in working memory until the full question sequence is complete
* Only write the project files after the last question has been answered, when the user explicitly asks to save mid-flow, or when the stage reaches a validation checkpoint
* Do not let any raw command text, tool call text, or file-action narration appear inside the live question sequence
* Do not use commentary during the active question sequence unless there is a real blocker that must be surfaced
* After the full sequence is complete, write the relevant project files, then present the processed output for validation in the main user-visible response
* During the active sequence, never call tools just to read back project files or confirm the current working directory
* Default to waiting for an explicit `save and synthesize` style signal if the sequence is long or if platform behavior has already looked unstable

## Prior-answer recap rule

When a question depends on a previous answer the user already gave in the same intake or simulation flow:

* Restate the relevant earlier answer directly in the new question
* Do not assume the user will scroll back to find the earlier answer
* Use short recap phrasing such as `Your current Option A is: ...`
* Apply this especially when asking follow-up questions about options, criteria, chosen directions, constraints, or any earlier named concept

## Simulation fallback rule

If any raw command text, tool-call text, or other internal action leaks into the visible conversation during a simulated intake or activity:

* Treat that leak as a workflow blocker for the one-question-at-a-time format
* Stop the live question sequence immediately
* Do not continue in the same one-step mode if the interface is clearly unstable
* Switch first to a grouped-step fallback mode instead of immediately dumping the whole rest of the activity
* In grouped-step fallback mode, show a short recap of what has already been captured
* Then ask for the remaining questions for the current step or the next logical step in one grouped reply
* Keep the same visible progress format, for example `Activity 2.1, step 3 of 4`
* Only if the grouped-step fallback also feels unstable should you switch to a single-message fallback for the remaining activity
* After the user replies, save and synthesize in one pass
* Name the issue explicitly as a platform or workflow limitation rather than pretending it has been solved
* Capture the incident as pilot feedback if the project is being used as a live workflow test

Do not store live project artifacts inside `Packages/`, `Sales materials/`, or `skills/`. Those folders are for reusable source material.

## Package maintenance rule

If a package is updated in `Packages/English/strategic_ux_packages.md`, the associated English and Danish package files must be updated to use the same logic, naming, and language pattern:

* `Packages/English/Package_A_core_activities.md`
* `Packages/English/Package_B_core_activities.md`
* `Packages/English/Package_C_core_activities.md`
* `Packages/Danish/Package_A_core_activities_danish.md`
* `Packages/Danish/Package_B_core_activities_danish.md`
* `Packages/Danish/Package_C_core_activities_danish.md`

Where relevant, the matching facilitator and AI-process files should also be kept in sync.

The summary and detailed versions should read as one consistent offer, not as separate drafts.

## Review standard

All new or revised client-facing materials should be reviewed against the `ux-strategy-reviewer` criteria:

* Danish-pragmatic tone
* Clear ROI, risk, or waste-reduction logic
* Removal of vague buzzwords and unnecessary hype
* Tool-agnostic wording
* Clear markdown structure
* Complete package logic covering activities, timeline, outcomes, and client involvement

## Definition of done

A strategy document in this repository should be considered ready when it:

* Explains the business value in plain language
* Differentiates the offer tiers clearly
* Describes the work in concrete terms
* Produces tangible deliverables a client can recognize and buy
* Supports a clear next decision, investment choice, or delivery step
