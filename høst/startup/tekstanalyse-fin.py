'''
Analyse av tekst

Trontalen 2018

Skriv et program som tar inn teksten under som én lang string-variabel. Utfør følgende analyse:

- Tell antall ord i teksten og print antallet ut til konsoll
- Tell antall setninger i teksten og print antallet ut til konsoll
- Beregn gjennomsnittlig antall ord i hver setning og print til konsoll
- Tell hvor mange ganger hver bokstav i alfabetet forekommer i teksten, og skriv en sortert liste som går fra høyest til lavest til konsoll.

Tips: mellomrom kan definere slutten av et ord, og punktum kan definere slutten av en setning.
'''
############################################################
############################################################
### Del 1 - ta imot inputtet###
##############################

#leser fil
filnavn = input("hvor er filen? (f.eks. mappe/navn.txt)")
inpfil = open(filnavn) #'startup/trontale.txt'
inptxt = inpfil.read()

############################################################
############################################################
### Del 2 - håndter inputtet ###
##############################

###
#antall ord i teksten 
antOrd = inptxt.count(' ')
#kunne tatt hensyn til dobbeltmellomrom

print(antOrd)

###
# antall setninger
antSetnin = inptxt.count('. ')
# tar ikke hensyn til evt dropping av dette på slutten av setningen. det kan evt fikses med split[-1] elrns

###
# gjennomsnittlig antall ord i hver setning

if antSetnin == 0:
    snittOrdSetnin = float(antOrd)
else:
    snittOrdSetnin = antOrd/antSetnin #feil her betyr ingen input
# ikke egentlig nødvendig

###
# hvor mange ganger hver bokstav i alfabetet forekommer i teksten
# -> skriv en sortert liste som går fra høyest til lavest til konsoll.
alfabet = "abcdefghijklmnopqrstuvwxyzæøå" #norskt

litenTXT = inptxt.lower()


abcTallListe = []
for i in alfabet:
    a = litenTXT.count(i)
    abcTallListe.append({'nbr':a, 'bokstav': i})

sortertLi = sorted(abcTallListe, key = lambda x: x['nbr'], reverse=True)
#sorterer listen etter antall, hvor det høyeste kommer først
    
############################################################
############################################################
### Del 3 - skriver ut resultatet ###
##############################

print(f"det er {antOrd} ord og {antSetnin} ", end="")
if antSetnin==1:
    print("setning. ", end="")
else:
    print("setninger. ", end="")

print(f"Hver setning har i gjennomsnittet {snittOrdSetnin:.3} ord.")
print("bokstaver rangert etter antall i teksten:")
for i in range(len(alfabet)):
    print(f"{i+1:2}. {sortertLi[i]['bokstav']}: ",sortertLi[i]['nbr'])
    # skriver plassnummer, bokstaven som er først etter rangeringen, og hvor mange det er av den
# kunne vært tydligere på hva tallene betyr kanskje?
############################################################
############################################################

