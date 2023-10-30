import random

#vektet alfabet
alfabet : list = ["a","b","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","å"]
#ekte alfabet
# alfabet : list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","æ","ø","å"]
listeAvEkteOrd : list = ["om", "hvis", "og", "nå","og", "meg", "jeg", "skal", "Alltid", "noe", "i", "alfabetet"]

def genererOrd():
    #1/20 sjangse for å bare velge et ekte ord
    RealWordYesNo = random.randint(0,20)
    if RealWordYesNo == 14:
        max = len(listeAvEkteOrd) -1
        a = random.randint(0,max)
        realWord = listeAvEkteOrd[a]
        return realWord #ferdig her hvis det blir et ekte ord
    
    #lager en rekke bokstaver ca like langt som et ord
    ordlengde = random.randint(2,10)
    nyttOrd = ""
    
    for i in range(ordlengde):
        max = len(alfabet) -1
        a = random.randint(0,max)
        nyttOrd+=str(alfabet[a])
    
    return nyttOrd

def genererAvsnitt():
    avsnitt = ""
    
    #antall setninger i hvert avsnitt
    avsnittLengde = range(1,10)
    #antall ord i hver setning 
    setningslengde = range(1,7)
    
    for setning in avsnittLengde:
        for ordNr in setningslengde:
            generertOrd = genererOrd()
            avsnitt += generertOrd + " "
            
    return avsnitt

