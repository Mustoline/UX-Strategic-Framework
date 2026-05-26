# Facilitatorguide til Pakke B

## Formål

Brug denne guide til at forberede og gennemføre de virkelige Pakke B-aktiviteter med kunden.

Målet er at sikre, at du indsamler det rigtige materiale i den rigtige rækkefølge, så AI'en kan behandle hver aktivitet rent og omsætte den til et valideret output, før næste trin begynder.

Brug denne guide sammen med:

* [Package_B_core_activities_danish.md](Package_B_core_activities_danish.md) til pakkeopsummeringen
* [Package_B_ai_process_danish.md](Package_B_ai_process_danish.md) til AI-handoff og den trinvis styrede workflowlogik
* [prototype_prompt_pack_template_danish.md](prototype_prompt_pack_template_danish.md) til promptstrukturen, der bruges til at generere prototypen

## Delte forberedelsesaktiver til live-leverance

Brug disse delte filer, naar du skal forberede selve den virkelige session:

* [../../Projects/Templates/Danish/Shared/workshop_invite_template_danish.md](../../Projects/Templates/Danish/Shared/workshop_invite_template_danish.md)
* [../../Projects/Templates/Danish/Shared/interview_invite_and_consent_template_danish.md](../../Projects/Templates/Danish/Shared/interview_invite_and_consent_template_danish.md)
* [../../Projects/Templates/Danish/Shared/session_brief_template_danish.md](../../Projects/Templates/Danish/Shared/session_brief_template_danish.md)

## Sådan skal workflowet køre

1. Brug denne guide til at forberede og gennemføre én Pakke B-aktivitet med kunden.
2. Fang de nødvendige noter i den seed'ede projektinputfil for aktiviteten.
3. Bring dette input ind i AI-processen.
4. Review det bearbejdede output med kunden og bekræft eventuelle ændringer.
5. Gå først derefter videre til næste aktivitet.

Gå ikke videre, hvis det forrige output endnu ikke er accepteret. Værdien af Pakke B afhænger af, at hvert trin bygger på valideret input.

## Lean capture-regel

Pakke B maa ikke foeles som et langt gentaget spoergeskema.

Brug disse regler under faciliteringen:

* Start hver aktivitet fra det validerede output af det forrige trin
* Behandl bekraeftet kunde-, mulighedsomraade-, rejse-, maalbruger-, interessent- og begraensningskontekst som viderefoert standardkontekst, medmindre kunden eksplicit aendrer den
* Fang kun det reelt nye input, der er noedvendigt for den aktuelle aktivitet
* Hvis et punkt kun kraever bekraeftelse, saa bekraeft det hurtigt i stedet for at dokumentere det fuldt igen
* Hold den virkelige aktivitet fokuseret paa den naeste beslutning og ikke paa at genopbygge tidligere noter

Naar aktiviteten senere simuleres i chatten, skal AI'en spejle samme logik ved at bruge en kort step-baseret sekvens og kun bede om det minimum af nyt input, der er noedvendigt.

Brug den seed'ede projektinputfil i `01-inputs/` og [../../Projects/Templates/Danish/Package_B/package_b_template_library_danish.md](../../Projects/Templates/Danish/Package_B/package_b_template_library_danish.md) som den gaeldende reference for den konkrete step-baserede handoffstruktur. De korte lean capture-strukturer laengere nede i guiden opsummerer kun sekvensen for hver aktivitet og maa ikke udvides tilbage til fulde dublerede skabeloner.

## AI-handoff til næste live-aktivitet

Når det forrige trin er valideret, og næste skridt er en virkelig aktivitet:

* Skal AI'en eksplicit sige, at næste skridt nu er en live-aktivitet
* Skal AI'en linke til den seed'ede projektinputfil for aktiviteten
* Skal AI'en linke til den relevante del af denne facilitatorguide og eventuelle relevante skabeloner, spørgeguides eller værktøjsfiler
* Skal AI'en opsummere formålet, den estimerede tid og hvem der bør deltage, eller hvilket materiale der skal indsamles
* Skal AI'en vente på de færdige aktivitetsnoter, før syntesen genoptages, medmindre brugeren eksplicit beder om at simulere eller forberede aktiviteten i chatten
* Skal AI'en bruge den kanoniske handoff-struktur i [../../Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md](../../Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md)

## Endelige leverancer, pakken skal munde ud i

Ved afslutningen af Pakke B skal du kunne levere:

* En kort indsigtsopsamling fra 4-6 interviews
* Et kort over nuværende og fremtidig rejse
* En liste over nødvendige serviceændringer på tværs af proces, indhold, ejerskab og data
* En klikbar prototype af kerneflowet
* En prioriteret leveranceanbefaling

For at gøre prototypen pålidelig at producere skal den afsluttende syntese også generere:

