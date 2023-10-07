#oppgave
'''
A: Lister og ordbøker (dictionaries)
Lag ei #ordbok som representerer eit lager med produkt. 
Kvart produkt har eigenskapar/attributt som du kan sjå nærare spesifisert under. 
Nokre produkt kan ha fleire variantar lagra i ordboka - eksempelvis fargar. 
Nokre produkt kan ha #fleire_ulike_tekniske_eigenskapar. 

Lag ei ordbok kalla varer som inneheld fylgjande informasjon:
-	unik varetittel (eksempelvis Asus Zenbook GH215)
-	varenavn (eksempelvis Asus laptop)
-	pris
-	varelager
-	produktinfo
-	tekniske eigenskapar (NB: desse kan variere noko frå ein produktkategori til ein annan)
o	prosessor: Intel Core i5-1135G7
o	grafikkort": "Intel Iris Xe Graphics
o	batteritid: Opptil 8 timer
o	vekt: 1.8 kg
-	farger: grå, svart, blå
Ta utgangspunkt i eksempeldata i vedlegg slik at du slepp finne på noko. NB: Legg igjen merke til at ikkje alltid dei tekniske eigenskapane er like.
Benytt lister og dictionaries etter behov.


'''
#vedlegg:
'''
Produktdata
Vare-ID: Asus Zenbook GH215
Varenavn: Asus laptop
Pris: 9999
Varelager: 10
Produktinfo: En bærbar PC med 15.6 tommer skjerm, 8 GB RAM og 256 GB SSD
Tekniske egenskaper:
-	prosessor: Intel Core i5-1135G7
-	grafikkort: Intel Iris Xe Graphics
-	batterikapasitet: Opptil 8 timer
-	vekt: 1.8 kg
Farger: 
-	grå 
-	svart 
-	blå

Vare-ID: Samsung Galaxy S22 GH67
Varenavn: Samsung mobiltelefon
Pris: 6999
Varelager: 20
Produktinfo: En smarttelefon med 6.7 tommer skjerm, 128 GB lagring og 12 MP kamera
Tekniske egenskaper:
-	prosessor: Qualcomm Snapdragon 888
-	grafikkort: Adreno 660
-	batterikapasitet: 4500 mAh
-	vekt: 200 g
Farger: 
-	svart 
-	hvit 
-	grønn

Vare-ID: Apple Airpods Pro Gen 3 (2023)
Varenavn: Trådløse hodetelefoner
Pris: 2499
Varelager: 30
Produktinfo: Trådløse hodetelefoner med aktiv støydemping
Tekniske egenskaper:
-	batterikapasitet: Opptil 4.5 timer
-	vekt: 5.4 g
Farger: 
-	hvit 
-	gul 
-	spygrønn

'''


#kunne nok vært gjort med objekter/klasser
## f.eks:    self.dict = {"varetittel" : self.tittel}

standardDict = {"varetittel":"",
          "varenavn":"",
          "pris":0,
          "varelager":0,
          "produktinfo":"",
          "tekniske eigenskapar": {"prosessor":"","grafikkkort":"","batteritid":8, "vektKG":0,"farger":[0] }
          }

LagerDicts = [
    {"varetittel":"Asus Zenbook GH215",
    "varenavn":"Asus laptop",
    "pris":9999,
    "varelager":10,
    "produktinfo":"En bærbar PC med 15.6 tommer skjerm, 8 GB RAM og 256 GB SSD",
    "tekniske eigenskapar": {"prosessor":"Intel Core i5-1135G7","grafikkkort":"Intel Iris Xe Graphics","batteritid":"Opptil 8 timer", "vekt":"1.8 kg","farger":["grå","svart","blå"] }
    },
    
        {"varetittel":"Samsung Galaxy S22 GH67",
    "varenavn":"Samsung mobiltelefon",
    "pris":6999,
    "varelager":20,
    "produktinfo":"En smarttelefon med 6.7 tommer skjerm, 128 GB lagring og 12 MP kamera",
    "tekniske eigenskapar": {"prosessor":"Qualcomm Snapdragon 888","grafikkkort":"Adreno 660","batteritid":"4500 mAh", "vekt":"200 g","farger":["svart","hvit","grønn"] }
    },
        
    {"varetittel":"Apple Airpods Pro Gen 3 (2023)",
        "varenavn":"Trådløse hodetelefoner",
        "pris":2499,
        "varelager":30,
        "produktinfo":"Trådløse hodetelefoner med aktiv støydemping",
        "tekniske eigenskapar": {"batterikapasitet":"Opptil 4.5 timer", "vekt":"5.4 g","farger":["hvit", "gul", "spygrønn"] }
        }
]


Lager = {
    "Asus Zenbook GH215":{"varetittel":"Asus Zenbook GH215",
    "varenavn":"Asus laptop",
    "pris":9999,
    "varelager":10,
    "produktinfo":"En bærbar PC med 15.6 tommer skjerm, 8 GB RAM og 256 GB SSD",
    "tekniske eigenskapar": {"prosessor":"Intel Core i5-1135G7","grafikkkort":"Intel Iris Xe Graphics","batteritid":"Opptil 8 timer", "vekt":"1.8 kg","farger":["grå","svart","blå"] }
    },
    
    "Samsung Galaxy S22 GH67":{"varetittel":"Samsung Galaxy S22 GH67",
    "varenavn":"Samsung mobiltelefon",
    "pris":6999,
    "varelager":20,
    "produktinfo":"En smarttelefon med 6.7 tommer skjerm, 128 GB lagring og 12 MP kamera",
    "tekniske eigenskapar": {"prosessor":"Qualcomm Snapdragon 888","grafikkkort":"Adreno 660","batteritid":"4500 mAh", "vekt":"200 g","farger":["svart","hvit","grønn"] }
    },
        
    "Apple Airpods Pro Gen 3 (2023)":{"varetittel":"Apple Airpods Pro Gen 3 (2023)",
        "varenavn":"Trådløse hodetelefoner",
        "pris":2499,
        "varelager":30,
        "produktinfo":"Trådløse hodetelefoner med aktiv støydemping",
        "tekniske eigenskapar": {"batterikapasitet":"Opptil 4.5 timer", "vekt":"5.4 g","farger":["hvit", "gul", "spygrønn"] }
        }
}

# varetall = 1
# print(f" En av varene, {LagerDicts[varetall]['varetittel']} har en pris på {LagerDicts[varetall]['pris']} kr")
