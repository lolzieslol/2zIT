
#1
"""
setning = "fast and angry"

print(f"your sentence is {setning}")
for bokstav in setning:
    if bokstav=="a":
        print("I found an A!")
#sjekke output? hvis alle er nei?
        
print("bye")

"""

#2
"""
import random as rd
lista = []

for i in range(30):
    lista.append(rd.randint(1,5))

lista.insert(1,42)

print(lista)

i=0
for item in lista:
    if item<5:
        i+=1
    else:
        
        print("big")

print(f"{i} small ones")

"""
#3

fruits = ['apple', 'banana', 'cherry','cherry']

x = fruits.count("cherry")

print(x)