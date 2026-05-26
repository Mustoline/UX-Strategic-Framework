# Projects Folder Convention

Use `Projects/` for actual Package A, Package B, and Package C engagements.

## What belongs here

* Real Package A, Package B, and Package C engagements
* Any project-specific artifacts created while running a package

Do not store live project artifacts in `Packages/`, `Sales materials/`, or `skills/`. Those folders are for reusable source material.

## Preferred setup path

Use the bootstrap utility to create and seed a live project in one step:

```bash
python3 Projects/bootstrap_project.py --project-name "Fried IQ" --package A --language english
```

That command will:

* create the standard folder structure
* create `project_setup.md`
* create `project_index.md` as the project control center
* seed shared prep assets in `00-project-setup/shared-prep/`
* seed a package-specific ready-to-edit draft for the first live activity in `00-project-setup/shared-prep/`
* prepare the project so later review syncs can refresh the `next_activity_*.md` prep pack automatically
* seed the relevant Stage 0 and activity-input files in `01-inputs/`
* seed the relevant activity-output files in `02-working/`
* seed the relevant stage-review files in `03-reviews/`
* seed the package final-deliverable skeletons in `04-final/`, including separate prototype prompt-pack and prototype-record files where relevant

Manual setup should now be treated as a fallback only.

## Keeping the control center in sync

After a review file is updated with a validation decision, run:

```bash
python3 Projects/sync_project_status.py --project-name "Fried IQ"
```

Useful variants:

* `--resume`: move a paused project back to `Active` while syncing stage state
* `--on-hold`: keep or move the project to `On hold` while syncing stage state
* `--close`: mark the project `Closed` after syncing

This command reads the stage review files in `03-reviews/`, checks the approval status in `04-final/`, updates both `project_index.md` and `00-project-setup/project_setup.md`, and refreshes the generated `next_activity_*.md` prep files in `00-project-setup/shared-prep/`.

When the project is being run through this tool, the assistant should run this automatically in the same turn as the validation update.

When a validated stage moves the project into a real-world activity, the assistant should also:

* make it explicit that the next step is a live activity, not an AI-only step
* point to the relevant project input file in `01-inputs/`
* point to the matching facilitator guide and any relevant template, question guide, or tool file
* wait for the completed activity notes before resuming synthesis unless the user explicitly asks to simulate or prepare the activity in chat
* use the canonical response structure in [Templates/English/Shared/live_activity_handoff_message_template.md](Templates/English/Shared/live_activity_handoff_message_template.md) or the Danish equivalent

Use [Templates/English/Shared/activity_readiness_checklist.md](Templates/English/Shared/activity_readiness_checklist.md) if you want to sanity-check whether the next live activity is actually ready to run.

Use [Templates/English/Shared/evidence_request_template.md](Templates/English/Shared/evidence_request_template.md) when the next activity depends on evidence, access, exports, or supporting material from the client team.

Use [Templates/English/Shared/workshop_invite_template.md](Templates/English/Shared/workshop_invite_template.md), [Templates/English/Shared/interview_invite_and_consent_template.md](Templates/English/Shared/interview_invite_and_consent_template.md), and [Templates/English/Shared/session_brief_template.md](Templates/English/Shared/session_brief_template.md) when you need to prepare the live session itself, not just the synthesis around it.

For interview stages, `generate_next_activity_prep.py` also creates a project-specific `next_activity_interview_guide*.md` file in `00-project-setup/shared-prep/`, based on the validated project context so far.

For mapping stages, `generate_next_activity_prep.py` also creates a project-specific `next_activity_mapping_canvas*.md` file in `00-project-setup/shared-prep/`, based on the validated project context so far.

Use [Templates/English/Shared/pilot_retrospective_template.md](Templates/English/Shared/pilot_retrospective_template.md) after a pilot so framework changes are driven by observed friction rather than memory.

## Project naming rule

When a new real package engagement starts:

1. Ask for the project name before creating any project artifacts.
2. Convert the name into a folder-safe format by replacing spaces with hyphens and removing unsafe special characters.
3. Keep the result readable where possible.

Example:

* `Fried IQ` becomes `Projects/Fried-IQ/`

If the folder already exists, stop and ask whether to reuse the existing folder or create a new one with a different name.

## Standard folder structure

Each real project should use this structure:

```text
Projects/Fried-IQ/
  project_index.md
  00-project-setup/
    project_setup.md
    shared-prep/
  01-inputs/
  02-working/
  03-reviews/
  04-final/
```

## What goes where

* `project_index.md`: project control center showing current stage, status, seeded files, and final-deliverable checklist
* `00-project-setup/`: project setup note, package type, working language, sponsor, creation date, and status
* `00-project-setup/shared-prep/`: seeded shared prep assets such as invite templates, consent wording, session briefs, evidence requests, readiness checks, retrospective templates, a ready-to-edit draft for the first live activity, auto-refreshed `next_activity_*.md` prep files, project-specific interview guides for interview stages, and project-specific mapping canvases for mapping stages
* `01-inputs/`: raw client input, workshop notes, interview notes, evidence exports, and handoff templates
* `02-working/`: seeded activity-output drafts, in-progress synthesis, draft maps, draft recommendations, draft prompt packs, and other working files
* `03-reviews/`: seeded validation files, outputs shared for validation, review notes, change logs, and approved checkpoints
* `04-final/`: final deliverables, approved recommendation packs, separate prototype prompt packs, separate prototype records, and export-ready artifacts

## Storage rule

Once a project folder is created, all project-generated files for that engagement should stay inside that folder.

That includes:

* intake summaries
* activity handoffs
* synthesis drafts
* validation notes
* final package outputs
* prototype prompt packs
* prototype approval records

The package and sales documents in `Packages/` and `Sales materials/` remain the reusable operating system for the offer. They are not project folders.

## Reusable templates

Use [Templates/README.md](Templates/README.md) for the reusable template library that supports live projects.

That library contains:

* Shared project-setup, review, handoff, evidence-request, workshop-invite, interview-invite-and-consent, session-brief, activity-readiness, and pilot-retrospective templates
* Package-specific intake and activity handoff templates
* Package-specific final-deliverable templates
* Separate prototype prompt-pack and prototype-record templates where the package includes prototype work

`bootstrap_project.py` also generates the project dashboard plus the package-specific activity-output and review files that live inside each project folder. Use `sync_project_status.py` to keep those control files aligned once the project is moving and to refresh the next live activity prep pack automatically. You can also run `python3 Projects/generate_next_activity_prep.py --project-name "Fried IQ"` directly if you want to refresh only the prep pack.

Direct user-facing questions should stay in the main response, not in commentary updates, so they are not hidden by the interface.
During a simulated activity, prefer a short step-based sequence such as `Activity 1.2, step 2 of 3` rather than a long one-field-at-a-time questionnaire.
Carry forward validated context from earlier stages by default and ask only for the minimum new or changed input needed for the current step.
When a follow-up question depends on an earlier answer, restate that earlier answer inside the question so the user does not need to scroll back.
If internal command or tool text still leaks into the visible conversation, stop the active step flow, recap what is already captured, and switch first to a grouped-step fallback before falling all the way back to a full single-message reply.
