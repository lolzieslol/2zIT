class Ordet:
    def __init__(self,name : str): 
        self.name = name.lower()
        
    def skrivut(self):
        print(self.name)
    
    def __call__(self):
        return self.name
    
    def ordklassenavn():
        ordklasse = "ord"
        nounClass = "intetkjønn"
        return ordklasse, nounClass
        
    # classinfo
    
class Verbet(Ordet):
    
    def __init__(self, name: str, tid: str="presens"):
        super().__init__(name)
        self.tid = tid
        
    def ordklassenavn():
        ordklasse = "verb"
        nounClass = "intetkjønn"
        return ordklasse, nounClass

class Substantivet(Ordet):
    def __init__(self, name: str, wordgender: str):
        super().__init__(name)
        self.gender = wordgender
        
    def ordklassenavn():
        ordklasse = "substantiv"
        nounClass = "intetkjønn"
        return ordklasse, nounClass

class Pronomenet(Ordet):
    def __init__(self, name: str):
        super().__init__(name)
        
    def ordklassenavn():
        ordklasse = "pronomen"
        nounClass = "intetkjønn"
        return ordklasse, nounClass
        
class DetPersonligePronomenet(Pronomenet):
    
    def __init__(self, name: str, tall=3, form="subjekt", gender=None):
        super().__init__(name)
        
        form = form.lower()
        if gender:
            gender = gender.lower()
        
        assert(form== "subjekt" or form== "nominativ" or form== "objekt" or form== "akkusativ" or form== "refleksiv" or form== "possessiv")
        assert(tall <= 3 and tall >=1)
        
        if form=="objekt":
            form = "akkusativ"
        if form=="subjekt":
            form="nominativ"
        
        self.form = form
        self.gender = gender
        self.tall = tall
        
        self.classname = "personlig pronomen"
        
    def ordklassenavn():
        ordklasse = "personlig pronomen"
        nounClass = "intetkjønn"
        return ordklasse, nounClass


class Adjektivet(Ordet):
    def __init__(self, navn: str):
        super().__init__(navn)
        self.erBeskrivende = True
        
    def ordklassenavn():
        ordklasse = "adjektiv"
        nounClass = "intetkjønn"
        return ordklasse, nounClass

class Adverbet(Ordet):
    def __init__(self, navn: str):
        super().__init__(navn)
        self.erBeskrivende = True
        
    def ordklassenavn(self):
        ordklasse = "adverb"
        nounClass = "intetkjønn"
        return ordklasse, nounClass

class Konjunksjonen(Ordet):
    '''
    En konjunksjon er et ord eller en gruppe av ord som brukes til å koble sammen ord, setninger eller setningsdeler
    f.eks "og", "eller", "men" 
    '''
    def __init__(self, navn: str):
        super().__init__(navn)
        
    def ordklassenavn(self):
        #TODO: gjør om til substantiv
        ordklasse = "subjunksjon"
        nounClass = "hankjønn"
        return ordklasse, nounClass

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
        nounClass = "hankjønn"
        return ordklasse, nounClass
    

class Interjeksjonen(Ordet):
    '''
    En interjeksjon er et ord som uttrykker følelser eller reaksjoner fort, 
    f.eks "hurra" eller "oi"
    '''
    def __init__(self, navn: str):
        super().__init__(navn)
        
    def ordklassenavn(self):
        ordklasse = "subjunksjon"
        nounClass = "hankjønn"
        return ordklasse, nounClass
    
    
class Preposisjonen(Ordet):
    def __init__(self, navn: str):
        super().__init__(navn)
        
    def ordklassenavn(self):
        ordklasse = "preposisjon"
        nounClass = "hankjønn"
        return ordklasse, nounClass