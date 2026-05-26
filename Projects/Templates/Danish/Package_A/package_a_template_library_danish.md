# Skabelonbibliotek for Pakke A

Brug denne fil som den genanvendelige skabelonkilde til live-projekter i Pakke A.

## Foreslaaede filer i et live-projekt

* `project_index.md`
* `01-inputs/package_a_stage_0_intake_input.md`
* `01-inputs/package_a_activity_1_1_input.md`
* `01-inputs/package_a_activity_1_2_input.md`
* `01-inputs/package_a_activity_1_3_input.md`
* `01-inputs/package_a_activity_2_1_input.md`
* `01-inputs/package_a_activity_3_1_input.md`
* `02-working/package_a_stage_0_intake_summary.md`
* `02-working/package_a_activity_1_1_decision_frame.md`
* `02-working/package_a_activity_1_2_evidence_synthesis.md`
* `02-working/package_a_activity_1_3_breakdown_map.md`
* `02-working/package_a_activity_2_1_direction_review.md`
* `02-working/package_a_activity_3_1_recommendation_draft.md`
* `03-reviews/package_a_stage_0_intake_check.md`
* `03-reviews/package_a_activity_1_1_review.md`
* `03-reviews/package_a_activity_1_2_review.md`
* `03-reviews/package_a_activity_1_3_review.md`
* `03-reviews/package_a_activity_2_1_review.md`
* `03-reviews/package_a_activity_3_1_review.md`
* `04-final/package_a_final_deliverable.md`
* `04-final/package_a_prototype_prompt_pack.md`
* `04-final/package_a_prototype_record.md`

Bootstrap genererer filerne i `02-working/` og `03-reviews/` automatisk ud fra workflow-metadataen for Pakke A, naar et live-projekt startes.

## Designnoter til skabelonerne

Pakke A skal foeles let i brug.

Det betyder:

* Hver seed'et inputfil er struktureret som en kort trinvis sekvens og ikke som et langt spoergeskema.
* Tidligere valideret kontekst skal foeres videre som standard.
* Kun reelt nyt eller aendret input skal indfanges i hver aktivitet.
* Prototypeprompts og prototypegodkendelse skal ligge i deres egne filer, saa den vigtigste endelige leverance bliver laesbar.

## Skabelon til Trin 0-intake

```md
# Package A - Trin 0 intake input

## Sekvensguide
Brug denne intake som 4 korte trin:
1. Kunde og problem
2. Beslutning og hvorfor nu
3. Evidens og interessenter
4. Graenser

## Trin 1 af 4: Kunde og problem
### Kunde / kontekst
[Tekst]

### Problemomraade i scope
[Tekst]

## Trin 2 af 4: Beslutning og urgency
### Beslutning der skal understoettes
[Tekst]

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

### Elementer uden for scope
* [Element]
* [Element]
```

## Skabelon til Aktivitet 1.1

```md
# Package A - Aktivitet 1.1 input

## Sekvensguide
Brug denne aktivitet som 4 korte trin:
1. Workshopopsaetning og forretningsspoergsmaal
2. Brugere og scope
3. Maal, baseline og begraensninger
4. Spaendinger og aabne sprintspoergsmaal

## Viderefoert kontekst fra Trin 0
### Nuværende problemomraade
[Tekst]

### Nuværende beslutning der skal understoettes
[Tekst]

### Nuværende hvorfor-nu-kontekst
[Tekst]

### Interessentbaseline viderefoert fra Trin 0
* [Interessent eller team]
* [Interessent eller team]

### Noter kun aendringer, hvis workshoppen aendrede den viderefoerte kontekst
[Tekst]

## Trin 1 af 4: Workshopopsaetning og forretningsspoergsmaal
### Workshopdeltagere bekraeftet fra den viderefoerte interessentbaseline
* [Rolle]
* [Rolle]

### Yderligere workshopspecifikke deltagere
* [Rolle]
* [Rolle]

### Forretningsspoergsmaal der blev droeftet
[Tekst]

## Trin 2 af 4: Brugere og scope
### Maalbrugere
* [Gruppe]
* [Gruppe]

### I scope
* [Element]
* [Element]

### Ude af scope
* [Element]
* [Element]

## Trin 3 af 4: Maal og begraensninger
### Succeskriterier der blev droeftet
* [Maal]
* [Maal]

### Kendte baselinemetrics
* [Metric]
* [Metric]

### Begraensninger rejst
* [Begraensning]
* [Begraensning]

## Trin 4 af 4: Spaendinger og aabne sprintspoergsmaal
### Antagelser eller uenigheder
* [Punkt]
* [Punkt]

### Aabne sprintspoergsmaal
* [Spoergsmaal]
* [Spoergsmaal]
```

