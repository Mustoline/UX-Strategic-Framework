# Facilitatorguide til Pakke A

## Formål

Brug denne guide til at forberede og gennemføre de virkelige Pakke A-aktiviteter med kunden.

Målet er at sikre, at du indsamler det rigtige materiale i den rigtige rækkefølge, så AI'en kan behandle hver aktivitet rent og omsætte den til et valideret output, før næste trin begynder.

Brug denne guide sammen med:

* [Package_A_core_activities_danish.md](Package_A_core_activities_danish.md) til pakkeopsummeringen
* [Package_A_ai_process_danish.md](Package_A_ai_process_danish.md) til AI-handoff og den trinvis styrede workflowlogik
* [prototype_prompt_pack_template_danish.md](prototype_prompt_pack_template_danish.md) til promptstrukturen, der bruges til at generere prototypen

## Delte forberedelsesaktiver til live-leverance

Brug disse delte filer, naar du skal forberede selve den virkelige session:

* [../../Projects/Templates/Danish/Shared/workshop_invite_template_danish.md](../../Projects/Templates/Danish/Shared/workshop_invite_template_danish.md)
* [../../Projects/Templates/Danish/Shared/session_brief_template_danish.md](../../Projects/Templates/Danish/Shared/session_brief_template_danish.md)

## Sådan skal workflowet køre

1. Brug denne guide til at forberede og gennemføre én Pakke A-aktivitet med kunden.
2. Fang de nødvendige noter i den seed'ede projektinputfil for aktiviteten.
3. Bring dette input ind i AI-processen.
4. Review det bearbejdede output med kunden og bekræft eventuelle ændringer.
5. Gå først derefter videre til næste aktivitet.

Gå ikke videre, hvis det forrige output endnu ikke er accepteret. Værdien af Pakke A afhænger af, at hvert trin bygger på valideret input.

## Lean capture-regel

Pakke A maa ikke foeles som et langt gentaget spoergeskema.

Brug disse regler under faciliteringen:

* Start hver aktivitet fra det validerede output af det forrige trin
* Behandl bekraeftet kunde-, scope-, beslutnings-, maalbruger- og begraensningskontekst som viderefoert standardkontekst, medmindre kunden eksplicit aendrer den
* Fang kun det reelt nye input, der er noedvendigt for den aktuelle aktivitet
* Hvis et punkt kun kraever bekraeftelse, saa bekraeft det hurtigt i stedet for at dokumentere det fuldt igen
* Hold den virkelige aktivitet fokuseret paa den naeste beslutning og ikke paa at genopbygge tidligere noter

Naar aktiviteten senere simuleres i chatten, skal AI'en spejle samme logik ved at bruge en kort step-baseret sekvens og kun bede om det minimum af nyt input, der er noedvendigt.

Brug den seed'ede projektinputfil i `01-inputs/` og [../../Projects/Templates/Danish/Package_A/package_a_template_library_danish.md](../../Projects/Templates/Danish/Package_A/package_a_template_library_danish.md) som den gaeldende reference for den konkrete step-baserede handoffstruktur. De korte lean capture-strukturer laengere nede i guiden opsummerer kun sekvensen for hver aktivitet og maa ikke udvides tilbage til fulde dublerede skabeloner.

## AI-handoff til næste live-aktivitet

Når det forrige trin er valideret, og næste skridt er en virkelig aktivitet:

* Skal AI'en eksplicit sige, at næste skridt nu er en live-aktivitet
* Skal AI'en linke til den seed'ede projektinputfil for aktiviteten
* Skal AI'en linke til den relevante del af denne facilitatorguide og eventuelle relevante skabeloner, spørgeguides eller værktøjsfiler
* Skal AI'en opsummere formålet, den estimerede tid og hvem der bør deltage, eller hvilket materiale der skal indsamles
* Skal AI'en vente på de færdige aktivitetsnoter, før syntesen genoptages, medmindre brugeren eksplicit beder om at simulere eller forberede aktiviteten i chatten
* Skal AI'en bruge den kanoniske handoff-struktur i [../../Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md](../../Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md)

## Endelige leverancer, sprintet skal munde ud i

Ved afslutningen af Pakke A skal du kunne levere:

* Et anbefalingsoplæg
* Et kort over de vigtigste brud i det valgte trin af rejsen
* En klikbar prototype på 1-2 skærme, som illustrerer den anbefalede forbedring
* En kort liste over risici og næste skridt

For at gøre prototypen pålidelig at producere skal den afsluttende syntese også generere:

* En prototype prompt pack-fil med:
  * Et kanonisk prototypebrief
  * Fresh-generation prompts
  * Refinement prompts
