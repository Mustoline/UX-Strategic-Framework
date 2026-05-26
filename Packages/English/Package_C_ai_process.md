# Package C AI process

## Purpose

Use this file to run Package C as a stage-gated AI workflow after the facilitator has completed each real-world activity.

This file is for the AI operating logic, not for client-facing facilitation.

Use it together with:

* [Package_C_core_activities.md](Package_C_core_activities.md) for the package summary
* [Package_C_facilitator_guide.md](Package_C_facilitator_guide.md) for the real-world workshop and review guidance
* [prototype_prompt_pack_template.md](prototype_prompt_pack_template.md) when one selected high-risk journey slice needs optional prototype support

## Core operating rules

* Process one activity at a time
* Do not proceed to the next activity until the user has validated the current output
* If required input is missing, ask for the missing material instead of filling gaps with confident assumptions
* Distinguish clearly between supported findings, inference, and open assumption
* Treat unknown constraints as a risk to surface, not as proof that no constraints exist
* Keep the work bounded to the agreed service scope
* Keep the output commercially grounded and decision-oriented

## Validation states

The AI should treat validation in one of three states:

* **Validated:** The output is accepted and can be carried forward as confirmed input
* **Validated with changes:** The AI should update the output, then ask for final confirmation before moving on
* **Not validated:** The AI should stop and wait for more input or correction

Do not move to the next activity on implied approval. Wait for explicit confirmation from the user.

After a review file is updated with a validation decision, the AI should run `python3 Projects/sync_project_status.py --project-name "<Project name>"` in the same turn so the project control files stay aligned with the workflow state.

## Standard AI response pattern

After processing any Package C activity, the AI should return:

1. **Processed output for review**
2. **What is carried forward as confirmed input**
3. **What is still open or uncertain**
4. **What input is required for the next activity**
5. **A direct validation question**

## Lean input and sequence rules

Package C should default to the lightest input flow that still produces a strategic and decision-ready output.

That means:

* Carry forward validated context from earlier stages by default
* Do not re-ask for client, service scope, strategic decisions, stakeholders, or known constraints unless they changed, are missing, or are still contested
* Start each new activity by briefly restating the carried-forward context that matters for that activity
* Ask only for the minimum new input needed to support the current synthesis step
* Treat extra questions as optional follow-ups, not as mandatory default intake

When the user asks to run a stage or activity in chat:

* Use a short step-based sequence rather than a long field-by-field questionnaire
* Show visible progress in the main response using a format such as `Activity 2.1, step 2 of 3`
* Use 3-4 steps for most activities
* Each step can contain 1-3 tightly related questions
* If a later question depends on an earlier answer, restate that earlier answer inline before asking the follow-up

## Default guided sequence map for Package C

Use this as the default question-flow structure when a stage is being simulated or prepared in chat.

### Stage 0

Use 4 steps:

1. Client and service in scope
2. Strategic decisions and why now
3. Evidence and stakeholders
4. Boundaries

### Activity 1.1

Carry forward the Stage 0 context and use 3 steps:

1. Interviews and strategic framing
2. Service pressures and consequences
3. Tensions and investment questions

### Activity 1.2

Carry forward the strategic framing and use 3 steps:

1. Strategic question and service scope
2. Departments, channels, and systems
3. Critical moments and fieldwork focus

### Activity 2.1

Carry forward the agreed scope and use 3 steps:

1. Observation coverage
2. Operational friction and hidden effort
3. Breakdowns and blueprinting questions

### Activity 2.2

Carry forward the operational observation summary and use 3 steps:

1. Blueprint structure
2. Delays, duplication, and hotspots
3. Implications and carry-forward logic

### Activity 3.1

Carry forward the current-state implications and use 4 steps:

1. Future-state direction
2. Change model
3. Validation and refinement
4. Optional prototype slice

### Activity 4.1

Carry forward the future-state model and use 4 steps:

1. Strategic sequencing
2. Dependencies and change implications
3. Value logic and risk
4. Optional prototype support

## Real-world activity handoff and visibility rule

When the next step is a workshop, interview, evidence review, mapping session, or another real-world activity:

* Stop after validation and make it explicit that the next step happens in the real world before AI synthesis can continue
* Do not immediately start asking the activity capture questions as if the session has already been run
* Provide links to the relevant facilitator guide, the seeded project input file in `01-inputs/`, and any relevant template, question guide, or tool file
* Summarize the activity purpose, estimated time, and who should attend or what material should be gathered
* Ask the user to return with the completed activity notes or say if they want help preparing the activity
* Only run the next activity as an in-chat question sequence if the user explicitly asks to simulate or prepare it inside the tool
* Use the exact section order in [../../Projects/Templates/English/Shared/live_activity_handoff_message_template.md](../../Projects/Templates/English/Shared/live_activity_handoff_message_template.md)

Because commentary updates may be collapsed in the interface:

* Keep progress updates in commentary only
* Put the actual user-facing question, validation question, or next-step request in the main user-visible response
* Put the full live-activity handoff structure in the main user-visible response
* During a simulated live activity question sequence, switch to chat-only simulation mode
* In chat-only simulation mode, do not run file reads, file writes, sync commands, or any other tool actions during the active question flow
* Hold the notes in working memory until the sequence is complete, then write the project files and return the processed output for validation
* Do not let raw command text, tool call text, or file-action narration appear in the visible question flow
* When a follow-up question refers to an earlier user answer, restate that earlier answer in the question so the user does not need to scroll back
* If any internal command or tool text still leaks into the visible conversation, stop the one-question flow and switch to a grouped fallback capture mode for the remaining fields

## Final Package C output set

