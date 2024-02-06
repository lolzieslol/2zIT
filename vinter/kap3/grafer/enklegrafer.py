'''
kilde: https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/3-databehandling/3a-tegning-av-grafer/enkel-graftegning
'''

import matplotlib.pyplot as plt

''' Tegner punkter
#datasett
xverdier = [0, 1, 2, 3, 4]   # Liste med x-verdier
yverdier = [0, 1, 4, 9, 16]  # Liste med y-verdier

#grafen
plt.scatter(xverdier, yverdier)  # Lager grafen
plt.show()                       # Viser grafen

'''

''' Tegner en linje

def f(x):
    #eksponensiell funksjon
    return x**2

xverdier = []
yverdier = []

for xverdi in range(10):
    xverdier.append(xverdi)
    yverdier.append(f(xverdi))

plt.plot(xverdier, yverdier)
plt.show()
'''

''' Tegner en linje med forenklet skrivemåte

def f(x):
  return x**2

xverdier = [xverdi for xverdi in range(10)]
yverdier = [f(xverdi) for xverdi in xverdier]

plt.plot(xverdier, yverdier)
plt.show()
'''

''' tegner en linje med numpy linspace 
import numpy as np

def f(x):
  return x**2

xverdier = np.linspace(0, 10, 11)
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)
plt.show()
'''