* En prototype prompt pack-fil med:
  * Et kanonisk prototypebrief
  * Fresh-generation prompts
  * Refinement prompts
* En separat prototype record-fil, som fanger godkendte screenshots, prototypelink, iterationsnoter og godkendelsesstatus

Prompt packen er et produktionsstøttende artefakt, som hjælper med at skabe den klikbare prototype. Den må ikke erstatte selve prototypen, og den maa ikke gore den vigtigste endelige leverance unoedigt lang.

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
* Seed den separate prototype prompt-pack-fil i `04-final/`
* Seed den separate prototype record-fil i `04-final/`
* Registrér det oprindelige projektnavn, mappenavn, pakketype, arbejdssprog, oprettelsesdato og nuværende status i opsætningsnoten
* Hvis mappen allerede findes, så stop og bekræft, om den skal genbruges, før der gemmes filer
* Gem rå kundeinput i `01-inputs/`, igangværende syntese i `02-working/`, reviewversioner i `03-reviews/` og godkendte output i `04-final/`

## Før pakken starter

### Minimumstjekliste for intake

Indsaml dette før Aktivitet 1.1:

* Mulighedsområdet, produktet, portalen eller servicerejsen, der er i scope
* De beslutninger pakken skal understøtte
* Hvorfor dette er vigtigt nu i forretningsterminer
* Hvilken evidens der allerede findes, og hvem der ejer den
* De målbrugergrupper, der skal rekrutteres eller repræsenteres
* De relevante interessenter, teams og systemer
* De kendte begrænsninger, antagelser og elementer uden for scope

### Tjekliste til forberedelse før pakken

Før første aktivitet gennemføres:

* Bekræft sponsor og den navngivne ejer, som kan validere output
* Bekræft hvem der skal deltage i hver live-session
* Bekræft hvilken evidens der kan deles, før researchen starter
* Bekræft om rekruttering er realistisk, og hvem der kan hjælpe med adgang til brugere
* Book live-sessioner og reviewpunkter i den rigtige rækkefølge
* Fortæl kunden, at hver aktivitet slutter med et reviewpunkt, før næste trin starter

## Aktivitet 1.1: Afklaringsworkshop og undersøgelsesramme

### Formål

At aftale, hvilken rejse der er i scope, hvad forretningscasen er, hvilke succeskriterier der gælder, hvor scopegrænserne går, og hvilke spørgsmål pakken skal besvare.

### Estimeret aktivitetstid

2 timer

### Hvem bør deltage

* Sponsor eller budgetejer
* Produkt-, service- eller forretningsansvarlig
* Kommercielle, driftsnære, indholdsrelaterede eller leverancemæssige interessenter med relevant mandat

### Forberedelse før sessionen

* Bekræft hvilket mulighedsområde der skal drøftes
* Indsaml kendte input til business casen og forventede resultater
* Forbered et første billede af, hvad der er i scope og ude af scope
* Bekræft hvilken evidens der allerede findes

### Forslag til agenda

* Målsætning og indramning af beslutningen: 15 minutter
* Mulighedsområde og business case: 30 minutter
* Rejsen i scope og scopegrænser: 30 minutter
* Succeskriterier og spørgsmål til afklaringen: 30 minutter
* Opsamling og næste skridt: 15 minutter

### Kritiske spørgsmål der skal stilles

* Hvilken rejse eller hvilket serviceområde er faktisk i scope?
* Hvilken business case eller kommerciel logik gør dette arbejde værd at gennemføre nu?
* Hvilke resultater skal denne pakke påvirke?
* Hvad skal eksplicit være ude af scope?
* Hvad vil tælle som succes for denne pakke?
* Hvilke researchspørgsmål skal besvares, før leveranceomfanget kan fastlægges med sikkerhed?

### Hvad du skal fange

