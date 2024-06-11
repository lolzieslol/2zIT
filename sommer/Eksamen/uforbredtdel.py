
# pasienter og ansatte

class personer():
    
    def __init__(self,navn,id):
        self.navn = navn
        self.id = id
        
class pasienter(personer):
    
    def __init__(self, navn, id,sykdom):
        super().__init__(navn, id)
        sykdom = sykdom
    
    def hvilkenSykdom(self):
        print(self.sykdom)

class ansatte(personer):
    
    def __init__(self, navn, id):
        super().__init__(navn, id)


