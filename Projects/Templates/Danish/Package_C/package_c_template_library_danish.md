# Skabelonbibliotek for Pakke C

Brug denne fil som den genanvendelige skabelonkilde til live-projekter i Pakke C.

## Foreslaaede filer i et live-projekt

* `project_index.md`
* `01-inputs/package_c_stage_0_intake_input.md`
* `01-inputs/package_c_activity_1_1_input.md`
* `01-inputs/package_c_activity_1_2_input.md`
* `01-inputs/package_c_activity_2_1_input.md`
* `01-inputs/package_c_activity_2_2_input.md`
* `01-inputs/package_c_activity_3_1_input.md`
* `01-inputs/package_c_activity_4_1_input.md`
* `02-working/package_c_stage_0_intake_summary.md`
* `02-working/package_c_activity_1_1_strategic_framing_summary.md`
* `02-working/package_c_activity_1_2_service_scope_summary.md`
* `02-working/package_c_activity_2_1_operational_observation_summary.md`
* `02-working/package_c_activity_2_2_blueprint_summary.md`
* `02-working/package_c_activity_3_1_future_state_service_model_summary.md`
* `02-working/package_c_activity_4_1_roadmap_and_business_case_summary.md`
* `03-reviews/package_c_stage_0_intake_check.md`
* `03-reviews/package_c_activity_1_1_review.md`
* `03-reviews/package_c_activity_1_2_review.md`
* `03-reviews/package_c_activity_2_1_review.md`
* `03-reviews/package_c_activity_2_2_review.md`
* `03-reviews/package_c_activity_3_1_review.md`
* `03-reviews/package_c_activity_4_1_review.md`
* `04-final/package_c_final_deliverable.md`
* `04-final/package_c_prototype_prompt_pack.md`
* `04-final/package_c_prototype_record.md`

Bootstrap genererer filerne i `02-working/` og `03-reviews/` automatisk ud fra workflow-metadataen for Pakke C, naar et live-projekt startes.

## Designnoter til skabelonerne

Pakke C skal stadig foeles struktureret, men ikke bureaukratisk.

Det betyder:

* Hver seed'et inputfil er struktureret som en kort trinvis sekvens og ikke som et langt spoergeskema.
* Valideret kontekst skal foeres videre som standard.
* Kun reelt nyt eller aendret input skal indfanges i hver aktivitet.
* Valgfri prototypestoette til et udvalgt hoejrisiko-udsnit skal ligge i sine egne filer, saa den vigtigste endelige leverance bliver laesbar.

## Skabelon til Trin 0-intake

```md
# Package C - Trin 0 intake input

## Sekvensguide
Brug denne intake som 4 korte trin:
1. Kunde og service i scope
2. Strategiske beslutninger og hvorfor nu
3. Evidens og interessenter
4. Graenser

## Trin 1 af 4: Kunde og service i scope
### Kunde / kontekst
[Tekst]

### Service, proposition eller initiativ i scope
[Tekst]

## Trin 2 af 4: Strategiske beslutninger og urgency
### Strategiske eller investeringsmaessige beslutninger der skal understoettes
* [Beslutning]
* [Beslutning]

### Hvorfor dette er vigtigt nu
[Tekst]

## Trin 3 af 4: Evidens og interessenter
### Kendt evidens
[Tekst]

### Involverede interessenter eller teams
* [Interessent eller team]
* [Interessent eller team]

## Trin 4 af 4: Graenser
### Samlet graensesvar
[Et kort svar, der daekker baade kendte begraensninger og det, der skal holdes uden for scope]

### Kendte begraensninger
* [Begraensning]
* [Begraensning]

### Omraader uden for scope
* [Omraade]
* [Omraade]
```

## Skabelon til Aktivitet 1.1

```md
# Package C - Aktivitet 1.1 input

## Sekvensguide
Brug denne aktivitet som 3 korte trin:
1. Interviews og strategisk indramning
2. Pres paa servicen og konsekvenser
3. Spaendinger og investeringsspoergsmaal

## Viderefoert kontekst fra Trin 0
### Service eller initiativ i scope
[Tekst]

### Strategiske eller investeringsmaessige beslutninger der aktuelt antages
* [Beslutning]
* [Beslutning]

### Hvorfor-nu-kontekst der aktuelt antages
[Tekst]

## Trin 1 af 3: Interviews og strategisk indramning
### Interviewede roller
* [Rolle]
* [Rolle]

### Strategiske prioriteringer naevnt
* [Prioritet]
* [Prioritet]

## Trin 2 af 3: Pres paa servicen og konsekvenser
### Pres paa servicen eller sammenbrudspunkter
* [Pres]
* [Pres]

### Forretningsmaessige eller driftsmaessige konsekvenser
* [Konsekvens]
* [Konsekvens]

## Trin 3 af 3: Spaendinger og investeringsspoergsmaal
### Risici og spaendinger
* [Risiko eller spaending]
* [Risiko eller spaending]

### Investeringsspoergsmaal
* [Spoergsmaal]
* [Spoergsmaal]

### Konflikter eller uenigheder paa tvaers af interessenter
* [Konflikt]
* [Konflikt]
```