By the end of Package C, the AI-assisted workflow should support delivery of:

* An executive brief
* A current-state service blueprint
* A tested future-state service model
* A phased roadmap across teams and systems
* A change and business case summary

Where the validated future-state service model needs a more tangible test artifact, the final AI output may also include:

* A canonical prototype brief for one selected high-risk journey slice
* Fresh-generation prompts
* Refinement prompts
* A separate prototype record for that selected slice

That prompt pack is optional support. It should only be used for one selected high-risk journey slice and should not replace the core Package C deliverables. If prototype support is used, keep the main final deliverable, the prototype prompt pack, and the prototype record in separate files inside `04-final/`.

## Stage -1: Project setup before intake

### Input required from the user

The user should provide:

* Project name
* Confirmation to reuse the existing folder if the normalized project folder already exists

### What the AI should do

* Ask for the project name before processing intake or creating project artifacts
* Normalize the project name into a folder-safe format
* Check whether `../../Projects/<Project-Name>/` already exists
* If it exists, stop and ask whether to reuse it or choose a different project name
* If it does not exist, create `../../Projects/<Project-Name>/00-project-setup/`
* Create `../../Projects/<Project-Name>/01-inputs/`
* Create `../../Projects/<Project-Name>/02-working/`
* Create `../../Projects/<Project-Name>/03-reviews/`
* Create `../../Projects/<Project-Name>/04-final/`
* Create `../../Projects/<Project-Name>/project_index.md` as the project control center
* Create `../../Projects/<Project-Name>/00-project-setup/project_setup.md`
* Seed the relevant Stage 0 and activity-input files in `01-inputs/`
* Seed the relevant activity-output files in `02-working/`
* Seed the relevant stage-review files in `03-reviews/`
* Seed the main final-deliverable file in `04-final/`
* Seed the optional prototype prompt-pack file in `04-final/`
* Seed the optional prototype record file in `04-final/`
* Record the original project name, normalized folder name, package type, working language, created date, and current status in the setup note
* Keep all later project-generated files inside this folder structure

### Validation gate

Only move to Stage 0 when the user confirms that the project setup is correct.

## Stage 0: Intake check before Activity 1.1

### Intake dialogue rule

By default, the AI should run Stage 0 as a guided intake dialogue rather than asking the user to send the full intake list in one message.

The AI should:

* Ask one short step at a time instead of one isolated field at a time
* Use the visible progress format `Stage 0, step X of 4`
* Keep each step focused on 1-3 closely related questions
* Wait for the answer before moving to the next step
* Phrase each question in natural conversational language rather than as a bare field label
* Give one short illustrative example for every question except `Client / context`
* Make clear that each example is illustrative, not the expected answer
* Accept pasted multi-field input if the user prefers that format and then continue from the next missing field
* Summarize the completed intake back to the user for validation before Activity 1.1

### Input required from the user

The user should provide:

* Client or context
* Service, proposition, or initiative in scope
* Strategic or investment decisions to support
* Why this matters now
* Known evidence
* Stakeholders or teams involved
* Known constraints
* Out-of-scope areas

### Recommended dialogue sequence and wording

1. `Stage 0, step 1 of 4`
   Ask:
   * Who is the client, or what context should I keep in mind for this project?
   * Which service, proposition, or initiative should this package focus on?
   Example scope answer: Customers moving into or out of a home face a fragmented move-home service spread across website forms, the contact center, billing, CRM, and operational teams.
2. `Stage 0, step 2 of 4`
   Ask:
   * Which strategic or investment decisions should this package help support?
   * Why is this important to address now?
   Example decision answer: Should the utility invest in a broader move-home service redesign, and if yes, how should the work be sequenced across digital channels, operations, billing, and ownership?
   Example why-now answer: Billing corrections, delayed confirmations, and avoidable complaints are rising at a moment when churn risk is high.
3. `Stage 0, step 3 of 4`
   Ask:
   * What evidence do you already have today?
   * Which stakeholders or teams need to be part of this from the start?
   Example evidence answer: Contact-center pressure, billing corrections, move-date disputes, and complaint themes all indicate a fragmented end-to-end service.
   Example stakeholder answer: Digital product, contact center, billing operations, CRM, meter-data, and the operational back office.
4. `Stage 0, step 4 of 4`
   Ask:
   * What important boundaries should we keep in mind, including both known constraints and anything that should stay out of scope?
   Example answer: The package needs to frame sequencing and ownership change without assuming a full platform replacement upfront, and commercial-property move cases and long-term tariff redesign should stay out of scope.

### Validation gate

Only move to Activity 1.1 when the user confirms that the intake is good enough to begin.

## Activity-specific working rule

Use the seeded project input files and the Package C template library as the operating structure for each activity.

Keep the rhythm consistent:

1. Restate the carried-forward context briefly
2. Capture only the minimum new input needed for the activity
3. Synthesize into a review-ready output
4. Get explicit validation
5. Only then move on

For the concrete step-based input structures, use:

* [../../Projects/Templates/English/Package_C/package_c_template_library.md](../../Projects/Templates/English/Package_C/package_c_template_library.md)

## Optional prototype-support rule

When Activity 3.1 or Activity 4.1 identifies one selected high-risk journey slice that needs tangible prototype support:

* Keep the strategic main deliverable in `package_c_final_deliverable.md`
* Keep the optional prototype prompts in `package_c_prototype_prompt_pack.md`
* Keep the optional slice-specific artifact record, screenshots, links, and iteration notes in `package_c_prototype_record.md`
* Keep refinement prompts separate from fresh-generation prompts
* If the user provides screenshots or links to the current client experience, the prompt pack should explicitly instruct visual alignment with that existing design language
