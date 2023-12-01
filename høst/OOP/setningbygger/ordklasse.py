class ordklasseKlasseNavn:
    def __init__(self,name : str, wordgender): 
        self.name = name.lower()
        self.wordgender = wordgender
        
        
    def __call__(self):
        return self.name

        
class Ordet:
    def __init__(self,name : str): 
        self.name = name.lower()
        
    def skrivut(self):
        print(self.name)
    
    def __call__(self):
        return self.name
    
    def ordklassenavn():
        ordklasse = "ord"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)
        
    # classinfo
    
class Verbet(Ordet):
    
    def __init__(self, name: str, tid: str="presens"):
        super().__init__(name)
        self.tid = tid
        
    def ordklassenavn():
        ordklasse = "verb"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)
    
    def definisjon():
        definisjonen = "en ordklasse som består av ord som betegner en handling, tilstand eller overgang, også kalt 'gjøre-ord'"
        return definisjonen
        

        
class Determinativet(Ordet):
    def __init__(self, name: str):
        super().__init__(name)
        
    def ordklassenavn():
        ordklasse = "determinativ"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)

class Mengdeordet(Determinativet):
    def __init__(self, name: str, tall: int):
        super().__init__(name)
        self.tall = tall
        
        tall = str(tall)
        if tall.isnumeric():
            self.erTall = True
        else:
            self.erTall = False
        
        
        
    def ordklassenavn():
        ordklasse = "mengdeord"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)
        
    
    def definisjon():
        definisjonen = "en ordklasse som betegner determinativer som angir antall eller mengde"
        return definisjonen


class Pronomenet(Ordet):
    def __init__(self, name: str, form=None):
        super().__init__(name)
        self.form = form
        
    def ordklassenavn():
        ordklasse = "pronomen"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)
    
    def definisjon():
        definisjonen = "en ordklasse som består av ord som viser til, erstatter eller endrer et tidligere nevnt eller underforstått ord eller uttrykk i den samme språklige sammenhengen eller den aktuelle talesituasjonen, også kalt henvisningsord"
        return definisjonen
        
class DetPersonligePronomenet(Pronomenet):
    
    def __init__(self, name: str, tallte=3, form="subjekt", gender=None,enFlerTall = "entall"):
        super().__init__(name)
        
        form = form.lower()
        if gender:
            gender = gender.lower()
        
        assert(form== "subjekt" or form== "nominativ" or form== "objekt" or form== "akkusativ" or form== "refleksiv" or form== "possessiv")
        assert(tallte <= 3 and tallte >=1)
        
        if form=="objekt":
            form = "akkusativ"
        if form=="subjekt":
            form="nominativ"
        
        self.form = form
        self.gender = gender
        self.tallte = tallte
        self.enFlerTall = enFlerTall
        
    def ordklassenavn():
        ordklasse = "personlig pronomen"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse,wordgender)
    
    def definisjon():
        definisjonen = "en ordklasse som består av ord som kan stå i stedet for et substantiv eller navn"
        return definisjonen

class DetRelativePronomenet(Pronomenet):
    def __init__(self,name : str, form=None):
        super().__init__(name)
    
    
    def ordklassenavn():
        ordklasse = "relativt pronomen"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse,wordgender)
    
    def definisjon():
        definisjonen = "en ordklasse som består av pronomen som innleder en underordnet setning og viser tilbake til et ord (substantiv, annet pronomen eller lignende) i den overordnede setningen."
        return definisjonen
    
class SpørrePronomenet(Pronomenet):
    def __init__(self, name: str, form=None):
        super().__init__(name, form)
        
    def ordklassenavn():
        ordklasse = "spørrepronomen"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse,wordgender)

class Biordet(Ordet):
    def __init__(self, name: str):
        super().__init__(name)
        self.erBeskrivende = True
        
    def definisjon():
        definisjonen = "ikke en klasse, men beskriver både adjektiv og adverb - beskrivende ord."
        return definisjonen
    
    def ordklassenavn():
        ordklasse = "biord"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse,wordgender)
    
        
class Adjektivet(Biordet):
    def __init__(self, name: str):
        super().__init__(name)
        
    def ordklassenavn():
        ordklasse = "adjektiv"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)
    
    def definisjon():
        definisjonen = "en ordklasse som består av ord som uttrykker en egenskap og ofte står som bestemmelse til et substantiv"
        return definisjonen
        
    def flertall(self):
        if self.name[-2:] == "el":
            self.name += "le"
    
        elif self.name[-1] != "e":
            self.name += "e"
            
        elif self.name == "moderne" or self.name =="spennende":
            pass
       
        return self
    
    def bøydEtterSubstantiv(self,substantiv):
        if substantiv.wordgender == "intetkjønn":
            bøydform = self.name + "t"  
        else:
            bøydform = self.name
        return bøydform      
        
    

class Adverbet(Biordet):
    def __init__(self, name: str):
        super().__init__(name)
        self.erBeskrivende = True
        
    def ordklassenavn(self):
        ordklasse = "adverb"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)
    
    def definisjon():
        definisjonen = "en ordklasse som består av ord som uttrykker tid, sted, måte, grad, nektelse, den talendes holdning e.l., som kan stå til et verb, et adjektiv, et annet adverb eller (en del av) en setning"
        return definisjonen

