# Intern driftsmodel for pakkerne

Internt notat: Dette dokument beskriver, hvordan pakkeporteføljen leveres bag kulissen. Det er ikke kundevendt og bør ikke citeres eller refereres i tilbud, salgsmateriale eller ledelsesoplæg.

## Formål

Pakkeporteføljen kører nu på en ensartet intern struktur, så tilbuddets sprog, de faciliterede aktiviteter og den trinvis styrede synteseproces understøtter de samme leverancer.

Målet er at gøre hver pakke:

* Lettere at sælge, fordi pakkelogikken er tydelig og gentagelig
* Lettere at facilitere, fordi de virkelige aktiviteter bliver forberedt på en ensartet måde
* Lettere at køre med AI-støtte, fordi hver aktivitet har et tydeligt handoff, et output og en valideringsport
* Lettere at vedligeholde, fordi ændringer kan spores på tværs af opsummering, facilitering og intern syntese

## Tre-lags-modellen

Hver pakke vedligeholdes i tre forbundne lag:

### 1. Opsummeringslaget

Dette er pakkelogikken og den kommercielle beskrivelse.

Det definerer:

* Hvad pakken er til
* Hvornår den skal bruges
* Aktiviteter, tidslinje og estimeret indsats
* De konkrete leverancer og beslutninger, pakken understøtter

Primære filer:

* `./strategic_ux_packages_danish.md`
* `./Package_A_core_activities_danish.md`
* `./Package_B_core_activities_danish.md`
* `./Package_C_core_activities_danish.md`
* `../../Sales materials/Danish/executive_offer_one_pager_danish.md`
* `../../Sales materials/Danish/upstream_discovery_positioning_danish.md`

### 2. Facilitatorlaget

Dette er den praktiske leveranceguide til konsulenten eller facilitatoren.

Det definerer:

* Hvordan aktiviteten forberedes og gennemføres
* Hvem der skal deltage
* Hvilken evidens eller hvilket materiale der skal indsamles
* Hvad der skal fanges i handoffet tilbage til den interne syntese
* Hvad kunden skal validere, før næste aktivitet begynder

Primære filer:

* `./Package_A_facilitator_guide_danish.md`
* `./Package_B_facilitator_guide_danish.md`
* `./Package_C_facilitator_guide_danish.md`

### 3. Det interne synteselag

Dette er den trinvis styrede interne workflowlogik, som omsætter indsamlet input til beslutningsklare output.

Det definerer:

* Krav til inputformat for hver aktivitet
* Analyse- og syntesetrin
* Forventet outputformat
* Valideringsstatus og stop- eller go-regler
* Hvad der føres videre til næste aktivitet
* Produktion af prototype prompt pack, hvor det er relevant

Primære filer:

* `./Package_A_ai_process_danish.md`
* `./Package_B_ai_process_danish.md`
* `./Package_C_ai_process_danish.md`
* `./prototype_prompt_pack_template_danish.md`

## Understoettende eksekveringsbibliotek

Tre-lags-modellen er stadig den bærende ryggrad.

Mappen `/skills` er et understoettende eksekveringsbibliotek bag denne model og ikke et parallelt pakkesystem.

Det skal bruges til at:

* Drive aktivitetsspecifik syntese, faciliteringsstoette og review
* Holde specialiseret logik genanvendelig paa tvaers af pakker
* Understoette valgfrie specialistagenter hvor en afgraenset aktivitet tydeligt har gavn af dem

Det maa ikke bruges til at:

* Erstatte pakkernes stage gates
* Skabe et andet bruger-synligt workflow
* Drive vaek fra pakkefilerne og projektskabelonerne

Primaere filer:

* `./internal_activity_skill_mapping_danish.md`
* `../../skills/`

## Konvention for projektopbevaring

Ethvert reelt Pakke A-, Pakke B- eller Pakke C-forløb bør starte med et projektopsætningstrin, før intake begynder.

Ved start af et live-pakkeforløb:

* Bed brugeren om projektnavnet
* Normalisér navnet til et mappenavn, der er sikkert at bruge, og stop for bekræftelse, hvis den normaliserede mappe allerede findes
* Opret `../../Projects/<Project-Name>/`
* Opret `../../Projects/<Project-Name>/00-project-setup/`
* Opret `../../Projects/<Project-Name>/00-project-setup/shared-prep/`
* Opret `../../Projects/<Project-Name>/01-inputs/`
* Opret `../../Projects/<Project-Name>/02-working/`
* Opret `../../Projects/<Project-Name>/03-reviews/`
* Opret `../../Projects/<Project-Name>/04-final/`
* Opret `../../Projects/<Project-Name>/project_index.md` som projektets kontrolcenter
* Opret `../../Projects/<Project-Name>/00-project-setup/project_setup.md`
* Seed de delte forberedelsesaktiver i `00-project-setup/shared-prep/`
* Seed en pakkespecifik klar-til-tilpasning-kladde til den foerste live-aktivitet i `00-project-setup/shared-prep/`
* Genopfrisk de genererede `next_activity_*.md`-prepfiler i `00-project-setup/shared-prep/` efter hvert review-sync
* Seed de relevante filer til Trin 0 og aktivitetsinput i `01-inputs/`
* Seed de relevante aktivitetsoutputfiler i `02-working/`
* Seed de relevante reviewfiler i `03-reviews/`
* Seed den endelige leverancefil i `04-final/`
* Hold alle projektgenererede filer for forløbet inde i denne mappestruktur
* Efter at en reviewfil er opdateret med en valideringsbeslutning, saa koer `python3 Projects/sync_project_status.py --project-name "<Projektnavn>"`, saa projektets kontrolfiler afspejler den aktuelle workflowstatus og prep-pakken til naeste live-aktivitet bliver genopfrisket
* Naar arbejdet bliver koert gennem dette tool, skal assistenten goere det automatisk i samme tur som valideringsopdateringen

