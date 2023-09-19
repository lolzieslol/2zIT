import skoleinfo as skole

def skriver(skoleinp, faktiskSkole, year):
    if faktiskSkole:
        karakter = skole.karakter(faktiskSkole, year)
        print(f"du begynte på {faktiskSkole} i {year} og for å gjøre dette må du ha hatt minst en {karakter} i snitt")
    else:
        print(f"skolen din {skoleinp} finnes ikke i databasen, så programmet kan ikke finne info om den.")
        