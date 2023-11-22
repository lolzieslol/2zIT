import ordsortering as sorter
import ordklasse as ok

def PVDAN(wordlist): #pronoun verb [det/den] adjective noun
    
    def erSubjektPronomen(pronomen): #passer på at pronomenet er subjekt/nominativ
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
    
    #henter tilfeldig ord til setningen
    pronomen = sorter.tilfeldigIBestemtOrdKlasse(wordlist, ok.Pronomenet)
    pronomen = erSubjektPronomen(pronomen)
    verb = sorter.tilfeldigIBestemtOrdKlasse(wordlist, ok.Verbet)
    substantiv = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.Substantivet)
    adjektiv = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.Adjektivet)
    
    #den eller det
    if substantiv.gender == "intetkjønn":
        detDen = "det"
    else:
        detDen = "den"
    
    #bøyer adjektiv
    if adjektiv()[-2:] == "el":
        plAdjektiv = adjektiv() + "le"
        # print("adjektiv",adjektiv(),"+le")
    elif adjektiv()[-1] != "e":
        plAdjektiv = adjektiv() + "e"
        # print(adjektiv(),"+e")
    else:
        plAdjektiv = adjektiv()
        ''' 
    elif adjektiv() == "moderne" or adjektiv() =="spennende":
        plAdjektiv = adjektiv()
    else: #usikker på regelen brukt her TODO: finne ut hva greien er
        adjektiv = adjektiv() + "t"
        adjektiv = ok.Adjektivet(adjektiv)
        plAdjektiv = adjektiv()
        '''
        
    setning = f"{pronomen()} {verb()} {detDen} {plAdjektiv} {substantiv()}"
    return setning
    
    
    
def PVTS(wordlist : list): #pronomen verb (antall) substantiv'''
    pronomen = sorter.tilfeldigIBestemtOrdKlasse(wordlist, ok.Pronomenet)
    verb = sorter.tilfeldigIBestemtOrdKlasse(wordlist, ok.Verbet)
    substantiv = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.Substantivet)
    tall = sorter.tilfeldigIBestemtOrdKlasse(wordlist,ok.Tallordet)
    
    vokal : list = ["a","e","i","o","u","y","æ","ø","å"]
    if substantiv()[-1] in vokal:
        # print(substantiv())
        substantiv = substantiv()[:-1]
        plsubstantiv = substantiv + "er"
    else:
        plsubstantiv = substantiv() + "er"
    
    setning = f"{pronomen()} {verb()} {tall()}  {plsubstantiv}"
    return setning
    
#jeg spiser et eple