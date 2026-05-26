# Projects template library

Use this folder as the reusable template source for live Package A, Package B, and Package C engagements.

## Purpose

The templates in this folder are meant to make project setup, intake, activity handoffs, review checkpoints, and final deliverables easier to run consistently.

They are reusable source files for the project bootstrap utility. Do not fill them in directly for a live project. The normal workflow is to run `Projects/bootstrap_project.py`, which creates the project folder, adds `project_index.md`, and seeds the right files automatically.

## Structure

```text
Projects/Templates/
  English/
    Shared/
    Package_A/
    Package_B/
    Package_C/
  Danish/
    Shared/
    Package_A/
    Package_B/
    Package_C/
```

## What to use where

* `English/Shared/` and `Danish/Shared/`: reusable project-setup, review, live-activity handoff, evidence-request, workshop invite, interview invite and consent, session brief, activity-readiness, and pilot-retrospective templates that work across all packages
* `English/Package_A/` and `Danish/Package_A/`: Stage 0 intake, activity handoff, final-deliverable templates, and prototype-artifact templates for Package A
* `English/Package_B/` and `Danish/Package_B/`: Stage 0 intake, activity handoff, and final-deliverable templates for Package B
* `English/Package_C/` and `Danish/Package_C/`: Stage 0 intake, activity handoff, and final-deliverable templates for Package C

The project bootstrap utility also generates package-specific activity-output drafts and stage-review files directly from the package workflow metadata, so not every seeded file lives as a standalone source file in this folder.

Use [English/Shared/live_activity_handoff_message_template.md](English/Shared/live_activity_handoff_message_template.md) and its Danish counterpart as the canonical structure for the user-facing handoff message after a validated stage leads into the next live activity.

Use [English/Shared/evidence_request_template.md](English/Shared/evidence_request_template.md) when a package activity depends on evidence, access, exports, or supporting material from the client team.

Use [English/Shared/workshop_invite_template.md](English/Shared/workshop_invite_template.md) when you need a clear participant invite for a workshop, mapping session, or validation session.

Use [English/Shared/interview_invite_and_consent_template.md](English/Shared/interview_invite_and_consent_template.md) when you need to invite participants to interviews, contextual sessions, or shadowing and explain consent clearly.

Use [English/Shared/session_brief_template.md](English/Shared/session_brief_template.md) as the facilitator's internal run sheet before a live session.

Use [English/Shared/current_journey_mapping_template.md](English/Shared/current_journey_mapping_template.md) when you need a simple canvas structure for current-state journey mapping in a mapping session.

Use [English/Shared/activity_readiness_checklist.md](English/Shared/activity_readiness_checklist.md) before a live activity when you want to check whether the workshop, interview, evidence review, or mapping session is actually ready to run.

Use [English/Shared/pilot_retrospective_template.md](English/Shared/pilot_retrospective_template.md) after a pilot or dry run to capture friction, strengths, and concrete improvements for the next framework iteration.

## Suggested use inside a live project

1. Run `python3 Projects/bootstrap_project.py --project-name "<Project name>" --package <A|B|C> --language <english|danish>`.
2. Let the bootstrap utility create the standard project structure, `project_index.md`, and the relevant seeded files.
3. Fill in the seeded input files in `01-inputs/` as the package progresses.
4. Use the seeded output files in `02-working/` while the package is being synthesized.
5. Use the seeded review and final files as the project moves through validation and completion.

The input templates are intentionally moving toward shorter step-based sequences with carried-forward context, so live projects do not keep re-asking the same questions at every activity.

Manual copying from this folder should only be used if the bootstrap utility is unavailable.

## Language rule

Use the English templates for English-only engagements and the Danish templates for Danish-only engagements. The structure is mirrored so the same workflow can run in either language.
