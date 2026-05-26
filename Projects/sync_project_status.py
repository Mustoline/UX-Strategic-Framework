#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from bootstrap_project import (
    PACKAGE_TEMPLATE_CONFIG,
    PROJECTS_DIR,
    SHARED_PREP_DIRNAME,
    final_artifacts_for_config,
    final_seed_files_for_config,
    normalize_project_name,
    shared_prep_note,
)


NEXT_ACTIVITY_PREP_SCRIPT = PROJECTS_DIR / "generate_next_activity_prep.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync project_setup.md and project_index.md from the stage review files."
    )
    parser.add_argument(
        "--project-name",
        help="Project name to normalize into a project folder.",
    )
    parser.add_argument(
        "--project-path",
        help="Direct path to the project folder. Use this instead of --project-name if needed.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="If the project is on hold, mark it active again after syncing.",
    )
    parser.add_argument(
        "--on-hold",
        action="store_true",
        help="Mark the project on hold after syncing.",
    )
    parser.add_argument(
        "--close",
        action="store_true",
        help="Mark the project closed after syncing.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the derived project state without writing files.",
    )
    args = parser.parse_args()
    if not args.project_name and not args.project_path:
        parser.error("Provide either --project-name or --project-path.")
    if sum(bool(flag) for flag in [args.resume, args.on_hold, args.close]) > 1:
        parser.error("Use at most one of --resume, --on-hold, or --close.")
    return args


def simplify_text(value: str) -> str:
    return (
        value.replace("Æ", "Ae")
        .replace("Ø", "Oe")
        .replace("Å", "Aa")
        .replace("æ", "ae")
        .replace("ø", "oe")
        .replace("å", "aa")
    )


def split_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current_key: str | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            current_key = simplify_text(line[3:].strip()).lower()
            sections[current_key] = []
            continue
        if current_key is not None:
            sections[current_key].append(line)
    return {key: "\n".join(lines).strip() for key, lines in sections.items()}


def get_section(sections: dict[str, str], *names: str) -> str:
    for name in names:
        key = simplify_text(name).lower()
        if key in sections:
            return sections[key].strip()
    return ""


def first_content_line(value: str) -> str:
    for line in value.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


def clean_placeholder(value: str) -> str:
    stripped = value.strip()
    if stripped.startswith("[") and stripped.endswith("]"):
        return ""
    return stripped


def normalize_status_value(value: str) -> str:
    simplified = simplify_text(clean_placeholder(value)).strip().lower()
    mapping = {
        "setup complete": "setup_complete",
        "intake in progress": "intake_in_progress",
        "active": "active",
        "on hold": "on_hold",
        "closed": "closed",
        "opsaetning fuldfoert": "setup_complete",
        "intake i gang": "intake_in_progress",
        "aktiv": "active",
        "pauset": "on_hold",
        "lukket": "closed",
    }
    return mapping.get(simplified, "")


def parse_package_letter(value: str) -> str:
    match = re.search(r"\b([ABC])\b", simplify_text(value))
    if not match:
        raise ValueError("Could not determine the package from project_setup.md.")
    return match.group(1)


def parse_language_key(value: str) -> str:
    simplified = simplify_text(value).strip().lower()
    if simplified == "english":
        return "english"
    if simplified == "dansk":
        return "danish"
    raise ValueError("Could not determine the working language from project_setup.md.")


def facilitator_guide_reference(package: str, language: str) -> str:
    if language == "danish":
        return f"Packages/Danish/Package_{package}_facilitator_guide_danish.md"
    return f"Packages/English/Package_{package}_facilitator_guide.md"


