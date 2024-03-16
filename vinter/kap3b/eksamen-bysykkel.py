'''
Datasettet har følgende nøkler:
started_at, ended_at : tidspunkt
duration : tid
start_station_id, end_station_id : heltall
start_station_name, start_station_description, end_station_name, end_station_description : tekst
start_station_latitude, start_station_longitude, end_station_latitude, end_station_longitude : desimaltall (posisjon som lengdegrad og breddegrad)

Separatoren i CSV-filen er komma.


a)
Lag et program som presenterer de tre mest brukte startlokasjonene og de tre minst 
brukte startlokasjonene. Presentasjonen skal også vise antall turer fra disse startlokasjonene.

'''

import pandas as pd

#dataframe
df = pd.read_csv('sykkel.csv')

vanlighetStart = df['start_station_name'].value_counts() # lager en series

vanlighetSlutt = df['end_station_name'].value_counts() # lager en series

def skrivVanligste(vanligheten):
  toppTre = vanligheten.nlargest(3) # en series av de tre vaneligste

  bunnTre = vanligheten.nsmallest(3) # en series av de tre mist vanlige

  print("Mest Populære:")
  print(toppTre)  
  print()
  print("Minst Populære:")
  print(bunnTre)

print("-- Vanligste startstasjoner --")
skrivVanligste(vanlighetStart)

print()

print("-- Vanligste sluttstasjoner --")
skrivVanligste(vanlighetSlutt)