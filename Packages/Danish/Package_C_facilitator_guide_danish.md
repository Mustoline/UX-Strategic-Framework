# Facilitatorguide til Pakke C

## Formål

Brug denne guide til at forberede og gennemføre de virkelige Pakke C-aktiviteter med kunden.

Målet er at sikre, at du indsamler det rigtige materiale i den rigtige rækkefølge, så AI'en kan behandle hver aktivitet rent og omsætte den til et valideret output, før næste trin begynder.

Brug denne guide sammen med:

* [Package_C_core_activities_danish.md](Package_C_core_activities_danish.md) til pakkeopsummeringen
* [Package_C_ai_process_danish.md](Package_C_ai_process_danish.md) til AI-handoff og den trinvis styrede workflowlogik
* [prototype_prompt_pack_template_danish.md](prototype_prompt_pack_template_danish.md), hvis ét udvalgt højrisiko-udsnit af rejsen har brug for en understøttende prototype

## Delte forberedelsesaktiver til live-leverance

Brug disse delte filer, naar du skal forberede selve den virkelige session:

* [../../Projects/Templates/Danish/Shared/workshop_invite_template_danish.md](../../Projects/Templates/Danish/Shared/workshop_invite_template_danish.md)
* [../../Projects/Templates/Danish/Shared/interview_invite_and_consent_template_danish.md](../../Projects/Templates/Danish/Shared/interview_invite_and_consent_template_danish.md)
* [../../Projects/Templates/Danish/Shared/session_brief_template_danish.md](../../Projects/Templates/Danish/Shared/session_brief_template_danish.md)

## Sådan skal workflowet køre

1. Brug denne guide til at forberede og gennemføre én Pakke C-aktivitet med kunden.
2. Fang de nødvendige noter i den seed'ede projektinputfil for aktiviteten.
3. Bring dette input ind i AI-processen.
4. Review det bearbejdede output med kunden og bekræft eventuelle ændringer.
5. Gå først derefter videre til næste aktivitet.

Gå ikke videre, hvis det forrige output endnu ikke er accepteret. Værdien af Pakke C afhænger af, at hvert trin bygger på valideret input.

## Lean capture-regel

Pakke C skal foeles struktureret, men ikke bureaukratisk.

Brug disse regler under faciliteringen:

* Start hver aktivitet fra det validerede output af det forrige trin
* Behandl bekraeftet service-scope, strategisk beslutningsramme, interessentbillede og kendte begraensninger som viderefoert standardkontekst, medmindre kunden eksplicit aendrer den
* Fang kun det reelt nye input, der er noedvendigt for den aktuelle aktivitet
* Hvis et punkt kun kraever bekraeftelse, saa bekraeft det hurtigt i stedet for at dokumentere det fuldt igen
* Hold den virkelige aktivitet fokuseret paa den naeste strategiske beslutning og ikke paa at genopbygge tidligere noter

Naar aktiviteten senere simuleres i chatten, skal AI'en spejle samme logik ved at bruge en kort step-baseret sekvens og kun bede om det minimum af nyt input, der er noedvendigt.

Brug den seed'ede projektinputfil i `01-inputs/` og [../../Projects/Templates/Danish/Package_C/package_c_template_library_danish.md](../../Projects/Templates/Danish/Package_C/package_c_template_library_danish.md) som den gaeldende reference for den konkrete step-baserede handoffstruktur. De korte lean capture-strukturer laengere nede i guiden opsummerer kun sekvensen for hver aktivitet og maa ikke udvides tilbage til fulde dublerede skabeloner.

## AI-handoff til næste live-aktivitet

Når det forrige trin er valideret, og næste skridt er en virkelig aktivitet:

