

#1
skriv = print
skriv("noe")

#2
def skrivTingOgTypenDetEr(variabel):
    skriv(f"tallet er {(variabel)} og typen er {type(variabel)}")


#2a
tall : int = 2
skrivTingOgTypenDetEr(tall)
#typen er int selv om det ellers ville blitt float

#2b
inputTall : int = input("skriv en int")
skrivTingOgTypenDetEr(inputTall)
#output er str uansett

#2c
ikketall : int = "dette er ikke et tall"
skrivTingOgTypenDetEr(ikketall)
#typen er str

# å bruke [varnavn] : int = [str] gir str