* En separat prototype record-fil, som fanger godkendte screenshots, prototypelink, iterationsnoter og godkendelsesstatus

Prompt packen er et produktionsstøttende artefakt, som hjælper med at skabe den klikbare prototype. Den må ikke erstatte selve prototypen, og den maa ikke gore den vigtigste endelige leverance unoedigt lang.

## Projektopsætning før sprintet starter

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

## Før sprintet starter

### Minimumstjekliste for intake

Indsaml dette før Aktivitet 1.1:

* Problemområdet, arbejdsgangen, funktionsområdet eller trinnet i rejsen, der er i scope
* Den beslutning sprintet skal understøtte
* Hvorfor dette er vigtigt nu i forretningsterminer
* Hvilken evidens der allerede findes, og hvem der ejer den
* De relevante interessenter og teams
* De kendte begrænsninger, antagelser og elementer uden for scope

### Tjekliste til forberedelse før sprint

Før første aktivitet gennemføres:

* Bekræft sponsor og den navngivne ejer, som kan validere output
* Bekræft hvilke interessenter der skal deltage i hver live-session
* Bed om eksisterende evidens tidligt, så Aktivitet 1.2 ikke bliver forsinket
* Book live-sessionerne i den rigtige rækkefølge, så sprintet kan holde momentum
* Fortæl kunden, at hver aktivitet slutter med et reviewpunkt, før næste trin starter

## Aktivitet 1.1: Sponsorworkshop og beslutningsramme

### Formål

At blive enige om forretningsspørgsmålet, målbrugerne, succeskriterierne, scopegrænsen og de vigtigste begrænsninger for sprintet.

### Estimeret aktivitetstid

90 minutter

### Hvem bør deltage

* Sponsor eller budgetejer
* Produkt-, service- eller forretningsansvarlig
* Relevante interessenter fra drift, det kommercielle område eller leverancen
* Undgå at invitere observatører, som ikke kan bidrage til beslutningen

### Forberedelse før sessionen

* Bekræft den beslutning sprintet skal understøtte
* Bekræft hvad man allerede mener om problemet
* Forbered afgrænsningen af det, der er ude af scope, så diskussionen holder fokus
* Bed om eventuelle kendte baselinemål på forhånd

### Forslag til agenda

* Åbning og indramning af målet: 10 minutter
* Problemindramning og forretningskontekst: 20 minutter
* Målbrugere og fokus i rejsen: 20 minutter
* Succeskriterier og begrænsninger: 20 minutter
* Åbne spørgsmål og sprintprioriteter: 15 minutter
* Opsamling og afslutning: 5 minutter

### Kritiske spørgsmål der skal stilles

* Hvilken beslutning skal træffes, før leverancen starter?
* Hvorfor er dette problem værd at adressere nu?
* Hvilke bruger- eller medarbejdergrupper betyder mest for den beslutning?
* Hvilken del af rejsen er i scope, og hvad er ikke?
* Hvordan ser succes ud i forretningsmæssige, brugerrelaterede og driftsmæssige termer?
* Hvilke begrænsninger er faste, og hvilke er stadig antagelser?

### Hvad du skal fange

* Forretningsspørgsmål
* Beslutning der skal understøttes
* Hvorfor dette er vigtigt nu
* Målbrugere
* Scope og grænse for det, der er ude af scope
* Succeskriterier, inklusiv baseline og mål hvor det er muligt
* Begrænsninger
* Åbne sprintspørgsmål

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_a_activity_1_1_input.md`-fil til denne aktivitet.

Fang kun:

* videreført kontekst der har ændret sig
* reelt nyt input fra workshoppen

Kort sekvens:

1. Workshopopsætning og forretningsspørgsmål
2. Brugere og scope
3. Mål og begrænsninger
4. Spændinger og åbne sprintspørgsmål

### Valideringscheckpoint

Kunden bør bekræfte:

* At sprintet er fokuseret på det rigtige problem
* At scopegrænsen er tydelig
* At succeskriterierne er gode nok til at guide resten af sprintet
* At ukendte begrænsninger er registreret som ukendte og ikke skjult

## Aktivitet 1.2: Gennemgang af evidensgrundlag

### Formål

At omsætte den tilgængelige evidens til et praktisk grundlag, som skiller veldokumenterede signaler fra antagelser.

### Estimeret aktivitetstid

2-4 timer afhængigt af evidensens kvalitet og tilgængelighed

### Evidens der skal efterspørges

* Analytics for det valgte trin i rejsen
* Segmenterede performance-data fordelt på device, trafikkilde, nye versus tilbagevendende besøgende eller relevant kundesegment, hvor det er muligt
* Supporthenvendelser eller klagetemaer
* Input fra salg eller det kommercielle område
* Tidligere research eller usabilityfund
* Sessionsoptagelser, heatmaps eller anden adfærdsmæssig evidens, hvis det findes

Brug [../../Projects/Templates/Danish/Shared/evidence_request_template_danish.md](../../Projects/Templates/Danish/Shared/evidence_request_template_danish.md), hvis du vil efterspoerge dette materiale fra kundeteamet paa en mere struktureret maade.

### Sådan gennemføres dette trin

* Gennemgå de stærkeste kilder først og ikke alle tænkelige kilder
* Hold gennemgangen stramt afgrænset til det valgte problem
* Marker hvad der er evidens, hvad der er fortolkning, og hvad der stadig er antagelse
* Vær opmærksom på manglende segmentering, fordi brede gennemsnit ofte skjuler, hvor problemet er størst

### Hvad du skal fange

* Kilder der er gennemgået
* De stærkeste signaler
* Velunderstøttede fund
* Fund der peger i en retning, men endnu ikke er bevist
* Resterende antagelser
* Konflikter eller huller i evidensen
* Spørgsmål sprintet stadig skal validere

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_a_activity_1_2_input.md`-fil til denne aktivitet.

