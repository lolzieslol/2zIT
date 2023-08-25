'''
#dict hent nøkkel og verdi
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for key in thisdict.keys():
    print(key)
    
for value in thisdict.values():
    print(f"verdien er {value}")

for key, value in thisdict.items():
    print(f"nøkkel og verdi {key, value}")
#første er nøkkel andre er verdi 

for key, value in thisdict.items():
    print(f"nøkkel {key} og verdi: {value}")
 '''   
#tuppel
print("tuppel")
tuppel = ('fornavn', 'Per')
a, b = tuppel
print(a,b)

#hente for liste har kronologisk hiarki

asdf = [{"ord": "skuff", "dfaf" :"drawer"},"ost", 1,["list",2,1,[0,1,2,3,4]]]

print(asdf[0]["ord"],asdf[3][3][3])

