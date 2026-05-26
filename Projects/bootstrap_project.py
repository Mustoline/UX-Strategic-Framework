#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


PROJECTS_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = PROJECTS_DIR / "Templates"
SHARED_PREP_DIRNAME = "shared-prep"


SHARED_PREP_ASSET_CONFIG = {
    "workshop_invite": {
        "english_filename": "workshop_invite_template.md",
        "danish_filename": "workshop_invite_template_danish.md",
        "english_title": "Workshop invite template",
        "danish_title": "Skabelon til workshopinvitation",
        "english_use": "Use for workshop invites, mapping sessions, and validation sessions.",
        "danish_use": "Bruges til workshopinvitationer, mappingsessioner og valideringssessioner.",
    },
    "interview_invite_and_consent": {
        "english_filename": "interview_invite_and_consent_template.md",
        "danish_filename": "interview_invite_and_consent_template_danish.md",
        "english_title": "Interview invite and consent template",
        "danish_title": "Skabelon til interviewinvitation og samtykke",
        "english_use": "Use for interviews, contextual sessions, observation, and shadowing.",
        "danish_use": "Bruges til interviews, kontekstuelle sessioner, observation og shadowing.",
    },
    "session_brief": {
        "english_filename": "session_brief_template.md",
        "danish_filename": "session_brief_template_danish.md",
        "english_title": "Session brief template",
        "danish_title": "Skabelon til session brief",
        "english_use": "Use as the facilitator's internal run sheet before a live session.",
        "danish_use": "Bruges som facilitatorens interne run sheet foer en live-session.",
    },
    "evidence_request": {
        "english_filename": "evidence_request_template.md",
        "danish_filename": "evidence_request_template_danish.md",
        "english_title": "Evidence request template",
        "danish_title": "Skabelon til evidensrequest",
        "english_use": "Use when evidence, access, exports, or supporting material must be requested from the client team.",
        "danish_use": "Bruges naar evidens, adgang, eksporter eller stoettemateriale skal efterspoerges hos kundeteamet.",
    },
    "activity_readiness": {
        "english_filename": "activity_readiness_checklist.md",
        "danish_filename": "activity_readiness_checklist_danish.md",
        "english_title": "Activity readiness checklist",
        "danish_title": "Tjekliste for aktivitetsparathed",
        "english_use": "Use before a live activity when you want a structured readiness check.",
        "danish_use": "Bruges foer en live-aktivitet, naar du vil have et struktureret readiness-check.",
    },
    "pilot_retrospective": {
        "english_filename": "pilot_retrospective_template.md",
        "danish_filename": "pilot_retrospective_template_danish.md",
        "english_title": "Pilot retrospective template",
        "danish_title": "Skabelon til pilotretrospektiv",
        "english_use": "Use after a pilot or dry run to capture strengths, friction, and next improvements.",
        "danish_use": "Bruges efter en pilot eller dry run til at indfange styrker, friktion og naeste forbedringer.",
    },
}


PACKAGE_SHARED_PREP_ASSETS = {
    "A": [
        "workshop_invite",
        "session_brief",
        "evidence_request",
        "activity_readiness",
        "pilot_retrospective",
    ],
    "B": [
        "workshop_invite",
        "interview_invite_and_consent",
        "session_brief",
        "evidence_request",
        "activity_readiness",
        "pilot_retrospective",
    ],
    "C": [
        "workshop_invite",
        "interview_invite_and_consent",
        "session_brief",
        "evidence_request",
        "activity_readiness",
        "pilot_retrospective",
    ],
}


FIRST_LIVE_ACTIVITY_DRAFT_CONFIG = {
    ("english", "A"): {
        "activity": "Activity 1.1: Sponsor workshop and decision frame",
        "session_type": "Workshop",
        "objective": "Agree the business question, target users, success measures, scope boundary, and main constraints for the sprint.",
        "decision_output": "A validated decision frame for the sprint.",
        "estimated_time": "90 minutes",
        "roles": [
            "Sponsor or budget owner",
            "Product, service, or business owner",
            "Relevant operational, commercial, or delivery stakeholders",
        ],
        "prepare": [
            "The decision the sprint must support",
            "What is already believed about the problem",
            "A first out-of-scope boundary",
            "Any baseline metrics already known",
        ],
        "cover": [
            "Business question and commercial context",
            "Target users and the journey focus",
            "Success measures, constraints, and open questions",
        ],
        "questions": [
            "What decision must be made before delivery starts?",
            "Which users matter most to that decision?",
            "What part of the journey is in scope, and what is not?",
        ],
        "capture": [
            "Business question",
            "Target users",
            "Scope boundary",
            "Success measures and constraints",
        ],
        "prep_files": [
            "workshop_invite_template.md",
            "session_brief_template.md",
            "activity_readiness_checklist.md",
        ],
    },
    ("english", "B"): {
        "activity": "Activity 1.1: Scoping workshop and research frame",
        "session_type": "Workshop",
        "objective": "Agree the journey in scope, business case, success measures, scope boundaries, and the questions the package must answer.",
        "decision_output": "A validated scope and research frame for the package.",
        "estimated_time": "2 hours",
        "roles": [
            "Sponsor or budget owner",
            "Product, service, or business owner",
            "Commercial, operational, content, or delivery stakeholders with relevant authority",
        ],
        "prepare": [
            "The opportunity area under discussion",
            "Known business case inputs and outcome expectations",
            "A first view of in-scope and out-of-scope areas",
            "What evidence already exists",
        ],
        "cover": [
            "Opportunity area and business case",
            "Journey in scope and scope boundaries",
            "Success measures and discovery questions",
        ],
        "questions": [
            "Which journey or service area is actually in scope?",
            "What business case makes this work worth doing now?",
            "Which research questions must be answered before delivery scope can be set with confidence?",
        ],
        "capture": [
            "Business case",
            "Journey in scope",
            "Scope boundaries",
            "Discovery questions",
        ],
        "prep_files": [
            "workshop_invite_template.md",
            "session_brief_template.md",
            "activity_readiness_checklist.md",
        ],
    },
    ("english", "C"): {
        "activity": "Activity 1.1: Executive and service-owner interviews",
        "session_type": "Interview",
        "objective": "Clarify the business case, strategic priorities, service pressures, and investment questions that should shape the redesign.",
        "decision_output": "A strategic framing summary that can guide the redesign.",
        "estimated_time": "1-2 days across 5-7 interviews of 45-60 minutes each, plus first synthesis",
        "roles": [
            "Senior sponsors",
            "Service owners",
            "Leaders responsible for operations, channels, or core systems",
        ],
        "prepare": [
            "Which decisions or investments the package must inform",
            "An interview guide around service pressure, business consequences, and investment questions",
            "Any strategy, operating-model, or performance material already available",
        ],
        "cover": [
            "Strategic priorities and business case",
            "Service pressures, failure points, and tensions",
            "Investment questions and stakeholder alignment",
        ],
        "questions": [
            "Which strategic priorities should shape the redesign?",
            "Where is the service under the most pressure today?",
            "Which investment questions or tensions need to be clarified before moving forward?",
        ],
        "capture": [
            "Strategic priorities",
            "Service pressures and failure points",
            "Business and operational consequences",
            "Investment questions and tensions",
        ],
        "prep_files": [
            "interview_invite_and_consent_template.md",
            "session_brief_template.md",
            "activity_readiness_checklist.md",
        ],
    },
    ("danish", "A"): {
        "activity": "Aktivitet 1.1: Sponsorworkshop og beslutningsramme",
        "session_type": "Workshop",
        "objective": "At blive enige om forretningsspørgsmålet, målbrugerne, succeskriterierne, scopegrænsen og de vigtigste begrænsninger for sprintet.",
        "decision_output": "En valideret beslutningsramme for sprintet.",
        "estimated_time": "90 minutter",
        "roles": [
            "Sponsor eller budgetejer",
            "Produkt-, service- eller forretningsansvarlig",
            "Relevante interessenter fra drift, det kommercielle område eller leverancen",
        ],
        "prepare": [
            "Den beslutning sprintet skal understøtte",
            "Hvad man allerede mener om problemet",
            "En første afgrænsning af det, der er ude af scope",
            "Eventuelle kendte baselinemål",
        ],
        "cover": [
            "Forretningsspørgsmålet og den kommercielle kontekst",
            "Målbrugere og fokus i rejsen",
            "Succeskriterier, begrænsninger og åbne spørgsmål",
        ],
        "questions": [
            "Hvilken beslutning skal træffes, før leverancen starter?",
            "Hvilke bruger- eller medarbejdergrupper betyder mest for den beslutning?",
            "Hvilken del af rejsen er i scope, og hvad er ikke?",
        ],
        "capture": [
            "Forretningsspørgsmål",
            "Målbrugere",
            "Scopegrænse",
            "Succeskriterier og begrænsninger",
        ],
        "prep_files": [
            "workshop_invite_template_danish.md",
            "session_brief_template_danish.md",
            "activity_readiness_checklist_danish.md",
        ],
    },
    ("danish", "B"): {
        "activity": "Aktivitet 1.1: Afklaringsworkshop og undersøgelsesramme",
        "session_type": "Workshop",
        "objective": "At aftale, hvilken rejse der er i scope, hvad forretningscasen er, hvilke succeskriterier der gælder, hvor scopegrænserne går, og hvilke spørgsmål pakken skal besvare.",
        "decision_output": "En valideret scope- og undersøgelsesramme for pakken.",
        "estimated_time": "2 timer",
        "roles": [
            "Sponsor eller budgetejer",
            "Produkt-, service- eller forretningsansvarlig",
            "Kommercielle, driftsnære, indholdsrelaterede eller leverancemæssige interessenter med relevant mandat",
        ],
        "prepare": [
            "Hvilket mulighedsområde der skal drøftes",
            "Kendte input til business casen og forventede resultater",
            "Et første billede af, hvad der er i scope og ude af scope",
            "Hvilken evidens der allerede findes",
        ],
        "cover": [
            "Mulighedsområde og business case",
            "Rejsen i scope og scopegrænser",
            "Succeskriterier og spørgsmål til afklaringen",
        ],
        "questions": [
            "Hvilken rejse eller hvilket serviceområde er faktisk i scope?",
            "Hvilken business case eller kommerciel logik gør dette arbejde værd at gennemføre nu?",
            "Hvilke researchspørgsmål skal besvares, før leveranceomfanget kan fastlægges med sikkerhed?",
        ],
        "capture": [
            "Business case",
            "Rejsen i scope",
            "Scopegrænser",
            "Spørgsmål til afklaringen",
        ],
        "prep_files": [
            "workshop_invite_template_danish.md",
            "session_brief_template_danish.md",
            "activity_readiness_checklist_danish.md",
        ],
    },
    ("danish", "C"): {
        "activity": "Aktivitet 1.1: Interviews med ledere og serviceansvarlige",
        "session_type": "Interview",
        "objective": "At afklare business casen, de strategiske prioriteringer, presset på servicen og de investeringsspørgsmål, der skal forme redesignarbejdet.",
        "decision_output": "En strategisk indramning, som kan guide redesignarbejdet.",
        "estimated_time": "1-2 dage fordelt på 5-7 interviews på 45-60 minutter hver samt den første syntese",
        "roles": [
            "Senior sponsorer",
            "Serviceansvarlige",
            "Ledere med ansvar for drift, kanaler eller centrale systemer",
        ],
        "prepare": [
            "Hvilke beslutninger eller investeringer pakken skal informere",
            "En interviewguide om pres på servicen, forretningsmæssige konsekvenser og investeringsspørgsmål",
            "Eventuelt strategi-, driftsmodel- eller performancemateriale, der allerede findes",
        ],
        "cover": [
            "Strategiske prioriteringer og business case",
            "Pres på servicen, sammenbrudspunkter og spændinger",
            "Investeringsspørgsmål og områder med enighed eller konflikt",
        ],
        "questions": [
            "Hvilke strategiske prioriteringer skal forme redesignarbejdet?",
            "Hvor er presset på servicen størst i dag?",
            "Hvilke investeringsspørgsmål eller spændinger skal afklares, før arbejdet kan gå videre?",
        ],
        "capture": [
            "Strategiske prioriteringer",
            "Pres på servicen og sammenbrudspunkter",
            "Forretningsmæssige og driftsmæssige konsekvenser",
            "Investeringsspørgsmål og spændinger",
        ],
        "prep_files": [
            "interview_invite_and_consent_template_danish.md",
            "session_brief_template_danish.md",
            "activity_readiness_checklist_danish.md",
        ],
    },
}


