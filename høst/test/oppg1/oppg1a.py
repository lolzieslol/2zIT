'''
Skriv ein funksjon som tek som input bredde og høgde, i form av antall pikslar. 
Returner "Landscape" (liggande bilete) eller "Portrait" (ståande bilete) basert på kva den får inn. 

Bakgrunnsinformasjon: https://www.adobe.com/creativecloud/photography/discover/portrait-vs-landscape.html 

'''

#input


def main():
    bredde = input("hva er bredden? ")
    lengde = input("hva er lengden? ")
    
    if bredde.isnumeric():
        bredde = int(bredde)
    else:
        print("bredde var ikke et heltall, det må være et heltall")
        main()
        return

    def portraitOrLandscape(bredde, lengde):
        # if inp == landscape:
        if bredde > lengde:
            return "Landscape"
        elif bredde < lengde:
            return "Portrait"
        else:
            return "Kvadrat"
        
    print(f"Skjermen din er {portraitOrLandscape(bredde, lengde)}")

main()