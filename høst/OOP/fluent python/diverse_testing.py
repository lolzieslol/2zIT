
class enKlasse:
    
    def __init__(self, name, value=1):
        self.name = name
        self.value = value
    
    def __iter__(self):
        return (i for i in (self.name, self.value))
        
    def pick(self):
        return self.name
    
    def __call__(self):
        #s 152 og 151
        
        # print(self.name)
        # return self.pick()
        return "call returnerer"
    
    def str(self):
        #bruker __iter__
        return str(tuple(self))
        
aObjekt = enKlasse("navn")

# print(aObjekt.__call__())
print(aObjekt())
print(aObjekt.str())
aObjekt()

# print(callable(aObjekt))


