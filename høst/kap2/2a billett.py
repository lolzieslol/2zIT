'''
Klasser:
underklasser

eksempel med bilett
'''
class Billett():
  def __init__(self):
      self.mva = 0.12
      self.pris = 20

  def beregnPris(self):
    return self.pris + (self.pris * self.mva)

class Barnebillett(Billett):
  def __init__(self):
      super().__init__()
      self.rabatt = 0.5
  
  def beregnPris(self):
      return super().beregnPris() * self.rabatt
#   super er viktig fordi funksjonen finnes i begge og vi vil at den nye skal erstatte den gamle for underklassen

enVanligBilett = Billett()

enBarnebillett = Barnebillett()

# print("prisen på en vanlig bilett er",enVanligBilett.beregnPris())

# print("prisen på en barnebillett er",enBarnebillett.beregnPris())