## Skabelon til Aktivitet 1.2

```md
# Package C - Aktivitet 1.2 input

## Sekvensguide
Brug denne aktivitet som 3 korte trin:
1. Strategisk spoergsmaal og service-scope
2. Afdelinger, kanaler og systemer
3. Kritiske momenter og fokus for feltarbejdet

## Viderefoert kontekst fra Aktivitet 1.1
### Strategisk spoergsmaal dette scope skal understoette
[Tekst]

### Vigtigste servicepres der skal holdes i mente
[Tekst]

## Trin 1 af 3: Strategisk spoergsmaal og service-scope
### Aftalt service-scope
[Tekst]

## Trin 2 af 3: Afdelinger, kanaler og systemer
### Afdelinger og driftsaktoerer
* [Aktoer]
* [Aktoer]

### Kanaler og kontaktpunkter
* [Kontaktpunkt]
* [Kontaktpunkt]

### Systemer og afhaengigheder
* [Afhaengighed]
* [Afhaengighed]

## Trin 3 af 3: Kritiske momenter og fokus for feltarbejdet
### Kritiske servicemomenter
* [Moment]
* [Moment]

### I scope
* [Element]
* [Element]

### Ude af scope
* [Element]
* [Element]

### Fokusomraader for feltarbejdet
* [Omraade]
* [Omraade]
```

## Skabelon til Aktivitet 2.1

```md
# Package C - Aktivitet 2.1 input

## Sekvensguide
Brug denne aktivitet som 3 korte trin:
1. Daekning af observationer
2. Driftsfriktion og skjult arbejde
3. Brud og spoergsmaal til blueprinting

## Viderefoert kontekst fra Aktivitet 1.2
### Observeret service-scope
[Tekst]

### Kritiske momenter der aktuelt antages
* [Moment]
* [Moment]

## Trin 1 af 3: Daekning af observationer
### Sessionstyper og deltagerfordeling
* [Type eller rolle]
* [Type eller rolle]

### Driftsnaer evidens gennemgaaet
* [Kilde]
* [Kilde]

## Trin 2 af 3: Driftsfriktion og skjult arbejde
### Observerede omveje
* [Omvej]
* [Omvej]

### Forsinkelser eller skjult arbejde
* [Forsinkelse]
* [Forsinkelse]

### Huller i ejerskab
* [Hul]
* [Hul]

## Trin 3 af 3: Brud og spoergsmaal til blueprinting
### Brud paa tvaers af kanaler, teams eller systemer
* [Brud]
* [Brud]

### Forskelle mellem beskrevet proces og levet virkelighed
* [Forskel]
* [Forskel]

### Spoergsmaal til blueprinting
* [Spoergsmaal]
* [Spoergsmaal]
```

## Skabelon til Aktivitet 2.2

```md
# Package C - Aktivitet 2.2 input

## Sekvensguide
Brug denne aktivitet som 3 korte trin:
1. Struktur for blueprintet
2. Forsinkelser, dobbeltarbejde og hotspots
3. Implikationer og carry-forward-logik

## Viderefoert kontekst fra Aktivitet 2.1
### Service i scope
[Tekst]

### Vigtigste driftsnaere brud der skal afspejles
[Tekst]

## Trin 1 af 3: Struktur for blueprintet
### Frontstage-interaktioner
* [Interaktion]
* [Interaktion]

### Backstage-processer
* [Proces]
* [Proces]

### Systemer og afhaengigheder
* [Afhaengighed]
* [Afhaengighed]

## Trin 2 af 3: Forsinkelser, dobbeltarbejde og hotspots
### Forsinkelser og dobbeltarbejde
* [Problem]
* [Problem]

### Huller i ejerskab
* [Hul]
* [Hul]

### Hotspots med omkostning, indsats eller tabt vaerdi
* [Hotspot]
* [Hotspot]

## Trin 3 af 3: Implikationer og carry-forward-logik
### Vigtigste implikationer fra blueprintet
* [Implikation]
* [Implikation]

### Aabne huller der skal foeres videre til fremtidig model
* [Hul]
* [Hul]
```

## Skabelon til Aktivitet 3.1

```md
# Package C - Aktivitet 3.1 input

## Sekvensguide
Brug denne aktivitet som 4 korte trin:
1. Fremtidig retning
2. Aendringsmodel
3. Validering og forfining
4. Valgfrit prototypeudsnit

## Viderefoert kontekst fra Aktivitet 2.2
### Implikationer fra den nuvaerende service der skal reageres paa
[Tekst]

### Strategisk spoergsmaal der stadig er i fokus
[Tekst]

## Trin 1 af 4: Fremtidig retning
### Formaal med den fremtidige retning
[Tekst]

### Fremtidig servicemodel
* [Element]
* [Element]

## Trin 2 af 4: Aendringsmodel
### Aendringer paa tvaers af kanaler, teams, systemer og ejerskab
* [Aendring]
* [Aendring]

## Trin 3 af 4: Validering og forfining
### Deltagere i valideringen
* [Deltagertype]
* [Deltagertype]

### Feedback fra validering
* [Signal]
* [Signal]

### Bekymringer om gennemfoerlighed eller afhaengigheder
* [Bekymring]
* [Bekymring]

### Forfininger der er lavet
* [Forfining]
* [Forfining]

### Aabne spoergsmaal til roadmap og business case
* [Spoergsmaal]
* [Spoergsmaal]

## Trin 4 af 4: Valgfrit prototypeudsnit
### Udvalgt hoejrisiko-udsnit af rejsen til valgfri prototypestoette
[Tekst eller ingen]
```

