# Konvention for Projects-mappen

Brug `Projects/` til faktiske pakkeforløb og til dry runs, som skal holdes adskilt fra de delte kildedokumenter.

## Hvad hører til her

* Reelle Pakke A-, Pakke B- og Pakke C-forløb
* Dry runs og scenariotests i `Projects/Dry runs/`
* Alle projektspecifikke artefakter, der bliver skabt under et pakkeforløb

Gem ikke live-projektartefakter i `Packages/`, `Sales materials/` eller `skills/`. De mapper er til genanvendeligt kildemateriale.

## Foretrukken vej til opsætning

Brug bootstrap-værktøjet til at oprette og seed'e et live-projekt i ét trin:

```bash
python3 Projects/bootstrap_project.py --project-name "Fried IQ" --package A --language english
```

Kommandoen vil:

* oprette den standardiserede mappestruktur
* oprette `project_setup.md`
* oprette `project_index.md` som projektets kontrolcenter
* seed'e delte forberedelsesaktiver i `00-project-setup/shared-prep/`
* seed'e en pakkespecifik klar-til-tilpasning-kladde til den foerste live-aktivitet i `00-project-setup/shared-prep/`
* forberede projektet saa senere review-syncs automatisk kan opdatere `next_activity_*.md`-prep-pakken
* seed'e de relevante filer til Trin 0 og aktivitetsinput i `01-inputs/`
* seed'e de relevante aktivitetsoutputfiler i `02-working/`
* seed'e de relevante reviewfiler i `03-reviews/`
* seed'e pakkens endelige leveranceskabelon i `04-final/`

Manuel opsætning bør nu kun bruges som fallback.

## Saa holdes kontrolcenteret opdateret

Efter at en reviewfil er blevet opdateret med en valideringsbeslutning, saa koer:

```bash
python3 Projects/sync_project_status.py --project-name "Fried IQ"
```

Nyttige varianter:

* `--resume`: flyt et pauset projekt tilbage til `Aktiv`, mens trinstatus bliver synkroniseret
* `--on-hold`: behold eller flyt projektet til `Pauset`, mens trinstatus bliver synkroniseret
* `--close`: marker projektet som `Lukket` efter synkronisering

Kommandoen laeser reviewfilerne i `03-reviews/`, tjekker godkendelsesstatus i `04-final/`, opdaterer baade `project_index.md` og `00-project-setup/project_setup.md` og genopfrisker de genererede `next_activity_*.md`-prepfiler i `00-project-setup/shared-prep/`.

Naar projektet bliver koert gennem dette tool, skal assistenten koere denne kommando automatisk i samme tur som valideringsopdateringen.

Naar et valideret trin flytter projektet videre til en virkelig aktivitet, skal assistenten ogsaa:

* goere det eksplicit, at naeste skridt er en live-aktivitet og ikke et rent AI-trin
* pege paa den relevante projektinputfil i `01-inputs/`
* pege paa den matchende facilitatorguide og eventuelle relevante skabeloner, spoergeguides eller vaerktoejsfiler
* vente paa de faerdige aktivitetsnoter, foer syntesen genoptages, medmindre brugeren eksplicit beder om at simulere eller forberede aktiviteten i chatten
* bruge den kanoniske svarstruktur i [Templates/Danish/Shared/live_activity_handoff_message_template_danish.md](Templates/Danish/Shared/live_activity_handoff_message_template_danish.md) eller den engelske pendant

Brug [Templates/Danish/Shared/activity_readiness_checklist_danish.md](Templates/Danish/Shared/activity_readiness_checklist_danish.md), hvis du vil sanity-tjekke, om naeste live-aktivitet faktisk er klar til at blive koert.

Brug [Templates/Danish/Shared/evidence_request_template_danish.md](Templates/Danish/Shared/evidence_request_template_danish.md), naar naeste aktivitet afhaenger af evidens, adgang, eksporter eller andet stoettemateriale fra kundeteamet.

Brug [Templates/Danish/Shared/workshop_invite_template_danish.md](Templates/Danish/Shared/workshop_invite_template_danish.md), [Templates/Danish/Shared/interview_invite_and_consent_template_danish.md](Templates/Danish/Shared/interview_invite_and_consent_template_danish.md) og [Templates/Danish/Shared/session_brief_template_danish.md](Templates/Danish/Shared/session_brief_template_danish.md), naar du skal forberede selve live-sessionen og ikke kun syntesen omkring den.

Ved interviewaktiviteter opretter `generate_next_activity_prep.py` nu ogsaa en projektspecifik `next_activity_interview_guide*.md` i `00-project-setup/shared-prep/`, bygget paa den validerede projektkontekst indtil nu.

Ved mappingaktiviteter opretter `generate_next_activity_prep.py` nu ogsaa en projektspecifik `next_activity_mapping_canvas*.md` i `00-project-setup/shared-prep/`, bygget paa den validerede projektkontekst indtil nu.

