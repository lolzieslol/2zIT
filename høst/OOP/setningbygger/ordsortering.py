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

def tilfeldigIBestemtOrdKlasse(wordList,ordklasse):
    randomWord = ""    
    while not issubclass(type(randomWord), ordklasse):
        myint =randint(0,len(wordList)-1)
        
        randomWord = wordList[myint]
    # ordklassen, nounClass = ordklasse.ordklassenavn() 
    # print(f'ditt tilfeldige ord i klassen {ordklassen} er "{randomWord()}"')
    return randomWord



# tilfeldigIBestemtOrdKlasse(ordliste, ok.Verbet) #WIP

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
