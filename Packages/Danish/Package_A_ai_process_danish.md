# AI-proces for Pakke A

## Formaal

Brug denne fil til at koere Pakke A som en trinvis styret AI-workflow, efter at facilitatoren har gennemfoert hver virkelig aktivitet.

Denne fil er til den interne AI-logik og ikke til kundevendt facilitering.

Brug den sammen med:

* [Package_A_core_activities_danish.md](Package_A_core_activities_danish.md) til pakkeopsummeringen
* [Package_A_facilitator_guide_danish.md](Package_A_facilitator_guide_danish.md) til den virkelige workshop- og reviewvejledning
* [prototype_prompt_pack_template_danish.md](prototype_prompt_pack_template_danish.md) til den genanvendelige promptstruktur for prototypen

## Centrale driftsregler

* Behandl en aktivitet ad gangen
* Gaa ikke videre til naeste aktivitet, foer brugeren har valideret det nuvaerende output
* Hvis noedvendigt input mangler, saa bed om det manglende materiale i stedet for at udfylde hullerne med selvsikre antagelser
* Skeln tydeligt mellem underbyggede fund, inferens og aaben antagelse
* Behandl ukendte begraensninger som en risiko, der skal synliggoeres, og ikke som bevis for, at der ingen begraensninger findes
* Hold arbejdet afgraenset til et problemomraade, en arbejdsgang, et funktionsomraade eller et trin i rejsen
* Hold output forretningsnaert og beslutningsorienteret

## Valideringstilstande

AI'en skal behandle validering i en af tre tilstande:

* **Valideret:** Outputtet er accepteret og kan foeres videre som bekraeftet input
* **Valideret med aendringer:** AI'en skal opdatere outputtet og derefter bede om endelig bekraeftelse, foer arbejdet gaar videre
* **Ikke valideret:** AI'en skal stoppe og afvente mere input eller korrektion

Gaa ikke videre til naeste aktivitet paa baggrund af stiltiende godkendelse. Vent paa en eksplicit bekraeftelse fra brugeren.

Efter at en reviewfil er opdateret med en valideringsbeslutning, skal AI'en koere `python3 Projects/sync_project_status.py --project-name "<Projektnavn>"` i samme tur, saa projektets kontrolfiler holdes aligned med workflowets status.

## Standardmoenster for AI-svar

Efter behandling af enhver Pakke A-aktivitet skal AI'en returnere:

1. **Bearbejdet output til review**
2. **Hvad der foeres videre som bekraeftet input**
3. **Hvad der stadig er aabent eller usikkert**
4. **Hvilket input der kraeves til naeste aktivitet**
5. **Et direkte valideringsspoergsmaal**

## Lean input- og sekvensregler

Pakke A skal som standard bruge den letteste inputflow, der stadig giver et beslutningsklart output.

Det betyder:

* Foer valideret kontekst videre fra tidligere trin som standard
* Sporg ikke igen om kunde, scope, beslutning, maalbrugere, begraensninger eller maalinger, medmindre de har aendret sig, mangler eller stadig er omstridte
* Begynd hver ny aktivitet med kort at gentage den viderefoerte kontekst, der er relevant for netop den aktivitet
* Bed kun om det minimum af nyt input, der er noedvendigt for at understoette den aktuelle syntese
* Behandl ekstra spoergsmaal som valgfrie opfoelgninger og ikke som obligatorisk standardintake

Naar brugeren beder om at koere et trin eller en aktivitet i chatten:

* Brug en kort step-baseret sekvens i stedet for et langt felt-for-felt-spoergeskema
* Vis tydelig fremdrift i det primere svar med et format som `Aktivitet 1.2, trin 2 af 3`
* Brug 2-4 trin til de fleste aktiviteter
* Hvert trin kan indeholde 1-3 taet relaterede spoergsmaal
* Hvis et senere spoergsmaal afhaenger af et tidligere svar, saa gentag det tidligere svar inline foer opfoelgningsspoergsmaalet

## Standardiseret sekvenskort for Pakke A

Brug dette som standardstruktur, naar et trin bliver simuleret eller forberedt i chatten.

### Trin 0