Brug [../../Projects/README_danish.md](../../Projects/README_danish.md) som fælles konvention for opbevaring. Hold `../../Projects/Dry runs/` adskilt til scenariotests og ikke til live-kundearbejde.

Brug [../../Projects/Templates/Danish/Shared/activity_readiness_checklist_danish.md](../../Projects/Templates/Danish/Shared/activity_readiness_checklist_danish.md), naar en live-aktivitet har brug for et readiness-check foer afvikling, og brug [../../Projects/Templates/Danish/Shared/pilot_retrospective_template_danish.md](../../Projects/Templates/Danish/Shared/pilot_retrospective_template_danish.md) efter piloter eller dry runs til at indsamle forbedringer til naeste iteration.

Brug [../../Projects/Templates/Danish/Shared/evidence_request_template_danish.md](../../Projects/Templates/Danish/Shared/evidence_request_template_danish.md), naar en aktivitet afhaenger af kundeside-evidens, adgang, eksporter eller andet stoettemateriale.

Brug [../../Projects/Templates/Danish/Shared/workshop_invite_template_danish.md](../../Projects/Templates/Danish/Shared/workshop_invite_template_danish.md), [../../Projects/Templates/Danish/Shared/interview_invite_and_consent_template_danish.md](../../Projects/Templates/Danish/Shared/interview_invite_and_consent_template_danish.md) og [../../Projects/Templates/Danish/Shared/session_brief_template_danish.md](../../Projects/Templates/Danish/Shared/session_brief_template_danish.md), naar naeste skridt har brug for praktisk forberedelse af en live-session. Nye projekter boer ogsaa starte med den seed'ede `00-project-setup/shared-prep/first_live_activity_example_draft_danish.md` som et klar-til-tilpasning foerste udkast til den foerste live-aktivitet og derefter bruge de automatisk opdaterede `next_activity_*.md`-filer efter hvert valideret trin.

## Regel for kundevendt sprog

Kunder behøver ikke høre om agentiske workflows, interne prompts eller AI-processens mekanik.

I kundevendt materiale skal arbejdet beskrives som:

* En tydelig pakke med en defineret beslutning, der skal understøttes
* Fokuserede workshops, interviews, reviews og input af evidens
* Struktureret syntese mellem aktiviteterne
* Review- og valideringspunkter knyttet til konkrete output

Arbejd ikke med beskrivelser som:

* Et AI-workflow
* En agentisk proces
* En promptdrevet produktionsmodel
* Et skjult automationssystem

Kunden skal opleve arbejdet som en veldrevet afklaringsproces og ikke som en forklaring af den interne maskine, der understøtter den.

## Standardmønster for afhængigheder

Den normale rækkefølge er:

1. Kunden eller facilitatoren skaber det nødvendige input i den virkelige aktivitet.
2. Det indfangede input struktureres i det aftalte handoffformat.
3. Den interne synteseproces omsætter inputtet til et konkret output.
4. Kunden gennemgår og validerer outputtet.
5. Næste aktivitet starter først, når det forrige output er accepteret, eller åbne risici er gjort tydelige.

Dette mønster gælder på tværs af Pakke A, Pakke B og Pakke C.

## Regel for handoff til virkelige aktiviteter

Efter ethvert valideret trin skal der først tjekkes, om næste skridt er en virkelig aktivitet eller et internt syntesetrin.

Hvis næste skridt er en virkelig aktivitet:

* Stop og hand off til aktiviteten eksplicit i stedet for straks at bede om de færdige noter
* Navngiv aktiviteten, formålet og den estimerede tid
* Angiv hvem der bør deltage, eller hvilket materiale eller hvilken evidens der skal indsamles
* Link til den seed'ede projektinputfil i `Projects/<Project-Name>/01-inputs/`
* Link til den relevante facilitatorguide og eventuelle relevante skabeloner, spørgeguides eller værktøjsfiler
* Bed brugeren om at vende tilbage med de færdige noter eller sige til, hvis der er brug for hjælp til at forberede aktiviteten
* Brug den præcise sektionsrækkefølge i [../../Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md](../../Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md)

