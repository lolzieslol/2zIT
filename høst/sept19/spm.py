import random
import skoledatabase as skdb

def yearfunc():
    year = random.randint(2019,2023)
    print(f"Du startet på videregående i {year}")
    return year

# year = yearfunc()
# year = 2020

def yearInpFun(feil):
    yearinp = input("i hvilket år startet du på videregående? (YYYY) ")
    
    try:
        yearinp = int(yearinp)
    finally:    
        # print(type(yearinp))
        if feil < 5:
            if type(yearinp) == int:
                return yearinp
            else:
                feil += int(1)
                print(f"feil er: {feil}")
                print("skriv et tall")
                
                year = yearInpFun(feil)
                return year
                
        else: 
            year = False
            return year
# year = yearinpFun(feil)

def yearInpFun2(feil):
    try:
        year = input("skriv")
    except ValueError: #funker ikke
        print(f"skriv et årstall")
        year = yearInpFun2(feil)
    return year



def problem(year):
    
    print(f"problem: year var {year} og ikke gyldig")
    print("beklager, kan ikke si noe om dette. ", end="")
    if year is False or year is None:
        print("du skrev ikke et år")
    elif type(year) is not float:
        print("error: no clue what this is")
    elif year > skdb.skoleyrs[-1]:
        print("Det er etter det siste året i databasen")
    elif year < skdb.skoleyrs[0]:
        print("Det er før det første året i databasen")
    else:
        print("no response")