import skoledatabase as skdb

def info(skoleinp, year): #navn
    
    skole = skoleinp.lower()
    
    match skole:
        case "amalie" | "amalie skram" | "asvg" | "amalie skram videregående skole" | "amalie skrem vgs":
            faktiskSkole = "amalie skram"
        case "katten" | "katedralskolen" | "bergen katedralskole" | "katedralskolen i bergen" | "katten videregående" | "katten vgs":
            faktiskSkole = "bergen katedralskole"
        case "olsvik" | "olsvikåsen" | "olsvik videregående" | "olsvikåsen videregående" | "olsvikåsen videregående skole" | "olsvikåsen videregående skule" | "olsvik vgs" | "olsvikåsen vgs":
            faktiskSkole = "olsvikåsen vgs"
        case "ng" | "nordahl grieg" | "nordahl grieg vgs" |"nordal grig":
            faktiskSkole = "nordahl grieg"
        case _:
            faktiskSkole = False
            print("faktisk ikke skole") #logg TODO: erstatte med log-funksjon
    
    return faktiskSkole, year
    
def karakter(faktiskSkole, year):
    karakter = 3
    return karakter