'''
-	Opprett ei liste og fyll den med alle tala 1 – 100 (frå, til og med). 
-	Vis/kontroller med kode at den har 100 elementer (i motsetning til å ha la oss sei 99 eller 101). 
-	Skriv ein funksjon som tek som input:
    -	ei liste med tal
    -	eit tal 
-	Funksjonen skal gå gjennom lista, finne tala som er delelege med det gitte talet og legge desse til i ei ny liste. Til slutt skal funksjonen returnere den nye lista. Om den ikkje har noko innhald skal det returnerast ei tom liste.
-	Kall på funksjonen du nettopp har laga og send med lista du laga i første punkt (1-100), samt talet 7.
-	Skriv ei løkke som skriv ut alt innhaldet i det som blir returnert frå funksjonen.

'''

#1 Opprett ei liste og fyll den med alle tala 1 – 100 (frå, til og med)
mylist = []

for i in range(100):
    mylist.append(i+1)

#Vis/kontroller med kode at den har 100 elementer (i motsetning til å ha la oss sei 99 eller 101). 
print(f"listen har {len(mylist)} elementer")

# print(mylist[0], mylist[99])
# 1 end

# Skriv ein funksjon som tek som input:
#     -	ei liste med tal
#     -	eit tal 

def delbareTall(liste, tall):
    newList = []
    #Funksjonen skal gå gjennom lista
    for i in range(len(liste)):
        # finne tala som er delelege med det gitte talet og 
        if liste[i]%tall == 0:
            # legge desse til i ei ny liste. 
            newList.append(liste[i])
            
    # Til slutt skal funksjonen returnere den nye lista. 
    return newList
    
    # Om den ikkje har noko innhald skal det returnerast ei tom liste.
    
# -	Kall på funksjonen du nettopp har laga og send med lista du laga i første punkt (1-100), samt talet 7.
resultat = delbareTall(mylist, 7)

# -	Skriv ei løkke som skriv ut alt innhaldet i det som blir returnert frå funksjonen.
for i in range(len(resultat)):
    print(resultat[i])