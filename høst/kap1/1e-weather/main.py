'''
en inndeling av det programmet som allerede finnes om værdata
'''

from weatherdata import weatherdata
from datetime import datetime

for dag in weatherdata["daily"]:
  unixtid = dag["dt"]
  dato = datetime.fromtimestamp(unixtid)
  temperatur = dag["temp"]["day"] - 273.15
  vindfart = dag["wind_gust"]
  print(f"Varsel for {dato}. Temperatur: {temperatur:5.2f} grader celsius.")
  print(f"det blir {vindfart} m/s med vind")
  #teknisk sett kan det være km/h men la oss håpe det ikke er det (burde stått)