## Skabelon til Aktivitet 4.1

```md
# Package C - Aktivitet 4.1 input

## Sekvensguide
Brug denne aktivitet som 4 korte trin:
1. Strategisk sekventering
2. Afhaengigheder og aendringsimplikationer
3. Vaerdilogik og risiko
4. Valgfri prototypestoette

## Viderefoert kontekst fra Aktivitet 3.1
### Fremtidig servicemodel der aktuelt antages
[Tekst]

### Udvalgt hoejrisiko-udsnit der aktuelt antages
[Tekst eller ingen]

## Trin 1 af 4: Strategisk sekventering
### Strategisk beslutning dette output skal understoette
[Tekst]

### Hvad skal ske nu
* [Handling]
* [Handling]

### Hvad skal ske naeste gang
* [Handling]
* [Handling]

### Hvad skal ske senere
* [Handling]
* [Handling]

## Trin 2 af 4: Afhaengigheder og aendringsimplikationer
### Afhaengigheder og beslutningspunkter
* [Afhaengighed]
* [Afhaengighed]

### Aendringskonsekvenser paa tvaers af driftsmodel, governance eller ejerskab
* [Implikation]
* [Implikation]

## Trin 3 af 4: Vaerdilogik og risiko
### ROI-hypotese eller vaerdilogik
* [Vaerdilogik]
* [Vaerdilogik]

### Risici og antagelser
* [Risiko]
* [Risiko]

## Trin 4 af 4: Valgfri prototypestoette
### Hvis der er behov for prototypestoette, udvalgt hoejrisiko-udsnit af rejsen
[Tekst eller ingen]

### Valgfrie screenshots eller links som visuelle referencer
* [Valgfrit screenshot, link eller note]
* [Valgfrit screenshot, link eller note]

### Valgfri note om visuel alignment til prototypen
[Tekst eller ingen]
```

## Skabelon til endelig leverance

```md
# Endelig leverance for Pakke C

## Ledelsesoplaeg
[Tekst]

## Serviceproblem og vaerdi paa spil
[Tekst]

## Strategiske og investeringsmaessige beslutninger der understoettes
* [Beslutning]
* [Beslutning]

## Opsummering af blueprint over den nuvaerende service
### Vigtigste forsinkelser og dobbeltarbejde
* [Problem]
* [Problem]

### Huller i ejerskab og steder hvor vaerdi laekker
* [Hul]
* [Hul]

## Testet fremtidig servicemodel
* [Element]
* [Element]

## Signaler fra valideringen
* [Signal]
* [Signal]

## Faseopdelt roadmap
### Nu
* [Handling]
* [Handling]

### Naeste
* [Handling]
* [Handling]

### Senere
* [Handling]
* [Handling]

## Aendringsimplikationer
* [Implikation]
* [Implikation]

## ROI-hypotese og vaerdilogik
* [Vaerdilogik]
* [Vaerdilogik]

## Risici og antagelser
* [Risiko]
* [Risiko]

## Valgfri prototypestoette til hoejrisiko-udsnit af rejsen
### Udvalgt udsnit
[Tekst eller ingen]

### Prototyperegistrering
Se `package_c_prototype_record.md`.

### Prototype prompt pack
Se `package_c_prototype_prompt_pack.md`.

## Umiddelbare naeste skridt
* [Handling]
* [Handling]

## Godkendelsesstatus
[Draft / Ready for review / Approved]
```

## Skabelon til prototype prompt pack

```md
# Prototype prompt pack for Pakke C

## Kanonisk prototypebrief
[Tekst eller ingen]

## Fresh generation prompt - Figma Make
[Tekst eller ingen]

## Refinement prompt - Figma Make
[Tekst eller ingen]

## Fresh generation prompt - Google Stitch
[Tekst eller ingen]

## Refinement prompt - Google Stitch
[Tekst eller ingen]

## Promptnoter
* [Note]
* [Note]

## Godkendelsesstatus
[Draft / Ready for review / Approved]
```

## Skabelon til prototyperegistrering

```md
# Prototyperegistrering for Pakke C

## Vaerktoej brugt
[Figma Make / Google Stitch / other / none]

## Udvalgt hoejrisiko-udsnit
[Tekst eller ingen]

## Prototype-link eller arbejdsfil
[Tekst eller ingen]

## Godkendte screenshots eller referencer
* [Screenshot, URL eller note]
* [Screenshot, URL eller note]

## Iterationshistorik
1. [Fresh generation eller revision]
2. [Refinement-runde]

## Reviewresultat
[Tekst]

## Resterende polish-noter
* [Note]
* [Note]

## Godkendelsesstatus
[Draft / Ready for review / Approved]
```
