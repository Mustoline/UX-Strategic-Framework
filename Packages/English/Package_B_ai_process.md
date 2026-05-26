# Package B AI process

## Purpose

Use this file to run Package B as a stage-gated AI workflow after the facilitator has completed each real-world activity.

This file is for the AI operating logic, not for client-facing facilitation.

Use it together with:

* [Package_B_core_activities.md](Package_B_core_activities.md) for the package summary
* [Package_B_facilitator_guide.md](Package_B_facilitator_guide.md) for the real-world workshop and review guidance
* [prototype_prompt_pack_template.md](prototype_prompt_pack_template.md) for the reusable prototype prompt structure

## Core operating rules

* Process one activity at a time
* Do not proceed to the next activity until the user has validated the current output
* If required input is missing, ask for the missing material instead of filling gaps with confident assumptions
* Distinguish clearly between supported findings, inference, and open assumption
* Treat unknown constraints as a risk to surface, not as proof that no constraints exist
* Keep the work bounded to one journey, product area, portal, or service slice
* Keep the output commercially grounded and decision-oriented

## Validation states

The AI should treat validation in one of three states:

* **Validated:** The output is accepted and can be carried forward as confirmed input
* **Validated with changes:** The AI should update the output, then ask for final confirmation before moving on
* **Not validated:** The AI should stop and wait for more input or correction

Do not move to the next activity on implied approval. Wait for explicit confirmation from the user.

After a review file is updated with a validation decision, the AI should run `python3 Projects/sync_project_status.py --project-name "<Project name>"` in the same turn so the project control files stay aligned with the workflow state.

## Standard AI response pattern

After processing any Package B activity, the AI should return:

1. **Processed output for review**
2. **What is carried forward as confirmed input**
3. **What is still open or uncertain**
4. **What input is required for the next activity**
5. **A direct validation question**

## Lean input and sequence rules

Package B should default to the lightest input flow that still produces a decision-ready output.

That means:

* Carry forward validated context from earlier stages by default
* Do not re-ask for client, opportunity area, journey in scope, target users, key stakeholders, or known constraints unless they changed, are missing, or are still contested
* Start each new activity by briefly restating the carried-forward context that matters for that activity
* Ask only for the minimum new input needed to support the current synthesis step
* Treat extra questions as optional follow-ups, not as mandatory default intake

When the user asks to run a stage or activity in chat:

* Use a short step-based sequence rather than a long field-by-field questionnaire
* Show visible progress in the main response using a format such as `Activity 1.2, step 2 of 4`
* Use 3-4 steps for most activities
* Each step can contain 1-3 tightly related questions
* If a later question depends on an earlier answer, restate that earlier answer inline before asking the follow-up

## Default guided sequence map for Package B

Use this as the default question-flow structure when a stage is being simulated or prepared in chat.

### Stage 0

Use 4 steps:

1. Client and opportunity
2. Decisions and why now
3. Evidence, users, and stakeholders
4. Boundaries

### Activity 1.1

Carry forward the Stage 0 context and use 4 steps:

1. Workshop setup and business case
2. Journey, users, and scope
3. Measures and discovery focus
4. Constraints, tensions, and open questions

### Activity 1.2

Carry forward the validated scope and use 4 steps:

1. Evidence and research coverage
2. Needs and barriers
3. Decision criteria and workarounds
4. Conflicts, surprises, and next questions

### Activity 2.1

Carry forward the interview synthesis and use 3 steps:

1. Current-state structure
2. Breakdown pattern and dependencies
3. Opportunity areas and decision criteria

### Activity 3.1

Carry forward the current-state implications and use 3 steps:

1. Future-state direction and journey
2. Principles and service changes
3. Dependencies and prototype moments

### Activity 4.1

Carry forward the future-state concept and use 4 steps:

1. Decision and prototype objective
2. Prototype scope and interactions
3. Prioritization and sequencing
4. Risks, validation, and tool choice

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

## Final Package B output set

By the end of Package B, the AI-assisted workflow should support delivery of:

* A concise insight summary from 4-6 interviews
* A current-state and future-state journey map
* A list of required service changes across process, content, ownership, and data
* A clickable prototype of the core flow
* A prioritized delivery recommendation

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
* Opportunity area in scope
* Decisions the package should support
* Why this matters now
* Known evidence
* Target users
* Stakeholders or teams involved
* Known constraints
* Out-of-scope items

### Recommended dialogue sequence and wording

1. `Stage 0, step 1 of 4`
   Ask:
   * Who is the client, or what context should I keep in mind for this project?
   * What opportunity area should this package focus on?
   Example opportunity answer: Prospective home buyers begin a digital mortgage pre-approval journey, but many drop out before they understand affordability, document requirements, or what happens next.
2. `Stage 0, step 2 of 4`
   Ask:
   * Which decisions should this package help you make?
   * Why does this matter now?
   Example decision answer: What mortgage pre-approval concept should move into delivery first, and what should be built now, deferred, or validated further?
   Example why-now answer: The bank already sees the opportunity area, but needs clearer evidence before scope and priorities are locked in delivery.
3. `Stage 0, step 3 of 4`
   Ask:
   * What evidence do you already have today?
   * Which target users should we keep in view from the start?
   * Which stakeholders or teams need to be involved from the start?
   Example evidence answer: Web analytics, call-center topics, advisor input, and existing customer feedback all point to uncertainty around affordability, documents, and next steps.
   Example user answer: First-time buyers, existing homeowners planning a move, and customers who start digitally but switch to advisor help.
   Example stakeholder answer: Mortgage product, advisors, contact center, analytics, content, and compliance.
4. `Stage 0, step 4 of 4`
   Ask:
   * What important boundaries should we keep in mind, including both known constraints and anything that should stay out of scope?
   Example answer: The package must stay focused on early pre-approval and advisor handoff rather than a full underwriting redesign, and full underwriting and post-approval case handling should stay out of scope.

### Validation gate

Only move to Activity 1.1 when the user confirms that the intake is good enough to begin.

## Activity-specific working rule

Use the seeded project input files and the Package B template library as the operating structure for each activity.

Keep the rhythm consistent:

1. Restate the carried-forward context briefly
2. Capture only the minimum new input needed for the activity
3. Synthesize into a review-ready output
4. Get explicit validation
5. Only then move on

For the concrete step-based input structures, use:

* [../../Projects/Templates/English/Package_B/package_b_template_library.md](../../Projects/Templates/English/Package_B/package_b_template_library.md)

## Prototype-sequence rule

When Activity 4.1 is validated:

* Write the main delivery recommendation in `package_b_final_deliverable.md`
* Write the operational prototype prompt pack in `package_b_prototype_prompt_pack.md`
* Write the approved prototype flow, links, screenshots, and iteration notes in `package_b_prototype_record.md`
* Keep refinement prompts separate from fresh-generation prompts
* If the user provides screenshots or links to the existing client experience, the prompt pack should explicitly instruct visual alignment with the client's current design language