## Skabelon til Aktivitet 1.2

```md
# Package A - Aktivitet 1.2 input

## Sekvensguide
Brug denne aktivitet som 3 korte trin:
1. Evidenskilder og daekning
2. Staerkeste signaler og understoettede fund
3. Resterende usikkerhed og naeste valideringsspoergsmaal

## Viderefoert kontekst fra Aktivitet 1.1
### Valgt problemomraade i scope
[Tekst]

### Beslutning denne evidens skal understoette
[Tekst]

### Noter kun aendringer, hvis evidensreviewet aendrede noget af dette
[Tekst]

## Trin 1 af 3: Evidenskilder og daekning
### Kilder gennemgaaet
* [Kilde]
* [Kilde]

### Segmentering tilgaengelig
* [Segment eller ikke tilgaengeligt]
* [Segment eller ikke tilgaengeligt]

## Trin 2 af 3: Staerkeste signaler og understoettede fund
### Staerkeste signaler
1. [Signal]
2. [Signal]
3. [Signal]

### Velunderstoettet
* [Punkt]
* [Punkt]

### Retningsgivende men endnu ikke bevist
* [Punkt]
* [Punkt]

## Trin 3 af 3: Resterende usikkerhed
### Stadig antagelse
* [Punkt]
* [Punkt]

### Konflikter eller huller
* [Hul eller konflikt]
* [Hul eller konflikt]

### Spoergsmaal der skal valideres naeste gang
* [Spoergsmaal]
* [Spoergsmaal]
```

## Skabelon til Aktivitet 1.3

```md
# Package A - Aktivitet 1.3 input

## Sekvensguide
Brug denne aktivitet som 3 korte trin:
1. Trin i scope, aktoerer og nuvaerende handlinger
2. Kontaktpunkter, systemer og interne implikationer
3. Friktion, stoerste brud og valideringshuller

## Viderefoert kontekst fra Aktivitet 1.2
### Beslutning dette kort skal understoette
[Tekst]

### Evidensimplikation der skal holdes i mente
[Tekst]

## Trin 1 af 3: Trin i scope og nuvaerende flow
### Valgt trin i scope
[Tekst]

### Aktoerer
* [Aktoer]
* [Aktoer]

### Nuværende handlinger
* [Handling]
* [Handling]

## Trin 2 af 3: Kontaktpunkter og afhaengigheder
### Kontaktpunkter og kanaler
* [Kontaktpunkt]
* [Kontaktpunkt]

### Systemer og afhaengigheder
* [Afhaengighed]
* [Afhaengighed]

### Interne implikationer
* [Punkt]
* [Punkt]

## Trin 3 af 3: Brudmoenster
### Friktionspunkter
* [Punkt]
* [Punkt]

### Stoerste brud
1. [Brud]
2. [Brud]
3. [Brud]

### Hvorfor disse betyder noget
* [Implikation]
* [Implikation]

### Valideringshuller
* [Hul]
* [Hul]
```

## Skabelon til Aktivitet 2.1

```md
# Package A - Aktivitet 2.1 input

## Sekvensguide
Brug denne aktivitet som 4 korte trin:
1. Beslutning og muligheder
2. Sammenligningskriterier
3. Noter om mulighederne og tradeoffs
4. Foretrukken retning og aabne checks

## Viderefoert kontekst fra Aktivitet 1.3
### Problemomraade i scope
[Tekst]

### Brudmoenster der skal reageres paa
[Tekst]

## Trin 1 af 4: Beslutning og muligheder
### Beslutning denne gennemgang skal understoette
[Tekst]

### Muligheder sammenlignet
* Mulighed A: [Tekst]
* Mulighed B: [Tekst]

## Trin 2 af 4: Sammenligningskriterier
### Brugerkriterier
* [Kriterium]
* [Kriterium]

### Forretningskriterier
* [Kriterium]
* [Kriterium]

### Leverancekriterier
* [Kriterium]
* [Kriterium]

## Trin 3 af 4: Noter om mulighederne og tradeoffs
### Noter om mulighed A
* [Punkt]
* [Punkt]

### Noter om mulighed B
* [Punkt]
* [Punkt]

### Tradeoffs droeftet
* [Tradeoff]
* [Tradeoff]

## Trin 4 af 4: Foretrukken retning og aabne checks
### Foretrukken retning hvis en opstod
[Tekst]

### Risici og afhaengigheder
* [Risiko]
* [Risiko]

### Aabne checks
* [Check]
* [Check]
```