* Skal AI'en eksplicit sige, at næste skridt nu er en live-aktivitet
* Skal AI'en linke til den seed'ede projektinputfil for aktiviteten
* Skal AI'en linke til den relevante del af denne facilitatorguide og eventuelle relevante skabeloner, spørgeguides eller værktøjsfiler
* Skal AI'en opsummere formålet, den estimerede tid og hvem der bør deltage, eller hvilket materiale der skal indsamles
* Skal AI'en vente på de færdige aktivitetsnoter, før syntesen genoptages, medmindre brugeren eksplicit beder om at simulere eller forberede aktiviteten i chatten
* Skal AI'en bruge den kanoniske handoff-struktur i [../../Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md](../../Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md)

## Endelige leverancer, pakken skal munde ud i

Ved afslutningen af Pakke C skal du kunne levere:

* Et ledelsesoplæg
* Et blueprint over den nuværende service
* En testet fremtidig servicemodel
* Et faseopdelt roadmap på tværs af teams og systemer
* En opsummering af ændringsbehov og business case

Hvor den fremtidige servicemodel har brug for et mere håndgribeligt valideringsartefakt, kan den afsluttende syntese også generere:

* En prototype prompt pack-fil til ét udvalgt højrisiko-udsnit af rejsen, med:
  * Et kanonisk prototypebrief
  * Fresh-generation prompts
  * Refinement prompts
* En separat prototype record-fil til det udvalgte udsnit, som fanger godkendte screenshots, prototypelink, iterationsnoter og godkendelsesstatus

Denne prototype prompt pack er valgfri støtte til den testede servicemodel. Den bør kun bruges til ét udvalgt højrisiko-udsnit af rejsen og må ikke erstatte Pakke C's kerneleverancer.

## Projektopsætning før pakken starter

Før Aktivitet 1.1 skal projektets arbejdsmappe oprettes for forløbet.

### Tjekliste til projektopsætning

* Bed om projektnavnet og normalisér det til et mappenavn, der er sikkert at bruge
* Opret `../../Projects/<Project-Name>/`
* Opret `../../Projects/<Project-Name>/00-project-setup/`
* Opret `../../Projects/<Project-Name>/01-inputs/`
* Opret `../../Projects/<Project-Name>/02-working/`
* Opret `../../Projects/<Project-Name>/03-reviews/`
* Opret `../../Projects/<Project-Name>/04-final/`
* Opret `../../Projects/<Project-Name>/project_index.md` som projektets kontrolcenter
* Opret `../../Projects/<Project-Name>/00-project-setup/project_setup.md`
* Seed de relevante filer til Trin 0 og aktivitetsinput i `01-inputs/`
* Seed de relevante aktivitetsoutputfiler i `02-working/`
* Seed de relevante reviewfiler i `03-reviews/`
* Seed pakkens endelige leverancefil i `04-final/`
* Seed den valgfrie prototype prompt-pack-fil i `04-final/`
* Seed den valgfrie prototype record-fil i `04-final/`
* Registrér det oprindelige projektnavn, mappenavn, pakketype, arbejdssprog, oprettelsesdato og nuværende status i opsætningsnoten
* Hvis mappen allerede findes, så stop og bekræft, om den skal genbruges, før der gemmes filer
* Gem rå kundeinput i `01-inputs/`, igangværende syntese i `02-working/`, reviewversioner i `03-reviews/` og godkendte output i `04-final/`

## Før pakken starter

### Minimumstjekliste for intake

Indsaml dette før Aktivitet 1.1:

* Servicen, propositionen eller det tværgående initiativ, der er i scope
* De strategiske og investeringsmæssige beslutninger pakken skal understøtte
* Hvorfor dette er vigtigt nu i forretnings- og serviceterminer
* Hvilken evidens der allerede findes, og hvem der ejer den
* De ledelsesmæssige, serviceansvarlige, driftsnære og frontlinjenære deltagere, der skal involveres
* De kendte begrænsninger, antagelser og områder uden for scope

### Tjekliste til forberedelse før pakken

Før første aktivitet gennemføres:

