
class ordet:
    def __init__(self,name : str):
        self.name = name.lower()
        
    def skrivut(self):
        print(self.name)
        

jeg = ordet("jeg")

print(jeg.name)

