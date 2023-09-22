import skoledatabase as skdb

def navnNorm(skoleinp): #navn
    
    skole = skoleinp.lower()
    
    match skole:
        case "amalie" | "skram" | "amalie skram" | "asvg" | "amalie skram videregående skole" | "amalie skrem vgs":
            faktiskSkole = "amalie skram"
        case "katten" | "katedralskolen" | "bergen katedralskole" | "katedralskolen i bergen" | "katten videregående" | "katten vgs":
            faktiskSkole = "bergen katedralskole"
        case "olsvik" | "olsvikåsen" | "olsvik videregående" | "olsvikåsen videregående" | "olsvikåsen videregående skole" | "olsvikåsen videregående skule" | "olsvik vgs" | "olsvikåsen vgs":
            faktiskSkole = "olsvikåsen vgs"
        case "ng" | "enge" | "nordahl grieg" | "nordahl grieg vgs" |"nordal grig":
            faktiskSkole = "nordahl grieg"
        case "sandsli" | "sandsli videregående" | "sandsli vgs":
            faktiskSkole = "sandsli vgs"
        
            #privatskoler:
        case "bpg" | "bergen private gymnas" | "bergen privat gymnas" | "bpg vgs":
            faktiskSkole = "bpg"
        case "daniselsen" | "danielsen videregående" | "danielsen videregående skole" | "danielsen vgs":
            faktiskSkole = "danielsen vgs"
        case "metis" | "metis vgs" | "metis videregående":
            faktiskSkole = "metis"
        case "st. paul" | "st.paul" | "st paul" | "st. paul gymnas" | "sankt paul" | "sankt pauls":
            faktiskSkole = "st paul vgs"
        case "akademiet bergen fpg as" | "akademiet":
            faktiskSkole = "akademiet bergen fpg"
        case _:
            faktiskSkole = False
    
    return faktiskSkole
    
def yearBasertKarakter(faktiskSkole, year):
    '''
    match year:
        case 2020:
            poenggrensen = skdb.poenggrense2020
        case 2021:
            if skdb.poeng.year[2021]:
                skdb.poeng.
            # poenggrensen = skdb.poeng.year
        case _:
            poenggrensen = False
    # poenggrensen = skdb.navnn
    '''
    funketListesjekk = "nei"
    for i in range(len(skdb.poeng)):
        if skdb.poeng[i]["year"] == year:
            funketListesjekk = "ja"
            
            # print(skdb.poeng[i]["year"], "er ditt")
            poenggrensen = skdb.poeng[i]["list"]
        # else: 
            # print(skdb.poeng[i]["year"], "er ikke ditt")
    
    if funketListesjekk == "nei":
        print("feil i listesjekk")
        # poenggrensen = skdb.poenggrense2020
    skoler = []
    if poenggrensen in skdb.poeng:
        for i in range(len(poenggrensen)):
            skoler.append(poenggrensen[i]["skole"])
            
        if faktiskSkole in skoler:
            for i in range(len(poenggrensen)-1):
                a = poenggrensen[i]["skole"]
                if a == faktiskSkole:
                    karakter= poenggrensen[i]["karakter"]
                    t = 1
                # else:
                #     print(f"{a} er ikke din skole {faktiskSkole}")
        else: 
            karakter = 70.0 #ingen data om skolen
    else:
        karakter = 80.0 #ingen data om året
    return karakter

def skoleBasertKarakter(skolen, year):
    karakter = 30.0
    
    lenlist = len(skdb.skoleliste)
    
    for n in range(lenlist):
        # print(f"tester om {skdb.skoleliste[n]['skole']} er lik {skolen}")
        if skdb.skoleliste[n]["skole"] == skolen:
            # for i in range(lenlist):
                # if skdb.skoleliste[n]["dict"][year] == year:
            
            year = int(year)
            print(skdb.skoleliste[n]["dict"])
            karakter = skdb.skoleliste[n]["dict"][year]
                
        # else:
            # print(f"{skdb.skoleliste[n]['skole']} er ikke lik {skolen}")
    return karakter