Brug [Templates/Danish/Shared/pilot_retrospective_template_danish.md](Templates/Danish/Shared/pilot_retrospective_template_danish.md) efter en pilot eller dry run, saa forbedringer af frameworket bygger paa observeret friktion og ikke hukommelse.

## Regel for projektnavne

Når et nyt reelt pakkeforløb starter:

1. Bed om projektnavnet, før der oprettes projektspecifikke artefakter.
2. Omdan navnet til et mappenavn, der er sikkert at bruge, ved at erstatte mellemrum med bindestreger og fjerne usikre specialtegn.
3. Bevar resultatet læsbart, hvor det er muligt.

Eksempel:

* `Fried IQ` bliver til `Projects/Fried-IQ/`

Hvis mappen allerede findes, så stop og spørg, om den eksisterende mappe skal genbruges, eller om der skal oprettes en ny med et andet navn.

## Standard mappestruktur

Hvert reelt projekt bør bruge denne struktur:

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

## Hvad der skal ligge hvor

* `project_index.md`: projektets kontrolcenter med nuværende trin, status, seed'ede filer og tjekliste over endelige leverancer
* `00-project-setup/`: projektopsætning, pakketype, arbejdssprog, sponsor, oprettelsesdato og status
* `00-project-setup/shared-prep/`: seed'ede delte forberedelsesaktiver som invitationsskabeloner, samtykketekst, session briefs, evidensrequests, readiness-checks, retrospektivskabeloner, en klar-til-tilpasning-kladde til den foerste live-aktivitet, automatisk opdaterede `next_activity_*.md`-prepfiler, projektspecifikke interviewguides til interviewaktiviteter og projektspecifikke mapping-canvasfiler til mappingaktiviteter
* `01-inputs/`: rå kundeinput, workshopnoter, interviewnoter, eksporter af evidens og handoffskabeloner
* `02-working/`: seed'ede aktivitetsoutput, igangværende syntese, udkast til kort, anbefalinger, prototype prompt packs og andre arbejdsfiler
* `03-reviews/`: seed'ede reviewfiler, output delt til validering, reviewnoter, ændringslog og godkendte checkpoints
* `04-final/`: endelige leverancer, godkendte anbefalingspakker, endelige prototype prompt packs og eksportklare artefakter

## Opbevaringsregel

Når en projektmappe er oprettet, skal alle projektgenererede filer for forløbet blive i den mappe.

Det gælder blandt andet:

* intake-opsummeringer
* handoffs fra aktiviteter
* udkast til syntese
* noter fra validering
* endelige pakkeleverancer
* prototype prompt packs

Pakke- og salgsdokumenterne i `Packages/` og `Sales materials/` forbliver det genanvendelige styresystem for tilbuddet. De er ikke projektmapper.

## Genanvendelige skabeloner

Brug [Templates/README_danish.md](Templates/README_danish.md) til det genanvendelige skabelonbibliotek, som understøtter live-projekter.

Biblioteket indeholder:

* Delte skabeloner til projektopsætning, review, handoff, evidensrequest, workshopinvitation, interviewinvitation og samtykke, session brief, aktivitetsparathed og pilotretrospektiv
* Pakkespecifikke skabeloner til intake og handoffs fra aktiviteter
* Pakkespecifikke skabeloner til endelige leverancer

`bootstrap_project.py` genererer derudover projektets dashboard samt de pakkespecifikke aktivitetsoutput- og reviewfiler, som ligger inde i hver projektmappe. Brug `sync_project_status.py` til at holde kontrolfilerne aligned, naar projektet er i gang, og til automatisk at genopfriske prep-pakken til naeste live-aktivitet. Du kan ogsaa koere `python3 Projects/generate_next_activity_prep.py --project-name "Fried IQ"` direkte, hvis du kun vil genopfriske prep-pakken.

Direkte spoergsmaal til brugeren skal ligge i det primaere svar og ikke i commentary-opdateringer, saa de ikke bliver skjult i interfacet.
Under en simuleret aktivitet, der koeres som en spoergsmaal-for-spoergsmaal-sekvens, skal der skiftes til chat-only simulation mode, svarene skal bufferes i arbejdshukommelsen, og projektfilerne maa foerst persisteres, naar sekvensen er faerdig, eller naar brugeren eksplicit beder om at gemme midt i forloebet.
Naar et opfoelgende spoergsmaal afhænger af et tidligere svar, skal det tidligere svar gentages i spoergsmaalet, saa brugeren ikke skal scrolle tilbage.
Hvis intern kommando- eller tooltekst alligevel slipper ud i den synlige samtale, skal spoergsmaalssekvensen stoppes, og de resterende felter skal indsamles i en fallback mode med ét samlet svar.