Fang kun:

* videreført kontekst der har ændret sig
* de nye evidensfund og huller der faktisk betyder noget

Kort sekvens:

1. Evidenskilder og dækning
2. Stærkeste signaler og understøttede fund
3. Resterende usikkerhed og næste valideringsspørgsmål

### Valideringscheckpoint

Kunden bør bekræfte:

* At grundlaget afspejler den stærkeste tilgængelige evidens
* At forskellen mellem kendt og antaget er tydelig
* At de resterende huller er synlige nok til at guide kortlægning og gennemgang af løsningsmuligheder

## Aktivitet 1.3: Kortlægningssession af trin i rejsen

### Formål

At skabe et fælles billede af den nuværende situation i det valgte trin i rejsen og isolere de få brud, der betyder mest for beslutningen.

### Estimeret aktivitetstid

60-90 minutter

### Hvem bør deltage

* Interessenter tæt på det valgte trin
* Personer der forstår den nuværende arbejdsgang, indholdet, systemerne eller serviceoverleveringerne
* Undgå at gøre dette til en workshop om hele rejsen

### Forslag til sessionens flow

* Bekræft det valgte trin og beslutningen der skal understøttes: 10 minutter
* Kortlæg aktører, nuværende handlinger og kontaktpunkter: 20 minutter
* Kortlæg systemer, afhængigheder og overleveringer: 15 minutter
* Identificér de vigtigste friktionspunkter og interne konsekvenser: 20 minutter
* Prioritér de 3-5 vigtigste brud: 15 minutter

### Hvad du skal fange

* Det valgte trin i scope
* Aktører
* Nuværende handlinger
* Kontaktpunkter og kanaler
* Systemer og afhængigheder
* Friktionspunkter
* Interne konsekvenser
* De 3-5 største brud og hvorfor de betyder noget

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_a_activity_1_3_input.md`-fil til denne aktivitet.

Fang kun:

* inputtet til kortlægningen af den nuværende situation
* de få brud der betyder mest for beslutningen

Kort sekvens:

1. Trin i scope og nuværende flow
2. Kontaktpunkter og afhængigheder
3. Brudmønster

### Valideringscheckpoint

Kunden bør bekræfte:

* At kortet afspejler det, der sker i dag, og ikke en idealiseret version
* At de vigtigste brud er dem, der er mest relevante for beslutningen
* At scope fortsat er afgrænset til ét trin eller ét udsnit af arbejdsgangen

## Aktivitet 2.1: Gennemgang af løsningsmuligheder og foretrukken retning

### Formål

At sammenligne et lille antal realistiske retninger og identificere den foretrukne vej med tydelige tradeoffs.

### Estimeret aktivitetstid

2 timer

### Forberedelse før sessionen

* Medbring de validerede output fra Aktivitet 1.1 til 1.3
* Forbered 1-2 realistiske retninger
* Hvis kunden ikke har foreslået muligheder, skal der indsamles nok materiale til, at AI'en kan generere dem før gennemgangen
* Forbered fælles kriterier på tværs af bruger-, forretnings- og leverancelinse

### Forslag til sessionens flow

* Bekræft mål og kriterier: 15 minutter
* Gennemgang af mulighed A: 25 minutter
* Gennemgang af mulighed B: 25 minutter
* Sammenlign tradeoffs og afhængigheder: 25 minutter
* Opsamling på foretrukken retning og åbne checks: 30 minutter

### Hvad du skal fange

* Muligheder der er sammenlignet
* Sammenligningskriterier
* Vurderinger af hver mulighed op mod kriterierne
* Tradeoffs
* Risici og afhængigheder
* Foretrukken retning
* Åbne checks før anbefalingsarbejdet

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_a_activity_2_1_input.md`-fil til denne aktivitet.

