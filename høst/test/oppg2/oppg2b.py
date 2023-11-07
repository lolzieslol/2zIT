#videre fra oppg2a
# import oppg2a as db
from oppg2a import Lager

'''
-	Skriv ut alle data på ein organisert måte, eksempelvis slik som i vedlegg (der du hentar data om produkta frå).
-	Skriv ein funksjon som tekk inn vare-ID og deretter skriv ut all informasjon om produktet. Feilmelding om den gitte vara ikkje finnes.
-	Skriv ein funksjon som tek inn vare-ID og ein ny-pris, og oppdaterer prisen til vara. Skriv deretter ut for å kontrollere om det blei gjort riktig ved å bruke funksjonen i førre punkt.
-	Skriv ein funksjon som tek inn ein vare-ID og ein ny farge, og legg til fargen i lista over farger
-	Skriv ein funksjon som tek inn ein vare-ID og ein farge, og fjerner fargen frå lista over farger
-	Skriv ein funksjon som tek inn ein vare-ID og ein ny egenskap, og legg til egenskapen i tekniske egenskaper
'''


# for dag in weatherdata["daily"]:


# Skriv ut alle data på ein organisert måte, eksempelvis slik som i vedlegg (der du hentar data om produkta frå).
def printAllLagerInfo():
                
    for varetittel in Lager.keys():
        print("-------------------")
        # print(varetittel)
        for DetaljKey, DetaljVerdi in Lager[varetittel].items():
            #for å håndtere "tekniske eigeskaper" sjekker programmet om typen er dict
            if type(DetaljVerdi) == dict:
                #printer ver ting individuelt
                for DetaljDetaljKey, DetaljDetaljVerdi in DetaljVerdi.items():
                    if type(DetaljDetaljVerdi) == list:
                        for i in range(len(DetaljDetaljVerdi)):
                            print(f"{DetaljDetaljVerdi[i]} er i listen av {DetaljDetaljKey}")
                    else:
                        print(f"{DetaljDetaljVerdi} er {DetaljDetaljKey}")
            else:
                print(f"{DetaljVerdi} er {DetaljKey} ")
    
# printAllLagerInfo()


# -	Skriv ein funksjon som tekk inn vare-ID og deretter skriv ut all informasjon om produktet. Feilmelding om den gitte vara ikkje finnes.
def UtskriftVareFraLager(varetittel):
    if varetittel in Lager.keys():
            for DetaljKey, DetaljVerdi in Lager[varetittel].items():
                #hvis det er en dictionary
                if type(DetaljVerdi) == dict:
                    print(DetaljVerdi)
                    for listeKey, listeVerdi in DetaljVerdi.items():
                        if listeKey != "farger":
                            print("-",listeKey,":",listeVerdi)
                        else:
                            farger = listeVerdi
                            print("- farger")
                            # farger = Lager[varetittel]["tekniske eigenskapar"][listeVerdi]
                            for i in range(len(farger)):
                                print(f"\t-- {farger[i]}")
                else:
                    # {type(verdi)} aasdf
                    print(DetaljKey,":",DetaljVerdi)
            
    else:
        print(f"varen, {varetittel} var ikke i listen")
    
    return

vareinp = "Samsung Galaxy S22 GH67"
# UtskriftVareFraLager(vareinp)


# -	Skriv ein funksjon som tek inn vare-ID og ein ny-pris, og oppdaterer prisen til vara. Skriv deretter ut for å kontrollere om det blei gjort riktig ved å bruke funksjonen i førre punkt.
def VareNyPrisFraLager(varetittel, nypris):
    print("pris før:",Lager[varetittel]["varetittel"],Lager[varetittel]["pris"])
    if varetittel in Lager.keys():
        Lager[varetittel]["pris"] = nypris
    
    print("pris etter:",Lager[varetittel]["varetittel"],Lager[varetittel]["pris"])
    


vareinp = "Samsung Galaxy S22 GH67"
# VareNyPrisFraLager(vareinp, "0")

# -	Skriv ein funksjon som tek inn ein vare-ID og ein ny farge, og legg til fargen i lista over farger
def VareNyFargeFraLager(varetittel, nyFarge):
    
    if varetittel in Lager.keys():
        print("farger før:",Lager[varetittel]["varetittel"],Lager[varetittel]["tekniske eigenskapar"]["farger"])
        Lager[varetittel]["tekniske eigenskapar"]["farger"].append(nyFarge)
    
        print("farger etter:",Lager[varetittel]["varetittel"],Lager[varetittel]["tekniske eigenskapar"]["farger"])
    else:
        print("varen er ikke i lageret")
    

vareinp = "Samsung Galaxy S22 GH67"
VareNyFargeFraLager(vareinp, "oransje")



# -	Skriv ein funksjon som tek inn ein vare-ID og ein farge, og fjerner fargen frå lista over farger
def VareFjernFargeFraLager(varetittel, nyFarge):
    print("farger før:",Lager[varetittel]["varetittel"],Lager[varetittel]["tekniske eigenskapar"]["farger"])
    if varetittel in Lager.keys():
        Lager[varetittel]["tekniske eigenskapar"]["farger"].remove(nyFarge)
    
    print("farger etter:",Lager[varetittel]["varetittel"],Lager[varetittel]["tekniske eigenskapar"]["farger"])
    

vareinp = "Samsung Galaxy S22 GH67"
# VareFjernFargeFraLager(vareinp, "hvit")



# -	Skriv ein funksjon som tek inn ein vare-ID og ein ny egenskap, og legg til egenskapen i tekniske egenskaper

def VareFraLagerLeggTilEgenskap(varetittel, egenskap, verdi):
    print("tekniske egenskaper før: ",Lager[varetittel]["varetittel"],Lager[varetittel]["tekniske eigenskapar"])
    if varetittel in Lager.keys():
        Lager[varetittel]["tekniske eigenskapar"][egenskap] = verdi
    
    print("tekniske egenskaper etter: ",Lager[varetittel]["varetittel"],Lager[varetittel]["tekniske eigenskapar"])
    

vareinp = "Samsung Galaxy S22 GH67"
# VareFraLagerLeggTilEgenskap(vareinp, "fotball", "hvit")
