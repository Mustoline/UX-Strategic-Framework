# Skabelonbibliotek for Pakke B

Brug denne fil som den genanvendelige skabelonkilde til live-projekter i Pakke B.

## Foreslaaede filer i et live-projekt

* `project_index.md`
* `01-inputs/package_b_stage_0_intake_input.md`
* `01-inputs/package_b_activity_1_1_input.md`
* `01-inputs/package_b_activity_1_2_input.md`
* `01-inputs/package_b_activity_2_1_input.md`
* `01-inputs/package_b_activity_3_1_input.md`
* `01-inputs/package_b_activity_4_1_input.md`
* `02-working/package_b_stage_0_intake_summary.md`
* `02-working/package_b_activity_1_1_scope_summary.md`
* `02-working/package_b_activity_1_2_insight_summary.md`
* `02-working/package_b_activity_2_1_current_state_journey_summary.md`
* `02-working/package_b_activity_3_1_future_state_concept_summary.md`
* `02-working/package_b_activity_4_1_prioritization_and_prototype_summary.md`
* `03-reviews/package_b_stage_0_intake_check.md`
* `03-reviews/package_b_activity_1_1_review.md`
* `03-reviews/package_b_activity_1_2_review.md`
* `03-reviews/package_b_activity_2_1_review.md`
* `03-reviews/package_b_activity_3_1_review.md`
* `03-reviews/package_b_activity_4_1_review.md`
* `04-final/package_b_final_deliverable.md`
* `04-final/package_b_prototype_prompt_pack.md`
* `04-final/package_b_prototype_record.md`

Bootstrap genererer filerne i `02-working/` og `03-reviews/` automatisk ud fra workflow-metadataen for Pakke B, naar et live-projekt startes.

## Designnoter til skabelonerne

Pakke B skal foeles guidet og ikke tung.

Det betyder:

* Hver seed'et inputfil er struktureret som en kort trinvis sekvens og ikke som et langt spoergeskema.
* Valideret kontekst skal foeres videre som standard.
* Kun reelt nyt eller aendret input skal indfanges i hver aktivitet.
* Prototypeprompts og prototypegodkendelse skal ligge i deres egne filer, saa den vigtigste endelige leverance bliver laesbar.

## Skabelon til Trin 0-intake

```md
# Package B - Trin 0 intake input

## Sekvensguide
Brug denne intake som 4 korte trin:
1. Kunde og mulighed
2. Beslutninger og hvorfor nu
3. Evidens, brugere og interessenter
4. Graenser

## Trin 1 af 4: Kunde og mulighed
### Kunde / kontekst
[Tekst]

### Mulighedsomraade i scope
[Tekst]

## Trin 2 af 4: Beslutninger og urgency
### De beslutninger pakken skal understoette
* [Beslutning]
* [Beslutning]

### Hvorfor dette er vigtigt nu
[Tekst]

## Trin 3 af 4: Evidens, brugere og interessenter
### Kendt evidens
[Tekst]

### Maalbrugere
* [Gruppe]
* [Gruppe]

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
# Package B - Aktivitet 1.1 input

## Sekvensguide
Brug denne aktivitet som 4 korte trin:
1. Workshopopsaetning og business case
2. Rejse, brugere og scope
3. Maal og discovery-fokus
4. Begraensninger, spaendinger og aabne spoergsmaal

## Viderefoert kontekst fra Trin 0
### Nuværende mulighedsomraade
[Tekst]

### Nuværende beslutninger der skal understoettes
* [Beslutning]
* [Beslutning]

### Nuværende hvorfor-nu-kontekst
[Tekst]

### Interessentbaseline viderefoert fra Trin 0
* [Interessent eller team]
* [Interessent eller team]

### Noter kun aendringer, hvis workshoppen aendrede den viderefoerte kontekst
[Tekst]

## Trin 1 af 4: Workshopopsaetning og business case
### Workshopdeltagere bekraeftet fra den viderefoerte interessentbaseline
* [Rolle]
* [Rolle]

### Yderligere workshopspecifikke deltagere
* [Rolle]
* [Rolle]

### Business case eller hvorfor dette er vigtigt nu
[Tekst]

## Trin 2 af 4: Rejse, brugere og scope
### Rejse i scope
[Tekst]

### Maalbrugere
* [Gruppe]
* [Gruppe]

### I scope
* [Element]
* [Element]

### Ude af scope
* [Element]
* [Element]

## Trin 3 af 4: Maal og discovery-fokus
### Succeskriterier droeftet
* [Maal]
* [Maal]

### Kendte baselinemetrics
* [Metric]
* [Metric]

### Sporgsmaal til afklaringen
* [Spoergsmaal]
* [Spoergsmaal]

## Trin 4 af 4: Begraensninger, spaendinger og aabne spoergsmaal
### Begraensninger, antagelser eller uenigheder
* [Punkt]
* [Punkt]

### Aabne pakkespoergsmaal der skal foeres videre
* [Spoergsmaal]
* [Spoergsmaal]
```

