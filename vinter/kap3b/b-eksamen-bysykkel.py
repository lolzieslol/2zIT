'''
b)
Utvid programmet slik at det også presenter et passende diagram som viser totalt antall turer 
fra alle startlokasjoner til sammen, per ukedag.
'''

import pandas as pd

df = pd.read_csv('sykkel.csv')

#  dataframe[dataframe['Percentage'] > 70] 

uniquedates = []
for date in df.items(): 
    if date not in  uniquedates:
        uniquedates.append(date)

for date in uniquedates:
    filtrert = df.filter(df['started_at'] == date)

def main(df):
    vanlighetStart = df['start_station_name'].value_counts() # lager en series med hvor mange starter totalt

    print(vanlighetStart)

for datoen in range(len(uniquedates)):
    main(filtrert)

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
