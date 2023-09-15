'''
#hvert tall mellom 1 og 31
intagPl = [x for x in range(1,31)]
print(intagPl,end=" - list end.")

'''

nmbr = []

for i in range(10):
    nmbr.append(i+0.4)

#print(nmbr)
print("liste: " + str(nmbr) + "ant er: "+ str(len(nmbr)))


nmbr.insert(0,123)
print("liste: " + str(nmbr) + "ant er: "+ str(len(nmbr)))

print(f"tredje:{nmbr[3]}")
#3 or 4

if 0.4 in nmbr:
    print("0.4 is present")

#index

#pop m/index

# array gjrø at ganging (dobbel len (sam in) -> ganging dobbel verdi all)

# https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/1-grunnleggende-programmering-i-python/1d-lister/redigere-lister

# print(f"ord{verdi} ord")
'''
tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

oddetall = tall[::2]
partall = tall[1::2]

print(f"oddetall: {oddetall}")

'''

'''
tall = [9, 1, 5, 8, 3, 4, 10, 7, 11, 2, 6] 
print(tall)        # Skriver ut: [9, 1, 5, 8, 3, 4, 10, 7, 11, 2, 6]
tall.sort(reverse=True)
print(tall)        # Skriver ut: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#Med sort() forblir lista sortert. Hvis vi bare ønsker en midlertidig sortering, kan vi bruke sorted() 
'''

#print(sum(tall))