def parse_review_decision(review_path: Path, language: str) -> tuple[str | None, str | None]:
    if not review_path.exists():
        return None, None

    text = review_path.read_text(encoding="utf-8")
    sections = split_sections(text)
    decision_raw = get_section(
        sections,
        "Validation decision",
        "Valideringsbeslutning",
        "Validation status",
        "Valideringsstatus",
    )
    date_raw = get_section(sections, "Review date", "Reviewdato")

    decision_line = simplify_text(first_content_line(decision_raw)).strip()
    date_line = clean_placeholder(first_content_line(date_raw))
    if date_line and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_line):
        date_line = ""

    decision_normalized = clean_placeholder(decision_line).lower()
    if not decision_normalized:
        legacy_validated = re.search(r"validated on (\d{4}-\d{2}-\d{2})", decision_line, re.I)
        legacy_danish = re.search(r"valideret den (\d{4}-\d{2}-\d{2})", decision_line, re.I)
        if legacy_validated:
            return "validated", legacy_validated.group(1)
        if legacy_danish:
            return "validated", legacy_danish.group(1)
        return None, None

    if "validated with changes" in decision_normalized or "valideret med aendringer" in decision_normalized:
        return "validated_with_changes", date_line or None
    if decision_normalized.startswith("validated") or decision_normalized.startswith("valideret"):
        if "ikke" not in decision_normalized and "not" not in decision_normalized:
            legacy_validated = re.search(r"(\d{4}-\d{2}-\d{2})", decision_normalized)
            if not date_line and legacy_validated:
                date_line = legacy_validated.group(1)
            return "validated", date_line or None
    if "not validated" in decision_normalized or "ikke valideret" in decision_normalized:
        return "not_validated", date_line or None
    return None, date_line or None


def parse_final_approval_status(final_path: Path) -> str | None:
    if not final_path.exists():
        return None
    text = final_path.read_text(encoding="utf-8")
    sections = split_sections(text)
    raw = get_section(sections, "Approval status", "Godkendelsesstatus")
    value = simplify_text(clean_placeholder(first_content_line(raw))).strip().lower()
    mapping = {
        "draft": "draft",
        "ready for review": "ready_for_review",
        "approved": "approved",
        "udkast": "draft",
        "klar til review": "ready_for_review",
        "godkendt": "approved",
    }
    return mapping.get(value)


def parse_final_approval_statuses(project_dir: Path, config: dict[str, object]) -> dict[str, str | None]:
    return {
        final_file: parse_final_approval_status(project_dir / "04-final" / final_file)
        for final_file in final_seed_files_for_config(config)
    }


def collect_existing_project_notes(project_index_path: Path, language: str) -> list[str]:
    if not project_index_path.exists():
        return []
    sections = split_sections(project_index_path.read_text(encoding="utf-8"))
    raw = get_section(sections, "Project notes", "Projektnoter")
    notes = [line.strip() for line in raw.splitlines() if line.strip()]
    return notes


def collect_legacy_notes(project_dir: Path, language: str) -> list[str]:
    notes: list[str] = []
    for path in sorted((project_dir / "01-inputs").glob("*_template.md")):
        if language == "danish":
            notes.append(
                f"* `{path.relative_to(project_dir)}` er beholdt som en legacy-fil fra den tidligere opsaetning og behoever ikke bruges fremadrettet."
            )
        else:
            notes.append(
                f"* `{path.relative_to(project_dir)}` has been kept as a legacy file from the earlier setup and does not need to be used going forward."
            )
    return notes


def clean_project_setup_notes(notes: str, language: str) -> str:
    stale_exact_lines = {
        "* Stage 0 intake answers have been captured.",
        "* The project is waiting for Stage 0 validation before Activity 1.1 begins.",
        "* Trin 0-intakesvarene er indfanget.",
        "* Projektet venter paa validering af Trin 0, foer Aktivitet 1.1 begynder.",
    }
    stale_prefixes = (
        "* Shared prep assets",
        "* Delte forberedelsesaktiver",
    )
    cleaned_lines: list[str] = []
    for line in notes.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped in stale_exact_lines:
            continue
        if any(stripped.startswith(prefix) for prefix in stale_prefixes):
            continue
        cleaned_lines.append(stripped)

    if cleaned_lines:
        return "\n".join(cleaned_lines)
    return "* [Note]" if language == "english" else "* [Note]"


