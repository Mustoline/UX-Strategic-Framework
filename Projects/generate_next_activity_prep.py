#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from bootstrap_project import PACKAGE_TEMPLATE_CONFIG, PROJECTS_DIR, SHARED_PREP_DIRNAME, normalize_project_name
from sync_project_status import (
    clean_placeholder,
    derive_workflow_state,
    get_section,
    normalize_status_value,
    parse_language_key,
    parse_package_letter,
    simplify_text,
    split_sections,
)


STAGE_METADATA = {
    ("A", "Activity 1.1"): {
        "kind": "workshop",
        "english_time": "90 minutes",
        "danish_time": "90 minutter",
    },
    ("A", "Activity 1.2"): {
        "kind": "evidence_review",
        "english_time": "2-4 hours",
        "danish_time": "2-4 timer",
    },
    ("A", "Activity 1.3"): {
        "kind": "mapping_session",
        "english_time": "2 hours",
        "danish_time": "2 timer",
    },
    ("A", "Activity 2.1"): {
        "kind": "concept_review",
        "english_time": "90 minutes",
        "danish_time": "90 minutter",
    },
    ("A", "Activity 3.1"): {
        "kind": "concept_review",
        "english_time": "60-90 minutes",
        "danish_time": "60-90 minutter",
    },
    ("B", "Activity 1.1"): {
        "kind": "workshop",
        "english_time": "2 hours",
        "danish_time": "2 timer",
    },
    ("B", "Activity 1.2"): {
        "kind": "interview",
        "english_time": "5-8 interviews of 45-60 minutes each",
        "danish_time": "5-8 interviews af 45-60 minutter",
    },
    ("B", "Activity 2.1"): {
        "kind": "mapping_session",
        "english_time": "2 hours",
        "danish_time": "2 timer",
    },
    ("B", "Activity 3.1"): {
        "kind": "concept_review",
        "english_time": "2 hours",
        "danish_time": "2 timer",
    },
    ("B", "Activity 4.1"): {
        "kind": "concept_review",
        "english_time": "90 minutes",
        "danish_time": "90 minutter",
    },
    ("C", "Activity 1.1"): {
        "kind": "interview",
        "english_time": "5-7 interviews of 45-60 minutes each",
        "danish_time": "5-7 interviews af 45-60 minutter",
    },
    ("C", "Activity 1.2"): {
        "kind": "evidence_review",
        "english_time": "2-4 hours",
        "danish_time": "2-4 timer",
    },
    ("C", "Activity 2.1"): {
        "kind": "observation",
        "english_time": "1-3 days of observation and evidence capture",
        "danish_time": "1-3 dage med observation og evidensindsamling",
    },
    ("C", "Activity 2.2"): {
        "kind": "mapping_session",
        "english_time": "2-3 hours",
        "danish_time": "2-3 timer",
    },
    ("C", "Activity 3.1"): {
        "kind": "concept_review",
        "english_time": "2-3 hours",
        "danish_time": "2-3 timer",
    },
    ("C", "Activity 4.1"): {
        "kind": "concept_review",
        "english_time": "2 hours",
        "danish_time": "2 timer",
    },
}


KIND_CONFIG = {
    "english": {
        "workshop": {
            "session_type": "Workshop",
            "objective": "Use this workshop to align the next decision-making step and collect the strongest input needed for the next synthesis.",
            "decision_output": "A clearer aligned framing for the next synthesis step.",
            "default_roles": [
                "Decision owner or sponsor",
                "Relevant product, service, or business owner",
                "Relevant commercial, operational, or delivery stakeholders",
            ],
            "prepare": [
                "The last validated output and review notes",
                "Current scope and out-of-scope boundaries",
                "Any evidence or data the session needs to discuss",
            ],
            "evidence_request": [
                "Any missing evidence, dashboards, or exports needed to keep the session grounded",
                "Any background material that helps participants arrive prepared",
            ],
        },
        "evidence_review": {
            "session_type": "Evidence review",
            "objective": "Use this evidence review to separate strong signals from assumptions before the recommendation moves forward.",
            "decision_output": "A clearer evidence picture with supported findings, gaps, and next validation questions.",
            "default_roles": [
                "Analytics or evidence owner",
                "Relevant product or service owner",
                "Anyone holding support, sales, research, or behavior data relevant to the scope",
            ],
            "prepare": [
                "Analytics, exports, or dashboards tied to the in-scope journey or service area",
                "Any segmentation, trend, or behavior view relevant to the decision",
                "Any support, sales, or research signal that can challenge assumptions",
            ],
            "evidence_request": [
                "The strongest available analytics or performance evidence tied to the step or service area in scope",
                "Segmentation by device, user type, basket size, channel, or service context where possible",
                "Any support themes, complaint patterns, prior research, recordings, or operational notes that sharpen the picture",
            ],
        },
        "mapping_session": {
            "session_type": "Mapping session",
            "objective": "Use this mapping session to make breakdowns, handoffs, actors, and dependencies visible enough to support the next decision.",
            "decision_output": "A clearer map of the current state and the breakdowns that matter most.",
            "default_roles": [
                "Owner of the in-scope step, journey, or service area",
                "Relevant cross-functional stakeholders tied to the breakdowns",
                "Facilitator or synthesis owner",
            ],
            "prepare": [
                "The last validated synthesis and open questions",
                "Any process, journey, or service documentation already available",
                "A clear note-taking and capture approach",
            ],
            "evidence_request": [
                "Any existing process maps, service documentation, or operating notes relevant to the in-scope flow",
                "Any evidence that clarifies where the breakdowns happen and who they affect",
            ],
        },
        "concept_review": {
            "session_type": "Review workshop",
            "objective": "Use this review session to compare directions, surface tradeoffs, and clarify what should move forward.",
            "decision_output": "A clearer decision on the preferred direction, tradeoffs, and what needs validation next.",
            "default_roles": [
                "Decision owner or sponsor",
                "Relevant product, service, design, operational, or technical stakeholders",
                "Anyone needed to validate feasibility or commercial fit",
            ],
            "prepare": [
                "The last validated output, options, or concept material",
                "Decision criteria and delivery constraints",
                "Any draft concept, map, or prototype material relevant to the discussion",
            ],
            "evidence_request": [
                "Any missing feasibility, dependency, or delivery information needed to compare options credibly",
                "Any policy, content, operational, or technical input needed to keep the recommendation realistic",
            ],
        },
        "interview": {
            "session_type": "Interview",
            "objective": "Use these interviews to gather first-hand input that can shape the next synthesis step with real evidence rather than assumption.",
            "decision_output": "A sharper understanding of needs, barriers, pressures, or decisions that the package must respond to.",
            "default_roles": [
                "The relevant user, customer, stakeholder, or internal role for this stage",
                "Anyone coordinating access, scheduling, or recruitment where needed",
            ],
            "prepare": [
                "The interview guide or question set for the stage",
                "Any access, recruitment, or consent details that must be handled upfront",
                "Any existing evidence that should shape the interview focus",
            ],
            "evidence_request": [
                "Any access, recruitment support, or permission needed to reach the right participants",
                "Any prior research or performance evidence that should inform the interviews",
            ],
        },
        "observation": {
            "session_type": "Observation and evidence capture",
            "objective": "Use this step to understand how the service operates in practice and where the real pressure points appear.",
            "decision_output": "A clearer view of operational reality, dependencies, and the service pressures that the redesign must account for.",
            "default_roles": [
                "Relevant frontline, operational, or service-owning roles",
                "Anyone needed to grant access to observation, systems, or environments",
            ],
            "prepare": [
                "Observation access, permissions, and timing",
                "The note-taking, privacy, and capture approach",
                "Any current-state process or service documentation already available",
            ],
            "evidence_request": [
                "Any access, permissions, or schedule information needed for observation",
                "Any operational data, current-state documentation, or role mapping that will make the observation more useful",
            ],
        },
    },
    "danish": {
        "workshop": {
            "session_type": "Workshop",
            "objective": "Brug workshoppen til at skabe alignment om naeste beslutningstrin og indsamle det staerkeste input til den naeste syntese.",
            "decision_output": "En tydeligere og mere alignet ramme for naeste syntesetrin.",
            "default_roles": [
                "Beslutningsejer eller sponsor",
                "Relevant produkt-, service- eller forretningsansvarlig",
                "Relevante kommercielle, driftsnaere eller leverancemaessige interessenter",
            ],
            "prepare": [
                "Det senest validerede output og reviewnoter",
                "Aktuelt scope og out-of-scope-graenser",
                "Eventuel evidens eller data som sessionen skal forholde sig til",
            ],
            "evidence_request": [
                "Manglende evidens, dashboards eller eksporter der er noedvendige for at holde sessionen forankret",
                "Baggrundsmateriale der kan hjaelpe deltagerne med at moede forberedte",
            ],
        },
        "evidence_review": {
            "session_type": "Evidensreview",
            "objective": "Brug evidensreviewet til at skille staerke signaler fra antagelser, foer anbefalingen gaar videre.",
            "decision_output": "Et tydeligere evidensbillede med underbyggede fund, huller og naeste valideringsspoergsmaal.",
            "default_roles": [
                "Analyse- eller evidensejer",
                "Relevant produkt- eller serviceansvarlig",
                "Personer med support-, salgs-, research- eller adfaerdsdata relevante for scopet",
            ],
            "prepare": [
                "Analytics, eksporter eller dashboards knyttet til den rejse eller service der er i scope",
                "Segmentering, trends eller adfaerdsvisninger der er relevante for beslutningen",
                "Support-, salgs- eller researchsignaler der kan udfordre antagelserne",
            ],
            "evidence_request": [
                "Den staerkeste tilgaengelige analytics- eller performanceevidens knyttet til det trin eller serviceomraade der er i scope",
                "Segmentering pa tvivce af device, brugertype, kurvstoerrelse, kanal eller servicekontekst hvor det er muligt",
                "Supporttemaer, klagemoenstre, tidligere research, optagelser eller driftsnoter der kan goere billedet skarpere",
            ],
        },
        "mapping_session": {
            "session_type": "Mappingsession",
            "objective": "Brug mappingsessionen til at synliggoere breakdowns, handoffs, aktoerer og afhaengigheder nok til at understoette naeste beslutning.",
            "decision_output": "Et tydeligere kort over nuvaerende situation og de breakdowns der betyder mest.",
            "default_roles": [
                "Ejer af det trin, den rejse eller den service der er i scope",
                "Relevante tvcergaende interessenter knyttet til breakdowns",
                "Facilitator eller synteseansvarlig",
            ],
            "prepare": [
                "Den seneste validerede syntese og de aabne spoergsmaal",
                "Eksisterende proces-, rejse- eller servicedokumentation",
                "En tydelig tilgang til notetagning og capture",
            ],
            "evidence_request": [
                "Eksisterende proceskort, servicedokumentation eller driftsnoter relevante for flowet i scope",
                "Evidens der afklarer hvor breakdowns sker, og hvem de rammer",
            ],
        },
        "concept_review": {
            "session_type": "Reviewworkshop",
            "objective": "Brug reviewsessionen til at sammenligne retninger, synliggoere tradeoffs og afklare hvad der skal videre.",
            "decision_output": "En tydeligere beslutning om foretrukken retning, tradeoffs og hvad der skal valideres naest.",
            "default_roles": [
                "Beslutningsejer eller sponsor",
                "Relevante produkt-, service-, design-, drifts- eller tekniske interessenter",
                "Personer der skal validere feasibility eller kommercielt fit",
            ],
            "prepare": [
                "Det senest validerede output, muligheder eller konceptmateriale",
                "Beslutningskriterier og leverancebegraensninger",
                "Udkast til koncept, kort eller prototype som er relevant for diskussionen",
            ],
            "evidence_request": [
                "Manglende feasibility-, afhaengigheds- eller leveranceinformation der er noedvendig for at sammenligne muligheder trovaerdigt",
                "Manglende policy-, indholds-, drifts- eller teknisk input der skal til for at holde anbefalingen realistisk",
            ],
        },
        "interview": {
            "session_type": "Interview",
            "objective": "Brug interviewene til at indsamle foerstehaandsinput, der kan forme den naeste syntese med reel evidens frem for antagelser.",
            "decision_output": "En skarpere forstaaelse af behov, barrierer, pres eller beslutninger som pakken skal svare paa.",
            "default_roles": [
                "Den relevante bruger-, kunde-, interessent- eller interne rolle for dette trin",
                "Personer der koordinerer adgang, planlaegning eller rekruttering hvor det er noedvendigt",
            ],
            "prepare": [
                "Interviewguide eller spoergesaet til aktiviteten",
                "Adgangs-, rekrutterings- eller samtykkedetaljer der skal afklares paa forhaand",
                "Eksisterende evidens der skal forme interviewfokus",
            ],
            "evidence_request": [
                "Adgang, rekrutteringsstotte eller tilladelser der er noedvendige for at naa de rigtige deltagere",
                "Tidligere research eller performanceevidens der boer informere interviewene",
            ],
        },
        "observation": {
            "session_type": "Observation og evidensindsamling",
            "objective": "Brug dette trin til at forstaa hvordan servicen fungerer i praksis, og hvor de reelle trykpunkter viser sig.",
            "decision_output": "Et tydeligere billede af driftsvirkeligheden, afhaengighederne og det servicepres redesignarbejdet skal tage hoejde for.",
            "default_roles": [
                "Relevante frontline-, drifts- eller serviceejende roller",
                "Personer der skal give adgang til observation, systemer eller miljoeer",
            ],
            "prepare": [
                "Adgang, tilladelser og timing for observationen",
                "Tilgang til notetagning, privatliv og capture",
                "Eventuel eksisterende current-state proces- eller servicedokumentation",
            ],
            "evidence_request": [
                "Adgang, tilladelser eller planlaegningsinformation der er noedvendig for observation",
                "Driftsdata, current-state dokumentation eller rollekortlaegning der kan goere observationen mere brugbar",
            ],
        },
    },
}


