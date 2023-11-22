'''
program som bygger setninger.
- for norsk, funker IKKE i alle språk 

'''
from random import randint

import ordklasse as ok
import ordene as ordobjekt
import setningstrukturer as setningen
from ordsortering import tilfeldigIBestemtOrdKlasse

def genererAvsnitt(wordlist):
    avsnitt = ""
    
    #antall setninger i hvert avsnitt
    avsnittLengde = range(1,10)
    #antall ord i hver setning 
    setningslengde = range(1,7)
    
    for setning in avsnittLengde:
        setninger = setningen.PVDAN(wordlist) 
        avsnitt += setninger + ". "
            
    return avsnitt

print(genererAvsnitt(ordobjekt.setningOrientertOrdlisteForståelig))
'''
i =0
while i<10:
    setningen.PVTS(ordobjekt.setningOrientertOrdlisteForståelig)
    i +=1


i =0
while i<10:
    setningen.PVDAN(ordobjekt.setningOrientertOrdlisteForståelig)
    i +=1
''' 
# print(ok.DetPersonligePronomenet.ordklassenavn()())
# print(f"{ordet()} er {ordet.__class__.ordklassenavn()()}")
