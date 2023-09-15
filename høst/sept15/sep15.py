'''
Fredag 15. september:
Basert på tilbakemeldingar og kva eg såg sist så får de endå ei økt med hovedfokus på ordbok/dictionary. For dei som treng nye oppgåver så har eg laga ei ny oppgåve som er "typisk" for ein vurderingssituasjon:

Me lagar ein form for eit spørreprogram, med noko attåt. 
Ordboka du tek utgangspunkt i skal innehalde 
    land med hovudstad, 
    innbyggjartal og 
    ei liste med naboland.

Utfordring 1: Repetisjon
Finn land med fleste innbyggjarar.
Finn land med fleste naboland.

Utfordring 2:
Still tilfeldige spørsmål til brukaren. Form: "Kva er -- i --?" Eksempelvis, "Kva er hovudstaden i Norge?" eller "Kva er innbyggjartalet i Canada?" Korleis vil du handtere at det kan kome både tal og tekst som svar?

Utfordring 3:
Tillat svar som er litt unøyaktige. Eksempelvis kan det vere ein viss feilprosent på innbyggjarar, eller at ein svarar 2 av 3 riktige naboland. Du bestemmer kor snill du er.

Utfordring 4:
Finn ein utfordring og 10 sjølv. 
'''
#dictionary
from pyliste import landtabell

'''
### test


##spør
inp = input("si et land: ")
inpformat = inp.lower #gjør at KapitalisasjOn ikke betyr noe

## resultat 

# print(landtabell[0]["land"])

# print(landtabell[0]["innbyggertall"])
# print(inp)
gyldigesvar=0

for i in range (len(landtabell)):
    if inp == landtabell[i]["land"]:
        print("gyldig svar")
        gyldigesvar = 1
    
if gyldigesvar == 0:
    print("Det er ikke et land på listen")
    
'''

# hvilket land har flest innbyggere
sortertLi = sorted(landtabell, key = lambda x: x["innbyggertall"], reverse=True)

print("befolkning sortert fra høy til lav")
for i in range(len(landtabell)):
    print(f'det er {sortertLi[i]["innbyggertall"]:,} innbyggere i {sortertLi[i]["land"]}') #norsk formattering
print(f"altså er {sortertLi[0]['land']} størst av disse landene")

print("----------------------------------")

# nabolandvinner = 

for i in range(len(landtabell)):
    landtall = landtabell[i]["naboland"].count
    landtabell[i]["nabolandtall"] = landtall
    
# nabolandLi = sorted(landtabell, key = lambda x: landtabell["nabolandtall"], reverse=True)

print(landtabell[1]["nabolandtall"])
print("det er {nabolandvinner} som har flest naboland")
