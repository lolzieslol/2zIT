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

#input -> analyse -> resultat

############################################################
############################################################
### Del 1 - ta imot inputtet###
##############################

# innledning her
print("hei, dette programmet skal: ")
print("- Telle antall ord i teksten")
print("- Beregne gjennomsnittlig antall ord i hver setning")
print("- Tell hvor mange ganger hver bokstav i alfabetet forekommer i teksten, og skrive en sortert liste som går fra høyest til lavest")

#input
inptxt = str(input("skriv: "))

############################################################
############################################################
### Del 2 - håndter inputtet ###
##############################

#TODO: gi feilmeldinger

###
#antall ord i teksten 
antOrd = inptxt.count(' ')

###
#antall setninger
antSetnin = inptxt.count('. ')
## tar ikke hensyn til evt dropping av dette på slutten av setningen. det kan evt fikses med split[-1] elrns

###
# gjennomsnittlig antall ord i hver setning
snittOrdSetnin = antOrd/antSetnin

###
# hvor mange ganger hver bokstav i alfabetet forekommer i teksten
# -> skriv en sortert liste som går fra høyest til lavest til konsoll.
alfabet = "abcdefghijklmnopqrstuvwxyzæøå" #norskt

litenTXT = inptxt.lower()


abcTallListe = []
for i in alfabet:
    a = litenTXT.count(i)
    abcTallListe.append({i: a})

sortertLi = abcTallListe #sorter her
'''
abcTallDict = {}
for i in alfabet:
    a = litenTXT.count(i)
    abcTallDict[i] = a


sortertLi = abcTallDict.sort()
'''
'''
abcTall = []
abcABC = []
for i in alfabet:
    abcTall.append(litenTXT.count(i))
    abcABC.append(i)


sortertLi = []
'''

    
############################################################
############################################################
### Del 3 - skriver ut resultatet ###
##############################

##bruker engelsk format, TO DO: evt fikse det (eller bytte språket på strengen)
print(f"det er {antOrd} ord og {antSetnin} setninger. Hver setning har i gjennomsnittet {snittOrdSetnin:3} ord.")
print(f"hvor mange av hver bokstav: {sortertLi}")
#TODO: formatter listen


############################################################
############################################################