* Bekræft sponsor og den navngivne ejer, som kan validere output
* Bekræft hvem der skal deltage i lederinterviews, økosystemkortlægning, feltarbejde, validering og roadmap-arbejde
* Bed tidligt om materiale om service, support, drift og analytics
* Bekræft hvilke tilladelser eller fortrolighedsgrænser der påvirker feltarbejdet
* Book live-sessioner og reviewpunkter i den rigtige rækkefølge
* Fortæl kunden, at hver aktivitet slutter med et reviewpunkt, før næste trin starter

## Aktivitet 1.1: Interviews med ledere og serviceansvarlige

### Formål

At afklare business casen, de strategiske prioriteringer, presset på servicen og de investeringsspørgsmål, der skal forme redesignarbejdet.

### Estimeret aktivitetstid

1-2 dage fordelt på 5-7 interviews på 45-60 minutter hver samt den første syntese

### Hvem bør interviewes

* Senior sponsorer
* Serviceansvarlige
* Ledere med ansvar for drift, kanaler eller centrale systemer

### Forberedelse før interviews

* Bekræft hvilke beslutninger eller investeringer pakken skal informere
* Forbered en interviewguide om pres på servicen, forretningsmæssige konsekvenser og investeringsspørgsmål
* Indsaml eventuelt strategi-, driftsmodel- eller performancemateriale, der allerede findes

### Hvad du skal fange

* Strategiske prioriteringer
* Pres på servicen og sammenbrudspunkter
* Forretningsmæssige og driftsmæssige konsekvenser
* Risici og spændinger
* Investeringsspørgsmål
* Områder med enighed og konflikt mellem interessenter

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_c_activity_1_1_input.md`-fil til denne aktivitet.

Fang kun:

* den strategiske indramning der kom frem i interviewene
* de pres, konsekvenser og investeringsspørgsmål der betyder noget næste gang

Kort sekvens:

1. Interviews og strategisk indramning
2. Pres på servicen og konsekvenser
3. Spændinger og investeringsspørgsmål

### Valideringscheckpoint

Kunden bør bekræfte:

* At den strategiske indramning afspejler det reelle serviceproblem
* At de vigtigste investeringsspørgsmål er synlige
* At resten af pakken er fokuseret på de rigtige strategiske spændinger

## Aktivitet 1.2: Økosystemworkshop og afgrænsning af servicen

### Formål

At aftale service-scope på tværs af afdelinger, kontaktpunkter, systemer og driftsaktører.

### Estimeret aktivitetstid

En halv dag

### Hvem bør deltage

* Senior sponsorer
* Serviceansvarlige
* Driftsnære interessenter
* Personer der forstår kanaler, systemer, afhængigheder og overleveringer

### Forslag til workshopflow

* Strategisk opsamling og mål: 20 minutter
* Afdelinger, kontaktpunkter, systemer og aktører: 60 minutter
* Kritiske servicemomenter og scopegrænse: 60 minutter
* Opsamling på service-scope og fokus for feltarbejde: 30 minutter

### Hvad du skal fange

* Service-scope
* Afdelinger og driftsaktører
* Kanaler og kontaktpunkter
* Systemer og afhængigheder
* Kritiske servicemomenter
* Områder i scope og ude af scope

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_c_activity_1_2_input.md`-fil til denne aktivitet.

Fang kun:

* den servicegrænse gruppen faktisk blev enige om
* de aktører, afhængigheder og kritiske momenter der skal styre feltarbejdet

Kort sekvens:

1. Strategisk spørgsmål og service-scope
2. Afdelinger, kanaler og systemer
3. Kritiske momenter og fokus for feltarbejdet

### Valideringscheckpoint

Kunden bør bekræfte:

* At servicegrænsen er tydelig nok til at guide feltarbejdet
* At de kritiske servicemomenter er de rigtige at undersøge
* At pakken ikke har udvidet sig ud over det aftalte service-scope

## Aktivitet 2.1: Kontekstuel feltundersøgelse og gennemgang af data

### Formål

At undersøge, hvordan servicen fungerer i praksis, og synliggøre omveje, forsinkelser, skjult arbejde og uklarheder i ejerskab.

### Estimeret aktivitetstid

