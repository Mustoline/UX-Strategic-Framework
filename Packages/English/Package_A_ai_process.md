# Package A AI process

## Purpose

Use this file to run Package A as a stage-gated AI workflow after the facilitator has completed each real-world activity.

This file is for the AI operating logic, not for client-facing facilitation.

Use it together with:

* [Package_A_core_activities.md](Package_A_core_activities.md) for the package summary
* [Package_A_facilitator_guide.md](Package_A_facilitator_guide.md) for the real-world workshop and review guidance
* [prototype_prompt_pack_template.md](prototype_prompt_pack_template.md) for the reusable prototype prompt structure

## Core operating rules

* Process one activity at a time
* Do not proceed to the next activity until the user has validated the current output
* If required input is missing, ask for the missing material instead of filling gaps with confident assumptions
* Distinguish clearly between supported findings, inference, and open assumption
* Treat unknown constraints as a risk to surface, not as proof that no constraints exist
* Keep the work bounded to one problem area, workflow, feature area, or journey step
* Keep the output commercially grounded and decision-oriented

## Validation states

The AI should treat validation in one of three states:

* **Validated:** The output is accepted and can be carried forward as confirmed input
* **Validated with changes:** The AI should update the output, then ask for final confirmation before moving on
* **Not validated:** The AI should stop and wait for more input or correction

Do not move to the next activity on implied approval. Wait for explicit confirmation from the user.

After a review file is updated with a validation decision, the AI should run `python3 Projects/sync_project_status.py --project-name "<Project name>"` in the same turn so the project control files stay aligned with the workflow state.

## Standard AI response pattern

After processing any Package A activity, the AI should return:

1. **Processed output for review**
2. **What is carried forward as confirmed input**
3. **What is still open or uncertain**
4. **What input is required for the next activity**
5. **A direct validation question**

## Lean input and sequence rules

Package A should default to the lightest input flow that still produces a decision-ready output.

That means:

* Carry forward validated context from earlier stages by default
* Do not re-ask for client, scope, decision, target users, constraints, or measures unless they changed, are missing, or are still contested
* Start each new activity by briefly restating the carried-forward context that matters for that activity
* Ask only for the minimum new input needed to support the current synthesis step
* Treat extra questions as optional follow-ups, not as mandatory default intake

When the user asks to run a stage or activity in chat:

* Use a short step-based sequence rather than a long field-by-field questionnaire
* Show visible progress in the main response using a format such as `Activity 1.2, step 2 of 3`
* Use 2-4 steps for most activities
* Each step can contain 1-3 tightly related questions
* If a later question depends on an earlier answer, restate that earlier answer inline before asking the follow-up

## Default guided sequence map for Package A

Use this as the default question-flow structure when a stage is being simulated or prepared in chat.

### Stage 0

Use 4 steps:

1. Client and problem area
2. Decision and why now
3. Evidence and stakeholders
4. Constraints and out-of-scope boundary

### Activity 1.1

Carry forward the Stage 0 context and use 4 steps:

1. Workshop setup and business question
2. Users and scope
3. Measures, baseline, and constraints
4. Disagreements and open sprint questions

### Activity 1.2

Carry forward the validated decision frame and use 3 steps:

1. Evidence sources and coverage
2. Strongest signals and supported findings
3. Assumptions, gaps, and next validation questions

### Activity 1.3

Carry forward the evidence implications and use 3 steps:

1. Step in scope, actors, and current actions
2. Touchpoints, systems, dependencies, and internal implications
3. Friction points, biggest breakdowns, and validation gaps

### Activity 2.1

Carry forward the breakdown map and use 4 steps:

1. Decision and options
2. Comparison criteria
3. Option notes and tradeoffs
4. Preferred direction, risks, and open checks

### Activity 3.1

Carry forward the preferred direction from Activity 2.1 and use 4 steps:

1. Recommendation lock and sponsor notes
2. Build now, defer, users, and success measures
3. Risks, validate next, and immediate next steps
4. Prototype scope, interactions, constraints, tool choice, and optional visual references

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
* If any internal command or tool text still leaks into the visible conversation, stop the one-question flow and switch to a single-message fallback capture mode for the remaining fields

## Final Package A output set

By the end of Package A, the AI-assisted workflow should support delivery of:

* A recommendation document
* A map of the key breakdowns in the selected journey step
* A 1-2 screen clickable prototype illustrating the recommended improvement
* A short list of risks and next steps

To make the prototype reliably producible, the final AI output should also include:

* A canonical prototype brief
* Fresh-generation prompts
* Refinement prompts
* A separate prototype record capturing the approved artifact, review notes, and approval status

The prompt pack is an enabling output. It helps create the clickable prototype, but it does not replace the prototype itself. Keep the main final deliverable, the prototype prompt pack, and the prototype record in separate files inside `04-final/`.

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
* Seed the prototype prompt-pack file in `04-final/`
* Seed the prototype record file in `04-final/`
* Record the original project name, normalized folder name, package type, working language, created date, and current status in the setup note
* Keep all later project-generated files inside this folder structure

