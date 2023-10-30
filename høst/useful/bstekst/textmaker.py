import textfunctions as fun
import random 
#input

antallAvsnitt = int(input("Hvor mange avsnitt vil du generere?" ))
# print(f"generer {antallAvsnitt} avsnitt")
#legg sammen tilfeldig for å lage ord  og setninger og paragrafer

result = ""
for i in range(antallAvsnitt):
    avsnitt = fun.genererAvsnitt()
    if i+1 < antallAvsnitt:
        result+= avsnitt + "\n" + "\n"
    else:
        result+= avsnitt
#print
print(result)