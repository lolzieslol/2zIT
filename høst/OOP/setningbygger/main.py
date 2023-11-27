'''
program som bygger setninger.
- for norsk, funker IKKE i alle språk 

'''
from random import randint

import ordklasse as ok 
import ordene as ordobjekt
import setningstrukturer as lagSetningMedStruktur
from ordsortering import tilfeldigIBestemtOrdKlasse

def genererAvsnitt(wordlist):
    avsnitt = ""
    
    #antall setninger i hvert avsnitt
    avsnittLengde = range(6,15)
    
    for setning in avsnittLengde:
        randomDecider = randint(1,3)
        match randomDecider:
            case 1:
                setningen = lagSetningMedStruktur.PVDAN(wordlist) 
            case 2:
                setningen = lagSetningMedStruktur.PVTS(wordlist)
            case 3:
                setningen = lagSetningMedStruktur.SEA(wordlist)
        
        setningen = setningen[0].upper() + setningen[1:]        
        avsnitt += setningen + ". "
            
    return avsnitt

print(genererAvsnitt(ordobjekt.setningOrientertOrdlisteForståelig))

# print(lagSetningMedStruktur.PEA(ordobjekt.setningOrientertOrdlisteForståelig))
'''
i =0
while i<10:
    lagSetningMedStruktur.PVTS(ordobjekt.setningOrientertOrdlisteForståelig)
    i +=1


i =0
while i<10:
    lagSetningMedStruktur.PVDAN(ordobjekt.setningOrientertOrdlisteForståelig)
    i +=1
''' 
# print(ok.DetPersonligePronomenet.ordklassenavn()())
# print(f"{ordet()} er {ordet.__class__.ordklassenavn()()}")
