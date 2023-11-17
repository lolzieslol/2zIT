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
    ordklassen, nounClass = ordklasse.ordklassenavn() 
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
    
    pronomen = tilfeldigIBestemtOrdKlasse(wordlist, o.Pronomenet)
    verb = tilfeldigIBestemtOrdKlasse(wordlist, o.Verbet)
    substantiv = tilfeldigIBestemtOrdKlasse(wordlist,o.Substantivet)
    adjektiv = tilfeldigIBestemtOrdKlasse(wordlist,o.Adjektivet)
    
    if substantiv.gender == "hunkjønn" or substantiv.gender == "hankjønn":
        detDen = "den"
    else:
        detDen = "det"
    if adjektiv()[-1] != "e":
        plAdjektiv = adjektiv() + "e"
    else:
        adjektiv = adjektiv() + "t"
        adjektiv = o.adjektiv(adjektiv)
        plAdjektiv = adjektiv()
    print(pronomen(),verb(),detDen,plAdjektiv,substantiv())
  
makeSentence(setningOrientertOrdliste)