def english_status_label(decision: str | None, review_date: str | None) -> str:
    if decision == "validated":
        return f"Validated on {review_date}" if review_date else "Validated"
    if decision == "validated_with_changes":
        return f"Validated with changes on {review_date}" if review_date else "Validated with changes"
    if decision == "not_validated":
        return "Not validated"
    return ""


def danish_status_label(decision: str | None, review_date: str | None) -> str:
    if decision == "validated":
        return f"Valideret den {review_date}" if review_date else "Valideret"
    if decision == "validated_with_changes":
        return f"Valideret med aendringer den {review_date}" if review_date else "Valideret med aendringer"
    if decision == "not_validated":
        return "Ikke valideret"
    return ""


def english_final_status_label(status: str | None) -> str:
    if status == "draft":
        return "Draft"
    if status == "ready_for_review":
        return "Ready for review"
    if status == "approved":
        return "Approved"
    return "Draft seeded"


def danish_final_status_label(status: str | None) -> str:
    if status == "draft":
        return "Udkast"
    if status == "ready_for_review":
        return "Klar til review"
    if status == "approved":
        return "Godkendt"
    return "Udkast seedet"


def derive_workflow_state(
    project_dir: Path,
    package: str,
    language: str,
    existing_status: str,
) -> dict[str, object]:
    config = PACKAGE_TEMPLATE_CONFIG[(language, package)]
    stage_results: list[dict[str, str | None]] = []
    first_open_index: int | None = None
    any_decision = False

    for index, stage in enumerate(config["stages"]):
        review_path = project_dir / "03-reviews" / stage["review_file"]
        decision, review_date = parse_review_decision(review_path, language)
        if decision:
            any_decision = True
        if decision != "validated" and first_open_index is None:
            first_open_index = index
        stage_results.append(
            {
                "stage": stage["stage"],
                "purpose": stage["purpose"],
                "input_file": stage["input_file"],
                "working_file": stage["working_file"],
                "review_file": stage["review_file"],
                "decision": decision,
                "review_date": review_date,
            }
        )

    final_statuses = parse_final_approval_statuses(project_dir, config)
    all_final_approved = bool(final_statuses) and all(
        status == "approved" for status in final_statuses.values()
    )
    pending_final_files = [
        final_file for final_file, status in final_statuses.items() if status != "approved"
    ]

    if first_open_index is None:
        if all_final_approved:
            current_stage = "Project complete" if language == "english" else "Projektet er afsluttet"
            next_action = (
                "Project outputs are approved. The project can be closed or archived."
                if language == "english"
                else "Projektets outputs er godkendt. Projektet kan lukkes eller arkiveres."
            )
        else:
            current_stage = (
                "Final deliverable completion"
                if language == "english"
                else "Afslutning af den endelige leverance"
            )
            if pending_final_files:
                pending_list = ", ".join(f"`04-final/{name}`" for name in pending_final_files)
                next_action = (
                    f"Complete the remaining final files {pending_list} and move them toward approval."
                    if language == "english"
                    else f"Faerdiggoer de resterende finalfiler {pending_list} og flyt dem mod godkendelse."
                )
            else:
                next_action = (
                    "Complete the remaining final files in `04-final/` and move them toward approval."
                    if language == "english"
                    else "Faerdiggoer de resterende finalfiler i `04-final/` og flyt dem mod godkendelse."
                )
    else:
        current_stage_info = stage_results[first_open_index]
        current_stage = f"{current_stage_info['stage']} - {current_stage_info['purpose']}"
        decision = current_stage_info["decision"]
        if decision == "validated_with_changes":
            next_action = (
                f"Update `02-working/{current_stage_info['working_file']}` from `03-reviews/{current_stage_info['review_file']}` and ask for final confirmation before moving on."
                if language == "english"
                else f"Opdater `02-working/{current_stage_info['working_file']}` ud fra `03-reviews/{current_stage_info['review_file']}` og bed om endelig bekraeftelse, foer projektet gaar videre."
            )
        elif decision == "not_validated":
            next_action = (
                f"Revise `02-working/{current_stage_info['working_file']}` using `03-reviews/{current_stage_info['review_file']}` and re-run review for {current_stage_info['stage']}."
                if language == "english"
                else f"Ret `02-working/{current_stage_info['working_file']}` med udgangspunkt i `03-reviews/{current_stage_info['review_file']}` og koer review igen for {current_stage_info['stage']}."
            )
        else:
            if first_open_index == 0:
                next_action = (
                    f"Run the guided Stage 0 intake dialogue and validate the intake before Activity 1.1 starts."
                    if language == "english"
                    else "Koer den guidede Trin 0-intake-dialog og valider intaken, foer Aktivitet 1.1 starter."
                )
            else:
                guide_path = facilitator_guide_reference(package, language)
                next_action = (
                    f"Run the real-world {current_stage_info['stage']} {current_stage_info['purpose']} using `{guide_path}`, then capture the notes in `01-inputs/{current_stage_info['input_file']}` before returning for synthesis and validation."
                    if language == "english"
                    else f"Koer den virkelige {current_stage_info['stage']} {current_stage_info['purpose']} med `{guide_path}`, og fang derefter noterne i `01-inputs/{current_stage_info['input_file']}`, foer syntese og validering genoptages."
                )

    derived_status = existing_status
    if not derived_status:
        derived_status = "setup_complete"

    if existing_status == "closed":
        derived_status = "closed"
    elif existing_status == "on_hold":
        derived_status = "on_hold"
    elif first_open_index is None and all_final_approved:
        derived_status = "closed"
    elif any_decision:
        derived_status = "active"

    return {
        "config": config,
        "stage_results": stage_results,
        "current_stage": current_stage,
        "next_action": next_action,
        "final_statuses": final_statuses,
        "derived_status": derived_status,
    }


