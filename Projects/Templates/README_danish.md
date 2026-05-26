# Projekternes skabelonbibliotek

Brug denne mappe som genanvendelig kilde til skabeloner for live-forløb i Pakke A, Pakke B og Pakke C.

## Formål

Skabelonerne i denne mappe skal gøre projektopsætning, intake, handoffs fra aktiviteter, reviewpunkter og endelige leverancer lettere at gennemføre på en ensartet måde.

De er genanvendelige kildefiler for projektets bootstrap-værktøj. Udfyld dem ikke direkte til et live-projekt. Den normale workflow er at køre `Projects/bootstrap_project.py`, som opretter projektmappen, tilføjer `project_index.md` og seed'er de rigtige filer automatisk.

## Struktur

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

## Hvad der skal bruges hvor

* `English/Shared/` og `Danish/Shared/`: genanvendelige skabeloner til projektopsætning, review, handoff til live-aktiviteter, evidensrequest, workshopinvitation, interviewinvitation og samtykke, session brief, aktivitetsparathed og pilotretrospektiv, som kan bruges på tværs af alle pakker
* `English/Package_A/` og `Danish/Package_A/`: skabeloner til Trin 0-intake, handoffs fra aktiviteter og endelige leverancer i Pakke A
* `English/Package_B/` og `Danish/Package_B/`: skabeloner til Trin 0-intake, handoffs fra aktiviteter og endelige leverancer i Pakke B
* `English/Package_C/` og `Danish/Package_C/`: skabeloner til Trin 0-intake, handoffs fra aktiviteter og endelige leverancer i Pakke C

Bootstrap-værktøjet genererer derudover pakkespecifikke udkast til aktivitetsoutput og reviewfiler direkte fra pakke-workflowets metadata, så ikke alle seed'ede filer findes som selvstændige kildefiler i denne mappe.

Brug [Danish/Shared/live_activity_handoff_message_template_danish.md](Danish/Shared/live_activity_handoff_message_template_danish.md) og den engelske pendant som den kanoniske struktur for den brugerrettede handoff-besked, naar et valideret trin foerer videre til den naeste live-aktivitet.

Brug [Danish/Shared/evidence_request_template_danish.md](Danish/Shared/evidence_request_template_danish.md), naar en pakkeaktivitet afhænger af evidens, adgang, eksporter eller andet støttemateriale fra kundeteamet.

Brug [Danish/Shared/workshop_invite_template_danish.md](Danish/Shared/workshop_invite_template_danish.md), naar du har brug for en tydelig invitation til en workshop, mappingsession eller valideringssession.

Brug [Danish/Shared/interview_invite_and_consent_template_danish.md](Danish/Shared/interview_invite_and_consent_template_danish.md), naar du skal invitere deltagere til interviews, kontekstuelle sessioner eller shadowing og forklare samtykke klart.

Brug [Danish/Shared/session_brief_template_danish.md](Danish/Shared/session_brief_template_danish.md) som facilitatorens interne run sheet foer en live-session.

Brug [Danish/Shared/current_journey_mapping_template_danish.md](Danish/Shared/current_journey_mapping_template_danish.md), naar du skal kortlaegge den nuvaerende rejse i en mappingsession og vil have en enkel canvas-struktur at arbejde i.

Brug [Danish/Shared/activity_readiness_checklist_danish.md](Danish/Shared/activity_readiness_checklist_danish.md) foer en live-aktivitet, naar du vil tjekke, om workshoppen, interviewet, evidensreviewet eller mappingsessionen faktisk er klar til at blive koert.

Brug [Danish/Shared/pilot_retrospective_template_danish.md](Danish/Shared/pilot_retrospective_template_danish.md) efter en pilot eller dry run til at indfange friktion, styrker og konkrete forbedringer til naeste iteration af frameworket.

## Foreslået brug i et live-projekt

1. Kør `python3 Projects/bootstrap_project.py --project-name "<Projektnavn>" --package <A|B|C> --language <english|danish>`.
2. Lad bootstrap-værktøjet oprette den standardiserede projektstruktur, `project_index.md` og de relevante seed'ede filer.
3. Udfyld de seed'ede inputfiler i `01-inputs/`, efterhånden som pakken skrider frem.
4. Brug de seed'ede outputfiler i `02-working/`, mens pakken bliver syntetiseret.
5. Brug de seed'ede review- og leverancefiler, når projektet bevæger sig gennem validering og afslutning.

Manuel kopiering fra denne mappe bør kun bruges, hvis bootstrap-værktøjet ikke er tilgængeligt.

## Sprogregel

Brug de engelske skabeloner til engelsksprogede forløb og de danske skabeloner til dansksprogede forløb. Strukturen er spejlet, så den samme workflow kan køre på begge sprog.