3-5 dage fordelt på 5-8 sessioner på 60-90 minutter hver samt gennemgang af evidens og første syntese

### Evidens og adgang der skal efterspørges

* Driftsdata og signaler om serviceperformance
* Supportmønstre og sagstyper
* Analytics eller data om servicevolumen
* Adgang til relevante brugere, kunder, frontlinjeteams eller interne roller
* Mulighed for observation eller shadowing, hvor det er muligt

Brug [../../Projects/Templates/Danish/Shared/evidence_request_template_danish.md](../../Projects/Templates/Danish/Shared/evidence_request_template_danish.md), hvis du vil efterspoerge denne evidens eller adgang fra kundeteamet paa en mere struktureret maade.

### Sådan gennemføres dette trin

* Fokuser på, hvad der faktisk sker i praksis, og ikke kun på det procesejerne siger burde ske
* Fang bevægelse på tværs af kanaler, forsinkelser, omarbejde, eskaleringer og skjult understøttende arbejde
* Skeln mellem direkte observation og fortolkning

### Hvad du skal fange

* Observerede servicemomenter
* Omveje
* Forsinkelser og skjult arbejde
* Huller i ejerskab
* Brud på tværs af teams, systemer og kanaler
* Spørgsmål til blueprint-arbejdet

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_c_activity_2_1_input.md`-fil til denne aktivitet.

Fang kun:

* den driftsnære evidens og de observationer der faktisk flytter billedet
* de brud og blueprint-spørgsmål der skal videreføres

Kort sekvens:

1. Dækning af observationer
2. Driftsfriktion og skjult arbejde
3. Brud og spørgsmål til blueprinting

### Valideringscheckpoint

Kunden bør bekræfte:

* At feltarbejdet afspejler, hvordan servicen faktisk opfører sig
* At de vigtigste mønstre i brud er synlige
* At blueprint-trinnet har nok evidens til at gå videre

## Aktivitet 2.2: Blueprint over den nuværende service

### Formål

At skabe et blueprint over den nuværende service, som synliggør forsinkelser, dobbeltarbejde, omkostninger og huller i ejerskab på tværs af frontstage og backstage.

### Estimeret aktivitetstid

1-2 dages blueprinting og syntese samt et reviewcheckpoint med interessenter på 60-90 minutter

### Hvad du skal fange

* Frontstage-interaktioner
* Backstage-processer
* Systemer og afhængigheder
* Forsinkelser og dobbeltarbejde
* Huller i ejerskab
* Hotspots med omkostninger, indsats eller tabt værdi

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_c_activity_2_2_input.md`-fil til denne aktivitet.

Fang kun:

* blueprint-strukturen der skal være synlig
* hotspots og implikationer der er vigtige for arbejdet med fremtidig model

Kort sekvens:

1. Struktur for blueprintet
2. Forsinkelser, dobbeltarbejde og hotspots
3. Implikationer og carry-forward-logik

### Valideringscheckpoint

Kunden bør bekræfte:

* At blueprintet afspejler den nuværende servicevirkelighed
* At de vigtigste hotspots er de rigtige at arbejde med i target state
* At implikationerne for driftsmodellen er tydelige nok til næste trin

## Aktivitet 3.1: Workshop om fremtidig servicemodel og validering af koncept

### Formål

At definere en fremtidig servicemodel og validere, om den holder hos de mennesker, der skal leve med den.

### Estimeret aktivitetstid

En halv dags workshop samt 1-2 dage til valideringssessioner, syntese og forfining

### Hvem bør deltage

* Tværgående interessenter, der former den fremtidige servicemodel
* Valideringsdeltagere, der kan synliggøre reel friktion, risiko for lav adoption eller gennemførlighedsproblemer

### Forberedelse før workshoppen

* Medbring det validerede blueprint og hotspots fra den nuværende situation
* Bekræft hvilke brud den fremtidige model først skal adressere
* Bekræft hvem der skal deltage i valideringen

### Hvad du skal fange