def apply_status_override(current_status: str, language: str, args: argparse.Namespace) -> str:
    if args.on_hold:
        return "on_hold"
    if args.close:
        return "closed"
    if args.resume:
        return "closed" if current_status == "closed" else "active"
    return current_status


def display_status(status: str, language: str) -> str:
    if language == "danish":
        mapping = {
            "setup_complete": "Opsaetning fuldfoert",
            "intake_in_progress": "Intake i gang",
            "active": "Aktiv",
            "on_hold": "Pauset",
            "closed": "Lukket",
        }
    else:
        mapping = {
            "setup_complete": "Setup complete",
            "intake_in_progress": "Intake in progress",
            "active": "Active",
            "on_hold": "On hold",
            "closed": "Closed",
        }
    return mapping.get(status, status)


def refresh_next_activity_prep(project_dir: Path, dry_run: bool) -> tuple[bool, str]:
    command = [
        sys.executable,
        str(NEXT_ACTIVITY_PREP_SCRIPT),
        "--project-path",
        str(project_dir),
    ]
    if dry_run:
        command.append("--dry-run")
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    combined = "\n".join(part for part in [result.stdout.strip(), result.stderr.strip()] if part).strip()
    if result.returncode == 0:
        activity_line = next(
            (line.strip() for line in combined.splitlines() if line.strip().startswith("Activity: ")),
            "",
        )
        if activity_line:
            return True, activity_line.replace("Activity: ", "Refreshed prep for ", 1)
        return True, "Next-activity prep refreshed."
    if "No upcoming live activity is available to prepare." in combined:
        return True, "No upcoming live activity prep needed."
    return False, combined or "Next-activity prep refresh failed."