* Business case
* Rejsen i scope
* Scopegrænser
* Målbrugere
* Succeskriterier
* Spørgsmål til afklaringen
* Risici eller uenigheder

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_b_activity_1_1_input.md`-fil til denne aktivitet.

Fang kun:

* videreført kontekst der har ændret sig
* reelt nyt indramningsinput fra workshoppen

Kort sekvens:

1. Workshopopsætning og business case
2. Rejse, brugere og scope
3. Mål og discovery-fokus
4. Begrænsninger, spændinger og åbne spørgsmål

### Valideringscheckpoint

Kunden bør bekræfte:

* At rejsen i scope er tydelig
* At business casen er konkret nok til at styre researchen
* At succeskriterierne og spørgsmålene til afklaringen er gode nok til at drive resten af pakken

## Aktivitet 1.2: Gennemgang af evidens, rekruttering og brugerinterviews

### Formål

At skabe et velunderbygget billede af brugerbehov, barrierer, omveje og beslutningspunkter, før arbejdet går videre til kortlægning af rejse og koncept.

### Estimeret aktivitetstid

1-2 dage fordelt på forberedelse af evidens, koordinering af rekruttering, 4-6 interviews og første syntese

### Evidens og adgang der skal efterspørges

* Analytics og adfærdsevidens, der er relevant for rejsen
* Kundefeedback, supporttemaer og input fra salg
* Tidligere research eller usabilityfund
* Adgang til de brugergrupper, der betyder mest for rejsen i scope
* Eventuelle begrænsninger, der påvirker rekruttering, fortrolighed eller interviewformat

Brug [../../Projects/Templates/Danish/Shared/evidence_request_template_danish.md](../../Projects/Templates/Danish/Shared/evidence_request_template_danish.md), hvis du vil efterspoerge denne evidens eller adgang fra kundeteamet paa en mere struktureret maade.

### Sådan gennemføres dette trin

* Gennemgå den stærkeste evidens, før interviewene starter
* Rekruttér ud fra relevans for rejsen og ikke demografisk spredning for sin egen skyld
* Brug interviewene til at forstå reelle mål, barrierer, beslutningspunkter og omveje
* Adskil citater fra deltagere, teamets fortolkninger og resterende antagelser

### Hvad du skal fange

* Formål med researchen
* Deltagerprofil eller logik bag rekrutteringen
* Evidens der er gennemgået
* Vigtigste brugerbehov
* Centrale barrierer
* Beslutningspunkter og sammenligningslogik
* Åbne spørgsmål til rejse- og konceptarbejdet

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_b_activity_1_2_input.md`-fil til denne aktivitet.

Fang kun:

* de stærkeste evidens- og interviewfund
* de nye behov, barrierer og beslutningslogikker der betyder noget for pakken

Kort sekvens:

1. Evidens og researchdækning
2. Behov og barrierer
3. Beslutningskriterier og workarounds
4. Konflikter, overraskelser og næste spørgsmål

### Valideringscheckpoint

Kunden bør bekræfte:

* At indsigtsopsamlingen afspejler de rigtige brugere
* At behov, barrierer og beslutningspunkter virker troværdige
* At de vigtigste spørgsmål til rejsearbejdet er synlige

## Aktivitet 2.1: Kort over nuværende rejse og indramning af muligheder

### Formål

At skabe et fælles billede af den nuværende rejse og identificere de vigtigste mulighedsområder for det fremtidige koncept.

### Estimeret aktivitetstid

4-6 timers syntese og kortlægning samt et reviewcheckpoint med interessenter på 45-60 minutter

### Hvem bør deltage i reviewet

* Interessenter der forstår rejsen i dag
* Teams der påvirker service, indhold, proces eller systemer i rejsen

### Sådan gennemføres dette trin

* Kortlæg rejsen ende til anden på tværs af brugere, teams og systemer
* Vis hvor brugere tøver, hvor overleveringer fejler, og hvor servicelogikken skaber friktion
* Destillér de få mulighedsområder, der betyder mest for konceptfasen

### Hvad du skal fange

* Faser i den nuværende rejse
* Brugerbehov og barrierer pr. fase
* Involverede teams, systemer og overleveringer
* De vigtigste brud
* Mulighedsområder
* Beslutningskriterier det fremtidige koncept skal leve op til

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_b_activity_2_1_input.md`-fil til denne aktivitet.
Brug [../../Projects/Templates/Danish/Shared/current_journey_mapping_template_danish.md](../../Projects/Templates/Danish/Shared/current_journey_mapping_template_danish.md) eller den genererede `next_activity_mapping_canvas_danish.md` i projektets `00-project-setup/shared-prep/`, hvis du vil have en konkret canvas til at kortlaegge den nuvaerende rejse.

Fang kun:

* den nuværende rejse der skal være synlig
* de få brud, mulighedsområder og beslutningskriterier der er vigtige næste gang

Kort sekvens:

1. Struktur for den nuværende rejse
2. Brudmønster og afhængigheder
3. Mulighedsområder og beslutningskriterier

### Valideringscheckpoint

Kunden bør bekræfte:

* At den nuværende rejse er realistisk
* At de vigtigste brud betyder noget for de beslutninger, der ligger foran
* At mulighedsområderne er stramme nok til at guide konceptarbejdet

## Aktivitet 3.1: Arbejdssession om fremtidigt koncept

### Formål

At definere den fremtidige rejse og de nødvendige serviceændringer bag den.

### Estimeret aktivitetstid

2-3 timer til konceptsessionen samt 3-5 timers syntese

### Hvem bør deltage

* Interessenter der kan påvirke produkt-, service-, indholds-, drifts-, ejerskabs- og datakonsekvenser

### Forberedelse før sessionen

* Medbring den validerede nuværende rejse og mulighedsområderne
* Forbered en ramme for det fremtidige koncept
* Bekræft hvilke leverancespørgsmål konceptet skal gøre lettere at besvare

### Forslag til sessionens flow

* Gennemgang af mulighedsrammen fra den nuværende situation: 20 minutter
* Definition af den fremtidige rejse: 60-75 minutter
* Ændringer i proces, indhold, ejerskab og data: 40-50 minutter
* Opsamling på koncept, serviceændringer og åbne spørgsmål: 20-25 minutter

### Hvad du skal fange

* Fremtidig rejse
* Oplevelsesprincipper
* Nødvendige serviceændringer på tværs af proces, indhold, ejerskab og data
* Afhængigheder og åbne spørgsmål
* De dele af konceptet, der skal gøres konkrete i prototypen

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_b_activity_3_1_input.md`-fil til denne aktivitet.