Brug 4 trin:

1. Kunde og problemomraade
2. Beslutning og hvorfor nu
3. Evidens og interessenter
4. Graenser

### Aktivitet 1.1

Foer Trin 0-konteksten videre og brug 4 trin:

1. Workshopopsaetning og forretningsspoergsmaal
2. Brugere og scope
3. Maal, baseline og begraensninger
4. Uenigheder og aabne sprintspoergsmaal

### Aktivitet 1.2

Foer den validerede beslutningsramme videre og brug 3 trin:

1. Evidenskilder og daekning
2. Staerkeste signaler og understoettede fund
3. Antagelser, huller og naeste valideringsspoergsmaal

### Aktivitet 1.3

Foer evidensimplikationerne videre og brug 3 trin:

1. Trin i scope, aktoerer og nuvaerende handlinger
2. Kontaktpunkter, systemer, afhaengigheder og interne implikationer
3. Friktionspunkter, stoerste brud og valideringshuller

### Aktivitet 2.1

Foer breakdown-kortet videre og brug 4 trin:

1. Beslutning og muligheder
2. Sammenligningskriterier
3. Noter om mulighederne og tradeoffs
4. Foretrukken retning, risici og aabne checks

### Aktivitet 3.1

Foer den foretrukne retning fra Aktivitet 2.1 videre og brug 4 trin:

1. Laas anbefalingen og sponsor-noter
2. Byg nu, udskyd, maalbrugere og succeskriterier
3. Risici, validering og naeste skridt
4. Prototype-scope, interaktioner, begraensninger, vaerktoejsvalg og valgfrie visuelle referencer

## Regel for handoff til virkelige aktiviteter og synlighed

Naar naeste skridt er en workshop, et interview, et evidensreview, en mappingsession eller en anden virkelig aktivitet:

* Stop efter validering og goer det eksplicit, at naeste skridt sker i virkeligheden, foer AI-syntesen kan fortsaette
* Begynd ikke straks at stille aktivitetens capture-spoergsmaal, som om sessionen allerede er gennemfoert
* Link til den relevante facilitatorguide, den seed'ede projektinputfil i `01-inputs/` og eventuelle relevante skabeloner, spoergeguides eller vaerktoejsfiler
* Opsummer aktivitetens formaal, estimerede tid og hvem der boer deltage, eller hvilket materiale der skal indsamles
* Bed brugeren om at vende tilbage med de faerdige aktivitetsnoter eller sige til, hvis der er brug for hjaelp til at forberede aktiviteten
* Koer kun den naeste aktivitet som en spoergesekvens i chatten, hvis brugeren eksplicit beder om at simulere eller forberede den inde i vaerktoejet
* Brug den praecise sektionsraekkefoelge i [../../Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md](../../Projects/Templates/Danish/Shared/live_activity_handoff_message_template_danish.md)

Fordi commentary-opdateringer kan vaere skjult i interfacet:

* Hold fremdriftsopdateringer i commentary
* Laeg det egentlige brugerrettede spoergsmaal, valideringsspoergsmaalet eller next-step-request i det primaere brugersvar
* Laeg hele handoff-strukturen til live-aktiviteter i det primaere brugersvar
* Under en simuleret live aktivitetssekvens skal der skiftes til chat-only simulation mode
* Koer ingen fillaesninger, filskrivninger, sync-kommandoer eller andre tool actions under den aktive spoergeflow
* Hold noterne i arbejdshukommelsen, indtil sekvensen er faerdig, og skriv foerst derefter projektfilerne og returner det bearbejdede output til validering
* Lad ikke rae kommando-, tool call- eller filaktions-tekst optraede i den synlige spoergeflow
* Naar et opfoelgende spoergsmaal bygger paa et tidligere svar, skal det tidligere svar gentages i spoergsmaalet, saa brugeren ikke skal scrolle tilbage
* Hvis intern kommando- eller tooltekst alligevel slipper ud i samtalen, skal spoergsmaal-for-spoergsmaal-flowet stoppes, og resten skal indsamles i en fallback-mode med et samlet svar

## Endeligt outputsaet for Pakke A

