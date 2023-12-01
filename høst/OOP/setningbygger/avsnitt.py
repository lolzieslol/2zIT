from random import randint

import setningstrukturer as lagSetningMedStruktur

def genererAvsnitt(wordlist):
    avsnitt = ""
    
    #antall setninger i hvert avsnitt
    avsnittLengde = range(6,15)
    
    for setning in avsnittLengde:
        randomDecider = randint(1,5)
        match randomDecider:
            case 1:
                setningen = lagSetningMedStruktur.PVDAN(wordlist) 
            case 2:
                setningen = lagSetningMedStruktur.PVTS(wordlist)
            case 3:
                setningen = lagSetningMedStruktur.SEA(wordlist)
            case 4:
                setningen = lagSetningMedStruktur.SpVSu(wordlist)
            case 5:
                setningen = lagSetningMedStruktur.DVMASA(wordlist)
        
        setningen = setningen[0].upper() + setningen[1:]        
        avsnitt += setningen + " "
            
    return avsnitt