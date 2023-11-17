'''
fjerner newline

Laget med tanke på kopiering fra pdf
'''
import sys as haha

inptxt = ""
ferdig = False
while not ferdig:
    #leser en linje om gangen
    inplinje = haha.stdin.readline()
    
    #bestemmer om programmet er ferdig
    if inplinje.strip() == "-- end --":
        ferdig = True #ender while-loopen
    
    #hvis programmet ikke er ferdig legges den nyeste linjen til
    if not ferdig:
        inptxt += inplinje

#erstatter newline med et mellomrom
text =inptxt.replace("\n"," ")

#gir tilbake resultatet
print(text)