def build_project_index_text(
    project_name: str,
    folder_name: str,
    package: str,
    language: str,
    created_date: str,
    project_status: str,
    current_stage: str,
    next_action: str,
    stage_results: list[dict[str, str | None]],
    final_statuses: dict[str, str | None],
    project_notes: list[str],
) -> str:
    config = PACKAGE_TEMPLATE_CONFIG[(language, package)]
    on_hold = project_status == "on_hold"

    if language == "danish":
        workflow_rows = [
            "| Trin | Formaaling | Inputfil | Arbejdsoutput | Reviewfil | Status |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for index, stage in enumerate(stage_results):
            decision = stage["decision"]
            if decision:
                row_status = danish_status_label(decision, stage["review_date"])
            else:
                first_open_index = next(
                    (i for i, result in enumerate(stage_results) if result["decision"] != "validated"),
                    None,
                )
                if first_open_index == index:
                    row_status = "Naeste naar projektet genoptages" if on_hold else "Aktuelt trin"
                else:
                    row_status = "Ikke startet"
            workflow_rows.append(
                "| {stage_label} | {purpose} | `{input_file}` | `{working_file}` | `{review_file}` | {status} |".format(
                    stage_label=stage["stage"],
                    purpose=stage["purpose"],
                    input_file=f"01-inputs/{stage['input_file']}",
                    working_file=f"02-working/{stage['working_file']}",
                    review_file=f"03-reviews/{stage['review_file']}",
                    status=row_status,
                )
            )

        final_rows = [
            "| Leverance | Hovedfil | Status |",
            "| --- | --- | --- |",
        ]
        for artifact in final_artifacts_for_config(config):
            final_label = danish_final_status_label(final_statuses.get(artifact["file"]))
            final_rows.append(
                f"| {artifact['deliverable']} | `04-final/{artifact['file']}` | {final_label} |"
            )

        notes_block = ""
        if project_notes:
            notes_block = "## Projektnoter\n\n" + "\n".join(project_notes) + "\n\n"

        return f"""# Projektindex

## Projektoversigt

* Projektnavn: {project_name}
* Mappenavn: {folder_name}
* Pakke: Pakke {package}
* Arbejdssprog: {config['language_label']}
* Oprettelsesdato: {created_date}
* Status: {display_status(project_status, language)}
* Nuvaerende trin: {current_stage}
* Delte forberedelsesaktiver: `00-project-setup/{SHARED_PREP_DIRNAME}/`
* Anbefalet naeste handling: {next_action}

## Workflowtracker

{chr(10).join(workflow_rows)}

## Endelige leverancer der skal afsluttes

{chr(10).join(final_rows)}

{notes_block}## Arbejdsregler

* Hold alle projektgenererede filer inde i denne projektmappe.
* Brug `01-inputs/` til raa input og handoffs fra virkelige aktiviteter.
* Brug `02-working/` til synteser og udkast, som endnu ikke er valideret.
* Brug `03-reviews/` til valideringscheckpointet efter hvert trin.
* Brug `00-project-setup/{SHARED_PREP_DIRNAME}/` til seed'ede invitationsskabeloner, session briefs, evidensrequests, readiness-checks, retrospektiver, den klar-til-tilpasning-kladde til den foerste live-aktivitet og de automatisk opdaterede `next_activity_*.md`-filer.
* Koer `python3 Projects/sync_project_status.py --project-name "{project_name}"` efter hvert review, saa kontrolcenteret og `next_activity_*.md`-preppen bliver opdateret.
"""

    workflow_rows = [
        "| Stage | Purpose | Input file | Working output | Review file | Status |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    first_open_index = next(
        (i for i, result in enumerate(stage_results) if result["decision"] != "validated"),
        None,
    )
    for index, stage in enumerate(stage_results):
        decision = stage["decision"]
        if decision:
            row_status = english_status_label(decision, stage["review_date"])
        else:
            if first_open_index == index:
                row_status = "Next when resumed" if on_hold else "Current stage"
            else:
                row_status = "Not started"
        workflow_rows.append(
            "| {stage_label} | {purpose} | `{input_file}` | `{working_file}` | `{review_file}` | {status} |".format(
                stage_label=stage["stage"],
                purpose=stage["purpose"],
                input_file=f"01-inputs/{stage['input_file']}",
                working_file=f"02-working/{stage['working_file']}",
                review_file=f"03-reviews/{stage['review_file']}",
                status=row_status,
            )
        )

    final_rows = [
        "| Deliverable | Main file | Status |",
        "| --- | --- | --- |",
    ]
    for artifact in final_artifacts_for_config(config):
        final_label = english_final_status_label(final_statuses.get(artifact["file"]))
        final_rows.append(
            f"| {artifact['deliverable']} | `04-final/{artifact['file']}` | {final_label} |"
        )

    notes_block = ""
    if project_notes:
        notes_block = "## Project notes\n\n" + "\n".join(project_notes) + "\n\n"

    return f"""# Project index

## Project overview

* Project name: {project_name}
* Folder name: {folder_name}
* Package: Package {package}
* Working language: {config['language_label']}
* Created date: {created_date}
* Status: {display_status(project_status, language)}
* Current stage: {current_stage}
* Shared prep assets: `00-project-setup/{SHARED_PREP_DIRNAME}/`
* Recommended next action: {next_action}

## Workflow tracker

{chr(10).join(workflow_rows)}

## Final deliverables to complete

{chr(10).join(final_rows)}

{notes_block}## Working rules

* Keep all project-generated files inside this project folder.
* Use `01-inputs/` for raw input and handoffs from real-world activities.
* Use `02-working/` for syntheses and drafts that are not yet validated.
* Use `03-reviews/` for the validation checkpoint after each stage.
* Use `00-project-setup/{SHARED_PREP_DIRNAME}/` for seeded invite templates, session briefs, evidence requests, readiness checks, retrospectives, the ready-to-edit first live activity draft, and the auto-refreshed `next_activity_*.md` files.
* When the next stage is a real-world activity, run that activity first and then return with the completed notes in the matching input file.
* Run `python3 Projects/sync_project_status.py --project-name "{project_name}"` after each review so the control center and `next_activity_*.md` prep stay up to date.
"""


def build_project_setup_text(
    project_name: str,
    folder_name: str,
    package: str,
    language: str,
    sections: dict[str, str],
    project_status: str,
) -> str:
    sponsor = clean_placeholder(
        get_section(
            sections,
            "Sponsor or main client owner",
            "Sponsor eller primaer kundeansvarlig",
        )
    ) or ("[Tekst]" if language == "danish" else "[Text]")
    created_date = clean_placeholder(get_section(sections, "Created date", "Oprettelsesdato"))
    notes = get_section(sections, "Notes", "Noter")
    if not clean_placeholder(notes):
        notes = "* [Note]\n* [Note]" if language == "english" else "* [Note]\n* [Note]"
    notes = clean_project_setup_notes(notes, language)
    shared_note = shared_prep_note(language)
    notes = f"{shared_note}\n{notes}"
    storage_rule = clean_placeholder(get_section(sections, "Storage rule", "Regel for opbevaring"))
    if not storage_rule:
        storage_rule = (
            "Alle projektgenererede filer for dette forloeb gemmes inde i denne projektmappe."
            if language == "danish"
            else "All project-generated files for this engagement are stored inside this project folder."
        )

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
{sponsor}

## Oprettelsesdato
{created_date}

## Status
{display_status(project_status, language)}

## Kontrolcenter
project_index.md

## Regel for opbevaring
{storage_rule}

## Noter
{notes}
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
{sponsor}

## Created date
{created_date}

## Status
{display_status(project_status, language)}

## Control center
project_index.md

## Storage rule
{storage_rule}

## Notes
{notes}
"""


def resolve_project_dir(args: argparse.Namespace) -> Path:
    if args.project_path:
        path = Path(args.project_path).expanduser().resolve()
        return path
    return (PROJECTS_DIR / normalize_project_name(args.project_name)).resolve()


def main() -> int:
    args = parse_args()
    project_dir = resolve_project_dir(args)
    if not project_dir.exists():
        print(f"Error: {project_dir} does not exist.", file=sys.stderr)
        return 1

    setup_path = project_dir / "00-project-setup" / "project_setup.md"
    if not setup_path.exists():
        print(f"Error: {setup_path} does not exist.", file=sys.stderr)
        return 1

    setup_text = setup_path.read_text(encoding="utf-8")
    setup_sections = split_sections(setup_text)

    project_name = clean_placeholder(get_section(setup_sections, "Project name", "Projektnavn"))
    folder_name = clean_placeholder(get_section(setup_sections, "Folder name", "Mappenavn")) or project_dir.name
    package = parse_package_letter(get_section(setup_sections, "Package", "Pakke"))
    language = parse_language_key(get_section(setup_sections, "Working language", "Arbejdssprog"))
    created_date = clean_placeholder(get_section(setup_sections, "Created date", "Oprettelsesdato"))
    existing_status = normalize_status_value(get_section(setup_sections, "Status"))

    state = derive_workflow_state(project_dir, package, language, existing_status)
    final_project_status = apply_status_override(
        state["derived_status"], language, args
    )
    next_action = str(state["next_action"])
    if final_project_status == "on_hold":
        if language == "danish":
            next_action = f"Naar projektet genoptages, {next_action[:1].lower() + next_action[1:]}"
        else:
            next_action = f"When the project resumes, {next_action[:1].lower() + next_action[1:]}"

    project_notes = collect_existing_project_notes(project_dir / "project_index.md", language)
    legacy_notes = collect_legacy_notes(project_dir, language)
    for note in legacy_notes:
        if note not in project_notes:
            project_notes.append(note)

    project_index_text = build_project_index_text(
        project_name=project_name,
        folder_name=folder_name,
        package=package,
        language=language,
        created_date=created_date,
        project_status=final_project_status,
        current_stage=str(state["current_stage"]),
        next_action=next_action,
        stage_results=state["stage_results"],  # type: ignore[arg-type]
        final_statuses=state["final_statuses"],  # type: ignore[arg-type]
        project_notes=project_notes,
    )
    project_setup_text = build_project_setup_text(
        project_name=project_name,
        folder_name=folder_name,
        package=package,
        language=language,
        sections=setup_sections,
        project_status=final_project_status,
    )

    if args.dry_run:
        prep_ok, prep_message = refresh_next_activity_prep(project_dir, dry_run=True)
        print("Dry run:")
        print(f"  Project path: {project_dir}")
        print(f"  Derived status: {display_status(final_project_status, language)}")
        print(f"  Current stage: {state['current_stage']}")
        print(f"  Next action: {next_action}")
        print(f"  Next-activity prep: {'ready' if prep_ok else 'failed'}")
        if prep_message:
            print(f"  Prep detail: {prep_message.splitlines()[0]}")
        return 0

    (project_dir / "project_index.md").write_text(project_index_text, encoding="utf-8")
    setup_path.write_text(project_setup_text, encoding="utf-8")

    prep_ok, prep_message = refresh_next_activity_prep(project_dir, dry_run=False)
    if not prep_ok:
        print("Warning: next-activity prep generation failed.", file=sys.stderr)
        if prep_message:
            print(prep_message, file=sys.stderr)
        return 1

    print("Project control center synced:")
    print(f"  Project path: {project_dir}")
    print(f"  Status: {display_status(final_project_status, language)}")
    print(f"  Current stage: {state['current_stage']}")
    print(f"  Next action: {next_action}")
    if prep_message:
        print(f"  Next-activity prep: {prep_message.splitlines()[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
