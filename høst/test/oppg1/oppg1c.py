
fødselsnummer = input("skriv et ekte fødselsnummer: ")


def fødselsnummerRettLengde(fødselsnummer):
    if len(fødselsnummer) == 11:
        return True
    else:
        return False
    
def personBursdagTall(fødselsnummer):
    dag = int(fødselsnummer[:2])
    måned = int(fødselsnummer[2:4])
    år  = fødselsnummer[4:6]
    # print(f"personen har bursdag {dag}.{måned}.{år}")
    return dag, måned, år
    

def månedstallTilTxtMedMatch(måned):
    match måned:
        case 1:
            måned = "januar"
        case 2:
            måned = "februar"
        case 3:
            måned = "mars"
        case 4:
            måned = "april"
        case 5:
            måned = "mai"
        case 6:
            måned = "juni"
        case 7:
            måned = "juli"
        case 8:
            måned = "august"
        case 9:
            måned = "september"
        case 10:
            måned = "oktober"
        case 11:
            måned = "november"
        case 12:
            måned = "desember"
        case _:
            print("feil")
            return
    return måned
    
def månedstallTilTxtMedIf(måned):
    if måned == 1:
            måned = "januar"
    elif måned == 2:
            måned = "februar"
    elif måned == 3:
            måned = "mars"
    elif måned == 4:
            måned = "april"
    elif måned == 5:
            måned = "mai"
    elif måned == 6:
            måned = "juni"
    elif måned == 7:
            måned = "juli"
    elif måned == 8:
            måned = "august"
    elif måned == 9:
            måned = "september"
    elif måned == 10:
            måned = "oktober"
    elif måned == 11:
            måned = "november"
    elif måned == 12:
            måned = "desember"
    else:
            print("feil")
            return
    return måned

def personNummerÅr(år):
    if int(år) >= 23: #gjør dynamisk
        år = str(20)+str(år)
    elif int(år):
        år = str(19)+str(år)
    else:
        print("feil")
    return år


def personBursdagOrdUtskrift(dag, måned, år):        
    print(f"bursdagen din er {dag}. {måned} i {år}")



if fødselsnummerRettLengde(fødselsnummer):
    #separerer tallene i datoen
    bursdagsdag, bursdagsmånednbr, fødselssår = personBursdagTall(fødselsnummer)
    
    #gjør måned fra tall til tekst
    #1 : match
    bursdagsmånedtxt = månedstallTilTxtMedMatch(bursdagsmånednbr)
    #2 : if
    bursdagsmånedtxt = månedstallTilTxtMedIf(bursdagsmånednbr)
    
    #gjør året fra to siffer til fire
    fødselssår = personNummerÅr(fødselssår)
    
    #skriver ut svaret
    personBursdagOrdUtskrift(bursdagsdag, bursdagsmånedtxt, fødselssår)
    
else:
    print("ikke et gyldig personnummer")