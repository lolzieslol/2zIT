class Ordet:
    def __init__(self,name : str): 
        self.name = name.lower()
        
    def skrivut(self):
        print(self.name)
    
    def __call__(self):
        return self.name
        
class Verbet(Ordet):
    
    def __init__(self, name: str, tid: str="presens"):
        super().__init__(name)
        self.tid = tid
    
class Pronomenet(Ordet):
    def __init__(self, name: str):
        super().__init__(name)
        
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

    