Ved afslutningen af Pakke A skal den AI-understoettede workflow kunne understoette levering af:

* Et anbefalingsoplaeg
* Et kort over de vigtigste brud i det valgte trin i rejsen
* En klikbar prototype paa 1-2 skaerme, som illustrerer den anbefalede forbedring
* En kort liste over risici og naeste skridt

For at gøre prototypen paalidelig at producere skal det endelige AI-output ogsaa indeholde:

* Et kanonisk prototypebrief
* Fresh-generation prompts
* Refinement prompts
* En separat prototyperegistrering, som fanger det godkendte artefakt, reviewnoter og godkendelsesstatus

Prompt packen er et understoettende output. Den hjaelper med at skabe den klikbare prototype, men erstatter ikke selve prototypen. Hold den endelige hovedleverance, prototype prompt pack og prototyperegistrering i separate filer inde i `04-final/`.

## Trin -1: Projektopsaetning foer intake

### Input der kraeves fra brugeren

Brugeren boer levere:

* Projektnavn
* Bekraeftelse paa at genbruge den eksisterende mappe, hvis den normaliserede projektmappe allerede findes

### Hvad AI'en skal goere

* Bede om projektnavnet, foer intake behandles, eller projektspecifikke artefakter oprettes
* Normalisere projektnavnet til et mappenavn, der er sikkert at bruge
* Kontrollere om `../../Projects/<Project-Name>/` allerede findes
* Hvis den findes, saa stoppe og spoerge, om den skal genbruges, eller om der skal vaelges et andet projektnavn
* Hvis den ikke findes, oprette `../../Projects/<Project-Name>/00-project-setup/`
* Oprette `../../Projects/<Project-Name>/01-inputs/`
* Oprette `../../Projects/<Project-Name>/02-working/`
* Oprette `../../Projects/<Project-Name>/03-reviews/`
* Oprette `../../Projects/<Project-Name>/04-final/`
* Oprette `../../Projects/<Project-Name>/project_index.md` som projektets kontrolcenter
* Oprette `../../Projects/<Project-Name>/00-project-setup/project_setup.md`
* Seede de relevante filer til Trin 0 og aktivitetsinput i `01-inputs/`
* Seede de relevante aktivitetsoutputfiler i `02-working/`
* Seede de relevante reviewfiler i `03-reviews/`
* Seede den primere endelige leverancefil i `04-final/`
* Seede den separate prototype prompt-pack-fil i `04-final/`
* Seede den separate prototyperegistrering i `04-final/`
* Registrere det oprindelige projektnavn, det normaliserede mappenavn, pakketype, arbejdssprog, oprettelsesdato og nuvaerende status i opsaetningsnoten
* Holde alle efterfoelgende projektgenererede filer inde i denne mappestruktur

### Outputformat

Returner:

* Bekraeftet projektnavn
* Normaliseret mappenavn
* Projektsti
* Oprettet mappestruktur
* Oprettet kontrolcenterfil
* Anbefalet naeste skridt

### Valideringsport

Gaa kun videre til Trin 0, naar brugeren bekraefter, at projektopsaetningen er korrekt.

## Trin 0: Intake-check foer Aktivitet 1.1

### Regel for intake-dialog

Som standard skal AI'en koere Trin 0 som en guidet intake-dialog i stedet for at bede brugeren om at sende hele intake-listen i en besked.

AI'en skal:

* Stille et kort trin ad gangen i stedet for et isoleret felt ad gangen
* Bruge det synlige fremdriftsformat `Trin 0, trin X af 4`
* Holde hvert trin fokuseret paa 1-3 taet relaterede spoergsmaal
* Vente paa svaret, foer den gaar videre til naeste trin
* Formulere hvert spoergsmaal som naturlig guidet dialog frem for som en raa feltlabel
* Give et kort illustrativt eksempel til hvert spoergsmaal bortset fra `Kunde / kontekst`
* Goere tydeligt, at hvert eksempel er illustrativt og ikke det forventede svar
* Acceptere input med flere felter paa en gang, hvis brugeren foretraekker det format, og derefter fortsaette fra naeste manglende felt
* Opsummere den faerdige intake tilbage til brugeren til validering, foer Aktivitet 1.1 begynder

