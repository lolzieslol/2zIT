import math as m 
#bruker "import [lib] as [x]" istedefor "from [lib] import *" fordi med flere bibliotek kombinert har du kanskje flere funksjoner med samme navn


#sirkel-areal
areal = 102 
radiusi2n = areal / m.pi
radius = m.sqrt(radiusi2n)

print("radiusen er " + str(radius))



#p2
'''
sitat = "Datamaskiner er ubrukelige. De kan bare gi oss svar."

print("Sitatets lengde:", len(sitat)) #len(string)
print("Tegnet med indeks 26:", sitat[26]) # "string[plass el index]"
print("Tegnene til og med indeks 11:", sitat[:12]) #string[:til og uten]
print("Tegnene fra og med indeks 28:", sitat[28:])# string[fra og med:]
print("Tegnene med indeks 16 til 25:", sitat[16:26]) #string[fra:til]
'''

#diverse
"""
tekst.lower()
tekst.upper()
tekst.capitalize() 
tekst.title() #tittel-format
tekst.replace(",", ".")	
tekst.index("p") #index til p
len(tekst)
"""


#konkatenering

#feilmeldingsoppgave uten feil??
#26: https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/1-grunnleggende-programmering-i-python/1a-tall-og-tekster/feil-og-feilmeldinger


# f-strings

tall = input("tall: ")
print(f"Tallet ditt er {tall} hvis du ikke husker")

#{a:.2f}

'''
{whatever} #no-form
{int:8} #mellomr foran for å nå tall
{flaot:.1f} #en desimal
{flaot:6.1f} #mellomrom + kun 1 desimal
{str:8} #mellomr etter
{str:<8} #mellomrom etter
{str:<8} #mellomrom før
'''

# print("Hei", end="\n") = print("Hei") - linjeskift
'''
print("Hei ", end="")
print("på deg!")

print("01", end=" | ")
print("02", end=" | ")
print("03")
'''