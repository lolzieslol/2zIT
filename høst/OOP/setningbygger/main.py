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

print(jeg(), er(), jeg.form)

if jeg() == deg():
    print("hæ")
else: 
    print(jeg(),er(),ikke(), deg())
    
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

    print(f'ditt tilfeldige ord i klassen {ordklasse.ordklassenavn()} er "{randomWord()}"')

# tilfeldigPronomen(ordliste)

# tilfeldigIBestemtOrdKlasse(ordliste, o.Verbet) #WIP

def ErOrdeneIKlasse(ordlist : list,klasse : str): #klasse med stor bokstav
    # klasse = str
    erIKlasse : str = "er" + klasse
    
    i = 0
    for ordet in ordlist:
        ordet= ordet
        # print(ordet.__class__)
        # print(ordet)
        # if ordet.erIKlasse:
        #     print(f'ordet "{ordet}" er {klasse}')
        
        if hasattr(klasse, erIKlasse):
            
            print(f'ordet "{ordet}" er {klasse}')
            i+=1
        
    if i == 0:
        print("ingen av ordene var i klassen")            
#

ErOrdeneIKlasse(ordliste,"Verbet")
#