## Skabelon til Aktivitet 1.2

```md
# Package B - Aktivitet 1.2 input

## Sekvensguide
Brug denne aktivitet som 4 korte trin:
1. Evidens og researchdaekning
2. Behov og barrierer
3. Beslutningskriterier og workarounds
4. Konflikter, overraskelser og naeste spoergsmaal

## Viderefoert kontekst fra Aktivitet 1.1
### Rejse i scope
[Tekst]

### Beslutninger denne research skal understoette
* [Beslutning]
* [Beslutning]

### Maalbrugere der aktuelt antages
* [Gruppe]
* [Gruppe]

## Trin 1 af 4: Evidens og researchdaekning
### Evidens gennemgaaet
* [Kilde]
* [Kilde]

### Deltagerprofil
* [Gruppe]
* [Gruppe]

### Antal interviews og format
[Tekst]

## Trin 2 af 4: Behov og barrierer
### Vigtigste brugerbehov
* [Behov]
* [Behov]

### Centrale barrierer
* [Barriere]
* [Barriere]

## Trin 3 af 4: Beslutningskriterier og workarounds
### Beslutningspunkter og kriterier
* [Punkt]
* [Punkt]

### Omveje eller coping-adfaerd
* [Adfaerd]
* [Adfaerd]

## Trin 4 af 4: Konflikter, overraskelser og naeste spoergsmaal
### Konflikter eller overraskelser
* [Punkt]
* [Punkt]

### Sporgsmaal til det videre rejse- og konceptarbejde
* [Spoergsmaal]
* [Spoergsmaal]
```

## Skabelon til Aktivitet 2.1

```md
# Package B - Aktivitet 2.1 input

## Sekvensguide
Brug denne aktivitet som 3 korte trin:
1. Struktur for den nuvaerende rejse
2. Brudmoenster og afhaengigheder
3. Mulighedsomraader og beslutningskriterier

## Viderefoert kontekst fra Aktivitet 1.2
### Rejse i scope
[Tekst]

### Vigtigste brugersignaler der skal holdes i mente
[Tekst]

## Trin 1 af 3: Struktur for den nuvaerende rejse
### Faser i den nuvaerende rejse
* [Fase]
* [Fase]

### Brugerbehov pr. fase
* [Behov]
* [Behov]

## Trin 2 af 3: Brudmoenster og afhaengigheder
### Barrierer og friktion pr. fase
* [Barriere]
* [Barriere]

### Involverede teams, systemer eller overleveringer
* [Afhaengighed]
* [Afhaengighed]

### Vigtigste brud
1. [Brud]
2. [Brud]
3. [Brud]

## Trin 3 af 3: Mulighedsomraader og beslutningskriterier
### Mulighedsomraader
* [Omraade]
* [Omraade]

### Beslutningskriterier for det fremtidige koncept
* [Kriterium]
* [Kriterium]

### Huller i valideringen
* [Hul]
* [Hul]
```

## Skabelon til Aktivitet 3.1

```md
# Package B - Aktivitet 3.1 input

## Sekvensguide
Brug denne aktivitet som 3 korte trin:
1. Fremtidig retning og rejse
2. Principper og serviceaendringer
3. Afhaengigheder og prototypeoejeblikke

## Viderefoert kontekst fra Aktivitet 2.1
### Vigtigste brudmoenster der skal reageres paa
[Tekst]

### Beslutningskriterier der skal holdes i mente
* [Kriterium]
* [Kriterium]

## Trin 1 af 3: Fremtidig retning og rejse
### Formaal med det fremtidige koncept
[Tekst]

### Fremtidig rejse
* [Trin]
* [Trin]

## Trin 2 af 3: Principper og serviceaendringer
### Oplevelsesprincipper
* [Princip]
* [Princip]

### Noedvendige serviceaendringer
#### Proces
* [Aendring]
* [Aendring]

#### Indhold
* [Aendring]
* [Aendring]

#### Ejerskab
* [Aendring]
* [Aendring]

#### Data
* [Aendring]
* [Aendring]

## Trin 3 af 3: Afhaengigheder og prototypeoejeblikke
### Afhaengigheder og begraensninger
* [Afhaengighed]
* [Afhaengighed]

### Aabne spoergsmaal
* [Spoergsmaal]
* [Spoergsmaal]

### Momenter der skal goeres konkrete i prototypen naeste gang
* [Moment]
* [Moment]
```

