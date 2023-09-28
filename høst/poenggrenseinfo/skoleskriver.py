import skoledatabase as skdb

def info(skoleinp, faktiskSkole, year,karakter):
    #kan bytte om faktiskSkole 
    if faktiskSkole and karakter == 0.0: #formulering
        print(f'Du begynte på {faktiskSkole} i {year} og alle som søkte kom inn')   
    elif faktiskSkole and karakter == 70.0: #ingen data om skolen
        print(f'Du begynte på {faktiskSkole} i {year} og desverre har vi ingen info om poenggrensen på den skolen')
    elif faktiskSkole and karakter == 80.0: #ingen år
        print(f'Du begynte på {faktiskSkole} i {year} og desverre har vi ingen info om poenggrensen det året')
    elif faktiskSkole:
        print(f'Du begynte på {faktiskSkole} i {year} og for å gjøre dette må du ha hatt minst {karakter} karakterpoeng')
    else:
        print(f'Skolen din "{skoleinp}" finnes ikke i databasen, så programmet kan ikke finne info om den.')

def problem(year):
    
    # print(f"problem: året oppgitt var '{year}' og det er ikke gyldig")
    print("beklager, kan ikke si noe om dette. ", end="")
    if year is False:
        # print(f"du skrev '{year}' ikke et år")
        print("du skrev ikke et tall")
    elif  year is None:
        print(f"det er ikke lett å si noe om hvorfor")
    elif year == "ikke et skoleår i systemet":
        print("databasen har ingen info om dette året")
    elif type(year) is not float:
        print(f"problem: året oppgitt var '{year}' og det er ikke gyldig")
    elif year > skdb.skoleyrs[-1]:
        print("Det er etter det siste året i databasen")
    elif year < skdb.skoleyrs[0]:
        print("Det er før det første året i databasen")
    else:
        print("no response")
    