Bed kun direkte om de færdige aktivitetsnoter i chatten, når brugeren eksplicit beder om at simulere eller forberede aktiviteten inde i værktøjet.

## Regel for synlighed af brugerprompts

Fordi interfacet kan skjule statusopdateringer:

* Hold fremdriftsnarration i commentary eller statusopdateringer
* Læg direkte spørgsmål til brugeren, valideringsprompts og next-step-requests i det primære brugersvar
* Gem ikke selve prompten til brugeren inde i commentary-tekst
* Gem heller ikke nogen del af handoff-strukturen til live-aktiviteter inde i commentary-tekst

## Sikkerhedsregel for live spørgesekvenser

Når brugeren beder om at simulere en live aktivitet inde i værktøjet:

* Behandl hele sekvensen som en midlertidig capture mode
* Skift til chat-only simulation mode under hele sekvensen
* Kør ingen fillæsninger, filskrivninger, sync-kommandoer eller andre tool actions overhovedet under den aktive spørgeflow
* Hold de indsamlede noter i arbejdshukommelsen, indtil sekvensen er færdig
* Persistér kun noterne efter det sidste spørgsmål, når brugeren eksplicit beder om at gemme midt i forløbet, eller ved næste valideringscheckpoint
* Lad ikke rå kommando- eller tooltekst slippe ind i den synlige spørgeflow
* Hold det brugerrettede flow rent og uafbrudt, indtil sekvensen er færdig

## Regel for recap af tidligere svar

Når et opfølgende spørgsmål afhænger af et svar, brugeren allerede har givet i samme forløb:

* Gentag det relevante tidligere svar direkte i det nye spørgsmål
* Forvent ikke, at brugeren scroller tilbage for at genskabe konteksten
* Brug korte recap-formuleringer, især ved valg, constraints, foretrukne retninger og tidligere navngivne koncepter

## Fallback-regel for simulering

Hvis intern kommando- eller tooltekst slipper ud i den synlige samtale under en simuleret aktivitet:

* Behandl det som en blocker for spørgsmaal-for-spørgsmaal-formatet
* Stop den live spørgesekvens med det samme
* Skift til en fallback mode med ét samlet svar
* Giv brugeren en kort opsummering af det, der allerede er indfanget
* Bed derefter om alle resterende felter i ét almindeligt tekstsvar
* Gem og syntetisér først, når brugeren har returneret de resterende felter
* Navngiv problemet ærligt som en workflow- eller platformbegrænsning og tag det med i pilotfeedbacken

## Regel for leverancer

Hver pakke skal stadig producere de konkrete leverancer, der er lovet i tilbudsmaterialet. Den interne driftsmodel understøtter disse leverancer, men erstatter dem ikke.

Det betyder:

* Pakke A skal stadig producere anbefalingsoplægget, kortet over brud i det valgte trin i rejsen, den klikbare prototype og listen over risici eller næste skridt
* Pakke B skal stadig producere indsigtsopsamlingen, kortet over nuværende og fremtidig rejse, listen over nødvendige serviceændringer, den klikbare prototype og den prioriterede leveranceanbefaling
* Pakke C skal stadig producere ledelsesoplægget, blueprintet over den nuværende service, den testede fremtidige servicemodel, det faseopdelte roadmap og opsummeringen af ændringsbehov eller business case

Hvor en prototype er en del af leverancen, er prompt packen et internt produktionsstøttende artefakt. Den er ikke kundeleverancen i sig selv.
Hvor prototypearbejde er en del af pakken, skal den vigtigste endelige leverance, prototype prompt pack og prototype record holdes i separate filer i `04-final/`.

## Regel for vedligeholdelse

Når en pakke ændres, skal alle tre lag opdateres.

Minimumsopdateringen er:

* Pakkesproget i `./strategic_ux_packages_danish.md`
* Pakkeopsummeringen i `./Package_*_core_activities_danish.md`
* Den tilhørende facilitator guide
* Den tilhørende interne syntesefil
* Ethvert porteføljedokument, hvis ordlyd afhænger af pakkelogikken

## Anvendelse på porteføljeniveau

Brug modellen sådan:

* `./strategic_ux_packages_danish.md`, `../../Sales materials/Danish/upstream_discovery_positioning_danish.md` og `../../Sales materials/Danish/executive_offer_one_pager_danish.md` skal beskrive kundens oplevelse af modellen uden at nævne AI
* `../../Sales materials/Danish/discovery_sales_playbook_danish.md` skal hjælpe med at forklare den trinvise leverancemodel i kommercielle dialoger uden at eksponere intern mekanik
* `../../Sales materials/Danish/discovery_phase_proposal_template_danish.md` skal oversætte modellen til tilbudssikkert sprog og konkrete kundeforpligtelser
* Facilitator guides og interne syntesefiler skal bære den operationelle detalje, der er nødvendig for at køre arbejdet ensartet
