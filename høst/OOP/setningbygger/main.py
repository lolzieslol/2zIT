'''
Program som
- definerer ordklasser (ordklasse.py)
- generer setninger i flere strukturer med tilfedige, men definerte ord (setningsstrukturer.py, ordhenting.py, ordene.py)
- bygger avsnitt med setningene (avsnitt.py)

begrensninger
- for norsk, funker IKKE i alle språk 
- har kun 5 setningsstrukturer
- bestemmer ikke om setningene gir mening

ideer:
- legge til GUI
- kunne markere "coherent sentences" - samlinger

'''
import ordene as ordobjekt
import ordklasse as ok
from avsnitt import genererAvsnitt

print(genererAvsnitt(ordobjekt.setningOrientertOrdlisteForståelig))

# ok.Verbet.ordklassenavn()

'''
ordet = ordobjekt.bok
if ordet.wordgender == "intetkjønn":
    print("et",ordet())
else:
    print("en",ordet())
'''
# print(ok.Verbet("hopper"),"er", ok.Verbet.ordklassenavn()())

# print(ordobjekt.fire.erTall)
# print(lagSetningMedStruktur.PEA(ordobjekt.setningOrientertOrdlisteForståelig))

'''
i =0
while i<10:
    print(lagSetningMedStruktur.DVMASA(ordobjekt.setningOrientertOrdlisteForståelig))
    i +=1
'''
# print(ordobjekt.to.erTall)
# print(ordobjekt.to.tall.isnumeric())
'''

i =0
while i<10:
    lagSetningMedStruktur.PVDAN(ordobjekt.setningOrientertOrdlisteForståelig)
    i +=1
''' 
# print(ok.DetPersonligePronomenet.ordklassenavn()())
# print(f"{ordet()} er {ordet.__class__.ordklassenavn()()}")
