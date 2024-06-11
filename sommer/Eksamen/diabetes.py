''' OPPGAVE Databehandling diabetes

Dette er en oppgave med datasett. Spørsmål skal besvares, det skal gjøres begrensning og tilpassning.
Det skal presenteres grafisk hvor hensiktsmessig.

Delspørsmål:
- Hvilken alder har en "typisk person" med diabetes
- Vurder sammenhengen mellom påvist diabbetes og andre faktorer
--- Høyt kolestorol
--- BMI
--- Røyking
- Har personer som spiser frukt og trener (fysisk aktivtet) større sjanse for å ikke få diabetes?
'''

## ta med:
# unit test
# psuedokode

import unittest
import pandas as pd
# TODO: versjon uten pandas

diabetsFilPlasseringCSV = "sommer/Eksamen/diabetes_binary_health_indicators_BRFSS2015.csv"

#dataframe
pasientDF = pd.read_csv(diabetsFilPlasseringCSV) 

## Først: Begrens datasettet diabetes, 
# 1: diabets og alder
# 2: diabets, kolesterol, bmi, røyking
# 3: diabetes, frukt og fysisk aktivitet

### 1 ### Hvilken alder har en "typisk person" med diabetes
# Henter ut de relevante kollonnene
diabetesStatusOgAlderDF = pasientDF[["Diabetes_binary","Age"]]

# Prøver Diabetes først fordi jeg vet det ikke funker
alderMedDiabetes = diabetesStatusOgAlderDF[diabetesStatusOgAlderDF["Diabetes_binary"] == 2.0] 
medianAlderDiabetes = alderMedDiabetes["Age"].median()  # Bruker median for "typisk" alder

# Bruker prediabetes siden/når datasettet ikke har personer med diabetes
if medianAlderDiabetes != alderMedDiabetes["Age"].median(): 
    alderMedDiabetes = diabetesStatusOgAlderDF[diabetesStatusOgAlderDF["Diabetes_binary"] == 1.0] #bruker prediabetes fordi det ikke er noen med
    medianAlderDiabetes = alderMedDiabetes["Age"].median()  # Bruker median for "typisk" alder

#bruker forskjellige metoder for å definere "typisk" --> typetall, gjenomsnitt, median
typetallAlderDiabetes = alderMedDiabetes["Age"].mode()  # Bruker typetall for "typisk" alder
gjennomsnittAlderDiabetes = alderMedDiabetes["Age"].mean()  # Bruker gjennomsnitt for "typisk" alder

def byttTilAlderstall(alderkategori):
    
    assert(1<=alderkategori<=13)
    match alderkategori:
        case 1:
            alderstall = "18-23"
        case 2:
            alderstall = "24-28"
        case _:
            alderstall = "29+"
            
    return alderstall

# # Gir alderskategori
# print(f'Typisk alder for personer med diabetes, regnet ut med median: {medianAlderDiabetes}')

print(f'Typisk alder for personer med diabetes, regnet ut med median: {byttTilAlderstall(medianAlderDiabetes)}')
print(f'Typisk alder for personer med diabetes, regnet ut med typetall: {typetallAlderDiabetes}')
print(f'Typisk alder for personer med diabetes, regnet ut med gjennomsnitt: {gjennomsnittAlderDiabetes}')

### 2 ### Vurder sammenhengen mellom påvist diabetes og andre faktorer
# Høyt kolostorol, BMI, Røyking

# Statisk analyse av korrolasjon

# Henter ut de relevante kolonnene
diabetesStatusOgFlereFaktorer = pasientDF[["Diabetes_binary","HighChol","BMI","Smoker"]]
# finner korrelasjon med .corr(), returnerer tabell (pandas dataframe) over det
korrelasjonFlereFaktorerDiabetesStatusDF = diabetesStatusOgFlereFaktorer.corr()

# Skriver ut svaret
print(f'Korrelasjonen mellom diabetes og faktorene kolesterol, BMI og røyking:')
print(korrelasjonFlereFaktorerDiabetesStatusDF)

### 3 ### Har personer som spiser frukt og trener (fysisk aktivitet) større sjanse for å ikke få diabetes?
# Vitenskapelig påstand; konklusjon
# statisk analyse av korralasjon

del3DF = pasientDF[["Diabetes_binary","Fruits","PhysActivity"]]
fruktTreningDF = del3DF.groupby(["Fruits", "PhysActivity"]).mean()
fruktTreningDF = del3DF.groupby(["Fruits", "PhysActivity"])

# Skrivet ut svaret
print(f'Gjennomsnittlig diabetesrate basert på fruktinntak og fysisk aktivitet:')
print(fruktTreningDF)

# Enhetstest
class TestDiabetesAnalysis(unittest.TestCase):
    def test_median_alder(self):
        # Sjekker at medianvariabelen har den faktiske medianen
        self.assertEqual(medianAlderDiabetes, alderMedDiabetes["Age"].median())
    
    def test_korrelasjon(self):
        # Sjekker at alle kolonnene som skal sjekkes for korrelasjon eksisterer
        self.assertTrue("Diabetes_binary" in korrelasjonFlereFaktorerDiabetesStatusDF.columns)
        self.assertTrue("HighChol" in korrelasjonFlereFaktorerDiabetesStatusDF.columns)
        self.assertTrue("BMI" in korrelasjonFlereFaktorerDiabetesStatusDF.columns)
        self.assertTrue("Smoker" in korrelasjonFlereFaktorerDiabetesStatusDF.columns)
    
    # def test_frukt_trening(self):
    #     # 
    #     self.assertTrue((0, 0) in fruktTreningDF.index)
    #     self.assertTrue((1, 1) in fruktTreningDF.index)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)