# Skabelon til prototype prompt pack

## Formaal

Brug denne skabelon til at omsaette validerede pakkeoutput til en prompt pack, der kan bruges i vaerktoejer som Figma Make eller Google Stitch.

Dette er et produktionsstoettende artefakt. Det hjaelper med at generere en prototype, som afspejler beslutningerne, begraensningerne og laeringerne fra pakken. Det erstatter ikke anbefalingen, kortlaegningen, roadmapet eller andre kerneleverancer.

## Saadan bruger du skabelonen

Udfyld foerst det kanoniske prototypebrief.

Tilpas derefter briefet til:

* En fresh-generation Figma Make-prompt
* En refinement Figma Make-prompt
* En fresh-generation Google Stitch-prompt
* En refinement Google Stitch-prompt

Brug til sidst reviewtjeklisten og prototyperegistreringen til at vurdere, om den genererede prototype stadig matcher de validerede pakkeoutput, og om det godkendte artefakt er dokumenteret rent.

## Kanonisk prototypebrief

```md
# Kanonisk prototypebrief

## Pakke
[Pakke A / Pakke B / Pakke C]

## Formaal med prototypen
[Hvorfor denne prototype skal eksistere, og hvilken beslutning eller review den skal understoette]

## Beslutning prototypen skal understoette
[Tekst]

## Brugere i fokus
* [Gruppe]
* [Gruppe]

## Rejse eller flow i scope
[Afgraenset flow, trin eller udvalgt hoejrisiko-udsnit af rejsen]

## Hvad prototypen skal vise
* [Skaerm, trin eller moment]
* [Skaerm, trin eller moment]
* [Skaerm, trin eller moment]

## Hvilke beslutninger eller laeringer der skal afspejles
* [Beslutning eller laering]
* [Beslutning eller laering]
* [Beslutning eller laering]

## Hvad prototypen skal hjaelpe med at validere
* [Spoergsmaal]
* [Spoergsmaal]

## Prioriteter for indhold
* [Prioritet]
* [Prioritet]

## Interaktionsnoter
* [Interaktionsnote]
* [Interaktionsnote]

## Begraensninger der skal respekteres
* [Begraensning]
* [Begraensning]

## Eksisterende visuelle referencer hvis de findes
* [Screenshot, URL eller note]
* [Screenshot, URL eller note]

## Instruktion om visuel alignment
[Hvis der findes visuelle referencer, skal prototypen holdes aligned med kundens eksisterende visuelle design, medmindre en bevidst visuel aendring er en del af briefet]

## Hvad der skal undgaas
* [Element]
* [Element]

## Tone eller brandsignaler
* [Signal]
* [Signal]

## Forventning til device eller layout
[Desktop / mobil / responsivt / specifikt devicefokus]

## Forventning til output
[For eksempel: 1-2 klikbare skaerme, kun kerneflow, low fidelity, mid fidelity]
```

## Figma Make fresh-generation prompt

```md
Lav en klikbar prototype paa baggrund af foelgende validerede brief.

Vigtigt: behandl instruktionerne nedenfor som produktionsvejledning og ikke som synlig UI-tekst. Render ikke intern rationale, prototype-labels eller forklarende strategitekst i interfacet, medmindre briefet eksplicit beder om det indhold.

Maal:
[Formaal med prototypen]

Beslutning denne prototype skal understoette:
[Beslutning]

Brugere i fokus:
* [Gruppe]
* [Gruppe]

Flow i scope:
[Flow eller udsnit af rejse]

Skab:
* [Skaerm eller moment]
* [Skaerm eller moment]
* [Skaerm eller moment]

Prototypen skal afspejle disse validerede beslutninger og laeringer:
* [Beslutning eller laering]
* [Beslutning eller laering]
* [Beslutning eller laering]

Prototypen skal hjaelpe med at validere:
* [Spoergsmaal]
* [Spoergsmaal]

Prioriteter for indhold:
* [Prioritet]
* [Prioritet]

Interaktionsnoter:
* [Interaktionsnote]
* [Interaktionsnote]

Begraensninger der skal respekteres:
* [Begraensning]
* [Begraensning]

Eksisterende visuelle referencer hvis de findes:
* [Screenshot, URL eller note]
* [Screenshot, URL eller note]

Instruktion om visuel alignment:
[Tekst]

Undgaa:
* [Element]
* [Element]

Tone og brandsignaler:
* [Signal]
* [Signal]

Forventning til device eller layout:
[Tekst]

Forventning til output:
[Tekst]
```

## Figma Make refinement prompt

