#match er lettlest og (alledgedly) raskt

import skoleinfo as skole
import skoleskriver as skriver
import skoledatabase as skdb
import random
import spm  

#intro
print("Dette programmet kan fortelle deg hvilke karakterer du må ha hatt hvis du gikk på studiespesialisering i Bergen")

#år
'''
feil = 0
year = spm.yearInpFun(0) #lar brukeren gjøre 5 feil før programmet gir opp
# year = int(input())

print(feil)
'''

year = spm.yearInpFun2()

#v3: som v1 men med en while i main

#kjører eller kjører ikke programmet
if year in skdb.skoleyrs: #sjekker om programmet kan kjøre
    skoleinp = input("hvilken bergensk videregående skole begynte du på da? Du kan bruke et vanlig kallenavn. ")
    # skoleinp = "katten"
    
    faktiskSkole = skole.navnNorm(skoleinp) #gjør navnet om til en brukbar form hvis det finnes, ellers sier det at det ikke finnes
    
    #henter karakter hvis skolen er gyldig
    if faktiskSkole != False:
        # karakter = skole.yearBasertKarakter(faktiskSkole,year)
        karakter = skole.skoleBasertKarakter(faktiskSkole,year)
        
    else:
        karakter = False
    skriver.info(skoleinp, faktiskSkole, year, karakter) #skriver ut det den kan og omformulerer etter hvilke data mangler
        
else:
    skriver.problem(year) #finner ut hva som er galt og kommuniserer dette

    


'''

    if tidspunkt > skdb.skoleyrs[-1]:
        print("dette er etter det siste året i databasen")
    elif tidspunkt < skdb.skoleyrs[0]:
        print("dette er før det første året i datasettet")
'''