Fang kun:

* de retninger der faktisk blev sammenlignet
* kriterier, tradeoffs og den foretrukne retning der opstod

Kort sekvens:

1. Beslutning og retninger
2. Sammenligningskriterier
3. Noter om retninger og tradeoffs
4. Foretrukken retning og åbne checks

### Valideringscheckpoint

Kunden bør bekræfte:

* At de samme kriterier blev brugt på alle muligheder
* At tradeoffs er tydelige
* At den foretrukne retning er klar nok til at blive pakket som anbefaling

## Aktivitet 3.1: Anbefalingspakke og konceptbrief

### Formål

At omsætte de validerede sprintoutput til en beslutningsklar anbefaling og et koncept, der er konkret nok til review med sponsor.

### Estimeret aktivitetstid

4-8 timers syntese og paketering samt et reviewcheckpoint med sponsor på 30-45 minutter

### Forberedelse før AI-handoff

* Medbring den validerede foretrukne retning
* Bekræft den ønskede scopegrænse for det næste leverancetrin
* Bekræft eventuelle sidste begrænsninger eller afhængigheder, der påvirker anbefalingen
* Bekræft hvordan succes skal måles efter release
* Bekræft hvilke 1-2 skærme eller momenter prototypen skal vise
* Bekræft om brugeren kan dele screenshots eller links fra kundens eksisterende løsning, hvis prototypen skal ligge tæt på det nuværende visuelle design
* Bekræft om prototypen først skal bygges i Figma Make eller Google Stitch

### Hvad du skal fange

* Anbefalet retning
* Hvorfor denne retning er stærkere
* Målbrugere
* Succeskriterier
* Hvad der skal bygges nu
* Hvad der skal udskydes
* Hvad der skal valideres næste gang
* Risici og afhængigheder
* Umiddelbare næste skridt
* De præcise skærme, momenter og interaktioner prototypen skal indeholde
* Eventuelle krav til indhold, brand eller layout, som skal forme prototypeprompten

### Lean capture-struktur

Brug den seed'ede `01-inputs/package_a_activity_3_1_input.md`-fil til denne aktivitet.

Fang kun:

* den endelige anbefalingslogik der stadig skal bekræftes
* de prototypebrief-detaljer der er nødvendige for prompt packen

Kort sekvens:

1. Anbefalingslås og sponsor-noter
2. Scope og mål
3. Risici, validering og næste skridt
4. Prototypebrief

### Valideringscheckpoint

Kunden bør bekræfte:

* At anbefalingen understøtter den oprindelige beslutning
* At scope er stramt nok til næste leverancetrin
* At opdelingen mellem byg nu, udskyd og valider næste gang er troværdig
* At risici og målelogik er tydelige nok til at gå videre

### Trin til produktion af prototype

Efter at AI'en har produceret anbefalingspakken og prototype prompt packen:

1. Brug det kanoniske brief og den værktøjsspecifikke prompt i det valgte designværktøj.
2. Generér det første udkast til prototypen.
3. Gennemgå udkastet op mod den validerede anbefaling og prototype-reviewtjeklisten i [prototype_prompt_pack_template_danish.md](prototype_prompt_pack_template_danish.md).
4. Hvis der blev delt screenshots eller links fra kundens nuværende løsning, så tjek at udkastet ligger tæt på den eksisterende visuelle stil, medmindre briefet eksplicit beder om forandring.
5. Forfin prompten, hvis prototypen driver væk fra den aftalte retning.
6. Medtag den endelige klikbare prototype sammen med anbefalingspakken.

## Praktiske regler for facilitering

* Hold Pakke A afgrænset til ét problemområde, én arbejdsgang eller ét trin i rejsen
* Behandl ukendte begrænsninger som en risiko, der skal synliggøres tidligt
* Lad ikke sprintet glide over i en redesign-diskussion
* Hold sproget forretningsnært og beslutningsorienteret
* Pres på for at få baseline- og målniveauer frem, når interessenter taler om succes
* Gå kun videre, når det forrige output er reviewet og accepteret