```md
Brug dette som en opfoelgende refinement-prompt til den prototype, der allerede er genereret.

Vigtigt:
* Start ikke forfra med et nyt koncept, medmindre briefet eksplicit siger, at den forrige retning blev afvist.
* Behold den nuvaerende genererede prototype som base og lav kun maalrettede refinements.
* Behandl alt nedenfor som skjult produktionsvejledning og ikke som synlig UI-tekst.
* Render ikke intern rationale, prototype-labels eller forklarende strategitekst i interfacet, medmindre briefet eksplicit beder om det indhold.

Brug disse referencer sammen:
* De oprindelige visuelle referencer eller screenshots fra kunden
* Den nuvaerende genererede prototype, som nu skal raffineres

Maal:
[Hvad der skal forbedres i naeste iteration uden at skifte det overordnede koncept]

Behold disse dele fra det nuvaerende draft:
* [Det der allerede virker]
* [Det der allerede virker]

Aendr disse ting i det nuvaerende draft:
1. [Korrektion]
* [Specifik refinement]
* [Specifik refinement]
2. [Korrektion]
* [Specifik refinement]
* [Specifik refinement]

Raffiner disse eksisterende skaerme eller momenter:
* [Skaerm eller moment]
* [Skaerm eller moment]

Interaktionsforventninger:
* [Interaktionsnote]
* [Interaktionsnote]

Begraensninger der skal respekteres:
* [Begraensning]
* [Begraensning]

Synlig UI-tekst skal fortsat vaere:
* kortfattet
* produktnaer
* aligned med sproget og tonen i briefet

Undgaa:
* [Element]
* [Element]

Output:
* en opdateret version af den nuvaerende prototype
* [Hvad der skal vaere tydeligere eller bedre efter refinement]
* [Hvilken visuel eller interaktionsmaessig kvalitet der nu skal vaere bedre aligned]
```

## Google Stitch fresh-generation prompt

```md
Design en prototype, der udtrykker den foelgende validerede produkt- eller serviceretning.

Vigtigt: behandl instruktionerne nedenfor som produktionsvejledning og ikke som synlig UI-tekst. Render ikke intern rationale, prototype-labels eller forklarende strategitekst i interfacet, medmindre briefet eksplicit beder om det indhold.

Formaal med prototypen:
[Formaal med prototypen]

Beslutning denne prototype skal understoette:
[Beslutning]

Primaere brugere:
* [Gruppe]
* [Gruppe]

Flow eller udsnit af rejse i scope:
[Tekst]

Vis disse centrale momenter:
* [Skaerm eller moment]
* [Skaerm eller moment]
* [Skaerm eller moment]

Byg prototypen, saa den afspejler disse aftalte beslutninger og laeringer:
* [Beslutning eller laering]
* [Beslutning eller laering]
* [Beslutning eller laering]

Brug prototypen til at hjaelpe med at validere:
* [Spoergsmaal]
* [Spoergsmaal]

Prioriteter for indhold:
* [Prioritet]
* [Prioritet]

Interaktionsnoter:
* [Interaktionsnote]
* [Interaktionsnote]

Begraensninger:
* [Begraensning]
* [Begraensning]

Eksisterende visuelle referencer hvis de findes:
* [Screenshot, URL eller note]
* [Screenshot, URL eller note]

Instruktion om visuel alignment:
[Tekst]

Medtag ikke:
* [Element]
* [Element]

Tone eller brandsignaler:
* [Signal]
* [Signal]

Forventning til layout eller device:
[Tekst]

Forventning til output:
[Tekst]
```

## Google Stitch refinement prompt

```md
Brug dette som en opfoelgende refinement-prompt til den prototype, der allerede er genereret.

Vigtigt:
* Start ikke forfra med et nyt koncept, medmindre briefet eksplicit siger, at den forrige retning blev afvist.
* Behold den nuvaerende genererede prototype som base og lav kun maalrettede refinements.
* Behandl alt nedenfor som skjult produktionsvejledning og ikke som synlig UI-tekst.
* Render ikke intern rationale, prototype-labels eller forklarende strategitekst i interfacet, medmindre briefet eksplicit beder om det indhold.

Brug disse referencer sammen:
* De oprindelige visuelle referencer eller screenshots fra kunden
* Den nuvaerende genererede prototype, som nu skal raffineres

Maal:
[Hvad der skal forbedres i naeste iteration uden at skifte det overordnede koncept]

Behold disse dele fra det nuvaerende draft:
* [Det der allerede virker]
* [Det der allerede virker]

Aendr disse ting i det nuvaerende draft:
1. [Korrektion]
* [Specifik refinement]
* [Specifik refinement]
2. [Korrektion]
* [Specifik refinement]
* [Specifik refinement]

Raffiner disse eksisterende skaerme eller momenter:
* [Skaerm eller moment]
* [Skaerm eller moment]

Interaktionsforventninger:
* [Interaktionsnote]
* [Interaktionsnote]

Begraensninger der skal respekteres:
* [Begraensning]
* [Begraensning]

Synlig UI-tekst skal fortsat vaere:
* kortfattet
* produktnaer
* aligned med sproget og tonen i briefet

Undgaa:
* [Element]
* [Element]

Output:
* en opdateret version af den nuvaerende prototype
* [Hvad der skal vaere tydeligere eller bedre efter refinement]
* [Hvilken visuel eller interaktionsmaessig kvalitet der nu skal vaere bedre aligned]
```

## Reviewtjekliste for prototype

```md
# Reviewtjekliste for prototype

## Matcher prototypen den validerede retning?
[Ja / Delvist / Nej]

## Understoetter den den beslutning, den skulle understoette?
[Ja / Delvist / Nej]

## Er scope holdt stramt nok?
[Ja / Delvist / Nej]

## Matcher den eksisterende visuelle referencer, hvis de blev givet?
[Ja / Delvist / Nej / Ikke relevant]

## Er der kommet generisk AI-udtryk eller strategitekst ind i interfacet?
[Ja / Nej]

## Hvad fungerer godt?
* [Punkt]
* [Punkt]

## Hvad skal raffineres?
* [Punkt]
* [Punkt]

## Godkendelsesstatus
[Draft / Ready for review / Approved]
```

## Skabelon til prototyperegistrering

```md
# Prototyperegistrering

## Vaerktoej brugt
[Figma Make / Google Stitch / andet]

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