### Input der kraeves fra brugeren

Brugeren boer levere:

* Kunde eller kontekst
* Problemomraade i scope
* Beslutning der skal understoettes
* Hvorfor dette er vigtigt nu
* Kendt evidens
* Involverede interessenter eller teams
* Kendte begraensninger
* Elementer uden for scope

### Anbefalet sekvens og formulering

1. `Trin 0, trin 1 af 4`
   Spoerg:
   * Hvem er kunden, eller hvilken kontekst skal jeg have med for dette projekt?
   * Hvilket problemomraade skal denne pakke holde fokus paa?
   Eksempel paa problemomraadesvar: Eksisterende kunder proever at aendre deres mobilabonnement online, men mange falder fra i trin med sammenligning af abonnementer og vurdering af berettigelse.
2. `Trin 0, trin 2 af 4`
   Spoerg:
   * Hvilken konkret beslutning vil du have denne pakke til at hjaelpe dig med at traeffe?
   * Hvorfor er det vigtigt at faa afklaret nu?
   Eksempel paa beslutningssvar: Skal kunden investere nu i at forbedre det selvbetjente trin til abonnementsskift, og hvis ja, hvad skal saa foerst videre til leverance?
   Eksempel paa hvorfor-nu-svar: Trinnet skaber unoedigt pres paa supporten, og kunden har brug for en naert forestaaende go/no-go- og scopebeslutning, foer leverancen starter.
3. `Trin 0, trin 3 af 4`
   Spoerg:
   * Hvilken evidens har du allerede i dag?
   * Hvilke interessenter eller teams skal vi holde i billedet fra start?
   Eksempel paa evidenssvar: Portal-analytics viser 42 % frafald i trin med sammenligning af abonnementer og berettigelse, iser paa mobil.
   Eksempel paa interessentsvar: Digital produktejer, callcenterleder, analytics-ejer og teamet bag change flowet.
4. `Trin 0, trin 4 af 4`
   Spoerg:
   * Hvilke vigtige graenser skal vi holde i mente, inklusive baade kendte begraensninger og det, der skal holdes uden for scope?
   Eksempel paa svar: Billing-platformen har et fast release-vindue og kan ikke udskiftes i denne release, og redesign af hele account-portalen skal blive uden for scope.

### Hvad AI'en skal goere

* Koere intake som en sekventiel guidet dialog, medmindre brugeren vaelger at indsaette hele intaken paa en gang
* Kontrollere om sprintet er afgraenset nok til Pakke A
* Identificere manglende intake-input
* Markere ukendte begraensninger som en risiko, hvis brugeren ikke har bekraeftet dem
* Bekraefte om arbejdet kan starte med Aktivitet 1.1

### Valideringsport

Gaa kun videre til Aktivitet 1.1, naar brugeren bekraefter, at intaken er god nok til at begynde.

## Aktivitetsspecifik tommelfingerregel

Brug de seed'ede inputfiler i projektmappen og skabelonbiblioteket som den operative struktur for hver aktivitet.

Hold rytmen saadan:

1. Gentag den viderefoerte kontekst kort
2. Indfang kun det minimum af nyt input, der er noedvendigt for aktiviteten
3. Syntetiser til et reviewklart output
4. Faa eksplicit validering
5. Gaa foerst derefter videre

For de konkrete step-baserede inputstrukturer, brug:

* [../../Projects/Templates/Danish/Package_A/package_a_template_library_danish.md](../../Projects/Templates/Danish/Package_A/package_a_template_library_danish.md)

## Regel for prototypesekvensen

Naar Aktivitet 3.1 er valideret:

* Skriv den strategiske hovedleverance i `package_a_final_deliverable.md`
* Skriv den operative prompt pack i `package_a_prototype_prompt_pack.md`
* Skriv det godkendte prototypeforloeb, links, screenshots og iterationsnoter i `package_a_prototype_record.md`
* Hold refinement-prompts adskilt fra fresh-generation prompts
* Hvis brugeren giver screenshots eller links til den eksisterende loesning, saa skal prompt packen eksplicit instruere om visuel alignment med kundens eksisterende design