* Logik i den fremtidige servicemodel
* Vigtigste ændringer på tværs af kanaler, teams, systemer og ejerskab
* Feedback fra valideringen
* Signal om gennemførlighed
* Forfininger foretaget efter validering
* Åbne spørgsmål til roadmap og business case

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_c_activity_3_1_input.md`-fil til denne aktivitet.

Fang kun:

* den fremtidige retning der overlevede valideringen
* forfiningerne og eventuelt valgt højrisiko-udsnit der skal videreføres

Kort sekvens:

1. Fremtidig retning
2. Ændringsmodel
3. Validering og forfining
4. Valgfrit prototypeudsnit

### Valideringscheckpoint

Kunden bør bekræfte:

* At den fremtidige model adresserer de rigtige problemer fra den nuværende situation
* At modellen er testet godt nok til at understøtte roadmap-arbejdet
* At et højrisiko-udsnit af rejsen er tydeligt udvalgt og afgrænset, hvis der er behov for en prototype

## Aktivitet 4.1: Session om roadmap og business case

### Formål

At omsætte den validerede fremtidige servicemodel til et faseopdelt roadmap, en opsummering af ændringskonsekvenser og en troværdig ROI-hypotese.

### Estimeret aktivitetstid

En halv dags session samt 4-6 timers syntese og paketering

### Forberedelse før sessionen

* Medbring den validerede fremtidige servicemodel
* Bekræft hvilken strategisk eller investeringsmæssig beslutning dette trin skal understøtte
* Bekræft hvilke afhængigheder, ikke-forhandlingsbare krav og værdiområder der betyder mest

### Hvad du skal fange

* Hvad der skal ske nu, næste gang og senere
* Afhængigheder og beslutningspunkter
* Ændringer i driftsmodel, governance og ejerskab
* ROI-hypotese eller værdilogik
* Risici og antagelser der stadig har betydning

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_c_activity_4_1_input.md`-fil til denne aktivitet.

Fang kun:

* den sekventering, de ændringsimplikationer og den værdilogik ledelsen har brug for
* valgfri prototypedetaljer kun hvis ét udvalgt højrisiko-udsnit stadig kræver dem

Kort sekvens:

1. Strategisk sekventering
2. Afhængigheder og ændringsimplikationer
3. Værdilogik og risiko
4. Valgfri prototypestøtte

### Valideringscheckpoint

Kunden bør bekræfte:

* At roadmappet er praktisk nok til at guide de næste skridt
* At ændringskonsekvenserne er tydelige nok til ledelsesdialogen
* At ROI-hypotesen er troværdig nok på dette trin

### Valgfrit trin til produktion af prototype

Brug kun dette, hvis den validerede fremtidige servicemodel har brug for et mere håndgribeligt valideringsartefakt for ét udvalgt højrisiko-udsnit af rejsen.

Efter at AI'en har produceret servicemodelpakken og den valgfrie prototype prompt pack:

1. Brug det kanoniske brief og den værktøjsspecifikke prompt i det valgte designværktøj.
2. Generér kun prototypen for det udvalgte højrisiko-udsnit af rejsen.
3. Gennemgå udkastet op mod den validerede fremtidige servicemodel og prototype-reviewtjeklisten i [prototype_prompt_pack_template_danish.md](prototype_prompt_pack_template_danish.md).
4. Hvis der blev delt screenshots eller links fra kundens nuværende løsning, så tjek at udkastet ligger tæt på den eksisterende visuelle stil, medmindre briefet eksplicit beder om forandring.
5. Forfin prompten, hvis prototypen driver væk fra den aftalte serviceretning.

## Praktiske regler for facilitering

* Hold pakken knyttet til et reelt tværgående serviceproblem
* Bevar de strategiske og driftsmæssige spændinger i stedet for at glatte dem ud
* Hold arbejdet med nuværende og fremtidig situation forankret i evidens
* Lad ikke den valgfrie prototypestøtte tage over for arbejdet med servicemodel og roadmap
* Gå kun videre, når det forrige output er reviewet og accepteret
