'''
program som bygger setninger.
- for norsk, funker IKKE i alle språk 

'''
from random import randint

# from ordklasse import *
import ordklasse as o
from ordene import *

''' #test
#skriver ut
print(jeg(), er(), jeg.form)

if jeg() == deg():
    print("hæ")
else: 
    print(jeg(),er(),ikke(), deg())
'''
    
######
def tilfeldigPronomen(wordList):
    randomWord = ""    
    while randomWord.__class__ != o.DetPersonligePronomenet:
        myint =randint(0,len(wordList)-1)
        
        randomWord = wordList[myint]

    print(f"ditt tilfeldige pronomen er '{randomWord()}'")
    
# tilfeldigPronomen(ordliste)

def tilfeldigIBestemtOrdKlasse(wordList,ordklasse):
    randomWord = ""    
    while not issubclass(type(randomWord), ordklasse):
        myint =randint(0,len(wordList)-1)
        
        randomWord = wordList[myint]
    # ordklassen, nounClass = ordklasse.ordklassenavn() 
    # print(f'ditt tilfeldige ord i klassen {ordklassen} er "{randomWord()}"')
    return randomWord



# tilfeldigIBestemtOrdKlasse(ordliste, o.Verbet) #WIP

def ErOrdeneIKlasse(ordlist : list,klasse : str): #klasse med stor bokstav
    # print(str(klasse))
    
    AntallOrdIKlassen = 0
    for ordet in ordlist:
        # if ordet.erIKlasse:
        #     print(f'ordet "{ordet}" er {klasse}')
        if (issubclass(type(ordet), klasse)):
            klassenavn, nounClass = klasse.ordklassenavn()
            match nounClass:
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
#

# ErOrdeneIKlasse(ordliste,o.Verbet)
#

def makeSentence(wordlist): #pronoun verb [det/den] adjective noun
    
    def erSubjektPronomen(pronomen): #passer på at pronomenet er subjekt/nominativ
        if pronomen.__class__ != o.DetPersonligePronomenet:
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
            pronomen = tilfeldigIBestemtOrdKlasse(wordlist, o.Pronomenet)
            feil +=1
            if feil>=5:
                print("oops'", pronomen(),"'funker ikke")
                return o.Pronomenet("hen")
        
        return pronomen
    
    #henter tilfeldig ord til setningen
    pronomen = tilfeldigIBestemtOrdKlasse(wordlist, o.Pronomenet)
    pronomen = erSubjektPronomen(pronomen)
    verb = tilfeldigIBestemtOrdKlasse(wordlist, o.Verbet)
    substantiv = tilfeldigIBestemtOrdKlasse(wordlist,o.Substantivet)
    adjektiv = tilfeldigIBestemtOrdKlasse(wordlist,o.Adjektivet)
    
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
        adjektiv = o.Adjektivet(adjektiv)
        plAdjektiv = adjektiv()
        '''
    
    #print setningen
    print(pronomen(),verb(),detDen,plAdjektiv,substantiv())
  
# makeSentence(setningOrientertOrdliste)

i =0
while i<10:
    makeSentence(setningOrientertOrdlisteForståelig)
    i +=1
    

# print(o.DetPersonligePronomenet.ordklassenavn()())
# print(f"{ordet()} er {ordet.__class__.ordklassenavn()()}")
