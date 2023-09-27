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
    
    #gir ikke flere sjangser for feil tall
    #try er ikke egentlig ment for dette
    try:
        yearinp = int(yearinp) 
    except ValueError:    
        print(type(yearinp))
        feil += 1
        print(f"Du har skrevet {feil} feil")
        print("skriv et tall")
        
        if feil < 5:
            return yearInpFun(feil) 
        else:
            return False
    # except yearinp in skdb.skoleyrs:
    #     print("test")
    
    if feil < 5:
        if type(yearinp) == int:
            print("dette er et tall")
            if yearinp in skdb.skoleyrs: 
                return yearinp
            else:
                feil += 1
                print(f"Du har skrevet {feil} feil")
                print("skriv et år mellom 2020 og 2021")
                
                if feil < 5:
                    return yearInpFun(feil) 
                
                return "ikke et skoleår i systemet"
    else: 
        print("du får kun 5 sjangser, beklager")
        year = False
        return year
# year = yearinpFun(feil)

def yearInpFun2():
    
    feil = 0
    yearOK = False
    while feil < 5 and not yearOK:
        yearinp = input("i hvilket år startet du på videregående? (YYYY) ")
        
        if yearinp.isnumeric():
            year = int(yearinp)
            if year in skdb.skoleyrs: 
                yearOK = True
            
            else:
                year = "ikke et skoleår i systemet" #endre navn
                print("skriv et år mellom 2020 og 2023") #dynamisk senere
        else:
            print(type(yearinp))
            print("skriv et tall")
        
        if not yearOK:
            feil += 1
            print(f"Du har skrevet {feil} feil")
            
    if feil < 5:
        if type(yearinp) == int:
            print("dette er et tall")
            
    else: 
        print("du får kun 5 sjangser, beklager")
        return False #endre navn

    return year

