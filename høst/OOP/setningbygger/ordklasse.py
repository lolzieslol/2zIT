class Ordet:
    def __init__(self,name : str): 
        self.name = name.lower()
        self.erOrd = True
        
    def skrivut(self):
        print(self.name)
    
    def __call__(self):
        return self.name
    
    def ordklassenavn():
        ordklasse = "ord"
        return ordklasse
        
class Verbet(Ordet):
    
    def __init__(self, name: str, tid: str="presens"):
        super().__init__(name)
        self.tid = tid
        self.erVerb = True
        
    def ordklassenavn():
        ordklasse = "pronomen"
        return ordklasse
    
class Pronomenet(Ordet):
    def __init__(self, name: str):
        super().__init__(name)
        self.erPronomen = True
        
    def ordklassenavn():
        ordklasse = "pronomen"
        return ordklasse
        
class DetPersonligePronomenet(Pronomenet):
    
    def __init__(self, name: str, tall=3, form="subjekt", gender=None):
        super().__init__(name)
        self.erPersonligPronomen = True
        
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
        return ordklasse


class Adjektivet(Ordet):
    def __init__(self, navn: str):
        super().__init__(navn)
        self.erAdjektiv = True
        self.erBeskrivende = True
        
    def ordklassenavn(self):
        ordklasse = "adjektiv"
        return ordklasse

class Adverbet(Ordet):
    def __init__(self, navn: str):
        super().__init__(navn)
        self.erAdverb = True
        self.erBeskrivende = True
        
    def ordklassenavn(self):
        ordklasse = "adverb"
        return ordklasse

class Konjunksjonen(Ordet):
    '''
    En konjunksjon er et ord eller en gruppe av ord som brukes til å koble sammen ord, setninger eller setningsdeler
    f.eks "og", "eller", "men" 
    '''
    def __init__(self, navn: str):
        super().__init__(navn)
        self.erSubjunksjon = True
        
    def ordklassenavn(self):
        ordklasse = "subjunksjon"
        return ordklasse

class Subjunksjonen(Konjunksjonen):
    '''
    En subjunksjon, også kalt "underordnet konjunksjon" er et ord eller uttrykk 
    som brukes til å koble sammen setninger ved å underordne en setning til en annen (ofte leddsetninger)
    f.eks "fordi", "hvis" og 
    '''
    def __init__(self, navn: str):
        super().__init__(navn)
        self.erSubjunksjon = True
        
    def ordklassenavn(self):
        ordklasse = "subjunksjon"
        return ordklasse
    

class Interjeksjonen(Ordet):
    '''
    En interjeksjon er et ord som uttrykker følelser eller reaksjoner fort, 
    f.eks "hurra" eller "oi"
    '''
    def __init__(self, navn: str):
        super().__init__(navn)
        self.erInterjeksjon = True
        
    def ordklassenavn(self):
        ordklasse = "subjunksjon"
        return ordklasse
    
    
class Preposisjonen(Ordet):
    def __init__(self, navn: str):
        super().__init__(navn)
        self.erPreposisjon = True
        
    def ordklassenavn(self):
        ordklasse = "preposisjon"
        return ordklasse