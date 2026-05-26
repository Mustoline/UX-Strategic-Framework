# Internal activity-to-skill and agent mapping

Internal note: This document maps the package activities to the internal skill library and to the recommended agent pattern behind the scenes. It is not client-facing and should not be referenced in proposals, sales material, or executive summaries.

## Purpose

Use this mapping to keep the package operating system and the `/skills` library aligned.

The rule is:

* `Packages/` defines the package logic, stage gates, and client-visible sequence
* `Projects/Templates/` defines the project files and handoff structure
* `/skills` defines how the internal analysis, facilitation support, synthesis, and review should be executed
* Specialist agents are optional internal execution support and must not create a second visible workflow for the client

## Agent pattern legend

* `Main thread only`: Keep the activity in the main package flow. No separate specialist agent is worth the overhead.
* `Main thread + specialist worker`: The main thread owns the stage gate and user interaction, but a bounded worker can synthesize or structure the activity output.
* `Main thread + specialist worker + optional review sidecar`: Use a specialist worker for the main synthesis and add a sidecar review only when the output is close to client-ready or strategically sensitive.

## Shared helper skills

| Helper skill | Internal role |
| --- | --- |
| `artifact-writer` | Drafts clean client-facing or internal artifacts from validated package output. |
| `evidence-ingest` | Normalizes mixed evidence before synthesis-heavy activities. |
| `workshop-design-kit` | Supplies agenda, facilitation logic, and note-capture structure for workshop activities. |
| `map-structure-generator` | Supplies scaffolds for journey maps, ecosystem maps, and service blueprints. |
| `ux-strategy-reviewer` | Final quality check for business tone, clarity, and package completeness. |
| `discovery-interview` | Optional support when a stage is still too vague and needs deeper guided clarification. |

## Package A mapping