### Project setup note format

Use this structure for `project_setup.md`:

```md
# Project setup

## Project name
[Text]

## Folder name
[Text]

## Package
Package A

## Working language
[English / Danish]

## Created date
[YYYY-MM-DD]

## Status
[Setup complete / Intake in progress / Active / On hold / Closed]

## Control center
project_index.md

## Storage rule
All project-generated files for this engagement are stored inside this project folder.
```

### Output format

Return:

* Confirmed project name
* Normalized folder name
* Project path
* Folder structure created
* Control center file created
* Recommended next step

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
* Problem area in scope
* Decision to support
* Why this matters now
* Known evidence
* Stakeholders or teams involved
* Known constraints
* Out-of-scope items

### Recommended dialogue sequence and wording

1. `Stage 0, step 1 of 4`
   Ask:
   * Who is the client, or what context should I keep in mind for this project?
   * What problem area should this package stay focused on?
   Example problem-area answer: Existing customers try to change their mobile subscription online, but many drop out during the plan comparison and eligibility step.
2. `Stage 0, step 2 of 4`
   Ask:
   * What specific decision do you want this package to help you make?
   * Why is this important to address now?
   Example decision answer: Should the client invest now in improving the self-service subscription change step, and if yes, what should move into delivery first?
   Example why-now answer: The step is creating avoidable support load, and the client needs a near-term go or no-go and scope decision before delivery starts.
3. `Stage 0, step 3 of 4`
   Ask:
   * What evidence do you already have today?
   * Which stakeholders or teams should we keep in view from the start?
   Example evidence answer: Portal analytics show 42% drop-off at the plan comparison and eligibility stage, especially on mobile devices.
   Example stakeholder answer: Digital product owner, call-center lead, analytics owner, and the team responsible for the change flow.
4. `Stage 0, step 4 of 4`
   Ask:
   * What important boundaries should we keep in mind, including both known constraints and anything that should stay out of scope?
   Example answer: The billing platform has a fixed release window and cannot be replaced in this release, and redesigning the full account portal should stay out of scope.

### What the AI should do

* Run the intake as a sequenced guided dialogue unless the user chooses to paste the full intake at once
* Check whether the sprint is bounded enough for Package A
* Identify missing intake inputs
* Flag unknown constraints as a risk if the user has not confirmed them
* Confirm whether the work can start with Activity 1.1

### Output format

Return:

* Intake summary
* Intake gaps or risks
* Recommended next step

### Validation gate

Only move to Activity 1.1 when the user confirms that the intake is good enough to begin.

## Activity-specific working rule

Use the seeded project input files and the Package A template library as the operating structure for each activity.

Keep the rhythm consistent:

1. Restate the carried-forward context briefly
2. Capture only the minimum new input needed for the activity
3. Synthesize into a review-ready output
4. Get explicit validation
5. Only then move on

For the concrete step-based input structures, use:

* [../../Projects/Templates/English/Package_A/package_a_template_library.md](../../Projects/Templates/English/Package_A/package_a_template_library.md)

## Package A activity focus

Keep the activity outputs lean and decision-oriented:

* Activity 1.1 should turn sponsor input into a clear decision frame
* Activity 1.2 should separate supported signals from assumptions
* Activity 1.3 should isolate the few breakdowns that matter most
* Activity 2.1 should compare directions and identify a preferred route
* Activity 3.1 should package the recommendation, prototype brief, and final build-now, defer, and validate-next split

## Prototype-sequence rule

When Activity 3.1 is validated:

* Write the main recommendation in `package_a_final_deliverable.md`
* Write the operational prototype prompt pack in `package_a_prototype_prompt_pack.md`
* Write the approved prototype flow, links, screenshots, and iteration notes in `package_a_prototype_record.md`
* Keep refinement prompts separate from fresh-generation prompts
* If the user provides screenshots or links to the existing client experience, the prompt pack should explicitly instruct visual alignment with the client's current design language
* If the user brings back a prototype draft from Figma Make or Google Stitch, compare it against the validated recommendation and refine the prompt pack only where the draft drifts from the agreed direction

## Stop or pause conditions

The AI should stop and ask for clarification if any of the following are true:

* The problem is too broad for Package A
* The step in scope is not clear
* The client has not validated the previous output
* The evidence is too weak to support a credible option comparison without stating that limitation
* Constraints are missing but treated as settled

## Completion condition

Package A is complete when:

* Activities 1.1 to 3.1 have each been processed in order
* Each activity output has been explicitly validated
* The final recommendation package is accepted as the basis for the next delivery or validation decision
* The prototype prompt pack is accepted as the basis for building the clickable prototype

If a clickable prototype is included in the agreed sprint output, the package should only be treated as fully complete once that prototype has also been reviewed against the validated brief and accepted.
