#her kommer kap2

class Planet:
  def __init__(self, navn, solavstand, radius):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius
    
fiksjonellPlanet = Planet("fiksjonell",321,1232)

print(f"fiksjonell Planet radius: {fiksjonellPlanet.radius}"  )