SECTION_ALIASES = {
    "client_context": ["Client / context", "Kunde / kontekst"],
    "problem_area": ["Problem area in scope", "Problemomraade i scope"],
    "decision": [
        "Decision to support",
        "Decisions this package should support",
        "Strategic or investment decisions to support",
        "Beslutning at understoette",
        "Beslutninger som pakken skal understoette",
        "Strategiske eller investeringsmaessige beslutninger der skal understoettes",
    ],
    "why_now": ["Why this matters now", "Hvorfor det er vigtigt nu"],
    "participants": [
        "Participants",
        "Stakeholders or teams involved",
        "Stakeholders involved",
        "Interviewed roles",
        "Deltagere",
        "Interessenter eller teams involveret",
        "Involverede interessenter",
        "Interviewede roller",
    ],
    "target_users": [
        "Target users",
        "Users in scope",
        "Journey and users in scope",
        "Maalbrugere",
        "Brugere i scope",
        "Rejse og brugere i scope",
    ],
    "in_scope": ["In scope", "Selected journey in scope", "I scope", "Valgt rejse i scope"],
    "out_of_scope": ["Out of scope", "Out-of-scope items", "Ude af scope", "Ude-af-scope-elementer"],
    "success_measures": ["Success measures discussed", "Success measures", "Succeskriterier", "Succeskriterier drøftet"],
    "constraints": ["Constraints raised", "Known constraints", "Begraensninger rejst", "Kendte begraensninger"],
    "baseline": ["Known baseline metrics", "Known evidence", "Kendte baselinemaael", "Kendt evidens"],
    "open_questions": [
        "Open sprint questions",
        "Open questions or risks",
        "Questions to validate next",
        "Aabne sprintspoergsmaal",
        "Aabne spoergsmaal eller risici",
        "Spoergsmaal der skal valideres naeste gang",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a tailored prep pack for the next live activity in a project."
    )
    parser.add_argument("--project-name", help="Project name to normalize into a project folder.")
    parser.add_argument("--project-path", help="Direct path to the project folder.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which prep files would be created or updated without writing them.",
    )
    args = parser.parse_args()
    if not args.project_name and not args.project_path:
        parser.error("Provide either --project-name or --project-path.")
    return args


def resolve_project_dir(args: argparse.Namespace) -> Path:
    if args.project_path:
        return Path(args.project_path).expanduser().resolve()
    return (PROJECTS_DIR / normalize_project_name(args.project_name)).resolve()


def read_sections(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    return split_sections(path.read_text(encoding="utf-8"))


def extract_section_text(sections: dict[str, str], aliases: list[str]) -> str:
    return clean_placeholder(get_section(sections, *aliases))


def extract_list_items(value: str) -> list[str]:
    items: list[str] = []
    for raw_line in value.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        bullet_match = re.match(r"^[-*]\s+(.*)$", line)
        number_match = re.match(r"^\d+\.\s+(.*)$", line)
        if bullet_match:
            items.append(clean_placeholder(bullet_match.group(1).strip()))
            continue
        if number_match:
            items.append(clean_placeholder(number_match.group(1).strip()))
            continue
        cleaned = clean_placeholder(line)
        if cleaned:
            items.append(cleaned)
    return [item for item in items if item]


def extract_section_items(sections: dict[str, str], aliases: list[str]) -> list[str]:
    return extract_list_items(get_section(sections, *aliases))


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        normalized = item.strip()
        if not normalized:
            continue
        key = normalized.lower()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(normalized)
    return ordered


def markdown_headings(path: Path) -> list[str]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    return [match.group(1).strip() for match in re.finditer(r"^##\s+(.+)$", text, flags=re.M)]


def normalize_heading_for_display(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip())
    return value


def project_relative_path(path: Path) -> str:
    return str(path.relative_to(path.parents[1]))


def canonical_stage_label(stage_label: str) -> str:
    normalized = stage_label.strip()
    if normalized.startswith("Aktivitet "):
        return normalized.replace("Aktivitet ", "Activity ", 1)
    return normalized


def kind_metadata(package: str, stage_label: str, language: str) -> dict[str, str]:
    metadata = STAGE_METADATA.get((package, canonical_stage_label(stage_label)))
    if not metadata:
        raise ValueError(f"Missing stage metadata for Package {package} {stage_label}.")
    kind = metadata["kind"]
    labels = KIND_CONFIG[language][kind]
    return {
        "kind": kind,
        "session_type": labels["session_type"],
        "objective": labels["objective"],
        "decision_output": labels["decision_output"],
        "estimated_time": metadata["english_time"] if language == "english" else metadata["danish_time"],
    }


def default_roles_for_kind(kind: str, language: str) -> list[str]:
    return KIND_CONFIG[language][kind]["default_roles"]


def default_prepare_for_kind(kind: str, language: str) -> list[str]:
    return KIND_CONFIG[language][kind]["prepare"]


def default_evidence_request_for_kind(kind: str, language: str) -> list[str]:
    return KIND_CONFIG[language][kind]["evidence_request"]


def facilitator_guide_reference(package: str, language: str) -> str:
    if language == "danish":
        return f"Packages/Danish/Package_{package}_facilitator_guide_danish.md"
    return f"Packages/English/Package_{package}_facilitator_guide.md"


def generated_prep_filenames(language: str) -> dict[str, str]:
    suffix = "_danish" if language == "danish" else ""
    return {
        "overview": f"next_activity_prep_overview{suffix}.md",
        "invite": f"next_activity_invite_draft{suffix}.md",
        "session_brief": f"next_activity_session_brief{suffix}.md",
        "evidence_request": f"next_activity_evidence_request{suffix}.md",
        "readiness": f"next_activity_readiness_check{suffix}.md",
        "interview_guide": f"next_activity_interview_guide{suffix}.md",
        "mapping_canvas": f"next_activity_mapping_canvas{suffix}.md",
    }


def planned_prep_filenames(kind: str, filenames: dict[str, str]) -> list[str]:
    planned = [
        filenames["overview"],
        filenames["invite"],
        filenames["session_brief"],
        filenames["evidence_request"],
        filenames["readiness"],
    ]
    if kind == "interview":
        planned.append(filenames["interview_guide"])
    if kind == "mapping_session":
        planned.append(filenames["mapping_canvas"])
    return planned


def collect_context(
    project_dir: Path,
    package: str,
    language: str,
    current_stage_index: int,
    stage_results: list[dict[str, str | None]],
) -> dict[str, object]:
    config = PACKAGE_TEMPLATE_CONFIG[(language, package)]
    stage0_sections = read_sections(project_dir / "01-inputs" / config["stages"][0]["input_file"])

    previous_input_sections: dict[str, str] = {}
    previous_review_sections: dict[str, str] = {}
    previous_working_sections: dict[str, str] = {}

    if current_stage_index > 0:
        previous_stage = config["stages"][current_stage_index - 1]
        previous_input_sections = read_sections(project_dir / "01-inputs" / previous_stage["input_file"])
        previous_review_sections = read_sections(project_dir / "03-reviews" / previous_stage["review_file"])
        previous_working_sections = read_sections(project_dir / "02-working" / previous_stage["working_file"])

    decision_to_support = (
        extract_section_text(previous_input_sections, SECTION_ALIASES["decision"])
        or extract_section_text(stage0_sections, SECTION_ALIASES["decision"])
    )
    why_now = (
        extract_section_text(previous_input_sections, SECTION_ALIASES["why_now"])
        or extract_section_text(stage0_sections, SECTION_ALIASES["why_now"])
    )
    client_context = extract_section_text(stage0_sections, SECTION_ALIASES["client_context"])
    problem_area = extract_section_text(stage0_sections, SECTION_ALIASES["problem_area"])
    target_users = unique(
        extract_section_items(previous_input_sections, SECTION_ALIASES["target_users"])
        + extract_section_items(stage0_sections, SECTION_ALIASES["target_users"])
    )
    participants = unique(
        extract_section_items(previous_input_sections, SECTION_ALIASES["participants"])
        + extract_section_items(stage0_sections, SECTION_ALIASES["participants"])
    )
    in_scope = unique(
        extract_section_items(previous_input_sections, SECTION_ALIASES["in_scope"])
        + extract_section_items(stage0_sections, SECTION_ALIASES["in_scope"])
    )
    out_of_scope = unique(
        extract_section_items(previous_input_sections, SECTION_ALIASES["out_of_scope"])
        + extract_section_items(stage0_sections, SECTION_ALIASES["out_of_scope"])
    )
    success_measures = unique(
        extract_section_items(previous_input_sections, SECTION_ALIASES["success_measures"])
        + extract_section_items(previous_working_sections, ["Success measures and baseline logic", "Succeskriterier og baseline-logik"])
    )
    constraints = unique(
        extract_section_items(previous_input_sections, SECTION_ALIASES["constraints"])
        + extract_section_items(stage0_sections, SECTION_ALIASES["constraints"])
        + extract_section_items(previous_working_sections, ["Fixed constraints", "Faste begraensninger"])
    )
    baseline = unique(
        extract_section_items(previous_input_sections, SECTION_ALIASES["baseline"])
        + extract_section_items(stage0_sections, SECTION_ALIASES["baseline"])
    )
    validated_points = extract_section_items(
        previous_review_sections,
        ["What is validated as confirmed input", "Hvad der er valideret som bekraeftet input"],
    )
    open_questions = extract_section_items(previous_review_sections, SECTION_ALIASES["open_questions"])
    review_summary = extract_section_text(previous_review_sections, ["Review summary", "Opsummering af review"])

    carried_forward: list[str] = []
    for key, value in previous_working_sections.items():
        if "carried-forward input" in key or "viderefoert input" in key or "viderefort input" in key:
            carried_forward.extend(extract_list_items(value))
    carried_forward = unique(carried_forward)

    return {
        "client_context": client_context,
        "problem_area": problem_area,
        "decision_to_support": decision_to_support,
        "why_now": why_now,
        "target_users": target_users,
        "participants": participants,
        "in_scope": in_scope,
        "out_of_scope": out_of_scope,
        "success_measures": success_measures,
        "constraints": constraints,
        "baseline": baseline,
        "validated_points": validated_points,
        "open_questions": open_questions,
        "review_summary": review_summary,
        "carried_forward": carried_forward,
    }


def build_capture_fields(next_input_path: Path) -> list[str]:
    fields = []
    for heading in markdown_headings(next_input_path):
        if heading.lower().startswith("package "):
            continue
        fields.append(normalize_heading_for_display(heading))
    return fields


def format_bullets(items: list[str], empty_text: str) -> str:
    if not items:
        return f"* {empty_text}"
    return "\n".join(f"* {item}" for item in items)


def format_numbered(items: list[str], empty_text: str) -> str:
    if not items:
        return f"1. {empty_text}"
    return "\n".join(f"{index}. {item}" for index, item in enumerate(items, start=1))


def build_scope_summary(context: dict[str, object], language: str) -> list[str]:
    in_scope = context["in_scope"]  # type: ignore[assignment]
    out_of_scope = context["out_of_scope"]  # type: ignore[assignment]
    scope_bits: list[str] = []
    if in_scope:
        joined = "; ".join(in_scope)
        scope_bits.append(
            f"In scope: {joined}" if language == "english" else f"I scope: {joined}"
        )
    if out_of_scope:
        joined = "; ".join(out_of_scope)
        scope_bits.append(
            f"Out of scope: {joined}"
            if language == "english"
            else f"Ude af scope: {joined}"
        )
    return scope_bits


def build_context_snapshot(context: dict[str, object], language: str) -> list[str]:
    snapshot: list[str] = []
    if context["decision_to_support"]:
        label = "Decision to support" if language == "english" else "Beslutning der skal understoettes"
        snapshot.append(f"{label}: {context['decision_to_support']}")
    if context["target_users"]:
        label = "Target users" if language == "english" else "Maalbrugere"
        snapshot.append(f"{label}: {'; '.join(context['target_users'])}")
    if context["success_measures"]:
        label = "Success measures" if language == "english" else "Succeskriterier"
        snapshot.append(f"{label}: {'; '.join(context['success_measures'])}")
    if context["constraints"]:
        label = "Main constraints" if language == "english" else "Vigtigste begraensninger"
        snapshot.append(f"{label}: {'; '.join(context['constraints'])}")
    snapshot.extend(build_scope_summary(context, language))
    return snapshot


def build_invite_cover_items(capture_fields: list[str], carried_forward: list[str], open_questions: list[str]) -> list[str]:
    items = []
    items.extend(carried_forward[:2])
    items.extend(open_questions[:2])
    items.extend(capture_fields[:4])
    return unique(items)[:4]


def build_prepare_items(
    kind: str,
    language: str,
    context: dict[str, object],
    previous_working_path: Path | None,
) -> list[str]:
    items = default_prepare_for_kind(kind, language)
    if previous_working_path is not None:
        if language == "english":
            items.insert(0, f"The latest validated synthesis in `{project_relative_path(previous_working_path)}`")
        else:
            items.insert(0, f"Den seneste validerede syntese i `{project_relative_path(previous_working_path)}`")
    if context["baseline"]:
        if language == "english":
            items.append(f"The strongest known baseline signals: {'; '.join(context['baseline'][:3])}")
        else:
            items.append(f"De staerkeste kendte baselinesignaler: {'; '.join(context['baseline'][:3])}")
    if context["constraints"]:
        if language == "english":
            items.append(f"Known constraints to keep visible: {'; '.join(context['constraints'][:3])}")
        else:
            items.append(f"Kendte begraensninger der skal holdes synlige: {'; '.join(context['constraints'][:3])}")
    return unique(items)


def build_participants(
    kind: str,
    language: str,
    context: dict[str, object],
) -> list[str]:
    participants = list(context["participants"])  # type: ignore[arg-type]
    if len(participants) < 3:
        participants.extend(default_roles_for_kind(kind, language))
    return unique(participants)


def build_key_questions(context: dict[str, object], capture_fields: list[str], language: str) -> list[str]:
    questions = list(context["open_questions"])  # type: ignore[arg-type]
    if questions:
        return unique(questions)[:4]
    fallback = []
    for field in capture_fields[:4]:
        if language == "english":
            fallback.append(f"How should we clarify: {field}?")
        else:
            fallback.append(f"Hvordan skal vi afklare: {field}?")
    return fallback


def build_evidence_request_items(kind: str, language: str, context: dict[str, object], capture_fields: list[str]) -> list[str]:
    items = list(default_evidence_request_for_kind(kind, language))
    if context["success_measures"]:
        if language == "english":
            items.append(f"Anything that sharpens the picture around: {'; '.join(context['success_measures'][:3])}")
        else:
            items.append(f"Alt der kan skarpe billedet omkring: {'; '.join(context['success_measures'][:3])}")
    if capture_fields:
        if language == "english":
            items.append(f"Anything that helps us populate the next input areas: {'; '.join(capture_fields[:4])}")
        else:
            items.append(f"Alt der hjaelper os med at udfylde de naeste inputfelter: {'; '.join(capture_fields[:4])}")
    return unique(items)


def build_overview_content(
    project_name: str,
    package: str,
    language: str,
    current_stage: dict[str, str | None],
    meta: dict[str, str],
    context: dict[str, object],
    input_path: Path,
    guide_path: str,
    prep_files: list[str],
) -> str:
    generated = date.today().isoformat()
    context_snapshot = format_bullets(
        build_context_snapshot(context, language),
        "No tailored context has been carried forward yet." if language == "english" else "Der er endnu ikke foert tilpasset kontekst videre.",
    )
    carry_forward = format_bullets(
        list(context["carried_forward"]),  # type: ignore[arg-type]
        "No explicit carry-forward points were found in the previous validated output." if language == "english" else "Der blev ikke fundet eksplicitte viderefoerte punkter i det tidligere validerede output.",
    )
    open_questions = format_bullets(
        list(context["open_questions"]),  # type: ignore[arg-type]
        "No open questions are currently recorded." if language == "english" else "Der er ikke registreret aabne spoergsmaal lige nu.",
    )
    generated_files = format_bullets(
        [f"`{filename}`" for filename in prep_files],
        "No prep files generated." if language == "english" else "Ingen prepfiler genereret.",
    )

    if language == "danish":
        return f"""# Naeste aktivitets prep-overblik

## Projekt
{project_name}

## Pakke og aktivitet
Pakke {package} - {current_stage['stage']} - {current_stage['purpose']}

## Sessionstype
{meta['session_type']}

## Estimeret tid
{meta['estimated_time']}

## Genereret den
{generated}

## Hvorfor dette trin nu
{context['review_summary'] or meta['objective']}

## Kontekstsnapshot
{context_snapshot}

## Valideret input foert videre
{carry_forward}

## Aabne spoergsmaal som aktiviteten skal hjaelpe med
{open_questions}

## Projektfiler til brug i aktiviteten
* Inputfil: `{project_relative_path(input_path)}`
* Facilitatorguide: `{guide_path}`

## Genererede prepfiler
{generated_files}
"""

    return f"""# Next activity prep overview

## Project
{project_name}

## Package and activity
Package {package} - {current_stage['stage']} - {current_stage['purpose']}

## Session type
{meta['session_type']}

## Estimated time
{meta['estimated_time']}

## Generated on
{generated}

## Why this step now
{context['review_summary'] or meta['objective']}

## Context snapshot
{context_snapshot}

## Validated carry-forward
{carry_forward}

## Open questions this activity should help answer
{open_questions}

## Project files to use in the activity
* Input file: `{project_relative_path(input_path)}`
* Facilitator guide: `{guide_path}`

## Generated prep files
{generated_files}
"""


def build_invite_content(
    project_name: str,
    package: str,
    language: str,
    current_stage: dict[str, str | None],
    meta: dict[str, str],
    context: dict[str, object],
    capture_fields: list[str],
    participants: list[str],
    prepare_items: list[str],
) -> str:
    cover_items = build_invite_cover_items(
        capture_fields,
        list(context["carried_forward"]),  # type: ignore[arg-type]
        list(context["open_questions"]),  # type: ignore[arg-type]
    )
    if meta["kind"] in {"interview", "observation"}:
        if language == "danish":
            return f"""# Naeste aktivitets invitationsudkast

### Emnefelt
[Interviewinvitation: {project_name} - {current_stage['stage']}]

### Besked
Hej,

Vi vil gerne invitere dig til at deltage i en fokuseret samtale som en del af Pakke {package} for projektet `{project_name}`.

### Hvorfor vi inviterer dig
Denne aktivitet skal give os det staerkeste praktiske input til `{current_stage['purpose']}`. Dine perspektiver er relevante for den beslutning og det arbejde der nu skal underbygges.

### Hvad samtalen handler om
{context['decision_to_support'] or meta['objective']}

### Hvad deltagelsen indebaerer
* En samtale eller session paa cirka {meta['estimated_time']}
* Fokus paa foelgende temaer:
{format_bullets(cover_items, "Temaer afklares sammen i sessionen.")}
* Ingen forberedelse er noedvendig ud over materialet nedenfor, medmindre vi aftaler andet

### Samtykke og fortrolighed
* Deltagelse er frivillig
* Vi bruger inputtet til at forstaa moenstre, behov, barrierer eller driftsrealiteter relevante for projektet
* Vi knytter ikke citater til dit navn uden for det aftalte projektteam, medmindre vi eksplicit aftaler det

### Hvem vi gerne vil have med
{format_bullets(participants, "Relevante roller afklares ved invitation.")}

### Hvad vi gerne vil have klar
{format_bullets(prepare_items[:4], "Aftales naermere foer sessionen.")}

### Praktiske detaljer
* Dato og tidspunkt: [Tekst]
* Varighed: {meta['estimated_time']}
* Format: [Remote / fysisk / observation / shadowing]
* Lokation eller link: [Tekst]

### Hvad der sker bagefter
Vi omsaetter inputtet til et struktureret output for review, foer projektet gaar videre.
"""

        return f"""# Next activity invite draft

### Subject
[Interview invite: {project_name} - {current_stage['stage']}]

### Message
Hi,

We would like to invite you to take part in a focused conversation as part of Package {package} for the project `{project_name}`.

### Why we are inviting you
This activity needs strong practical input to support `{current_stage['purpose']}`. Your perspective is relevant to the decision and evidence the project now needs.

### What the conversation is about
{context['decision_to_support'] or meta['objective']}

### What participation involves
* A conversation or session of approximately {meta['estimated_time']}
* Focus on the following themes:
{format_bullets(cover_items, "Themes will be clarified together in the session.")}
* No preparation is required beyond the material below unless agreed otherwise

### Consent and confidentiality
* Participation is voluntary
* We will use the session to understand patterns, needs, barriers, or operational realities relevant to the project
* We will not attribute quotes by name outside the agreed project team unless explicitly agreed otherwise

### Who we would like involved
{format_bullets(participants, "Relevant roles will be confirmed in the invite.")}

### What we would like prepared
{format_bullets(prepare_items[:4], "To be agreed before the session.")}

### Practical details
* Date and time: [Text]
* Duration: {meta['estimated_time']}
* Format: [Remote / in person / observation / shadowing]
* Location or link: [Text]

### What happens after
We will turn the captured input into a structured output for review before the project moves on.
"""

    if language == "danish":
        return f"""# Naeste aktivitets invitationsudkast

### Emnefelt
[Workshopinvitation: {project_name} - {current_stage['stage']}]

### Besked
Hej,

Du inviteres til en fokuseret session som en del af Pakke {package} for projektet `{project_name}`.

### Hvorfor denne session afholdes
Vi skal nu skabe det bedste grundlag for `{current_stage['purpose']}`. Sessionen skal give os det input der mangler, foer naeste syntese og review.

### Hvilken beslutning eller hvilket output den understoetter
{meta['decision_output']}

### Hvad vi vil dække
{format_bullets(cover_items, "Temaer afklares i sessionen.")}

### Hvem der boer deltage
{format_bullets(participants, "Relevante roller afklares ved invitation.")}

### Hvad der boer forberedes
{format_bullets(prepare_items[:4], "Aftales naermere foer sessionen.")}

### Praktiske detaljer
* Dato og tidspunkt: [Tekst]
* Varighed: {meta['estimated_time']}
* Format: [Remote / fysisk / hybrid]
* Lokation eller link: [Tekst]

### Hvad der sker bagefter
Vi omsaetter inputtet til et struktureret output for review, foer projektet gaar videre.
"""

    return f"""# Next activity invite draft

### Subject
[Workshop invite: {project_name} - {current_stage['stage']}]

### Message
Hi,

You are invited to a focused session as part of Package {package} for the project `{project_name}`.

### Why this session is happening
We now need the strongest possible input for `{current_stage['purpose']}`. This session is intended to create the missing input before the next synthesis and review step.

### What decision or output it supports
{meta['decision_output']}

### What we will cover
{format_bullets(cover_items, "Topics will be clarified in the session.")}

### Who should attend
{format_bullets(participants, "Relevant roles will be confirmed in the invite.")}

### What to prepare
{format_bullets(prepare_items[:4], "To be agreed before the session.")}

### Practical details
* Date and time: [Text]
* Duration: {meta['estimated_time']}
* Format: [Remote / in person / hybrid]
* Location or link: [Text]

### What happens after
We will turn the captured input into a structured output for review before the project moves on.
"""


def build_session_brief_content(
    project_name: str,
    package: str,
    language: str,
    current_stage: dict[str, str | None],
    meta: dict[str, str],
    context: dict[str, object],
    capture_fields: list[str],
    participants: list[str],
    prepare_items: list[str],
    input_path: Path,
    guide_path: str,
) -> str:
    key_questions = build_key_questions(context, capture_fields, language)
    scope_lines = build_scope_summary(context, language)
    risks = unique(list(context["open_questions"])[:3] + list(context["constraints"])[:2])  # type: ignore[arg-type]
    materials = unique(
        prepare_items[:4]
        + [f"`{project_relative_path(input_path)}`", f"`{guide_path}`"]
    )

    if language == "danish":
        return f"""# Naeste aktivitets session brief

## Projekt
{project_name}

## Pakke og aktivitet
Pakke {package} - {current_stage['stage']} - {current_stage['purpose']}

## Sessionstype
{meta['session_type']}

## Formaal
{meta['objective']}

## Beslutning eller output som sessionen skal understoette
{meta['decision_output']}

## Deltagere
{format_bullets(participants, "Relevante roller skal stadig bekraeftes.")}

## Estimeret tid
{meta['estimated_time']}

## Scopegraenser
{format_bullets(scope_lines, "Scopegraenser skal bekraeftes foer sessionen.")}

## Noeglespoergsmaal der skal daekkes
{format_bullets(key_questions, "Noeglespoergsmaal fastlaegges i facilitatorbriefet.")}

## Materialer der skal vaere klar
{format_bullets(materials, "Materialer skal bekraeftes foer sessionen.")}

## Det der skal fanges
{format_bullets(capture_fields, "Capturefelter er endnu ikke afklaret.")}

## Risici eller opmaerksomhedspunkter
{format_bullets(risks, "Ingen saerlige risici registreret endnu.")}

## Handoff efter sessionen

### Projektinputfil
`{project_relative_path(input_path)}`

### Relateret guide
`{guide_path}`

### Reviewnote
Syntesen fra aktiviteten skal valideres, foer projektet gaar videre til det naeste trin.
"""

    return f"""# Next activity session brief

## Project
{project_name}

## Package and activity
Package {package} - {current_stage['stage']} - {current_stage['purpose']}

## Session type
{meta['session_type']}

## Objective
{meta['objective']}

## Decision or output this session should support
{meta['decision_output']}

## Participants
{format_bullets(participants, "Relevant roles still need confirming.")}

## Estimated time
{meta['estimated_time']}

## Scope guardrails
{format_bullets(scope_lines, "Scope guardrails should be confirmed before the session.")}

## Key questions to cover
{format_bullets(key_questions, "Key questions will be finalized in the facilitator brief.")}

## Materials to have ready
{format_bullets(materials, "Materials should be confirmed before the session.")}

## What must be captured
{format_bullets(capture_fields, "Capture fields have not been clarified yet.")}

## Risks or watchouts
{format_bullets(risks, "No major risks are currently recorded.")}

## Handoff after the session

### Project input file
`{project_relative_path(input_path)}`

### Related guide
`{guide_path}`

### Review note
The synthesis from this activity needs validation before the project moves to the next stage.
"""


def build_evidence_request_content(
    project_name: str,
    package: str,
    language: str,
    current_stage: dict[str, str | None],
    meta: dict[str, str],
    context: dict[str, object],
    capture_fields: list[str],
) -> str:
    request_items = build_evidence_request_items(meta["kind"], language, context, capture_fields)
    scope_lines = build_scope_summary(context, language)
    optional_note = (
        "Use this request only if the activity still depends on evidence, access, exports, or coordination that has not already been secured."
        if language == "english"
        else "Brug kun denne request hvis aktiviteten stadig afhaenger af evidens, adgang, eksporter eller koordinering som endnu ikke er paa plads."
    )

    if language == "danish":
        return f"""# Naeste aktivitets evidensrequest

## Projekt
{project_name}

## Pakke og aktivitet
Pakke {package} - {current_stage['stage']} - {current_stage['purpose']}

## Brug denne fil saadan
{optional_note}

### Emnefelt
[Evidensrequest: {project_name} - {current_stage['stage']}]

### Besked
Hej,

Vi forbereder nu den naeste aktivitet i pakkeforloebet og har brug for det staerkeste tilgaengelige materiale der kan goere aktiviteten beslutningsduelig.

### Hvorfor vi spoerger
{context['review_summary'] or meta['objective']}

### Hvilken aktivitet eller beslutning dette understoetter
{meta['decision_output']}

### Hvad der vil vaere mest brugbart
{format_bullets(request_items, "Det vigtigste materiale afklares sammen med teamet.")}

### Scopegraenser der skal respekteres
{format_bullets(scope_lines, "Scopegraenser skal bekraeftes foer udsendelse.")}

### Hvilket format der er fint
Raadata, screenshots, dashboards, noter, links eller korte opsummeringer er alle acceptable paa dette trin.

### Hvad der skal siges tydeligt hvis det mangler
Sig direkte til hvis segmentering, adgang, tilladelser eller centrale datakilder ikke er tilgaengelige endnu.

### Timing
[Tekst]

### Tak og naeste skridt
Tak. Naar vi har det staerkeste tilgaengelige input, bruger vi det til at underbygge naeste trin i pakken.
"""

    return f"""# Next activity evidence request

## Project
{project_name}

## Package and activity
Package {package} - {current_stage['stage']} - {current_stage['purpose']}

## How to use this file
{optional_note}

### Subject
[Evidence request: {project_name} - {current_stage['stage']}]

### Message
Hi,

We are now preparing the next activity in the package and need the strongest available material that can make the step decision-ready.

### Why we are asking
{context['review_summary'] or meta['objective']}

### What activity or decision this supports
{meta['decision_output']}

### What would be most useful
{format_bullets(request_items, "The strongest material will be agreed with the team.")}

### Scope boundaries to respect
{format_bullets(scope_lines, "Scope boundaries should be confirmed before sending.")}

### What format is acceptable
Raw data, screenshots, dashboards, notes, links, or short summaries are all acceptable at this stage.

### What to call out if missing
Please note directly if segmentation, access, permissions, or key data sources are not currently available.

### Timing
[Text]

### Thanks and next step
Thank you. Once we have the strongest available inputs, we will use them to support the next package step.
"""


def build_readiness_check_content(
    project_name: str,
    package: str,
    language: str,
    current_stage: dict[str, str | None],
    meta: dict[str, str],
    context: dict[str, object],
    input_path: Path,
    guide_path: str,
) -> str:
    participants_known = bool(context["participants"])
    scope_known = bool(context["in_scope"]) or bool(context["out_of_scope"])
    constraints_known = bool(context["constraints"])
    questions_known = bool(context["open_questions"])
    if participants_known and scope_known and constraints_known:
        ready = "Yes with caveats" if questions_known else "Yes"
        main_gaps = (
            list(context["open_questions"])[:2] if questions_known else []
        )
    else:
        ready = "No" if language == "english" else "Nej"
        main_gaps = []
        if not participants_known:
            main_gaps.append(
                "The right participants are not fully confirmed yet."
                if language == "english"
                else "De rigtige deltagere er endnu ikke fuldt bekraeftet."
            )
        if not scope_known:
            main_gaps.append(
                "The scope and out-of-scope guardrails are still too weak."
                if language == "english"
                else "Scope og out-of-scope-graenser er stadig for svage."
            )
        if not constraints_known:
            main_gaps.append(
                "Known constraints are not explicit enough yet."
                if language == "english"
                else "Kendte begraensninger er endnu ikke tydelige nok."
            )

    actions = [
        (
            f"Confirm who should actually be involved in `{current_stage['stage']}`."
            if language == "english"
            else f"Bekraeft hvem der faktisk skal deltage i `{current_stage['stage']}`."
        ),
        (
            f"Review `{project_relative_path(input_path)}` before running the activity."
            if language == "english"
            else f"Gennemgaa `{project_relative_path(input_path)}` foer aktiviteten koeres."
        ),
        (
            f"Use `{guide_path}` and the generated prep files in `00-project-setup/{SHARED_PREP_DIRNAME}/`."
            if language == "english"
            else f"Brug `{guide_path}` og de genererede prepfiler i `00-project-setup/{SHARED_PREP_DIRNAME}/`."
        ),
    ]

    if language == "danish":
        return f"""# Naeste aktivitets readiness-check

## Projekt
{project_name}

## Pakke og aktivitet
Pakke {package} - {current_stage['stage']} - {current_stage['purpose']}

## Aktivitetens formaal
{meta['objective']}

## Estimeret aktivitetstid
{meta['estimated_time']}

## Tjekliste

### 1. Beslutningsparathed

- [x] Den beslutning aktiviteten skal understoette er tydelig
- [{'x' if scope_known else ' '}] Scope er tydeligt nok til at kunne facilitere aktiviteten
- [{'x' if bool(context['success_measures']) else ' '}] Succeskriterier eller maalinger er synlige
- [x] Det forrige trin er valideret

### 2. People readiness

- [{'x' if participants_known else ' '}] De rigtige deltagere er kendt eller delvist kendt
- [{'x' if participants_known else ' '}] En beslutningsejer eller sponsor kan spores i konteksten
- [ ] Deltagerne er inviteret eller bekraeftet
- [{'x' if bool(context['open_questions']) else ' '}] Manglende interessenter eller evidensejere er noterede som en risiko

### 3. Materialeparathed

- [x] Den relevante inputfil er identificeret
- [x] Den relevante facilitatorguide er identificeret
- [{'x' if constraints_known else ' '}] Begraensninger og guardrails er synlige
- [ ] Noedvendig evidens eller adgang er bekraeftet

### 4. Faciliteringsparathed

- [x] Formål og forventet output er tydelige
- [{'x' if questions_known else ' '}] Kritiske spoergsmaal er synlige
- [x] Handoff tilbage til AI-processen er tydeligt
- [ ] Praktisk agenda og noteansvar er bekraeftet

### 5. Risiko og feasibility

- [{'x' if constraints_known else ' '}] Kendte begraensninger er eksplicitte
- [{'x' if bool(context['open_questions']) else ' '}] Centrale antagelser eller spoergsmaal er synlige
- [ ] Sandsynlige blokeringer er afklaret med de rette ejere
- [x] Aktiviteten er stadig vaerd at gennemfoere i sin nuvaerende form

## Readiness summary

### Klar til at koere
{ready if ready != 'Yes with caveats' else 'Ja med forbehold'}

### Vigtigste huller der skal lukkes
{format_bullets(main_gaps, "Ingen vaesentlige huller registreret endnu.")}

### Umiddelbare forberedelseshandlinger
{format_bullets(actions, "Ingen yderligere handlinger registreret.")}

### Prepared by
AI-generated draft

### Date
{date.today().isoformat()}
"""


def build_interview_guide_content(
    project_name: str,
    package: str,
    language: str,
    current_stage: dict[str, str | None],
    context: dict[str, object],
    capture_fields: list[str],
    input_path: Path,
    guide_path: str,
) -> str:
    stage_label = canonical_stage_label(str(current_stage["stage"]))
    target_users = list(context["target_users"])  # type: ignore[arg-type]
    open_questions = list(context["open_questions"])  # type: ignore[arg-type]
    validated_points = list(context["validated_points"])  # type: ignore[arg-type]
    scope_bits = build_scope_summary(context, language)
    key_capture = capture_fields[:6]

    if package == "B" and stage_label == "Activity 1.2":
        if language == "danish":
            intro = "Brug denne guide til semistrukturerede brugerinterviews om menuvalg, tilkoeb og tryghed foer checkout."
            participant_title = "Primaer deltagerprofil"
            moderator_notes = [
                "Bed altid om et konkret nyligt eksempel, foer du spoerger mere generelt",
                "Hold fokus paa faktisk adfaerd og ikke kun holdninger",
                "Spoerg ind til mobilkontekst, tempo og hvor sult eller tidspres paavirker valgene",
                "Adskil tydeligt hvad brugeren oplevede, hvad de antog, og hvad de gjorde bagefter",
            ]
            question_sections = """### 1. Opvarmning og seneste konkrete oplevelse
1. Kan du fortaelle om sidste gang du bestilte takeaway fra mobilen hos en restaurant som denne?
2. Hvad var du egentlig paa vej ind for at koebe, og hvor hurtigt ville du vaere faerdig?
3. Hvorfor brugte du mobil i den situation?

### 2. Menuvalg og overblik
1. Naar du ser menuen eller de forskellige valgmuligheder, hvad har du mest brug for at forstaa hurtigt?
2. Hvad goer det let eller svaert at gennemskue forskellen paa menuer, enkelte produkter og kombinationer?
3. Hvor bliver du mest usikker paa, hvad du faktisk faar?

### 3. Tilkoeb og valg undervejs
1. Hvordan beslutter du, om du vil tilfoeje sides eller ekstra produkter?
2. Hvad goer tilkoeb relevante eller irrelevante for dig i situationen?
3. Er der tidspunkter hvor tilkoeb foeles hjaelpsomme, og tidspunkter hvor de foeles forstyrrende eller uklare?

### 4. Pris og tryghed foer checkout
1. Hvornår begynder du for alvor at holde oje med den samlede pris?
2. Hvad kan faa dig til at blive usikker paa, om pris og indhold stadig giver mening?
3. Er der noget lige foer checkout, der faar dig til at stoppe op, gaa tilbage eller droppe bestillingen?

### 5. Frafald, omveje og forbedringsmuligheder
1. Har du proevet at afbryde eller forlade en bestilling i en situation som denne? Hvad skete der?
2. Hvis du bliver usikker undervejs, hvordan proever du saa at finde svar eller komme videre?
3. Hvad ville goere det lettere at vaelge rigtigt og foele sig tryg nok til at gennemfoere bestillingen?"""
            listening_for = [
                "Tegn paa at menuopbygningen skaber usikkerhed eller langsom beslutning",
                "Tegn paa at tilkoeb virker uklare, paatraengende eller svaere at vurdere",
                "Tegn paa at pris eller samlet vaerdi bliver uklar foer checkout",
                "Konkrete coping-adfaerd, fx at gaa frem og tilbage, droppe tilkoeb eller forlade flowet",
            ]
        else:
            intro = "Use this guide for semi-structured user interviews about menu choice, add-ons, and confidence before checkout."
            participant_title = "Primary participant profile"
            moderator_notes = [
                "Always start from a recent concrete example before moving to general opinions",
                "Keep the focus on actual behavior rather than abstract preferences",
                "Probe the mobile context, time pressure, and how hunger or stress shapes the choices",
                "Separate what the user experienced, what they assumed, and what they did next",
            ]
            question_sections = """### 1. Warm-up and recent concrete experience
1. Can you tell me about the last time you ordered takeaway on mobile from a restaurant like this?
2. What were you actually trying to buy, and how quickly were you hoping to finish?
3. Why did you use mobile in that situation?

### 2. Menu choice and overview
1. When you look at the menu or different options, what do you most need to understand quickly?
2. What makes it easy or hard to understand the difference between menus, single items, and combinations?
3. Where do you become most unsure about what you are actually getting?

### 3. Add-ons and in-flow decisions
1. How do you decide whether to add sides or extras?
2. What makes add-ons feel relevant or irrelevant in the moment?
3. Are there times when add-ons feel helpful, and other times when they feel distracting or unclear?

### 4. Price and confidence before checkout
1. At what point do you really start paying attention to the total price?
2. What can make you unsure whether the price and content still make sense?
3. Is there anything right before checkout that makes you stop, go back, or abandon the order?

### 5. Drop-off, workarounds, and improvements
1. Have you ever abandoned an order in a situation like this? What happened?
2. If you become unsure during the flow, how do you try to find answers or move forward?
3. What would make it easier to choose correctly and feel confident enough to complete the order?"""
            listening_for = [
                "Signs that menu structure creates uncertainty or slows decisions",
                "Signs that add-ons feel unclear, pushy, or hard to judge",
                "Signs that price or total value becomes unclear before checkout",
                "Concrete coping behavior such as going back, dropping add-ons, or leaving the flow",
            ]
    else:
        if language == "danish":
            intro = "Brug denne guide til et semistruktureret interview, der skal skabe reel evidens til den naeste syntese."
            participant_title = "Primaer deltagerprofil"
            moderator_notes = [
                "Tag udgangspunkt i et nyligt konkret eksempel",
                "Spoerg ind til faktisk adfaerd, ikke kun generelle holdninger",
                "Noter citater og konkrete eksempler saa ordret som muligt",
            ]
            question_sections = """### 1. Rolle og kontekst
1. Kan du kort beskrive din rolle i eller oplevelse af det omraade vi ser paa?
2. Hvilken opgave eller situation er vigtigst i den del af rejsen eller servicen vi taler om?

### 2. Nuværende oplevelse eller praksis
1. Kan du gaa os igennem et nyligt konkret eksempel?
2. Hvor fungerer det godt i dag, og hvor bliver det svaert eller usikkert?

### 3. Barrierer, afhaengigheder og beslutninger
1. Hvilke forhold paavirker beslutningerne mest i denne del af oplevelsen?
2. Hvilke barrierer, handoffs eller afhaengigheder goer oplevelsen eller arbejdet svaerere?

### 4. Omveje, konsekvenser og forbedringsmuligheder
1. Hvilke omveje eller kompromiser ser du i dag?
2. Hvilke forbedringer ville goere stoerst positiv forskel foerst?"""
            listening_for = [
                "Konkrete eksempler paa breakdowns, barrierer eller usikkerhed",
                "Tegn paa at nuvaerende workarounds skjuler et dybere problem",
                "Forhold der paavirker beslutninger, tillid eller fremdrift",
            ]
        else:
            intro = "Use this guide for a semi-structured interview that should create real evidence for the next synthesis."
            participant_title = "Primary participant profile"
            moderator_notes = [
                "Start from a recent concrete example",
                "Probe actual behavior rather than only general opinions",
                "Capture quotes and examples as close to verbatim as possible",
            ]
            question_sections = """### 1. Role and context
1. Can you briefly describe your role in or experience of the area we are looking at?
2. What task or situation matters most in the part of the journey or service we are discussing?

### 2. Current experience or practice
1. Can you walk us through a recent concrete example?
2. What works well today, and where does it become difficult or uncertain?

### 3. Barriers, dependencies, and decisions
1. Which conditions influence the decisions most in this part of the experience?
2. Which barriers, handoffs, or dependencies make the work or experience harder?

### 4. Workarounds, consequences, and improvements
1. Which workarounds or compromises do you see today?
2. Which improvements would make the biggest positive difference first?"""
            listening_for = [
                "Concrete examples of breakdowns, barriers, or uncertainty",
                "Signs that current workarounds are hiding a deeper problem",
                "Conditions that affect decisions, trust, or progress",
            ]

    if not target_users:
        target_users = [
            point
            for point in validated_points
            if any(
                term in simplify_text(point).lower()
                for term in ("maalbrugere", "brugere", "target users", "users")
            )
        ]
    if not scope_bits:
        scope_bits = [
            point
            for point in validated_points
            if any(
                term in simplify_text(point).lower()
                for term in ("scope", "rejse", "journey")
            )
        ]

    participant_profile = target_users or (
        ["Bekraeftes ud fra den aktuelle rekrutteringslogik."] if language == "danish" else ["Confirm against the current recruitment logic."]
    )
    project_focus = unique(
        ([str(context["problem_area"])] if context["problem_area"] else [])
        + ([str(context["decision_to_support"])] if context["decision_to_support"] else [])
        + open_questions[:3]
    )

    if language == "danish":
        return f"""# Naeste aktivitets interviewguide

## Projekt
{project_name}

## Pakke og aktivitet
Pakke {package} - {current_stage['stage']} - {current_stage['purpose']}

## Brug guiden saadan
{intro}

## Interviewets formaal
{context['review_summary'] or 'Skabe et skarpere evidensgrundlag for den naeste syntese.'}

## Hvad vi isaer skal laere i dette projekt
{format_bullets(project_focus, "Afklares i interviewet.")}

## {participant_title}
{format_bullets(participant_profile, "Bekraeftes foer interviewene koeres.")}

## Moderatornoter
{format_bullets(moderator_notes, "Moderatornoter afklares foer interviewet.")}

## Scopegraenser
{format_bullets(scope_bits, "Scopegraenser skal bekraeftes foer interviewene koeres.")}

## Spoergeguide
{question_sections}

## Det vi isaer skal lytte efter
{format_bullets(listening_for, "Ingen saerlige lyttefokus registreret endnu.")}

## Det der skal fanges i inputfilen bagefter
{format_bullets(key_capture, "Det relevante capture aftales i projektets inputfil.")}

## Handoff efter interviewene

### Projektinputfil
`{project_relative_path(input_path)}`

### Relateret guide
`{guide_path}`
"""

    return f"""# Next activity interview guide

## Project
{project_name}

## Package and activity
Package {package} - {current_stage['stage']} - {current_stage['purpose']}

## How to use this guide
{intro}

## Interview objective
{context['review_summary'] or 'Create a sharper evidence base for the next synthesis.'}

## What we especially need to learn in this project
{format_bullets(project_focus, "To be clarified through the interview.")}

## {participant_title}
{format_bullets(participant_profile, "Confirm before running the interviews.")}

## Moderator notes
{format_bullets(moderator_notes, "Moderator notes should be confirmed before the interview.")}

## Scope guardrails
{format_bullets(scope_bits, "Scope guardrails should be confirmed before the interviews.")}

## Question guide
{question_sections}

## What we should listen for
{format_bullets(listening_for, "No special listening points recorded yet.")}

## What should be captured in the input file afterwards
{format_bullets(key_capture, "Capture expectations should be confirmed in the project input file.")}

## Handoff after the interviews

### Project input file
`{project_relative_path(input_path)}`

### Related guide
`{guide_path}`
"""


def build_mapping_canvas_content(
    project_name: str,
    package: str,
    language: str,
    current_stage: dict[str, str | None],
    context: dict[str, object],
    input_path: Path,
    guide_path: str,
) -> str:
    scope_bits = build_scope_summary(context, language)
    open_questions = list(context["open_questions"])  # type: ignore[arg-type]
    success_measures = list(context["success_measures"])  # type: ignore[arg-type]
    validated_points = list(context["validated_points"])  # type: ignore[arg-type]
    carried_context = unique(
        ([str(context["problem_area"])] if context["problem_area"] else [])
        + ([str(context["decision_to_support"])] if context["decision_to_support"] else [])
        + list(context["target_users"])  # type: ignore[list-item]
    )
    if not carried_context:
        carried_context = validated_points[:3]
    if not scope_bits:
        scope_bits = [
            point
            for point in validated_points
            if any(term in simplify_text(point).lower() for term in ("scope", "rejse", "journey"))
        ]
    if not success_measures:
        success_measures = [
            point
            for point in validated_points
            if any(
                term in simplify_text(point).lower()
                for term in ("succeskriter", "success", "gennemfoert", "ordrestoerrelse", "drop-off", "frafald")
            )
        ]

    if language == "danish":
        return f"""# Naeste aktivitets mapping-canvas

## Projekt
{project_name}

## Pakke og aktivitet
Pakke {package} - {current_stage['stage']} - {current_stage['purpose']}

## Brug denne canvas saadan
Brug denne fil som arbejdsflade, naar I kortlaegger den nuvaerende rejse. Start med de faktiske faser i oplevelsen, og udfyld derefter behov, friktion, teams, systemer og de vigtigste brud. Hold fokus paa det, der skal vaere synligt nok til at understoette den naeste beslutning.

## Viderefoert fokus
{format_bullets(carried_context, "Viderefoert fokus bekraeftes i sessionen.")}

## Scopegraenser
{format_bullets(scope_bits, "Scopegraenser skal bekraeftes i sessionen.")}

## Aabne spoergsmaal som kortet skal hjaelpe med
{format_bullets(open_questions, "Aabne spoergsmaal afklares i sessionen.")}

## Succeskriterier der skal holdes synlige
{format_bullets(success_measures, "Succeskriterier afklares i sessionen.")}

## Current-state journey canvas

| Fase i rejsen | Brugerens maal eller behov | Touchpoints / indhold | Friktion eller barriere | Teams / systemer / handoffs | Evidens eller signal |
| --- | --- | --- | --- | --- | --- |
| [Fase 1] | [Behov] | [Touchpoint] | [Friktion] | [Team/system] | [Evidens] |
| [Fase 2] | [Behov] | [Touchpoint] | [Friktion] | [Team/system] | [Evidens] |
| [Fase 3] | [Behov] | [Touchpoint] | [Friktion] | [Team/system] | [Evidens] |

## Vigtigste brud
1. [Brud 1]
2. [Brud 2]
3. [Brud 3]

## Mulighedsomraader
* [Mulighedsomraade]
* [Mulighedsomraade]
* [Mulighedsomraade]

## Beslutningskriterier for det fremtidige koncept
* [Kriterium]
* [Kriterium]
* [Kriterium]

## Valideringshuller
* [Hul]
* [Hul]

## Handoff efter sessionen

### Projektinputfil
`{project_relative_path(input_path)}`

### Relateret guide
`{guide_path}`
"""

    return f"""# Next activity mapping canvas

## Project
{project_name}

## Package and activity
Package {package} - {current_stage['stage']} - {current_stage['purpose']}

## How to use this canvas
Use this file as the working surface when mapping the current state. Start with the real journey phases, then fill in needs, friction, teams, systems, and the main breakdowns. Keep the focus on what needs to be visible enough to support the next decision.

## Carried-forward focus
{format_bullets(carried_context, "Carry-forward focus will be confirmed in the session.")}

## Scope guardrails
{format_bullets(scope_bits, "Scope guardrails should be confirmed in the session.")}

## Open questions the map should help answer
{format_bullets(open_questions, "Open questions will be clarified in the session.")}

## Success measures to keep visible
{format_bullets(success_measures, "Success measures will be clarified in the session.")}

## Current-state journey canvas

| Journey phase | User goal or need | Touchpoints / content | Friction or barrier | Teams / systems / handoffs | Evidence or signal |
| --- | --- | --- | --- | --- | --- |
| [Phase 1] | [Need] | [Touchpoint] | [Friction] | [Team/system] | [Evidence] |
| [Phase 2] | [Need] | [Touchpoint] | [Friction] | [Team/system] | [Evidence] |
| [Phase 3] | [Need] | [Touchpoint] | [Friction] | [Team/system] | [Evidence] |

## Main breakdowns
1. [Breakdown 1]
2. [Breakdown 2]
3. [Breakdown 3]

## Opportunity areas
* [Opportunity area]
* [Opportunity area]
* [Opportunity area]

## Decision criteria for the future-state concept
* [Criterion]
* [Criterion]
* [Criterion]

## Validation gaps
* [Gap]
* [Gap]

## Handoff after the session

### Project input file
`{project_relative_path(input_path)}`

### Related guide
`{guide_path}`
"""

    return f"""# Next activity readiness check

## Project
{project_name}

## Package and activity
Package {package} - {current_stage['stage']} - {current_stage['purpose']}

## Activity objective
{meta['objective']}

## Estimated activity time
{meta['estimated_time']}

## Checklist

### 1. Decision readiness

- [x] The decision this activity should support is clear
- [{'x' if scope_known else ' '}] The activity is bounded enough for the package
- [{'x' if bool(context['success_measures']) else ' '}] Success measures or outcome anchors are visible
- [x] The previous stage has been validated

### 2. People readiness

- [{'x' if participants_known else ' '}] The right people are known or partly known
- [{'x' if participants_known else ' '}] A decision owner or sponsor can be traced in the current context
- [ ] Participants have been invited or confirmed
- [{'x' if bool(context['open_questions']) else ' '}] Missing stakeholders or evidence owners are visible as a risk

### 3. Material readiness

- [x] The relevant project input file is identified
- [x] The relevant facilitator guide is identified
- [{'x' if constraints_known else ' '}] Constraints and guardrails are visible
- [ ] Needed evidence or access is confirmed

### 4. Facilitation readiness

- [x] The objective and expected output are clear
- [{'x' if questions_known else ' '}] Critical questions are visible
- [x] The handoff back into the AI process is clear
- [ ] The practical agenda and note ownership are confirmed

### 5. Risk and feasibility check

- [{'x' if constraints_known else ' '}] Known constraints are explicit
- [{'x' if bool(context['open_questions']) else ' '}] Key assumptions or open questions are visible
- [ ] Likely blockers have been clarified with the right owners
- [x] The activity still feels worth running in its current form

## Readiness summary

### Ready to run
{ready}

### Main gaps to fix before running
{format_bullets(main_gaps, "No major gaps are currently recorded.")}

### Immediate preparation actions
{format_bullets(actions, "No further actions currently recorded.")}

### Prepared by
AI-generated draft

### Date
{date.today().isoformat()}
"""


def generate_prep_pack(project_dir: Path, dry_run: bool = False) -> tuple[list[Path], str]:
    setup_path = project_dir / "00-project-setup" / "project_setup.md"
    if not setup_path.exists():
        raise ValueError(f"{setup_path} does not exist.")

    setup_sections = split_sections(setup_path.read_text(encoding="utf-8"))
    project_name = clean_placeholder(get_section(setup_sections, "Project name", "Projektnavn"))
    package = parse_package_letter(get_section(setup_sections, "Package", "Pakke"))
    language = parse_language_key(get_section(setup_sections, "Working language", "Arbejdssprog"))

    current_status = normalize_status_value(get_section(setup_sections, "Status"))
    state = derive_workflow_state(project_dir, package, language, current_status)
    stage_results = state["stage_results"]  # type: ignore[assignment]
    current_index = next(
        (index for index, stage in enumerate(stage_results) if stage["decision"] != "validated"),
        None,
    )
    if current_index is None:
        raise ValueError("No upcoming live activity is available to prepare.")

    config = PACKAGE_TEMPLATE_CONFIG[(language, package)]
    current_stage = stage_results[current_index]
    current_stage_config = config["stages"][current_index]
    input_path = project_dir / "01-inputs" / current_stage_config["input_file"]
    guide_path = facilitator_guide_reference(package, language)
    meta = kind_metadata(package, str(current_stage["stage"]), language)
    context = collect_context(project_dir, package, language, current_index, stage_results)  # type: ignore[arg-type]
    capture_fields = build_capture_fields(input_path)
    participants = build_participants(meta["kind"], language, context)

    previous_working_path = None
    if current_index > 0:
        previous_working_path = project_dir / "02-working" / config["stages"][current_index - 1]["working_file"]
    prepare_items = build_prepare_items(meta["kind"], language, context, previous_working_path)

    prep_dir = project_dir / "00-project-setup" / SHARED_PREP_DIRNAME
    filenames = generated_prep_filenames(language)
    planned_files = planned_prep_filenames(meta["kind"], filenames)
    files = {
        prep_dir / filenames["overview"]: build_overview_content(
            project_name,
            package,
            language,
            current_stage,
            meta,
            context,
            input_path,
            guide_path,
            planned_files,
        ),
        prep_dir / filenames["invite"]: build_invite_content(
            project_name,
            package,
            language,
            current_stage,
            meta,
            context,
            capture_fields,
            participants,
            prepare_items,
        ),
        prep_dir / filenames["session_brief"]: build_session_brief_content(
            project_name,
            package,
            language,
            current_stage,
            meta,
            context,
            capture_fields,
            participants,
            prepare_items,
            input_path,
            guide_path,
        ),
        prep_dir / filenames["evidence_request"]: build_evidence_request_content(
            project_name,
            package,
            language,
            current_stage,
            meta,
            context,
            capture_fields,
        ),
        prep_dir / filenames["readiness"]: build_readiness_check_content(
            project_name,
            package,
            language,
            current_stage,
            meta,
            context,
            input_path,
            guide_path,
        ),
    }
    if meta["kind"] == "interview":
        files[prep_dir / filenames["interview_guide"]] = build_interview_guide_content(
            project_name,
            package,
            language,
            current_stage,
            context,
            capture_fields,
            input_path,
            guide_path,
        )
    if meta["kind"] == "mapping_session":
        files[prep_dir / filenames["mapping_canvas"]] = build_mapping_canvas_content(
            project_name,
            package,
            language,
            current_stage,
            context,
            input_path,
            guide_path,
        )

    written: list[Path] = []
    if not dry_run:
        prep_dir.mkdir(parents=True, exist_ok=True)
        for path, content in files.items():
            path.write_text(content, encoding="utf-8")
            written.append(path)
    else:
        written = list(files.keys())

    return written, f"{current_stage['stage']} - {current_stage['purpose']}"


def main() -> int:
    args = parse_args()
    try:
        project_dir = resolve_project_dir(args)
        written, stage_label = generate_prep_pack(project_dir, dry_run=args.dry_run)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    mode = "Dry run" if args.dry_run else "Next-activity prep generated"
    print(f"{mode}:")
    print(f"  Project path: {project_dir}")
    print(f"  Activity: {stage_label}")
    print("  Files:")
    for path in written:
        print(f"    - {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