class Konjunksjonen(Ordet):
    '''
    En konjunksjon er et ord eller en gruppe av ord som brukes til å koble sammen ord, setninger eller setningsdeler
    f.eks "og", "eller", "men" 
    '''
    def __init__(self, name: str):
        super().__init__(name)
        
    def ordklassenavn(self):
        ordklasse = "subjunksjon"
        wordgender = "hankjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)

    def definisjon():
        definisjonen = "en ordklasse som består av ubøyelige ord som binder sammen og sideordner ord, fraser eller setninger"
        return definisjonen
    
class Subjunksjonen(Konjunksjonen):
    '''
    En subjunksjon, også kalt "underordnet konjunksjon" er et ord eller uttrykk 
    som brukes til å koble sammen setninger ved å underordne en setning til en annen (ofte leddsetninger)
    f.eks "fordi", "hvis" og 
    '''
    def __init__(self, navn: str):
        super().__init__(navn)
        
    def ordklassenavn(self):
        ordklasse = "subjunksjon"
        wordgender = "hankjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)
    
    def definisjon():
        definisjonen = "en ordklasse som består av ubøyelige ord som innleder en leddsetning (eller en infinitivskonstruksjon)"
        return definisjonen

class Interjeksjonen(Ordet):
    '''
    En interjeksjon er et ord som uttrykker følelser eller reaksjoner fort, 
    f.eks "hurra" eller "oi"
    '''
    def __init__(self, navn: str):
        super().__init__(navn)
        
    def ordklassenavn(self):
        ordklasse = "subjunksjon"
        wordgender = "hankjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)
    
    def definisjon():
        definisjonen = "en ordklasse som består av ubøyelige ord som brukes alene eller som et uavhengig innskudd i en setning som uttrykk for et følelsesbetonet utbrudd eller i en kommunikativ funksjon (bl.a. svarord) eller for å etterligne lyder, også kalt utropsord"
        return definisjonen
    
class Preposisjonen(Ordet):
    def __init__(self, navn: str):
        super().__init__(navn)
        
    def ordklassenavn(self):
        ordklasse = "preposisjon"
        wordgender = "hankjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)
    
    def definisjon():
        definisjonen = "ordklasse som består av ubøyelige ord som står foran et substantiv, substantivisk ord eller ledd og angir et steds-, tids-, årsaksforhold e.l. mellom dette og et annet ord, ledd i setningen"
        return definisjonen
    

class Substantivet(Ordet):
    def __init__(self, name: str, wordgender: str,plBøyning = "standard"):
        super().__init__(name)
        
        plBøyning = plBøyning.lower()
        muligeBøyninger : list = ["standard","ingen","annen"]
        assert(plBøyning in muligeBøyninger)
        
        self.wordgender = wordgender #TODO: legg til flere kjønn av gangen
        self.plBøyning = plBøyning
        
        def definerbestemtEntall():
            vokal : list = ["a","e","i","o","u","æ","ø","å"] #dropper y grunnet det ikke blir rett
            if self.name[-1] in vokal and self.plBøyning != "ingen":
                ordrot = self.name[:-1]
            else: 
                ordrot = self.name
            
            if self.wordgender == "hankjønn":
                bestemtform = ordrot + "en"
            elif self.wordgender == "hunkjønn":
                bestemtform = ordrot + "a"
            else:
                bestemtform = ordrot + "et"
            
            self.entallBestemtBøyd = bestemtform
        definerbestemtEntall()
        
        def definerUbestemtFlertall():
            #standard (backup)
            self.ubestemtFlertall = self.name + "er"
            
            if self.plBøyning == "standard":
                #hvis det slutter på en vokal
                vokal : list = ["a","e","i","o","u","æ","ø","å"]
                if self.name[-1] in vokal:
                    ordrot = self.name[:-1]
                    self.ubestemtFlertall  = ordrot + "er"
                return 
            
            #unntak
            if self.plBøyning == "ingen":
                self.ubestemtFlertall  = self.name
                return 
                
            if self.plBøyning == "annen":
                if self.name == "bok":
                    self.ubestemtFlertall  = "bøker"
                return 
        definerUbestemtFlertall()
    
    def ordklassenavn():
        ordklasse = "substantiv"
        wordgender = "intetkjønn"
        return ordklasseKlasseNavn(ordklasse, wordgender)
 
    
    def definisjon():
        definisjonen = "en ordklasse som består av ord som betegner skapning, ting, egenskap, handling, tilstand eller abstrakt fenomen"
        return definisjonen
    
    
    def tallTilform(self,mengdeordObjekt : Mengdeordet):
        if not mengdeordObjekt.erTall:
            tallform = "flertall"
            return tallform
        
        mengdeordObjekt.tall = int(mengdeordObjekt.tall) 
        if mengdeordObjekt.tall > 1 or mengdeordObjekt.tall == 0:
            tallform = "flertall" 
        else: 
            tallform = "entall"
    
        return tallform