from random import randint
#
import ordklasse as ok
    
######


def tilfeldigPronomen(wordList):
    randomWord = ""    
    while randomWord.__class__ != ok.DetPersonligePronomenet:
        myint =randint(0,len(wordList)-1)
        
        randomWord = wordList[myint]

    print(f"ditt tilfeldige pronomen er '{randomWord()}'")
    
# tilfeldigPronomen(ordliste)

def tilfeldigOrdIBestemtOrdKlasse(wordList,ordklasse):
    randomWord = ""    
    while not issubclass(type(randomWord), ordklasse):
        myint =randint(0,len(wordList)-1)
        
        randomWord = wordList[myint]
    # ordklassen, wordgender = ordklasse.ordklassenavn() 
    # print(f'ditt tilfeldige ord i klassen {ordklassen} er "{randomWord()}"')
    return randomWord



# tilfeldigIBestemtOrdKlasse(ordliste, ok.Verbet) #WIP



def passPåAtPronomenetErSubjekt(wordlist,pronomenObjekt): #passer på at pronomenet er subjekt/nominativ
        if pronomenObjekt.__class__ != ok.DetPersonligePronomenet:
            # ordklasse, formen = pronomen.__class__.ordklassenavn()
            # print(f"{pronomen()} er {ordklasse} og  ikke et personlig pronomen")
            return pronomenObjekt
        
        if pronomenObjekt.form == "nominativ":
            # print(f"{pronomen()} er subjektform")
            return pronomenObjekt   
        
        '''
        print(f"{pronomenObjekt()} er {pronomenObjekt.form} og ikke subjektform")
        
        print("kjører for", pronomenObjekt())
        '''
        
        feil = 0
        while pronomenObjekt.form != "nominativ":
            pronomenObjekt = tilfeldigOrdIBestemtOrdKlasse(wordlist, ok.Pronomenet)
            feil +=1
            if feil>=5:
                print("oops'", pronomenObjekt(),"'funker ikke")
                return ok.Pronomenet("hen")
        
        return pronomenObjekt

def ErOrdeneIKlasse(wordlist : list,klasse : str): #klasse med stor bokstav
    # print(str(klasse))
    
    AntallOrdIKlassen = 0
    for ordet in wordlist:
        # if ordet.erIKlasse:
        #     print(f'ordet "{ordet}" er {klasse}')
        if (issubclass(type(ordet), klasse)):
            klassenavn, wordgender = klasse.ordklassenavn()
            match wordgender:
                case "intetkjønn":
                    enEtEi = "et"
                case "hankjønn":
                    enEtEi = "en"
                case "hunkjønn":
                    enEtEi = "ei"
                case _:
                    enEtEi = ""
            print(f'ordet "{ordet()}" er {enEtEi} {klassenavn}')
                
            AntallOrdIKlassen +=1
        
    if AntallOrdIKlassen == 0:
        print("ingen av ordene var i klassen")            

def tilfeldigSubjektOrd(wordlist : list):
    randomDecider = randint(1,2)
    
    match randomDecider:
        case 1:
            subjektObjekt = tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.DetPersonligePronomenet) 
            subjektObjekt = passPåAtPronomenetErSubjekt(wordlist, subjektObjekt)
            
        case 2:
            subjektObjekt = tilfeldigOrdIBestemtOrdKlasse(wordlist,ok.Substantivet)
    
    return subjektObjekt 

# TODO: miljø er fornybar
