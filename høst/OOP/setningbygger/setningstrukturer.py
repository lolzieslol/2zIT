from random import randint

import ordhenting as hent
import ordklasse as ok

def PVDAN(wordlist): #pronoun verb [det/den] adjective noun
    
    #henter tilfeldig ord til setningen
    pronomenObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist, ok.DetPersonligePronomenet)
    pronomenObjekt = hent.passPåAtPronomenetErSubjekt(wordlist, pronomenObjekt)
    verbObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist, ok.Verbet)
    substantivObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Substantivet)
    adjektivObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Adjektivet)
    
    #den eller det
    if substantivObjekt.wordgender == "intetkjønn":
        detDenString = "det"
    else:
        detDenString = "den"
    
    #bøyer adjektiv
    plAdjektivObjekt = adjektivObjekt.flertall()
        
    setning = f"{pronomenObjekt()} {verbObjekt()} {detDenString} {plAdjektivObjekt()} {substantivObjekt()}."
    return setning
    
    
    
def PVTS(wordlist : list): #pronomen verb (antall) substantiv'''
    pronomenObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist, ok.DetPersonligePronomenet)
    pronomenObjekt = hent.passPåAtPronomenetErSubjekt(wordlist, pronomenObjekt)
    
    verbObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist, ok.Verbet)
    
    substantivObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Substantivet)
    plsubstantivString = substantivObjekt.ubestemtFlertall
    
    mengdeObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Mengdeordet)
    
    
    setning = f"{pronomenObjekt()} {verbObjekt()} {mengdeObjekt()} {plsubstantivString}."
    return setning
    
#jeg spiser et eple

def SEA(wordlist : list): #pronomen/substantiv (subjekt) "er" adjektiv
    er = ok.Verbet("er")
    adjektivObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Adjektivet)
    
    # adjektivString = adjektivObjekt.bøydEtterSubstantiv()
    adjektivString = adjektivObjekt()
    substantivObjekt = hent.tilfeldigSubjektOrd(wordlist)
    # 
            # if subjektObjekt.enFlerTall == "flertall":
            #     adjektivString = adjektivObjekt.flertall()
    
    setning = f"{substantivObjekt()} {er()} {adjektivString}."
    return setning
    
def SpVSu(wordlist : list): #spørrepronomen verb substantiv (SVO/OVS)
    spørrepronomenObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.SpørrePronomenet)
    verbObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Verbet)
    substantivObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Substantivet)
    
    setning = f"{spørrepronomenObjekt()} {verbObjekt()} {substantivObjekt()}?"
    return setning

def DVMASA(wordlist : list): # Det/den verb mengdeord adjektiv substantiv adverb 
    verbObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Verbet)
    mengdeordObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Mengdeordet)
    adjektivObjekt =  hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Adjektivet)
    substantivObjekt = hent.tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Substantivet)
    adverbObjekt =  hent.tilfeldigOrdIBestemtOrdKlasse(wordlist, ok.Adverbet)
    
    adjektivObjekt = adjektivObjekt.flertall()
    
    # substantivObjekt = hent.tilfeldigSubjektOrd(wordlist)

    enFlerTall = substantivObjekt.tallTilform(mengdeordObjekt)
    if enFlerTall != "entall":
        substantivString = substantivObjekt.ubestemtFlertall
    else:
        substantivString = substantivObjekt()
        
    
    # adverbObjekt.bøydEtterSubstantiv(substantivObjekt)
    
    setning = f"{substantivObjekt()} {verbObjekt()} {mengdeordObjekt()} {adjektivObjekt()} {substantivString} {adverbObjekt()}."
    return setning
