# Pakke A gennemførelsesplan: Afklaringssprint

## Overblik

**Tidslinje:** 5 arbejdsdage  
**Fokus:** At træffe én nært forestående leverancebeslutning på et bedre grundlag og med mindre intern debat  
**Bruges bedst når:** Kunden skal beslutte, om og hvordan ét specifikt funktionsområde, én arbejdsgang eller ét trin i rejsen skal forbedres, før udviklingen starter

## Sådan bruger du dette dokument

Denne fil er opsummeringslaget for Pakke A.

Brug den til at forklare pakken, rækkefølgen af aktiviteterne, det estimerede tidsforbrug pr. aktivitet og de konkrete leverancer.

Til den detaljerede virkelige leverance bruges [Package_A_facilitator_guide_danish.md](Package_A_facilitator_guide_danish.md).

Til den trinvis styrede AI-proces bruges [Package_A_ai_process_danish.md](Package_A_ai_process_danish.md).

Til den genanvendelige promptstruktur, som bruges til at generere den klikbare prototype, bruges [prototype_prompt_pack_template_danish.md](prototype_prompt_pack_template_danish.md).

Ved reelle pakkeforløb skal der oprettes en dedikeret projektmappe under `../../Projects/<Project-Name>/`, før der produceres projektspecifikke artefakter. Brug strukturen i [../../Projects/README_danish.md](../../Projects/README_danish.md), og hold alle projektgenererede filer for forløbet inde i den mappe.

## Arbejdsmodel

Pakke A skal fortsat køres som en valideret sekvens. Hver aktivitet producerer et output, som bør reviewes, før næste aktivitet starter, så de senere anbefalinger bygger på bekræftet input frem for antagelser.

## Kerneaktiviteter

### Fase 1: Beslutning og evidensgrundlag (Dag 1-2)

* **Mål:** At skabe en hurtig og fælles forståelse af problemet og den beslutning, der skal træffes

#### Aktivitet 1.1: Sponsorworkshop og beslutningsramme

* **Estimeret aktivitetstid:** 90 minutter
* **Format:** Sponsorworkshop med 3-5 beslutningstagere
* **Deltagere:** Sponsor og relevante interessenter fra forretning, produkt, service eller leverance
* **Formål:** At definere forretningsspørgsmålet, målbrugerne, succeskriterierne og begrænsningerne for sprintet

#### Aktivitet 1.2: Gennemgang af evidensgrundlag

* **Estimeret aktivitetstid:** 2-4 timer afhængigt af kvaliteten og tilgængeligheden af evidens
* **Format:** Struktureret gennemgang af analytics, supporthenvendelser, input fra salg, tidligere research og anden relevant evidens
* **Deltagere:** Leveranceansvarlig eller strateg med adgang til ejere af evidens og relevante fageksperter
* **Formål:** At fastslå, hvad der allerede er kendt, hvad der stadig er antagelser, og hvilke spørgsmål sprintet fortsat skal besvare

#### Aktivitet 1.3: Kortlægningssession af trin i rejsen

* **Estimeret aktivitetstid:** 60-90 minutter
* **Format:** Kortlægning af den nuværende situation for det valgte trin i rejsen
* **Deltagere:** Relevante interessenter tæt på det valgte trin i rejsen, arbejdsgangen eller funktionsområdet
* **Formål:** At vise, hvor brugere eller medarbejdere mister tid, tryghed eller fremdrift i det valgte trin

### Fase 2: Sammenligning af retninger (Dag 3)

* **Mål:** At sammenligne løsningsretninger ud fra fælles kriterier og indsnævre anbefalingen til én foretrukken retning

#### Aktivitet 2.1: Gennemgang af løsningsmuligheder og foretrukken retning

* **Estimeret aktivitetstid:** 2 timer
* **Format:** Struktureret gennemgang af løsningsmuligheder med relevante interessenter
* **Deltagere:** Sponsor samt interessenter, der kan vurdere brugerværdi, forretningspåvirkning og leverancemæssig gennemførlighed
* **Formål:** At sammenligne 1-2 realistiske retninger mod aftalte kriterier for forretning, bruger og leverance

### Fase 3: Konceptudvikling og anbefaling (Dag 4-5)

* **Mål:** At omsætte afklaringsarbejdet til en praktisk retning, som kan bruges i planlægningen af leverancen

#### Aktivitet 3.1: Anbefalingspakke og konceptbrief

* **Estimeret aktivitetstid:** 4-8 timers syntese og paketering samt et reviewcheckpoint med sponsor på 30-45 minutter
* **Format:** Anbefalingsoplæg, enkel konceptvisning eller prototypebrief samt review med sponsor
* **Deltagere:** Leveranceansvarlig eller strateg, eventuelt designsupport og sponsor til den afsluttende gennemgang
* **Formål:** At omsætte den foretrukne retning til en praktisk anbefaling for næste leverancetrin

## Kundeinvolvering

* **Omfang:** Ca. 4-6 timer
* **Vigtigste handling:** Deltagelse fra sponsor og relevante interessenter i sponsorworkshop, kortlægningssession, gennemgang af løsningsmuligheder og reviewpunkter
* **Input der kræves:** Adgang til eksisterende evidens, interne fageksperter og rettidig feedback på outputtene

## Sådan bliver leverancerne produceret

* **Anbefalingsoplæg:** Bygges primært i Aktivitet 3.1 på baggrund af den validerede beslutningsramme, evidensgrundlaget, kortet over trin i rejsen og den foretrukne retning
* **Kort over trin i rejsen:** Produceres i Aktivitet 1.3 og forfines til den endelige leverance i Aktivitet 3.1
* **Klikbar prototype på 1-2 skærme:** Formes i Aktivitet 3.1 gennem et konceptbrief og en værktøjsklar prototype prompt pack og bygges derefter i det valgte designværktøj
* **Liste over risici og næste skridt:** Paketeres i Aktivitet 3.1 med udgangspunkt i de åbne antagelser, afhængigheder og implementeringskontroller, der er blevet synliggjort tidligere i sprintet

Prototype prompt packen er et understøttende artefakt og ikke en erstatning for den klikbare prototype. Dens rolle er at hjælpe med at generere en prototype, som afspejler de validerede beslutninger og læringer fra sprintet.

## Konkrete leverancer

1. **Et anbefalingsoplæg på 1-2 sider, som beskriver beslutningen, det anbefalede omfang, målbrugerne, succeskriterierne og det, der ikke bør bygges endnu:** Det giver sponsor et klart grundlag for en go eller no-go-beslutning og et strammere scope for næste leverancetrin.
2. **Et kort på én side over det valgte trin i rejsen, som viser de 3-5 største brud, der skaber forsinkelse, uklarhed eller intern merindsats:** Det synliggør, hvor brugere eller medarbejdere i dag mister tid, tryghed eller fremdrift.
3. **En enkel konceptvisning eller en klikbar prototype på 1-2 skærme, som illustrerer den anbefalede forbedring:** Det gør den anbefalede ændring konkret nok til review og tidlig planlægning af leverancen.
4. **En kort liste over risici og næste skridt, som dækker antagelser, afhængigheder og kontroller, der skal gennemføres før implementering:** Det viser, hvad der stadig skal løses, før arbejdet kan gå i build.