| Step | Primary skill | Supporting skills | Agent pattern | Expected input file | Expected working output | Expected review or final gate | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Stage 0 intake` | No dedicated specialist skill yet | `discovery-interview`, `artifact-writer` | Main thread only | `01-inputs/package_a_stage_0_intake_input.md` | `02-working/package_a_stage_0_intake_summary.md` | `03-reviews/package_a_stage_0_intake_check.md` | Candidate future skill: Package A intake and framing. |
| `Activity 1.1` | `sponsor-workshop-facilitator` | `workshop-design-kit`, `evidence-ingest`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_a_activity_1_1_input.md` | `02-working/package_a_activity_1_1_decision_frame.md` | `03-reviews/package_a_activity_1_1_review.md` | Main thread runs the live workshop handoff. Worker is best used after the notes are captured. |
| `Activity 1.2` | `evidence-baseline-reviewer` | `evidence-ingest`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_a_activity_1_2_input.md` | `02-working/package_a_activity_1_2_evidence_synthesis.md` | `03-reviews/package_a_activity_1_2_review.md` | This is the clearest example of a bounded specialist synthesis step. |
| `Activity 1.3` | `journey-step-mapper` | `map-structure-generator`, `workshop-design-kit`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_a_activity_1_3_input.md` | `02-working/package_a_activity_1_3_breakdown_map.md` | `03-reviews/package_a_activity_1_3_review.md` | Use the worker after notes exist, not during live step-by-step capture. |
| `Activity 2.1` | `option-review-facilitator` | `workshop-design-kit`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_a_activity_2_1_input.md` | `02-working/package_a_activity_2_1_direction_review.md` | `03-reviews/package_a_activity_2_1_review.md` | Good worker target because it is a bounded comparison problem with explicit criteria. |
| `Activity 3.1` | `recommendation-packager` | `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + optional review sidecar | `01-inputs/package_a_activity_3_1_input.md` | `02-working/package_a_activity_3_1_recommendation_draft.md` | `03-reviews/package_a_activity_3_1_review.md` | Use a reviewer sidecar only when the recommendation is close to client-ready. |
| `Final deliverable` | `recommendation-packager` | `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + optional review sidecar | `04-final/package_a_final_deliverable.md` plus prototype files | `04-final/package_a_final_deliverable.md`, `04-final/package_a_prototype_prompt_pack.md`, `04-final/package_a_prototype_record.md` | Final client approval | Keep the main recommendation, prompt pack, and prototype record separate. |

## Package B mapping

| Step | Primary skill | Supporting skills | Agent pattern | Expected input file | Expected working output | Expected review or final gate | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Stage 0 intake` | No dedicated specialist skill yet | `discovery-interview`, `artifact-writer` | Main thread only | `01-inputs/package_b_stage_0_intake_input.md` | `02-working/package_b_stage_0_intake_summary.md` | `03-reviews/package_b_stage_0_intake_check.md` | Candidate future skill: Package B intake and opportunity framing. |
| `Activity 1.1` | `scoping-workshop-facilitator` | `workshop-design-kit`, `evidence-ingest`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_b_activity_1_1_input.md` | `02-working/package_b_activity_1_1_scope_summary.md` | `03-reviews/package_b_activity_1_1_review.md` | Main thread handles the live scoping workshop. |
| `Activity 1.2` | `user-research-runner` | `evidence-ingest`, `discovery-interview`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_b_activity_1_2_input.md` | `02-working/package_b_activity_1_2_insight_summary.md` | `03-reviews/package_b_activity_1_2_review.md` | Specialist worker is useful after interview notes and evidence are assembled. |
| `Activity 2.1` | `current-journey-synthesizer` | `map-structure-generator`, `artifact-writer`, `evidence-ingest`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_b_activity_2_1_input.md` | `02-working/package_b_activity_2_1_current_state_journey_summary.md` | `03-reviews/package_b_activity_2_1_review.md` | Strong candidate for specialist synthesis because the output has map logic and opportunity framing. |
| `Activity 3.1` | `future-state-concept-facilitator` | `workshop-design-kit`, `map-structure-generator`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_b_activity_3_1_input.md` | `02-working/package_b_activity_3_1_future_state_concept_summary.md` | `03-reviews/package_b_activity_3_1_review.md` | Main thread owns the workshop. Worker helps package the concept and service changes. |
| `Activity 4.1` | `prototype-and-prioritization-facilitator` | `workshop-design-kit`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + optional review sidecar | `01-inputs/package_b_activity_4_1_input.md` | `02-working/package_b_activity_4_1_prioritization_and_prototype_summary.md` | `03-reviews/package_b_activity_4_1_review.md` | Use the review sidecar when the final recommendation is moving toward client-facing approval. |
| `Final deliverable` | `prototype-and-prioritization-facilitator` | `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + optional review sidecar | `04-final/package_b_final_deliverable.md` plus prototype files | `04-final/package_b_final_deliverable.md`, `04-final/package_b_prototype_prompt_pack.md`, `04-final/package_b_prototype_record.md` | Final client approval | Final packaging should keep the prototype artifacts separate from the main recommendation. |

## Package C mapping

| Step | Primary skill | Supporting skills | Agent pattern | Expected input file | Expected working output | Expected review or final gate | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Stage 0 intake` | No dedicated specialist skill yet | `discovery-interview`, `artifact-writer` | Main thread only | `01-inputs/package_c_stage_0_intake_input.md` | `02-working/package_c_stage_0_intake_summary.md` | `03-reviews/package_c_stage_0_intake_check.md` | Candidate future skill: Package C strategic intake and boundary framing. |
| `Activity 1.1` | `executive-and-service-owner-interviewer` | `evidence-ingest`, `discovery-interview`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_c_activity_1_1_input.md` | `02-working/package_c_activity_1_1_strategic_framing_summary.md` | `03-reviews/package_c_activity_1_1_review.md` | Main thread owns the interview stream and validation gate. |
| `Activity 1.2` | `ecosystem-workshop-facilitator` | `workshop-design-kit`, `map-structure-generator`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_c_activity_1_2_input.md` | `02-working/package_c_activity_1_2_service_scope_summary.md` | `03-reviews/package_c_activity_1_2_review.md` | Good place for structured synthesis after a dense cross-functional workshop. |
| `Activity 2.1` | `contextual-fieldwork-runner` | `evidence-ingest`, `discovery-interview`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_c_activity_2_1_input.md` | `02-working/package_c_activity_2_1_operational_observation_summary.md` | `03-reviews/package_c_activity_2_1_review.md` | Strong worker candidate because the fieldwork synthesis is evidence-heavy and bounded. |
| `Activity 2.2` | `service-blueprint-builder` | `map-structure-generator`, `evidence-ingest`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_c_activity_2_2_input.md` | `02-working/package_c_activity_2_2_blueprint_summary.md` | `03-reviews/package_c_activity_2_2_review.md` | Blueprint construction is a strong specialist activity and should not be improvised in the main thread. |
| `Activity 3.1` | `future-state-service-model-and-validation` | `workshop-design-kit`, `map-structure-generator`, `discovery-interview`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + optional review sidecar | `01-inputs/package_c_activity_3_1_input.md` | `02-working/package_c_activity_3_1_future_state_service_model_summary.md` | `03-reviews/package_c_activity_3_1_review.md` | Add the review sidecar only when the target-state model is close to external playback. |
| `Activity 4.1` | `roadmap-and-business-case-framer` | `workshop-design-kit`, `evidence-ingest`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + optional review sidecar | `01-inputs/package_c_activity_4_1_input.md` | `02-working/package_c_activity_4_1_roadmap_and_business_case_summary.md` | `03-reviews/package_c_activity_4_1_review.md` | The review sidecar is especially useful when the ROI logic will be used in leadership discussion. |
| `Final deliverable` | `roadmap-and-business-case-framer` | `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + optional review sidecar | `04-final/package_c_final_deliverable.md` plus optional prototype files | `04-final/package_c_final_deliverable.md`, optional `04-final/package_c_prototype_prompt_pack.md`, optional `04-final/package_c_prototype_record.md` | Final client approval | Prototype support remains optional and should only cover one selected high-risk journey slice. |

## Operating rules for future integration

When this mapping is used operationally:

* The main package flow must still own the user interaction, validation gate, and project-status sync.
* Skills should power the internal work behind each activity, not replace the package sequence.
* Specialist agents should be used only when they materially improve bounded synthesis quality.
* Review sidecars should be used selectively near client-ready outputs, not on every activity by default.
* If a skill and the package documents ever disagree, update the skill or the package so the mapping stays consistent.