Fang kun:

* den fremtidige retning som gruppen faktisk alignede sig om
* de serviceændringer, afhængigheder og prototypeøjeblikke der skal videreføres

Kort sekvens:

1. Fremtidig retning og rejse
2. Principper og serviceændringer
3. Afhængigheder og prototypeøjeblikke

### Valideringscheckpoint

Kunden bør bekræfte:

* At den fremtidige retning svarer på de vigtigste problemer i den nuværende situation
* At de nødvendige serviceændringer er synlige og troværdige
* At konceptet er stærkt nok til at gå videre til prototype og prioritering

## Aktivitet 4.1: Klikbar prototype, prioriteringsworkshop og leveranceanbefaling

### Formål

At gøre konceptet konkret og omsætte det til en anbefaling om, hvad der skal bygges først.

### Estimeret aktivitetstid

2 timer til prioriteringsworkshop samt 1-2 dage til prototypebrief, promptgenerering, støtte til prototypeproduktion og paketering af anbefaling

### Forberedelse før sessionen

* Bekræft hvilke dele af den fremtidige rejse prototypen skal vise
* Bekræft hvilke muligheder eller ændringer der skal prioriteres
* Bekræft kendte signaler om indsats, begrænsninger i leverancen og afhængigheder
* Bekræft hvilket designværktøj der skal bruges først til prototypen

### Forslag til sessionens flow

* Gennemgang af formål og scope for prototypen: 20 minutter
* Review af vigtige muligheder eller konceptelementer: 30 minutter
* Prioritering mod fælles kriterier: 45 minutter
* Opsamling på byg først, udskyd og valider næste gang: 25 minutter

### Hvad du skal fange

* Formål med prototypen
* Kerneflow eller momenter prototypen skal vise
* Prioriteringskriterier
* Anbefaling om hvad der skal bygges først
* Elementer der skal udskydes
* Elementer der skal valideres næste gang
* Risici, afhængigheder og konsekvenser for rækkefølgen

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_b_activity_4_1_input.md`-fil til denne aktivitet.

Fang kun:

* det prototype-scope og den prioriteringslogik der er nødvendig for den endelige anbefaling
* de begrænsninger, valideringspunkter og værktøjsvalg der er nødvendige for prompt packen

Kort sekvens:

1. Beslutning og prototypeformål
2. Prototype-scope og interaktioner
3. Prioritering og sekventering
4. Risici, validering og værktøjsvalg

### Valideringscheckpoint

Kunden bør bekræfte:

* At prototypens scope er stramt nok til at understøtte en reel beslutning
* At prioriteringslogikken er troværdig
* At anbefalingen om, hvad der skal bygges først, er tydelig nok til næste fase

### Trin til produktion af prototype

Efter at AI'en har produceret anbefalingspakken og prototype prompt packen:

1. Brug det kanoniske brief og den værktøjsspecifikke prompt i det valgte designværktøj.
2. Generér det første udkast til prototypen.
3. Gennemgå udkastet op mod det validerede koncept og prototype-reviewtjeklisten i [prototype_prompt_pack_template_danish.md](prototype_prompt_pack_template_danish.md).
4. Hvis der blev delt screenshots eller links fra kundens nuværende løsning, så tjek at udkastet ligger tæt på den eksisterende visuelle stil, medmindre briefet eksplicit beder om forandring.
5. Forfin prompten, hvis prototypen driver væk fra den aftalte retning.
6. Medtag den endelige klikbare prototype sammen med anbefalingspakken.

## Praktiske regler for facilitering

* Hold pakken knyttet til én rejse eller ét serviceområde
* Behandl evidens, research, rejsearbejde, konceptudvikling og prioritering som sammenhængende trin
* Lad ikke prototypearbejdet åbne det validerede koncept helt fra bunden
* Hold sproget forretningsnært og beslutningsorienteret
* Gå kun videre, når det forrige output er reviewet og accepteret
