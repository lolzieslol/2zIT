#match er lettlest og (alledgedly) raskt

import skoleinfo as skole
import skoleskriver as skut
import skoledatabase as skdb

#intro
print("Dette programmet kan fortelle deg hvilke karakterer du må ha hatt hvis du gikk på studiespesialisering i Bergen")

#år
year = int(input("i hvilket år startet du på videregående? (YYYY) ")) 

    
#kjører eller kjører ikke programmet
if year in skdb.skoleyrs: #sjekker om programmet kan kjøre
    skoleinp = input("hvilken bergensk videregående skole begynte du på da? ")
    faktiskSkole, skoleyear = skole.info(skoleinp,year) #kjører hovedprogrammet
        
    skut.skriver(skoleinp, faktiskSkole, skoleyear) #finner også karakter
        
else:
    print("beklager, kan ikke si noe om dette. ", end="")
    if year > skdb.skoleyrs[-1]:
        print("Det er etter det siste året i databasen")
    elif year < skdb.skoleyrs[0]:
        print("Det er før det første året i databasen")

    


'''

    if tidspunkt > skdb.skoleyrs[-1]:
        print("dette er etter det siste året i databasen")
    elif tidspunkt < skdb.skoleyrs[0]:
        print("dette er før det første året i datasettet")
'''