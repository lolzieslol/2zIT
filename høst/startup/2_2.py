# 2.2

'''
Brukeren skal bes om å gi to tall innenfor et lovlig verdiområde, 
    mellom 40-50 eller 
    mellom 70-90. 
En bekreftende beskjed skal gis om dette stemmer. 
Dersom ikke begge tallene har fått lovlig verdi, 
    skal koden i else-blokken utføres (eks. “Minst ett av tallene er utenfor gyldig intervall”). 
'''

# input
inp_1 = int(input("gi et tall innenfor et lovlig verdiområde: "))

inp_2 = int(input("gi enda et tall innenfor et lovlig verdiområde: "))

#test
def gyldigTall(intt):
    if (intt >= 40 and intt <= 50) or (intt >= 70 and intt <= 90):
        return True
    else:
        return False

if inp_1 == True and inp_2 == True:
    print("alt er rett")
# elif inp_1 == False and inp_2 == False:
#     print("alt er feil")
else:
    # print("en er rett")
    print("minst en er ugyldig")
    

#test 3