## Skabelon til Aktivitet 4.1

```md
# Package B - Aktivitet 4.1 input

## Sekvensguide
Brug denne aktivitet som 4 korte trin:
1. Beslutning og prototypeformaal
2. Prototype-scope og interaktioner
3. Prioritering og sekventering
4. Risici, validering og vaerktoejsvalg

## Viderefoert kontekst fra Aktivitet 3.1
### Det fremtidige koncept der aktuelt antages
[Tekst]

### Prototypeoejeblikke der aktuelt antages
* [Moment]
* [Moment]

## Trin 1 af 4: Beslutning og prototypeformaal
### Beslutning dette endelige output skal understoette
[Tekst]

### Formaal med prototypen
[Tekst]

## Trin 2 af 4: Prototype-scope og interaktioner
### Scope for prototype
* [Skaerm eller moment]
* [Skaerm eller moment]
* [Skaerm eller moment]

### Interaktioner prototypen skal vise
* [Interaktion]
* [Interaktion]

### Begraensninger for prototype
* [Begraensning]
* [Begraensning]

## Trin 3 af 4: Prioritering og sekventering
### Prioriteringskriterier
#### Brugervaerdi
* [Kriterium]
* [Kriterium]

#### Forretningsmaessig relevans
* [Kriterium]
* [Kriterium]

#### Implementeringsindsats
* [Kriterium]
* [Kriterium]

### Byg foerst
* [Element]
* [Element]

### Udskyd
* [Element]
* [Element]

## Trin 4 af 4: Risici, validering og vaerktoejsvalg
### Valider naeste gang
* [Spoergsmaal]
* [Spoergsmaal]

### Risici og afhaengigheder
* [Risiko]
* [Risiko]

### Valgfrie screenshots eller links som visuelle referencer
* [Valgfrit screenshot, link eller note]
* [Valgfrit screenshot, link eller note]

### Foretrukket vaerktoej
[Figma Make / Google Stitch / enten]
```

## Skabelon til endelig leverance

```md
# Endelig leverance for Pakke B

## Ledelsesopsummering
[Tekst]

## Beslutninger denne pakke understoetter
* [Beslutning]
* [Beslutning]

## Indsigtsopsamling
### Vigtigste brugerbehov
* [Behov]
* [Behov]

### Centrale barrierer
* [Barriere]
* [Barriere]

### Beslutningskriterier
* [Kriterium]
* [Kriterium]

## Opsummering af den nuvaerende rejse
* [Opsummering af fase]
* [Opsummering af fase]

## Opsummering af den fremtidige rejse
* [Opsummering af trin]
* [Opsummering af trin]

## Noedvendige serviceaendringer
### Proces
* [Aendring]
* [Aendring]

### Indhold
* [Aendring]
* [Aendring]

### Ejerskab
* [Aendring]
* [Aendring]

### Data
* [Aendring]
* [Aendring]

## Klikbar prototype
### Prototypeformaal
[Tekst]

### Prototype-scope
* [Skaerm eller moment]
* [Skaerm eller moment]

### Prototyperegistrering
Se `package_b_prototype_record.md`.

### Prototype prompt pack
Se `package_b_prototype_prompt_pack.md`.

## Byg foerst
* [Element]
* [Element]

## Udskyd
* [Element]
* [Element]

## Valider naeste
* [Spoergsmaal]
* [Spoergsmaal]

## Prioriteret leveranceanbefaling
[Tekst]

## Risici, afhaengigheder og sekventeringslogik
* [Risiko eller afhaengighed]
* [Risiko eller afhaengighed]

## Godkendelsesstatus
[Draft / Ready for review / Approved]
```

## Skabelon til prototype prompt pack

```md
# Prototype prompt pack for Pakke B

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
# Prototyperegistrering for Pakke B

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
