import skoleinfo as skole

def skriver(skoleinp, faktiskSkole, year,karakter):
    if faktiskSkole and karakter == 0.0: #formulering
        print(f'Du begynte på {faktiskSkole} i {year} og alle som søkte kom inn')   
    elif faktiskSkole and karakter == 70.0: #ingen data om skolen
        print(f'Du begynte på {faktiskSkole} i {year} og desverre har vi ingen info om poenggrensen på den skolen')
    elif faktiskSkole and karakter == 80.0: #ingen år
        print(f'Du begynte på {faktiskSkole} i {year} og desverre har vi ingen info om poenggrensen det året')
    elif faktiskSkole:
        print(f'Du begynte på {faktiskSkole} i {year} og for å gjøre dette må du ha hatt minst {karakter} i snitt')
    else:
        print(f'Skolen din "{skoleinp}" finnes ikke i databasen, så programmet kan ikke finne info om den.')
        