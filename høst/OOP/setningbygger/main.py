'''
program som bygger setninger.
- for norsk, funker IKKE i alle språk 

'''
from random import randint

# from ordklasse import *
import ordklasse as o

#definerer
jeg = o.DetPersonligePronomenet("jeg",1,"SubJekt")
er = o.Verbet("er", "presens")
ikke = o.Ordet("ikke")
deg = o.DetPersonligePronomenet("deg",1,"akkusativ")

#skriver ut
''' #test
print(jeg(), er(), jeg.form)

if jeg() == deg():
    print("hæ")
else: 
    print(jeg(),er(),ikke(), deg())
'''
    
######
ordliste : list = [jeg,er,ikke,deg]

def tilfeldigPronomen(wordList):
    randomWord = ""    
    while randomWord.__class__ != o.DetPersonligePronomenet:
        myint =randint(0,len(wordList)-1)
        
        randomWord = wordList[myint]

    print(f"ditt tilfeldige pronomen er '{randomWord()}'")
    
def tilfeldigIBestemtOrdKlasse(wordList,ordklasse):
    randomWord = ""    
    while randomWord.__class__ != ordklasse:
        myint =randint(0,len(wordList)-1)
        
        randomWord = wordList[myint]
    ordklassen, nounClass = ordklasse.ordklassenavn() 
    print(f'ditt tilfeldige ord i klassen {ordklassen} er "{randomWord()}"')

tilfeldigPronomen(ordliste)

tilfeldigIBestemtOrdKlasse(ordliste, o.Verbet) #WIP

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

ErOrdeneIKlasse(ordliste,o.Verbet)
#

