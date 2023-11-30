from random import randint

import ordsortering as sorter
import ordklasse as ok

def erPronomenetSubjekt(wordlist,pronomen): #passer på at pronomenet er subjekt/nominativ
        if pronomen.__class__ != ok.DetPersonligePronomenet:
            # ordklasse, formen = pronomen.__class__.ordklassenavn()
            # print(f"{pronomen()} er {ordklasse} og  ikke et personlig pronomen")
            return pronomen
        
        if pronomen.form == "nominativ":
            # print(f"{pronomen()} er subjektform")
            return pronomen   
        
        '''
        print(f"{pronomen()} er {pronomen.form} og ikke subjektform")
        
        print("kjører for", pronomen())
        '''
        
        feil = 0
        while pronomen.form != "nominativ":
            pronomen = sorter.tilfeldigIBestemtOrdKlasse(wordlist, ok.Pronomenet)
            feil +=1
            if feil>=5:
                print("oops'", pronomen(),"'funker ikke")
                return ok.Pronomenet("hen")
        
        return pronomen

def PVDAN(wordlist): #pronoun verb [det/den] adjective noun
    
    #henter tilfeldig ord til setningen
    pronomen = sorter.tilfeldigIBestemtOrdKlasse(wordlist, ok.DetPersonligePronomenet)
    pronomen = erPronomenetSubjekt(wordlist, pronomen)
    verb = sorter.tilfeldigIBestemtOrdKlasse(wordlist, ok.Verbet)
    substantiv = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.Substantivet)
    adjektiv = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.Adjektivet)
    
    #den eller det
    if substantiv.wordgender == "intetkjønn":
        detDen = "det"
    else:
        detDen = "den"
    
    #bøyer adjektiv
    plAdjektiv = adjektiv.flertall()
        
    setning = f"{pronomen()} {verb()} {detDen} {plAdjektiv} {substantiv()}"
    return setning
    
    
    
def PVTS(wordlist : list): #pronomen verb (antall) substantiv'''
    pronomen = sorter.tilfeldigIBestemtOrdKlasse(wordlist, ok.DetPersonligePronomenet)
    pronomen = erPronomenetSubjekt(wordlist, pronomen)
    
    verb = sorter.tilfeldigIBestemtOrdKlasse(wordlist, ok.Verbet)
    
    substantiv = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.Substantivet)
    plsubstantiv = substantiv.flertallUbestemt()
    
    tall = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.Mengdeordet)
    
    
    setning = f"{pronomen()} {verb()} {tall()} {plsubstantiv}"
    return setning
    
#jeg spiser et eple

def SEA(wordlist : list): #pronomen/substantiv (subjekt) "er" adjektiv
    
    
    er = ok.Verbet("er","presens")
    adjektivObjekt = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.Adjektivet)
    adjektivString = adjektivObjekt()
    randomDecider = randint(1,2)
    
    match randomDecider:
        case 1:
            subjektObjekt = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.DetPersonligePronomenet) 
            subjektObjekt = erPronomenetSubjekt(wordlist, subjektObjekt)
            
            if subjektObjekt.enFlerTall == "flertall":
                adjektivString = adjektivObjekt.flertall()
            
            subjektString = subjektObjekt()
            
        case 2:
            subjektObjekt = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.Substantivet)
            subjektString = subjektObjekt.entallBestemt()
    
    setning = f"{subjektString} {er()} {adjektivString}"
    return setning
    