def shared_prep_note(language: str) -> str:
    if language == "danish":
        return f"* Delte forberedelsesaktiver, inklusiv en klar-til-tilpasning-kladde til den foerste live-aktivitet, er seed'et i `00-project-setup/{SHARED_PREP_DIRNAME}/`. Efter hvert review-sync bliver `next_activity_*.md` opdateret automatisk."
    return f"* Shared prep assets, including a ready-to-edit draft for the first live activity, are seeded in `00-project-setup/{SHARED_PREP_DIRNAME}/`. After each review sync, `next_activity_*.md` is refreshed automatically."


PACKAGE_TEMPLATE_CONFIG = {
    ("english", "A"): {
        "library": TEMPLATES_DIR / "English" / "Package_A" / "package_a_template_library.md",
        "package_label": "Package A",
        "language_label": "English",
        "project_status": "Setup complete",
        "current_stage": "Stage 0 - Intake check before Activity 1.1",
        "next_action": "Run the guided Stage 0 intake dialogue and validate the intake before Activity 1.1 starts.",
        "final_seed_files": [
            "package_a_final_deliverable.md",
            "package_a_prototype_prompt_pack.md",
            "package_a_prototype_record.md",
        ],
        "final_artifacts": [
            {"deliverable": "Recommendation document", "file": "package_a_final_deliverable.md"},
            {"deliverable": "Key breakdown map for the selected journey step", "file": "package_a_final_deliverable.md"},
            {"deliverable": "Risks and next steps", "file": "package_a_final_deliverable.md"},
            {"deliverable": "Prototype prompt pack", "file": "package_a_prototype_prompt_pack.md"},
            {"deliverable": "Clickable prototype record", "file": "package_a_prototype_record.md"},
        ],
        "stages": [
            {
                "stage": "Stage 0",
                "purpose": "Intake check before Activity 1.1",
                "input_file": "package_a_stage_0_intake_input.md",
                "working_file": "package_a_stage_0_intake_summary.md",
                "review_file": "package_a_stage_0_intake_check.md",
                "working_title": "Package A - Stage 0 output",
                "working_sections": [
                    ("Intake summary", "text"),
                    ("Decision to support", "text"),
                    ("Scope boundaries", "bullets"),
                    ("Known evidence and signals", "bullets"),
                    ("Intake gaps or risks", "bullets"),
                    ("Recommended next step", "text"),
                    ("Validation question", "text"),
                ],
            },
            {
                "stage": "Activity 1.1",
                "purpose": "Sponsor workshop and decision frame",
                "input_file": "package_a_activity_1_1_input.md",
                "working_file": "package_a_activity_1_1_decision_frame.md",
                "review_file": "package_a_activity_1_1_review.md",
                "working_title": "Package A - Activity 1.1 output",
                "working_sections": [
                    ("Decision frame", "text"),
                    ("Confirmed business question", "text"),
                    ("Success measures and baseline logic", "bullets"),
                    ("Fixed constraints", "bullets"),
                    ("Assumptions or disagreements", "bullets"),
                    ("Open sprint questions", "bullets"),
                    ("Carried-forward input for Activity 1.2", "bullets"),
                ],
            },
            {
                "stage": "Activity 1.2",
                "purpose": "Evidence review and signal framing",
                "input_file": "package_a_activity_1_2_input.md",
                "working_file": "package_a_activity_1_2_evidence_synthesis.md",
                "review_file": "package_a_activity_1_2_review.md",
                "working_title": "Package A - Activity 1.2 output",
                "working_sections": [
                    ("Evidence objective", "text"),
                    ("Strongest supported findings", "numbered"),
                    ("Directional signals", "bullets"),
                    ("Assumptions and evidence gaps", "bullets"),
                    ("Implications for the selected step", "bullets"),
                    ("Carried-forward input for Activity 1.3", "bullets"),
                ],
            },
            {
                "stage": "Activity 1.3",
                "purpose": "Journey-step breakdown mapping",
                "input_file": "package_a_activity_1_3_input.md",
                "working_file": "package_a_activity_1_3_breakdown_map.md",
                "review_file": "package_a_activity_1_3_review.md",
                "working_title": "Package A - Activity 1.3 output",
                "working_sections": [
                    ("Journey step in scope", "text"),
                    ("Actors and dependencies", "bullets"),
                    ("Biggest breakdowns", "numbered"),
                    ("Why the breakdowns matter", "bullets"),
                    ("Internal implications", "bullets"),
                    ("Validation gaps", "bullets"),
                    ("Carried-forward input for Activity 2.1", "bullets"),
                ],
            },
            {
                "stage": "Activity 2.1",
                "purpose": "Concept-direction review",
                "input_file": "package_a_activity_2_1_input.md",
                "working_file": "package_a_activity_2_1_direction_review.md",
                "review_file": "package_a_activity_2_1_review.md",
                "working_title": "Package A - Activity 2.1 output",
                "working_sections": [
                    ("Decision this review supports", "text"),
                    ("Options compared", "bullets"),
                    ("Comparison summary", "bullets"),
                    ("Preferred direction", "text"),
                    ("Tradeoffs", "bullets"),
                    ("Risks and dependencies", "bullets"),
                    ("Open checks before final recommendation", "bullets"),
                    ("Carried-forward input for Activity 3.1", "bullets"),
                ],
            },
            {
                "stage": "Activity 3.1",
                "purpose": "Final recommendation and prototype brief",
                "input_file": "package_a_activity_3_1_input.md",
                "working_file": "package_a_activity_3_1_recommendation_draft.md",
                "review_file": "package_a_activity_3_1_review.md",
                "working_title": "Package A - Activity 3.1 output",
                "working_sections": [
                    ("Executive recommendation summary", "text"),
                    ("Recommended direction", "text"),
                    ("Why this direction is stronger", "bullets"),
                    ("Build now", "bullets"),
                    ("Defer", "bullets"),
                    ("Validate next", "bullets"),
                    ("Prototype brief inputs", "bullets"),
                    ("Risks and dependencies", "bullets"),
                    ("Carried-forward input for the final deliverable", "bullets"),
                ],
            },
        ],
    },
    ("english", "B"): {
        "library": TEMPLATES_DIR / "English" / "Package_B" / "package_b_template_library.md",
        "package_label": "Package B",
        "language_label": "English",
        "project_status": "Setup complete",
        "current_stage": "Stage 0 - Intake check before Activity 1.1",
        "next_action": "Run the guided Stage 0 intake dialogue and validate the intake before Activity 1.1 starts.",
        "final_seed_files": [
            "package_b_final_deliverable.md",
            "package_b_prototype_prompt_pack.md",
            "package_b_prototype_record.md",
        ],
        "final_artifacts": [
            {"deliverable": "Insight summary from interviews", "file": "package_b_final_deliverable.md"},
            {"deliverable": "Current-state and future-state journey summary", "file": "package_b_final_deliverable.md"},
            {"deliverable": "Required service changes across process, content, ownership, and data", "file": "package_b_final_deliverable.md"},
            {"deliverable": "Prototype prompt pack", "file": "package_b_prototype_prompt_pack.md"},
            {"deliverable": "Clickable prototype record", "file": "package_b_prototype_record.md"},
            {"deliverable": "Prioritized delivery recommendation", "file": "package_b_final_deliverable.md"},
        ],
        "stages": [
            {
                "stage": "Stage 0",
                "purpose": "Intake check before Activity 1.1",
                "input_file": "package_b_stage_0_intake_input.md",
                "working_file": "package_b_stage_0_intake_summary.md",
                "review_file": "package_b_stage_0_intake_check.md",
                "working_title": "Package B - Stage 0 output",
                "working_sections": [
                    ("Intake summary", "text"),
                    ("Decisions this package should support", "bullets"),
                    ("Scope boundaries", "bullets"),
                    ("Known evidence and target users", "bullets"),
                    ("Intake gaps or risks", "bullets"),
                    ("Recommended next step", "text"),
                    ("Validation question", "text"),
                ],
            },
            {
                "stage": "Activity 1.1",
                "purpose": "Scoping workshop and research frame",
                "input_file": "package_b_activity_1_1_input.md",
                "working_file": "package_b_activity_1_1_scope_summary.md",
                "review_file": "package_b_activity_1_1_review.md",
                "working_title": "Package B - Activity 1.1 output",
                "working_sections": [
                    ("Scoping summary", "text"),
                    ("Decisions this package should support", "bullets"),
                    ("Journey and users in scope", "bullets"),
                    ("Success measures and baseline logic", "bullets"),
                    ("Constraints, assumptions, or disagreements", "bullets"),
                    ("Discovery questions to carry forward", "bullets"),
                    ("Carried-forward input for Activity 1.2", "bullets"),
                ],
            },
            {
                "stage": "Activity 1.2",
                "purpose": "Interviews and evidence synthesis",
                "input_file": "package_b_activity_1_2_input.md",
                "working_file": "package_b_activity_1_2_insight_summary.md",
                "review_file": "package_b_activity_1_2_review.md",
                "working_title": "Package B - Activity 1.2 output",
                "working_sections": [
                    ("Research objective", "text"),
                    ("Top user needs", "bullets"),
                    ("Main barriers", "bullets"),
                    ("Decision criteria and moments of uncertainty", "bullets"),
                    ("Workarounds or coping behavior", "bullets"),
                    ("Conflicts or surprises", "bullets"),
                    ("Carried-forward input for Activity 2.1", "bullets"),
                ],
            },
            {
                "stage": "Activity 2.1",
                "purpose": "Current-state journey synthesis",
                "input_file": "package_b_activity_2_1_input.md",
                "working_file": "package_b_activity_2_1_current_state_journey_summary.md",
                "review_file": "package_b_activity_2_1_review.md",
                "working_title": "Package B - Activity 2.1 output",
                "working_sections": [
                    ("Current-state journey summary", "text"),
                    ("Main breakdowns", "numbered"),
                    ("Teams, systems, and handoffs involved", "bullets"),
                    ("Opportunity areas", "bullets"),
                    ("Decision criteria for the future-state concept", "bullets"),
                    ("Validation gaps", "bullets"),
                    ("Carried-forward input for Activity 3.1", "bullets"),
                ],
            },
            {
                "stage": "Activity 3.1",
                "purpose": "Future-state concept and service changes",
                "input_file": "package_b_activity_3_1_input.md",
                "working_file": "package_b_activity_3_1_future_state_concept_summary.md",
                "review_file": "package_b_activity_3_1_review.md",
                "working_title": "Package B - Activity 3.1 output",
                "working_sections": [
                    ("Future-state concept objective", "text"),
                    ("Future-state journey summary", "bullets"),
                    ("Experience principles", "bullets"),
                    ("Required service changes", "bullets"),
                    ("Dependencies and constraints", "bullets"),
                    ("Prototype moments to make tangible next", "bullets"),
                    ("Carried-forward input for Activity 4.1", "bullets"),
                ],
            },
            {
                "stage": "Activity 4.1",
                "purpose": "Prototype brief and prioritization",
                "input_file": "package_b_activity_4_1_input.md",
                "working_file": "package_b_activity_4_1_prioritization_and_prototype_summary.md",
                "review_file": "package_b_activity_4_1_review.md",
                "working_title": "Package B - Activity 4.1 output",
                "working_sections": [
                    ("Prototype objective", "text"),
                    ("Prototype scope and interactions", "bullets"),
                    ("Prioritization criteria", "bullets"),
                    ("Build first", "bullets"),
                    ("Defer", "bullets"),
                    ("Validate next", "bullets"),
                    ("Risks and dependencies", "bullets"),
                    ("Carried-forward input for the final deliverable", "bullets"),
                ],
            },
        ],
    },
    ("english", "C"): {
        "library": TEMPLATES_DIR / "English" / "Package_C" / "package_c_template_library.md",
        "package_label": "Package C",
        "language_label": "English",
        "project_status": "Setup complete",
        "current_stage": "Stage 0 - Intake check before Activity 1.1",
        "next_action": "Run the guided Stage 0 intake dialogue and validate the intake before Activity 1.1 starts.",
        "final_seed_files": [
            "package_c_final_deliverable.md",
            "package_c_prototype_prompt_pack.md",
            "package_c_prototype_record.md",
        ],
        "final_artifacts": [
            {"deliverable": "Executive brief", "file": "package_c_final_deliverable.md"},
            {"deliverable": "Current-state service blueprint summary", "file": "package_c_final_deliverable.md"},
            {"deliverable": "Tested future-state service model", "file": "package_c_final_deliverable.md"},
            {"deliverable": "Phased roadmap and business case summary", "file": "package_c_final_deliverable.md"},
            {"deliverable": "Optional prototype prompt pack", "file": "package_c_prototype_prompt_pack.md"},
            {"deliverable": "Optional high-risk journey-slice prototype record", "file": "package_c_prototype_record.md"},
        ],
        "stages": [
            {
                "stage": "Stage 0",
                "purpose": "Intake check before Activity 1.1",
                "input_file": "package_c_stage_0_intake_input.md",
                "working_file": "package_c_stage_0_intake_summary.md",
                "review_file": "package_c_stage_0_intake_check.md",
                "working_title": "Package C - Stage 0 output",
                "working_sections": [
                    ("Intake summary", "text"),
                    ("Strategic or investment decisions to support", "bullets"),
                    ("Scope boundaries", "bullets"),
                    ("Known evidence and stakeholder picture", "bullets"),
                    ("Intake gaps or risks", "bullets"),
                    ("Recommended next step", "text"),
                    ("Validation question", "text"),
                ],
            },
            {
                "stage": "Activity 1.1",
                "purpose": "Executive and service-owner interviews",
                "input_file": "package_c_activity_1_1_input.md",
                "working_file": "package_c_activity_1_1_strategic_framing_summary.md",
                "review_file": "package_c_activity_1_1_review.md",
                "working_title": "Package C - Activity 1.1 output",
                "working_sections": [
                    ("Strategic framing summary", "text"),
                    ("Service problem and value at stake", "text"),
                    ("Strategic priorities and tensions", "bullets"),
                    ("Investment questions", "bullets"),
                    ("Risks and watchouts", "bullets"),
                    ("Carried-forward input for Activity 1.2", "bullets"),
                ],
            },
            {
                "stage": "Activity 1.2",
                "purpose": "Service scope and fieldwork framing",
                "input_file": "package_c_activity_1_2_input.md",
                "working_file": "package_c_activity_1_2_service_scope_summary.md",
                "review_file": "package_c_activity_1_2_review.md",
                "working_title": "Package C - Activity 1.2 output",
                "working_sections": [
                    ("Service scope agreed", "text"),
                    ("Departments, channels, and systems in scope", "bullets"),
                    ("Critical service moments", "bullets"),
                    ("In-scope and out-of-scope boundaries", "bullets"),
                    ("Fieldwork focus areas", "bullets"),
                    ("Carried-forward input for Activity 2.1", "bullets"),
                ],
            },
            {
                "stage": "Activity 2.1",
                "purpose": "Operational observation synthesis",
                "input_file": "package_c_activity_2_1_input.md",
                "working_file": "package_c_activity_2_1_operational_observation_summary.md",
                "review_file": "package_c_activity_2_1_review.md",
                "working_title": "Package C - Activity 2.1 output",
                "working_sections": [
                    ("Operational evidence summary", "text"),
                    ("Workarounds observed", "bullets"),
                    ("Delays or hidden effort", "bullets"),
                    ("Ownership gaps", "bullets"),
                    ("Breakdowns across channels, teams, or systems", "bullets"),
                    ("Questions for blueprinting", "bullets"),
                    ("Carried-forward input for Activity 2.2", "bullets"),
                ],
            },
            {
                "stage": "Activity 2.2",
                "purpose": "Current-state blueprint synthesis",
                "input_file": "package_c_activity_2_2_input.md",
                "working_file": "package_c_activity_2_2_blueprint_summary.md",
                "review_file": "package_c_activity_2_2_review.md",
                "working_title": "Package C - Activity 2.2 output",
                "working_sections": [
                    ("Current-state blueprint summary", "text"),
                    ("Front-stage interactions", "bullets"),
                    ("Back-stage processes", "bullets"),
                    ("Delays, duplication, and value leaks", "bullets"),
                    ("Ownership gaps", "bullets"),
                    ("Main blueprint implications", "bullets"),
                    ("Carried-forward input for Activity 3.1", "bullets"),
                ],
            },
            {
                "stage": "Activity 3.1",
                "purpose": "Future-state service model and validation",
                "input_file": "package_c_activity_3_1_input.md",
                "working_file": "package_c_activity_3_1_future_state_service_model_summary.md",
                "review_file": "package_c_activity_3_1_review.md",
                "working_title": "Package C - Activity 3.1 output",
                "working_sections": [
                    ("Future-state objective", "text"),
                    ("Target-state service model", "bullets"),
                    ("Changes across channels, teams, systems, and ownership", "bullets"),
                    ("Validation signals", "bullets"),
                    ("Feasibility concerns or dependencies", "bullets"),
                    ("Selected high-risk journey slice for optional prototype support", "text"),
                    ("Carried-forward input for Activity 4.1", "bullets"),
                ],
            },
            {
                "stage": "Activity 4.1",
                "purpose": "Roadmap and business case synthesis",
                "input_file": "package_c_activity_4_1_input.md",
                "working_file": "package_c_activity_4_1_roadmap_and_business_case_summary.md",
                "review_file": "package_c_activity_4_1_review.md",
                "working_title": "Package C - Activity 4.1 output",
                "working_sections": [
                    ("Strategic decision this output should support", "text"),
                    ("What should happen now", "bullets"),
                    ("What should happen next", "bullets"),
                    ("What should happen later", "bullets"),
                    ("Dependencies and decision points", "bullets"),
                    ("ROI hypothesis or value logic", "bullets"),
                    ("Risks and assumptions", "bullets"),
                    ("Carried-forward input for the final deliverable", "bullets"),
                ],
            },
        ],
    },
    ("danish", "A"): {
        "library": TEMPLATES_DIR / "Danish" / "Package_A" / "package_a_template_library_danish.md",
        "package_label": "Pakke A",
        "language_label": "Dansk",
        "project_status": "Opsaetning fuldfoert",
        "current_stage": "Trin 0 - Intake-check foer Aktivitet 1.1",
        "next_action": "Koer den guidede Trin 0-intake-dialog og valider intaken, foer Aktivitet 1.1 starter.",
        "final_seed_files": [
            "package_a_final_deliverable.md",
            "package_a_prototype_prompt_pack.md",
            "package_a_prototype_record.md",
        ],
        "final_artifacts": [
            {"deliverable": "Anbefalingsoplaeg", "file": "package_a_final_deliverable.md"},
            {"deliverable": "Kort over de vigtigste brud i det valgte trin i rejsen", "file": "package_a_final_deliverable.md"},
            {"deliverable": "Risici og naeste skridt", "file": "package_a_final_deliverable.md"},
            {"deliverable": "Prototype prompt pack", "file": "package_a_prototype_prompt_pack.md"},
            {"deliverable": "Registrering af klikbar prototype", "file": "package_a_prototype_record.md"},
        ],
        "stages": [
            {
                "stage": "Trin 0",
                "purpose": "Intake-check foer Aktivitet 1.1",
                "input_file": "package_a_stage_0_intake_input.md",
                "working_file": "package_a_stage_0_intake_summary.md",
                "review_file": "package_a_stage_0_intake_check.md",
                "working_title": "Pakke A - Trin 0 output",
                "working_sections": [
                    ("Opsummering af intake", "text"),
                    ("Beslutning der skal understoettes", "text"),
                    ("Scopegraenser", "bullets"),
                    ("Kendt evidens og signaler", "bullets"),
                    ("Huller eller risici i intaken", "bullets"),
                    ("Anbefalet naeste skridt", "text"),
                    ("Valideringsspoergsmaal", "text"),
                ],
            },
            {
                "stage": "Aktivitet 1.1",
                "purpose": "Sponsorworkshop og beslutningsramme",
                "input_file": "package_a_activity_1_1_input.md",
                "working_file": "package_a_activity_1_1_decision_frame.md",
                "review_file": "package_a_activity_1_1_review.md",
                "working_title": "Pakke A - Aktivitet 1.1 output",
                "working_sections": [
                    ("Beslutningsramme", "text"),
                    ("Bekraeftet forretningsspoergsmaal", "text"),
                    ("Succeskriterier og baseline-logik", "bullets"),
                    ("Faste begraensninger", "bullets"),
                    ("Antagelser eller uenigheder", "bullets"),
                    ("Aabne sprintspoergsmaal", "bullets"),
                    ("Input der foeres videre til Aktivitet 1.2", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 1.2",
                "purpose": "Evidensreview og signalindramning",
                "input_file": "package_a_activity_1_2_input.md",
                "working_file": "package_a_activity_1_2_evidence_synthesis.md",
                "review_file": "package_a_activity_1_2_review.md",
                "working_title": "Pakke A - Aktivitet 1.2 output",
                "working_sections": [
                    ("Formaaling med evidensen", "text"),
                    ("Staerkest underbyggede fund", "numbered"),
                    ("Retningsgivende signaler", "bullets"),
                    ("Antagelser og evidenshuller", "bullets"),
                    ("Implikationer for det valgte trin", "bullets"),
                    ("Input der foeres videre til Aktivitet 1.3", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 1.3",
                "purpose": "Kortlaegning af sammenbrud i rejsetrinnet",
                "input_file": "package_a_activity_1_3_input.md",
                "working_file": "package_a_activity_1_3_breakdown_map.md",
                "review_file": "package_a_activity_1_3_review.md",
                "working_title": "Pakke A - Aktivitet 1.3 output",
                "working_sections": [
                    ("Trin i rejsen i scope", "text"),
                    ("Aktoerer og afhaengigheder", "bullets"),
                    ("Stoerste sammenbrud", "numbered"),
                    ("Hvorfor sammenbruddene er vigtige", "bullets"),
                    ("Interne implikationer", "bullets"),
                    ("Valideringshuller", "bullets"),
                    ("Input der foeres videre til Aktivitet 2.1", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 2.1",
                "purpose": "Review af konceptretning",
                "input_file": "package_a_activity_2_1_input.md",
                "working_file": "package_a_activity_2_1_direction_review.md",
                "review_file": "package_a_activity_2_1_review.md",
                "working_title": "Pakke A - Aktivitet 2.1 output",
                "working_sections": [
                    ("Beslutning dette review skal understoette", "text"),
                    ("Sammenlignede retninger", "bullets"),
                    ("Opsummering af sammenligningen", "bullets"),
                    ("Foretrukken retning", "text"),
                    ("Tradeoffs", "bullets"),
                    ("Risici og afhaengigheder", "bullets"),
                    ("Aabne checks foer endelig anbefaling", "bullets"),
                    ("Input der foeres videre til Aktivitet 3.1", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 3.1",
                "purpose": "Endelig anbefaling og prototypebrief",
                "input_file": "package_a_activity_3_1_input.md",
                "working_file": "package_a_activity_3_1_recommendation_draft.md",
                "review_file": "package_a_activity_3_1_review.md",
                "working_title": "Pakke A - Aktivitet 3.1 output",
                "working_sections": [
                    ("Opsummering af anbefalingen", "text"),
                    ("Anbefalet retning", "text"),
                    ("Hvorfor denne retning er staerkere", "bullets"),
                    ("Byg nu", "bullets"),
                    ("Udskyd", "bullets"),
                    ("Valider naeste", "bullets"),
                    ("Input til prototypebrief", "bullets"),
                    ("Risici og afhaengigheder", "bullets"),
                    ("Input der foeres videre til den endelige leverance", "bullets"),
                ],
            },
        ],
    },
    ("danish", "B"): {
        "library": TEMPLATES_DIR / "Danish" / "Package_B" / "package_b_template_library_danish.md",
        "package_label": "Pakke B",
        "language_label": "Dansk",
        "project_status": "Opsaetning fuldfoert",
        "current_stage": "Trin 0 - Intake-check foer Aktivitet 1.1",
        "next_action": "Koer den guidede Trin 0-intake-dialog og valider intaken, foer Aktivitet 1.1 starter.",
        "final_seed_files": [
            "package_b_final_deliverable.md",
            "package_b_prototype_prompt_pack.md",
            "package_b_prototype_record.md",
        ],
        "final_artifacts": [
            {"deliverable": "Indsigtsopsamling fra interviews", "file": "package_b_final_deliverable.md"},
            {"deliverable": "Opsummering af nuvaerende og fremtidig rejse", "file": "package_b_final_deliverable.md"},
            {"deliverable": "Noedvendige serviceaendringer paa tvaers af proces, indhold, ejerskab og data", "file": "package_b_final_deliverable.md"},
            {"deliverable": "Prototype prompt pack", "file": "package_b_prototype_prompt_pack.md"},
            {"deliverable": "Registrering af klikbar prototype", "file": "package_b_prototype_record.md"},
            {"deliverable": "Prioriteret leveranceanbefaling", "file": "package_b_final_deliverable.md"},
        ],
        "stages": [
            {
                "stage": "Trin 0",
                "purpose": "Intake-check foer Aktivitet 1.1",
                "input_file": "package_b_stage_0_intake_input.md",
                "working_file": "package_b_stage_0_intake_summary.md",
                "review_file": "package_b_stage_0_intake_check.md",
                "working_title": "Pakke B - Trin 0 output",
                "working_sections": [
                    ("Opsummering af intake", "text"),
                    ("Beslutninger denne pakke skal understoette", "bullets"),
                    ("Scopegraenser", "bullets"),
                    ("Kendt evidens og maalbrugere", "bullets"),
                    ("Huller eller risici i intaken", "bullets"),
                    ("Anbefalet naeste skridt", "text"),
                    ("Valideringsspoergsmaal", "text"),
                ],
            },
            {
                "stage": "Aktivitet 1.1",
                "purpose": "Afklaringsworkshop og undersoegelsesramme",
                "input_file": "package_b_activity_1_1_input.md",
                "working_file": "package_b_activity_1_1_scope_summary.md",
                "review_file": "package_b_activity_1_1_review.md",
                "working_title": "Pakke B - Aktivitet 1.1 output",
                "working_sections": [
                    ("Opsummering af scope", "text"),
                    ("Beslutninger denne pakke skal understoette", "bullets"),
                    ("Rejse og brugere i scope", "bullets"),
                    ("Succeskriterier og baseline-logik", "bullets"),
                    ("Begraensninger, antagelser eller uenigheder", "bullets"),
                    ("Spoergsmaal der foeres videre", "bullets"),
                    ("Input der foeres videre til Aktivitet 1.2", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 1.2",
                "purpose": "Interviews og syntese af evidens",
                "input_file": "package_b_activity_1_2_input.md",
                "working_file": "package_b_activity_1_2_insight_summary.md",
                "review_file": "package_b_activity_1_2_review.md",
                "working_title": "Pakke B - Aktivitet 1.2 output",
                "working_sections": [
                    ("Formaaling med researchen", "text"),
                    ("Top brugerbehov", "bullets"),
                    ("Vigtigste barrierer", "bullets"),
                    ("Beslutningskriterier og usikkerhedsmomenter", "bullets"),
                    ("Workarounds eller coping-adfaerd", "bullets"),
                    ("Konflikter eller overraskelser", "bullets"),
                    ("Input der foeres videre til Aktivitet 2.1", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 2.1",
                "purpose": "Syntese af den nuvaerende rejse",
                "input_file": "package_b_activity_2_1_input.md",
                "working_file": "package_b_activity_2_1_current_state_journey_summary.md",
                "review_file": "package_b_activity_2_1_review.md",
                "working_title": "Pakke B - Aktivitet 2.1 output",
                "working_sections": [
                    ("Opsummering af den nuvaerende rejse", "text"),
                    ("Vigtigste sammenbrud", "numbered"),
                    ("Involverede teams, systemer og handoffs", "bullets"),
                    ("Mulighedsomraader", "bullets"),
                    ("Beslutningskriterier for target state-konceptet", "bullets"),
                    ("Valideringshuller", "bullets"),
                    ("Input der foeres videre til Aktivitet 3.1", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 3.1",
                "purpose": "Fremtidigt koncept og serviceaendringer",
                "input_file": "package_b_activity_3_1_input.md",
                "working_file": "package_b_activity_3_1_future_state_concept_summary.md",
                "review_file": "package_b_activity_3_1_review.md",
                "working_title": "Pakke B - Aktivitet 3.1 output",
                "working_sections": [
                    ("Formaaling med target state-konceptet", "text"),
                    ("Opsummering af den fremtidige rejse", "bullets"),
                    ("Oplevelsesprincipper", "bullets"),
                    ("Noedvendige serviceaendringer", "bullets"),
                    ("Afhaengigheder og begraensninger", "bullets"),
                    ("Prototypeoejeblikke der skal goeres konkrete", "bullets"),
                    ("Input der foeres videre til Aktivitet 4.1", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 4.1",
                "purpose": "Prototypebrief og prioritering",
                "input_file": "package_b_activity_4_1_input.md",
                "working_file": "package_b_activity_4_1_prioritization_and_prototype_summary.md",
                "review_file": "package_b_activity_4_1_review.md",
                "working_title": "Pakke B - Aktivitet 4.1 output",
                "working_sections": [
                    ("Prototypeobjektiv", "text"),
                    ("Prototypescope og interaktioner", "bullets"),
                    ("Prioriteringskriterier", "bullets"),
                    ("Byg foerst", "bullets"),
                    ("Udskyd", "bullets"),
                    ("Valider naeste", "bullets"),
                    ("Risici og afhaengigheder", "bullets"),
                    ("Input der foeres videre til den endelige leverance", "bullets"),
                ],
            },
        ],
    },
    ("danish", "C"): {
        "library": TEMPLATES_DIR / "Danish" / "Package_C" / "package_c_template_library_danish.md",
        "package_label": "Pakke C",
        "language_label": "Dansk",
        "project_status": "Opsaetning fuldfoert",
        "current_stage": "Trin 0 - Intake-check foer Aktivitet 1.1",
        "next_action": "Koer den guidede Trin 0-intake-dialog og valider intaken, foer Aktivitet 1.1 starter.",
        "final_seed_files": [
            "package_c_final_deliverable.md",
            "package_c_prototype_prompt_pack.md",
            "package_c_prototype_record.md",
        ],
        "final_artifacts": [
            {"deliverable": "Ledelsesoplaeg", "file": "package_c_final_deliverable.md"},
            {"deliverable": "Opsummering af blueprint over den nuvaerende service", "file": "package_c_final_deliverable.md"},
            {"deliverable": "Testet fremtidig servicemodel", "file": "package_c_final_deliverable.md"},
            {"deliverable": "Faseopdelt roadmap og business case-opsummering", "file": "package_c_final_deliverable.md"},
            {"deliverable": "Valgfri prototype prompt pack", "file": "package_c_prototype_prompt_pack.md"},
            {"deliverable": "Valgfri registrering af prototype for hoejrisiko-udsnit", "file": "package_c_prototype_record.md"},
        ],
        "stages": [
            {
                "stage": "Trin 0",
                "purpose": "Intake-check foer Aktivitet 1.1",
                "input_file": "package_c_stage_0_intake_input.md",
                "working_file": "package_c_stage_0_intake_summary.md",
                "review_file": "package_c_stage_0_intake_check.md",
                "working_title": "Pakke C - Trin 0 output",
                "working_sections": [
                    ("Opsummering af intake", "text"),
                    ("Strategiske eller investeringsmaessige beslutninger der skal understoettes", "bullets"),
                    ("Scopegraenser", "bullets"),
                    ("Kendt evidens og interessentbillede", "bullets"),
                    ("Huller eller risici i intaken", "bullets"),
                    ("Anbefalet naeste skridt", "text"),
                    ("Valideringsspoergsmaal", "text"),
                ],
            },
            {
                "stage": "Aktivitet 1.1",
                "purpose": "Interviews med ledere og serviceansvarlige",
                "input_file": "package_c_activity_1_1_input.md",
                "working_file": "package_c_activity_1_1_strategic_framing_summary.md",
                "review_file": "package_c_activity_1_1_review.md",
                "working_title": "Pakke C - Aktivitet 1.1 output",
                "working_sections": [
                    ("Opsummering af den strategiske indramning", "text"),
                    ("Serviceproblemet og vaerdien paa spil", "text"),
                    ("Strategiske prioriteringer og spaendinger", "bullets"),
                    ("Investeringsspoergsmaal", "bullets"),
                    ("Risici og opmaerksomhedspunkter", "bullets"),
                    ("Input der foeres videre til Aktivitet 1.2", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 1.2",
                "purpose": "Service-scope og ramme for fieldwork",
                "input_file": "package_c_activity_1_2_input.md",
                "working_file": "package_c_activity_1_2_service_scope_summary.md",
                "review_file": "package_c_activity_1_2_review.md",
                "working_title": "Pakke C - Aktivitet 1.2 output",
                "working_sections": [
                    ("Aftalt service-scope", "text"),
                    ("Afdelinger, kanaler og systemer i scope", "bullets"),
                    ("Kritiske servicemomenter", "bullets"),
                    ("Graenser for i scope og uden for scope", "bullets"),
                    ("Fokusomraader for fieldwork", "bullets"),
                    ("Input der foeres videre til Aktivitet 2.1", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 2.1",
                "purpose": "Syntese af operationelle observationer",
                "input_file": "package_c_activity_2_1_input.md",
                "working_file": "package_c_activity_2_1_operational_observation_summary.md",
                "review_file": "package_c_activity_2_1_review.md",
                "working_title": "Pakke C - Aktivitet 2.1 output",
                "working_sections": [
                    ("Opsummering af operationel evidens", "text"),
                    ("Observerede workarounds", "bullets"),
                    ("Forsinkelser eller skjult indsats", "bullets"),
                    ("Ejerskabsgab", "bullets"),
                    ("Sammenbrud paa tvaers af kanaler, teams eller systemer", "bullets"),
                    ("Spoergsmaal til blueprintarbejdet", "bullets"),
                    ("Input der foeres videre til Aktivitet 2.2", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 2.2",
                "purpose": "Syntese af nuvaerende blueprint",
                "input_file": "package_c_activity_2_2_input.md",
                "working_file": "package_c_activity_2_2_blueprint_summary.md",
                "review_file": "package_c_activity_2_2_review.md",
                "working_title": "Pakke C - Aktivitet 2.2 output",
                "working_sections": [
                    ("Opsummering af nuvaerende blueprint", "text"),
                    ("Frontstage-interaktioner", "bullets"),
                    ("Backstage-processer", "bullets"),
                    ("Forsinkelser, duplikation og vaerdilaek", "bullets"),
                    ("Ejerskabsgab", "bullets"),
                    ("Vigtigste implikationer fra blueprintet", "bullets"),
                    ("Input der foeres videre til Aktivitet 3.1", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 3.1",
                "purpose": "Fremtidig servicemodel og validering",
                "input_file": "package_c_activity_3_1_input.md",
                "working_file": "package_c_activity_3_1_future_state_service_model_summary.md",
                "review_file": "package_c_activity_3_1_review.md",
                "working_title": "Pakke C - Aktivitet 3.1 output",
                "working_sections": [
                    ("Formaaling med target state", "text"),
                    ("Target state-servicemodel", "bullets"),
                    ("Aendringer paa tvaers af kanaler, teams, systemer og ejerskab", "bullets"),
                    ("Valideringssignaler", "bullets"),
                    ("Feasibility-bekymringer eller afhaengigheder", "bullets"),
                    ("Udvalgt hoejrisiko-udsnit af rejsen til valgfri prototypestotte", "text"),
                    ("Input der foeres videre til Aktivitet 4.1", "bullets"),
                ],
            },
            {
                "stage": "Aktivitet 4.1",
                "purpose": "Roadmap og syntese af business case",
                "input_file": "package_c_activity_4_1_input.md",
                "working_file": "package_c_activity_4_1_roadmap_and_business_case_summary.md",
                "review_file": "package_c_activity_4_1_review.md",
                "working_title": "Pakke C - Aktivitet 4.1 output",
                "working_sections": [
                    ("Strategisk beslutning dette output skal understoette", "text"),
                    ("Hvad der skal ske nu", "bullets"),
                    ("Hvad der skal ske naeste", "bullets"),
                    ("Hvad der skal ske senere", "bullets"),
                    ("Afhaengigheder og beslutningspunkter", "bullets"),
                    ("ROI-hypotese eller vaerdilogik", "bullets"),
                    ("Risici og antagelser", "bullets"),
                    ("Input der foeres videre til den endelige leverance", "bullets"),
                ],
            },
        ],
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a package project folder and seed the relevant templates."
    )
    parser.add_argument("--project-name", required=True, help="The project name to use.")
    parser.add_argument(
        "--package",
        required=True,
        help="Package to bootstrap: A, B, or C.",
    )
    parser.add_argument(
        "--language",
        default="english",
        help="Working language: english or danish.",
    )
    parser.add_argument(
        "--allow-existing",
        action="store_true",
        help="Allow using an existing project folder and create only missing files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing files.",
    )
    return parser.parse_args()


def normalize_package(value: str) -> str:
    package = value.strip().upper()
    if package not in {"A", "B", "C"}:
        raise ValueError("Package must be A, B, or C.")
    return package


def normalize_language(value: str) -> str:
    normalized = value.strip().lower()
    aliases = {"en": "english", "eng": "english", "da": "danish", "dk": "danish"}
    normalized = aliases.get(normalized, normalized)
    if normalized not in {"english", "danish"}:
        raise ValueError("Language must be english or danish.")
    return normalized


def normalize_project_name(value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9]+", "-", value.strip())
    normalized = normalized.strip("-")
    if not normalized:
        raise ValueError("Project name must contain at least one letter or number.")
    return normalized


def extract_md_code_blocks(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```md\n(.*?)```", text, flags=re.DOTALL)
    return [block.rstrip() + "\n" for block in blocks]


def final_artifacts_for_config(config: dict[str, object]) -> list[dict[str, str]]:
    artifacts = config.get("final_artifacts")
    if artifacts:
        return artifacts  # type: ignore[return-value]
    return [
        {"deliverable": deliverable, "file": config["final_file"]}  # type: ignore[index]
        for deliverable in config["final_deliverables"]  # type: ignore[index]
    ]


def final_seed_files_for_config(config: dict[str, object]) -> list[str]:
    seed_files = config.get("final_seed_files")
    if seed_files:
        return list(seed_files)  # type: ignore[arg-type]
    return [config["final_file"]]  # type: ignore[list-item]


def build_project_setup_content(
    project_name: str, folder_name: str, package: str, language: str
) -> str:
    created = date.today().isoformat()
    if language == "danish":
        return f"""# Projektopsaetning

## Projektnavn
{project_name}

## Mappenavn
{folder_name}

## Pakke
Pakke {package}

## Arbejdssprog
Dansk

## Sponsor eller primaer kundeansvarlig
[Tekst]

## Oprettelsesdato
{created}

## Status
Opsaetning fuldfoert

## Kontrolcenter
project_index.md

## Regel for opbevaring
Alle projektgenererede filer for dette forloeb gemmes inde i denne projektmappe.

## Noter
{shared_prep_note(language)}
* [Note]
"""

    return f"""# Project setup

## Project name
{project_name}

## Folder name
{folder_name}

## Package
Package {package}

## Working language
English

## Sponsor or main client owner
[Text]

## Created date
{created}

## Status
Setup complete

## Control center
project_index.md

## Storage rule
All project-generated files for this engagement are stored inside this project folder.

## Notes
{shared_prep_note(language)}
* [Note]
"""


def build_placeholder(kind: str, language: str) -> str:
    if language == "danish":
        if kind == "text":
            return "[Tekst]"
        if kind == "bullets":
            return "* [Punkt]\n* [Punkt]"
        if kind == "numbered":
            return "1. [Punkt]\n2. [Punkt]\n3. [Punkt]"
    else:
        if kind == "text":
            return "[Text]"
        if kind == "bullets":
            return "* [Point]\n* [Point]"
        if kind == "numbered":
            return "1. [Point]\n2. [Point]\n3. [Point]"
    raise ValueError(f"Unsupported placeholder kind: {kind}")


def build_working_output_content(
    title: str, sections: list[tuple[str, str]], language: str
) -> str:
    parts = [f"# {title}", ""]
    for heading, kind in sections:
        parts.append(f"## {heading}")
        parts.append(build_placeholder(kind, language))
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def build_review_content(
    project_name: str,
    package_label: str,
    stage_label: str,
    purpose: str,
    input_relative_path: str,
    working_relative_path: str,
    language: str,
) -> str:
    today = date.today().isoformat()
    if language == "danish":
        return f"""# Aktivitetreview og validering

## Projekt
{project_name}

## Pakke og trin
{package_label} - {stage_label}

## Aktivitet eller output der reviewes
{purpose}

## Filer eller output gennemgaaet
* `{working_relative_path}`
* `{input_relative_path}`

## Opsummering af review
[Tekst]

## Hvad der er valideret som bekraeftet input
* [Punkt]
* [Punkt]

## Oenskede aendringer
* [Aendring]
* [Aendring]

## Aabne spoergsmaal eller risici
* [Spoergsmaal eller risiko]
* [Spoergsmaal eller risiko]

## Valideringsbeslutning
[Valideret / Valideret med aendringer / Ikke valideret]

## Naeste noedvendige input
[Tekst]

## Reviewer
[Tekst]

## Reviewdato
{today}
"""

    return f"""# Activity review and validation

## Project
{project_name}

## Package and stage
{package_label} - {stage_label}

## Activity or output under review
{purpose}

## Files or outputs reviewed
* `{working_relative_path}`
* `{input_relative_path}`

## Review summary
[Text]

## What is validated as confirmed input
* [Confirmed point]
* [Confirmed point]

## Changes requested
* [Change]
* [Change]

## Open questions or risks
* [Question or risk]
* [Question or risk]

## Validation decision
[Validated / Validated with changes / Not validated]

## Next required input
[Text]

## Reviewer
[Text]

## Review date
{today}
"""


def shared_prep_assets_for_package(package: str, language: str) -> list[dict[str, str]]:
    language_key = "danish" if language == "danish" else "english"
    assets: list[dict[str, str]] = []
    for asset_key in PACKAGE_SHARED_PREP_ASSETS[package]:
        asset = SHARED_PREP_ASSET_CONFIG[asset_key]
        assets.append(
            {
                "filename": asset[f"{language_key}_filename"],
                "title": asset[f"{language_key}_title"],
                "use": asset[f"{language_key}_use"],
            }
        )
    return assets


def build_shared_prep_readme(package: str, language: str) -> str:
    assets = shared_prep_assets_for_package(package, language)
    if language == "danish":
        lines = [
            "# Delte forberedelsesaktiver",
            "",
            "Denne mappe er seed'et automatisk ved projektopstart.",
            "",
            "Brug filerne her, naar du skal forberede den virkelige aktivitet og ikke kun AI-syntesen bagefter.",
            "",
            "## Filer i denne mappe",
            "",
            "* `first_live_activity_example_draft_danish.md`: Klar-til-tilpasning-eksempel paa den foerste live-aktivitet i projektet.",
            "* `next_activity_*.md`: Genererede arbejdsfiler til den naeste live-aktivitet. De bliver opdateret automatisk efter review-sync.",
        ]
        for asset in assets:
            lines.append(f"* `{asset['filename']}`: {asset['use']}")
        return "\n".join(lines).rstrip() + "\n"

    lines = [
        "# Shared prep assets",
        "",
        "This folder is seeded automatically when a project starts.",
        "",
        "Use the files here when you need to prepare the real-world activity itself, not just the AI synthesis afterwards.",
        "",
        "## Files in this folder",
        "",
        "* `first_live_activity_example_draft.md`: Ready-to-edit example draft for the first live activity in the project.",
        "* `next_activity_*.md`: Generated working files for the next live activity. These are refreshed automatically after review sync.",
    ]
    for asset in assets:
        lines.append(f"* `{asset['filename']}`: {asset['use']}")
    return "\n".join(lines).rstrip() + "\n"


def first_live_activity_example_filename(language: str) -> str:
    if language == "danish":
        return "first_live_activity_example_draft_danish.md"
    return "first_live_activity_example_draft.md"


def build_first_live_activity_example_draft(
    project_name: str, package: str, language: str
) -> str:
    config = FIRST_LIVE_ACTIVITY_DRAFT_CONFIG[(language, package)]
    package_label = f"Pakke {package}" if language == "danish" else f"Package {package}"
    language_label = "Dansk" if language == "danish" else "English"
    prep_files = "\n".join(f"* `{filename}`" for filename in config["prep_files"])
    roles = "\n".join(f"* {role}" for role in config["roles"])
    prepare = "\n".join(f"* {item}" for item in config["prepare"])
    cover = "\n".join(f"* {item}" for item in config["cover"])
    questions = "\n".join(
        f"{index}. {question}" for index, question in enumerate(config["questions"], start=1)
    )
    capture = "\n".join(f"* {item}" for item in config["capture"])

    if language == "danish":
        session_label = "interviewinvitation" if config["session_type"] == "Interview" else "workshopinvitation"
        return f"""# Eksempelkladde til foerste live-aktivitet

## Projekt
{project_name}

## Pakke
{package_label}

## Arbejdssprog
{language_label}

## Foerste live-aktivitet
{config['activity']}

## Saadan bruges filen
Denne fil er en klar-til-tilpasning startkladde til projektets foerste virkelige aktivitet. Tilpas tekst, deltagere og fokus, foer du sender invitationen eller bruger briefet internt.

## Anbefalede forberedelsesfiler i `shared-prep/`

{prep_files}

## Klar-til-tilpasning {session_label}

**Formaal**
{config['objective']}

**Foreslaaet varighed**
{config['estimated_time']}

**Forslag til deltagere**
{roles}

**Det skal deltagerne forberede eller medbringe**
{prepare}

**Forventet output**
{config['decision_output']}

## Klar-til-tilpasning session brief

### Aktivitetens maal
{config['objective']}

### Beslutningsoutput
{config['decision_output']}

### Estimeret tid
{config['estimated_time']}

### Hvem boer vaere med
{roles}

### Forbered foer sessionen
{prepare}

### Det skal aktiviteten daekke
{cover}

### Kerne-spoergsmaal
{questions}

### Det skal fanges i noterne
{capture}
"""

    session_label = "interview invite" if config["session_type"] == "Interview" else "workshop invite"
    return f"""# First live activity example draft

## Project
{project_name}

## Package
{package_label}

## Working language
{language_label}

## First live activity
{config['activity']}

## How to use this file
This file is a ready-to-edit starting draft for the first real-world activity in the project. Adapt the wording, participants, and focus before sending the invite or using the brief internally.

## Recommended prep files in `shared-prep/`

{prep_files}

## Ready-to-edit {session_label}

**Purpose**
{config['objective']}

**Suggested duration**
{config['estimated_time']}

**Suggested participants**
{roles}

**What participants should prepare or bring**
{prepare}

**Expected output**
{config['decision_output']}

## Ready-to-edit session brief

### Activity objective
{config['objective']}

### Decision output
{config['decision_output']}

### Estimated time
{config['estimated_time']}

### Who should be involved
{roles}

### Prepare before the session
{prepare}

### What the activity should cover
{cover}

### Core questions
{questions}

### What should be captured in the notes
{capture}
"""


def build_project_index_content(
    project_name: str,
    folder_name: str,
    package: str,
    language: str,
) -> str:
    config = PACKAGE_TEMPLATE_CONFIG[(language, package)]
    created = date.today().isoformat()
    if language == "danish":
        workflow_rows = [
            "| Trin | Formaaling | Inputfil | Arbejdsoutput | Reviewfil | Status |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for index, stage in enumerate(config["stages"]):
            status = "Klar til at starte" if index == 0 else "Ikke startet"
            workflow_rows.append(
                "| {stage_label} | {purpose} | `{input_file}` | `{working_file}` | `{review_file}` | {status} |".format(
                    stage_label=stage["stage"],
                    purpose=stage["purpose"],
                    input_file=f"01-inputs/{stage['input_file']}",
                    working_file=f"02-working/{stage['working_file']}",
                    review_file=f"03-reviews/{stage['review_file']}",
                    status=status,
                )
            )

        final_rows = [
            "| Leverance | Hovedfil | Status |",
            "| --- | --- | --- |",
        ]
        for artifact in final_artifacts_for_config(config):
            final_rows.append(
                f"| {artifact['deliverable']} | `04-final/{artifact['file']}` | Kladde oprettet |"
            )

        return f"""# Projektindex

## Projektoversigt

* Projektnavn: {project_name}
* Mappenavn: {folder_name}
* Pakke: Pakke {package}
* Arbejdssprog: {config['language_label']}
* Oprettelsesdato: {created}
* Status: {config['project_status']}
* Nuvaerende trin: {config['current_stage']}
* Delte forberedelsesaktiver: `00-project-setup/{SHARED_PREP_DIRNAME}/`
* Anbefalet naeste handling: {config['next_action']}

## Workflowtracker

{chr(10).join(workflow_rows)}

## Endelige leverancer der skal afsluttes

{chr(10).join(final_rows)}

## Arbejdsregler

* Hold alle projektgenererede filer inde i denne projektmappe.
* Brug `01-inputs/` til raa input og handoffs fra virkelige aktiviteter.
* Brug `02-working/` til synteser og udkast, som endnu ikke er valideret.
* Brug `03-reviews/` til valideringscheckpointet efter hvert trin.
* Brug `00-project-setup/{SHARED_PREP_DIRNAME}/` til seed'ede invitationsskabeloner, session briefs, evidensrequests, readiness-checks, retrospektiver, den klar-til-tilpasning-kladde til den foerste live-aktivitet og de automatisk opdaterede `next_activity_*.md`-filer.
* Naar naeste trin er en virkelig aktivitet, saa gennemfoer foerst aktiviteten og vend derefter tilbage med de faerdige noter i den matchende inputfil.
* Opdater status, nuvaerende trin, naeste handling og `next_activity_*.md`-preppen, naar et review er valideret.
"""

    workflow_rows = [
        "| Stage | Purpose | Input file | Working output | Review file | Status |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for index, stage in enumerate(config["stages"]):
        status = "Ready to start" if index == 0 else "Not started"
        workflow_rows.append(
            "| {stage_label} | {purpose} | `{input_file}` | `{working_file}` | `{review_file}` | {status} |".format(
                stage_label=stage["stage"],
                purpose=stage["purpose"],
                input_file=f"01-inputs/{stage['input_file']}",
                working_file=f"02-working/{stage['working_file']}",
                review_file=f"03-reviews/{stage['review_file']}",
                status=status,
            )
        )

    final_rows = [
        "| Deliverable | Main file | Status |",
        "| --- | --- | --- |",
    ]
    for artifact in final_artifacts_for_config(config):
        final_rows.append(
            f"| {artifact['deliverable']} | `04-final/{artifact['file']}` | Draft seeded |"
        )

    return f"""# Project index

## Project overview

* Project name: {project_name}
* Folder name: {folder_name}
* Package: Package {package}
* Working language: {config['language_label']}
* Created date: {created}
* Status: {config['project_status']}
* Current stage: {config['current_stage']}
* Shared prep assets: `00-project-setup/{SHARED_PREP_DIRNAME}/`
* Recommended next action: {config['next_action']}

## Workflow tracker

{chr(10).join(workflow_rows)}

## Final deliverables to complete

{chr(10).join(final_rows)}

## Working rules

* Keep all project-generated files inside this project folder.
* Use `01-inputs/` for raw input and handoffs from real-world activities.
* Use `02-working/` for syntheses and drafts that are not yet validated.
* Use `03-reviews/` for the validation checkpoint after each stage.
* Use `00-project-setup/{SHARED_PREP_DIRNAME}/` for seeded invite templates, session briefs, evidence requests, readiness checks, retrospectives, the ready-to-edit first live activity draft, and the auto-refreshed `next_activity_*.md` files.
* When the next stage is a real-world activity, run that activity first and then return with the completed notes in the matching input file.
* Update the status, current stage, next action, and `next_activity_*.md` prep when a review checkpoint is validated.
"""


def build_seed_plan(project_name: str, package: str, language: str) -> dict[str, str]:
    folder_name = normalize_project_name(project_name)
    config = PACKAGE_TEMPLATE_CONFIG[(language, package)]
    code_blocks = extract_md_code_blocks(config["library"])
    input_files = [stage["input_file"] for stage in config["stages"]]
    final_seed_files = final_seed_files_for_config(config)
    expected_count = len(input_files) + len(final_seed_files)
    if len(code_blocks) != expected_count:
        raise ValueError(
            f"Template library {config['library']} contains {len(code_blocks)} code blocks; expected {expected_count}."
        )

    files: dict[str, str] = {
        "00-project-setup/project_setup.md": build_project_setup_content(
            project_name, folder_name, package, language
        ),
        "project_index.md": build_project_index_content(
            project_name, folder_name, package, language
        ),
    }

    input_block_count = len(input_files)
    for destination, content in zip(input_files, code_blocks[:input_block_count]):
        files[f"01-inputs/{destination}"] = content

    for stage in config["stages"]:
        files[f"02-working/{stage['working_file']}"] = build_working_output_content(
            stage["working_title"], stage["working_sections"], language
        )
        files[f"03-reviews/{stage['review_file']}"] = build_review_content(
            project_name=project_name,
            package_label=config["package_label"],
            stage_label=stage["stage"],
            purpose=stage["purpose"],
            input_relative_path=f"01-inputs/{stage['input_file']}",
            working_relative_path=f"02-working/{stage['working_file']}",
            language=language,
        )

    for destination, content in zip(final_seed_files, code_blocks[input_block_count:]):
        files[f"04-final/{destination}"] = content

    shared_prep_relative_dir = f"00-project-setup/{SHARED_PREP_DIRNAME}"
    shared_language_dir = "Danish" if language == "danish" else "English"
    files[f"{shared_prep_relative_dir}/README.md"] = build_shared_prep_readme(
        package, language
    )
    files[
        f"{shared_prep_relative_dir}/{first_live_activity_example_filename(language)}"
    ] = build_first_live_activity_example_draft(project_name, package, language)
    for asset in shared_prep_assets_for_package(package, language):
        source = TEMPLATES_DIR / shared_language_dir / "Shared" / asset["filename"]
        files[f"{shared_prep_relative_dir}/{asset['filename']}"] = source.read_text(
            encoding="utf-8"
        )
    return files


def ensure_directories(project_dir: Path, dry_run: bool) -> list[Path]:
    directories = [
        project_dir / "00-project-setup",
        project_dir / "00-project-setup" / SHARED_PREP_DIRNAME,
        project_dir / "01-inputs",
        project_dir / "02-working",
        project_dir / "03-reviews",
        project_dir / "04-final",
    ]
    if not dry_run:
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    return directories


def write_seed_files(
    project_dir: Path, files: dict[str, str], dry_run: bool
) -> tuple[list[Path], list[Path]]:
    created: list[Path] = []
    skipped: list[Path] = []
    for relative_path, content in files.items():
        destination = project_dir / relative_path
        if destination.exists():
            skipped.append(destination)
            continue
        if not dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(content, encoding="utf-8")
        created.append(destination)
    return created, skipped


def main() -> int:
    args = parse_args()
    try:
        package = normalize_package(args.package)
        language = normalize_language(args.language)
        folder_name = normalize_project_name(args.project_name)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    project_dir = PROJECTS_DIR / folder_name
    if project_dir.exists() and not args.allow_existing:
        print(
            f"Error: {project_dir} already exists. Re-run with --allow-existing if you want to seed missing files into it.",
            file=sys.stderr,
        )
        return 1

    try:
        seed_files = build_seed_plan(args.project_name, package, language)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    directories = ensure_directories(project_dir, args.dry_run)
    created_files, skipped_files = write_seed_files(project_dir, seed_files, args.dry_run)

    mode = "Dry run" if args.dry_run else "Bootstrap complete"
    print(f"{mode}:")
    print(f"  Project name: {args.project_name}")
    print(f"  Folder name: {folder_name}")
    print(f"  Package: {package}")
    print(f"  Language: {language}")
    print(f"  Project path: {project_dir}")
    print("  Directories:")
    for directory in directories:
        print(f"    - {directory}")
    print("  Seeded files:")
    for path in created_files:
        print(f"    - {path}")
    if skipped_files:
        print("  Skipped existing files:")
        for path in skipped_files:
            print(f"    - {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
