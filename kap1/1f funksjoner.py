import random as rd

def girandom():
    tall1 = rd.randint(1,10)
    tall2 = rd.randint(1,10)
    
    return(tall1,tall2)

result = girandom()

t1, t2 = result
#tupple?

print(result)
print(t1)
print(t2)

import mittbib as mb

setning, ordd, alt = mb.best(1,2,3)

print(setning,ordd,alt)

# help(mb)

print(mb.tall(1))