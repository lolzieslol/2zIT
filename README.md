# Skolearbeid i programfaget IT 2
Dette er en samling av det jeg lærer i IT 2. Hittil har jeg bl.a. gått gjennom kapittel 1 og 2 fra aunivers. (27. september 2023)

## Bibliotek som har blitt brukt:
- random (se: høst -> kap1 -> 1c, høst -> OOP -> setningsbygger)
- pygame (se: vinter -> kap4 (alt der))
## Jeg har tatt i bruk eller notert ned:
### Generelt
- input
- tekstbehandling
### Løkker og sånt
- while-løkker
- for-løkker
- if-setninger 
- match-setninger 
- funksjoner
### Klasser
- klasser (se: høst -> kap2 (alt der), høst -> OOP (alt der), vinter -> kap4 -> ballanimation)
- subklasser/underklasser
- innebygde metoder for klasser (se: setningsbygger)

### Lister og slikt
- lister
- dictionaries
- tabeller
- tupler

### Annet
- assert
- lese fra:
-- JSON
-- CSV
-- TXT
## Andre ferdigheter
- linket egne program med import
- navngiving av variabler
- gitignore
## Programeringsparadigmer
- Object-oriented programming (OOP)
- funksjonell
## Større Prosjekt:
### Poenggrense 
Dette prosjektet, som i filene heter "poenggrenseinfo", spør når du begynte på vgs og hvilken vgs og gir poenggrensen. Det funker for spesefikke videregående skoler.

Karakterprosjektet bruker input, funksjoner, tekstbehandling, if-setninger, match-setninger, try (kun i gammel versjon), tabeller, lister, dictionaries (kan bygges videre på), linking/importering av egne program

### Setnings- og avsnittsbygger
Dette prosjektet, som i filene heter 'setningsbygger', kan lage setninger basert på ord og setningsstruktur. Ordene er i et ordklassesystem, som er definert med klasser (der hver klasse representerer en ordklasse). Setningsstrukturene er implementert som funksjoner som lager en setning og returner den. De får tak i ordene ved hjelp av "ordhenting" filens "tilfeldigOrdIBestemtOrdKlasse" funksjon, som gjør akkurat det det høres ut som den gjør, henter et tilfeldig ord i en bestemt ordklasse. 'avsnitt' programmet lager et avsnitt med setninger i forskjellige setningsstrukturer.

ordklassene som er implementert er som følger: Ordet (overklassen for alle), Verbet, Determinativet, Mengdeordet (determinativ underklasse), Pronomenet, DetPersonligePronomenet (pronomen underklasse), DetRelativePronomenet (pronomen underklasse), SpørrePronomenet (pronomen underklasse), Biordet (beskriver adjektiv og adverb, men er ikke helt en klasse), Adjektivet (biord underklasse), Adverbet, Konjunksjonen, Subjunksjonen (konjunksjon underklasse), Interjeksjonen, Preposisjonen, Substantivet. Alle klassene har metodene definisjon (som gir deg en skriftlig definisjon av ordklassen, vanligvis fra NAOB), ordklassenavn (som gir det et ordklasseKlasseNavn-objekt med navnet til klassen (f.eks "verb") og det gramatiske kjønnet (slik som substantivklassen gjør)). Alle klassene har også "__call__"-metoden som lar deg kalle det ved å skrive ordet med () bak for å få ut "ordnavnet", altså selve ordet. Bøyning av ord er, hvor relevant, metoder til ordklassen.

Setningsstrukturene er som følger: PVDAN (pronoun verb det/den adjektiv noun), PVTS (pronomen, verb, tallord (mengdeord), substantiv), SEA (subjekt/substantiv/pronomen, "er, adjektiv), SpVSu (spørrepronomen, verb, substantiv), DVMASA (det/den, verb, mengdeord, adjektiv, substantiv, adverb).

programmet bruker: klasser (overklasser, underklasser), funksjoner, tekstbehandling, match-setninger, if-setninger, while, lister, linking/importering av egne program (det er delt over 6 filer), f-string, ranint (fra biblioteket random), print

### påbegynt/tidlig i prosessen:
Det er ikke garantert at jeg kommer til å fortsette på noen av disse
- fraværsgrensespill
- fileditor

## Mindre prosjekt
- oppgave: tekstanalyse fra txt-fil (startup -> tekstanalyse-fin)
- eksempel fra bok: værdatahenting fra dictionary (1e)
- eksempel fra bok: planet klasser (2a planet)
- eksempel fra bok: bilett klasser (2a bilett)
- eksempel fra bok: graftegning (kap3 -> graftegning)
- egen ide: generere nonsense tekst (bstekst) 
- eksempel fra bok: pygame baller som beveger seg m/fullstendig elastisk støt (ballanimation)
