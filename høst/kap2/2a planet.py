#her kommer kap2

## 1 (12.09.23)
text = "hei og hei, men også nei."

# print(text.upper())
 

## 2
class Planet:
  def __init__(self, navn = "planet", solavstand = 1, radius = 2):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius
  
  def planetInfo(self):
    print(f' planeten "{self.navn}" har radius: {self.radius}'  )
fiksjonellPlanet = Planet("fiksjonell",321,1232)

#utdatert
'''
print(f"fiksjonell Planet radius: {fiksjonellPlanet.radius}"  )

planet2 = Planet("hei")

print(planet2.radius)

'''

fiksjonellPlanet.planetInfo()


