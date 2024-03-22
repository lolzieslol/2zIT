'''
b)
Utvid programmet slik at det også presenter et passende diagram som viser totalt antall turer 
fra alle startlokasjoner til sammen, per ukedag.
'''

import pandas as pd
from datetime import datetime
df = pd.read_csv('sykkel.csv')
import dateutil

# FiltrerrtSeries = df.groupby('started_at').get_group('2022-05-15')

# print(FiltrerrtSeries)


def getUniqueDatos(df : pd.DataFrame):        
    uniquedatos = []
    for started_at in df['started_at']: 
        candiDato = dateutil.parser.parse(started_at).date()
        
        
        # if candiDato not in  uniquedatos:
        #     uniquedatos.append(candiDato)
            # print(type(candiDato))
            # print(candiDato)
            # print("lagt til noe")
    return uniquedatos

def checkDatos(uniquedatos):
    for uniquedato in uniquedatos:
        print(uniquedato)

# uniquedatos = getUniqueDatos(df)
# checkDatos(uniquedatos)

def TellAllePåDagen(df : pd.DataFrame ,dagen):
    filtrert = df['started_at'].filter(like=str(dagen))
    print(filtrert)
    antall = filtrert.count()
    return antall

'''
for dato in uniquedatos:
    print(TellAllePåDagen(df,dato))
    # main(filtrert)
'''
def main(df : pd.DataFrame):
    vanlighetStart = df['start_station_name'].value_counts() # lager en series med hvor mange starter totalt
    
    print(vanlighetStart)

# for i in range(len(uniquedatos)):
#     print(i)
    # main(filtrert)

# mylist = []
# mycount = []
# i = 0

# for stasjon, antall in vanlighetStart.items(): 
#     i +=1
#     if stasjon in  mylist:
#         mycount[i] +=1
#         print("repeat")
#     else: 
#         mylist.append(stasjon)
#         mycount.append(1)
#         # print(stasjon)
    
#     # mylist.append((f"{stasjon}: {antall}"))
#     # mylist.append((stasjon,":",antall))

# # print(mylist)

# print(mycount)
