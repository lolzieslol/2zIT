## kopiert
# kilde: https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/2-objektorientert-programmering/2b-systemutvikling/gjenbruk-av-kode

import datetime as dt

class Tidspunkt:
  """
  Klasse for å lage tidspunkt-objekter.

  Parametre:
    tidsstempel = dt.datetime.now().timestamp() (int): tidspunktets tidsstempel
  """
  def __init__(self, tidsstempel = dt.datetime.now().timestamp()):
    """Konstruktør"""
    self.datoTid = dt.datetime.fromtimestamp(tidsstempel)
  
  def tidsstempel(self):
    """Gir hele tidsstemplet"""
    return self.datoTid

  def dato(self):
    """Gir dato i formatet dd.mm.yyyy"""
    return self.datoTid.strftime("%d.%m.%Y")

  def dag(self):
    """Gir datoens dag (01-31)"""
    return self.datoTid.strftime("%d")

  def måned(self):
    """Gir månedens fulle navn (på engelsk)"""
    return self.datoTid.strftime("%B")
    
  def år(self):
    """Gir årstall med fire siffer"""
    return self.datoTid.strftime("%Y")

# help(Tidspunkt)