## Skabelon til Aktivitet 3.1

```md
# Package A - Aktivitet 3.1 input

## Sekvensguide
Brug denne aktivitet som 4 korte trin:
1. Laas anbefalingen og sponsor-noter
2. Scope og maaling
3. Risici, validering og naeste skridt
4. Prototypebrief

## Viderefoert kontekst fra Aktivitet 2.1
### Foretrukken retning der aktuelt antages
[Tekst]

### Problemfokus der aktuelt antages
[Tekst]

### Noter kun aendringer, hvis sponsorene aendrede den viderefoerte retning eller problemfokus
[Tekst]

## Trin 1 af 4: Laas anbefalingen og sponsor-noter
### Beslutning der skal understoettes
[Tekst]

### Hvorfor denne retning er staerkere
* [Begrundelse]
* [Begrundelse]

### Endelige sponsor-kommentarer eller scope-noter
* [Note]
* [Note]

## Trin 2 af 4: Scope og maaling
### Maalbrugere
* [Gruppe]
* [Gruppe]

### Succeskriterier
* [Maal]
* [Maal]

### Byg nu
* [Element]
* [Element]

### Udskyd
* [Element]
* [Element]

## Trin 3 af 4: Risici, validering og naeste skridt
### Valider naeste
* [Spoergsmaal]
* [Spoergsmaal]

### Risici og afhaengigheder
* [Risiko]
* [Risiko]

### Umiddelbare naeste skridt
* [Handling]
* [Handling]

## Trin 4 af 4: Prototypebrief
### Prototype-scope
* [Skaerm eller moment]
* [Skaerm eller moment]

### Prototypeinteraktioner der skal vises
* [Interaktion]
* [Interaktion]

### Prototypebegraensninger
* [Begraensning]
* [Begraensning]

### Valgfrie visuelle referencescreenshots eller links
* [Valgfrit screenshot, link eller note]
* [Valgfrit screenshot, link eller note]

### Foretrukket vaerktoej
[Figma Make / Google Stitch / either]
```

## Skabelon til endelig leverance

```md
# Package A final deliverable

## Executive summary
[Tekst]

## Beslutning der skal understoettes
[Tekst]

## Anbefalet retning
[Tekst]

## Hvorfor denne retning
* [Begrundelse]
* [Begrundelse]

## Anbefalet scope
* [Byg nu]
* [Byg nu]

## Hvad der ikke skal bygges endnu
* [Udskyd]
* [Udskyd]

## Maalbrugere
* [Gruppe]
* [Gruppe]

## Succeskriterier og maalelogik
* [Maal]
* [Maal]

## Opsummering af det endelige kort over rejsetrinnet
### Trin i scope
[Tekst]

### Stoerste brud
1. [Brud]
2. [Brud]
3. [Brud]

### Hvorfor de betyder noget
* [Implikation]
* [Implikation]

## Klikbar prototype
### Prototypeformaal
[Tekst]

### Prototype-scope opsummeret
* [Skaerm eller moment]
* [Skaerm eller moment]

### Prototyperegistrering
Se `package_a_prototype_record.md`.

### Prototype prompt pack
Se `package_a_prototype_prompt_pack.md`.

## Risici og afhaengigheder
* [Risiko]
* [Risiko]

## Valider naeste
* [Spoergsmaal]
* [Spoergsmaal]

## Umiddelbare naeste skridt
* [Handling]
* [Handling]

## Godkendelsesstatus
[Draft / Ready for review / Approved]
```

## Skabelon til prototype prompt pack

```md
# Package A prototype prompt pack

## Kanonisk prototypebrief
[Tekst]

## Fresh generation prompt - Figma Make
[Tekst]

## Refinement prompt - Figma Make
[Tekst]

## Fresh generation prompt - Google Stitch
[Tekst]

## Refinement prompt - Google Stitch
[Tekst]

## Promptnoter
* [Note]
* [Note]

## Godkendelsesstatus
[Draft / Ready for review / Approved]
```

## Skabelon til prototyperegistrering

```md
# Package A prototype record

## Vaerktoej brugt
[Figma Make / Google Stitch / other]

## Prototype-link eller arbejdsfil
[Tekst]

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
