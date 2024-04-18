'''
-- Databehandling --

Del 1: Summer kor mange idrettsutøvere som er i de forskjellige alderskategoriane.
Del 2: Lag eit søylediagram over det
Del 3: Finn ut i kva veke det var mest aktivitet 
    - og vis det fram vha ei oversikt over alle vekene (m/vekenummer) i eit søylediagram

'''

''' Del 1 '''
# Summer kor mange idrettsutøvere som er i de forskjellige alderskategoriane.
# kolonnenavn: age_group aldersgrupper: '18-34','35-54','55+'

import pandas as pd

#dataframe
# df = pd.read_csv('vaar/test 19032024/run_ww_2020_w-PROVE.csv')
# df = pd.read_csv('vaar\\test 19032024\\run_ww_short.csv')
df = pd.read_csv('run_ww_short.csv') #må kjøres i integrert terminal for test 19032024

# print(type(df))

#lager et 'DataFrameGroupBy' klasse objekt med en tuple av hver unike age_group verdi og en dataframe med kun de med den age_group
ageGroup_groupedby = df.groupby("age_group") 

athlete_count_list = []
athlete_categories = []

for ageGroupTuple in ageGroup_groupedby:
    group_name : str = ageGroupTuple[0] 
    group_df = ageGroupTuple[1]
    athlete_count : int = group_df["athlete"].count() #antar at det ikke er flere like
    
    print(f"I alderskategorien {group_name} er det {athlete_count} utøvarar")
    
    #1 & 2 (se del 2)
    # data = {"age group" : group_name, "athletes count" : athlete_count}
    #thisList.append(data)
    

    #til del 2
    athlete_count_list.append(athlete_count)    
    athlete_categories.append(group_name)
    
## første fungerende løsning
# atheleteCount = df['age_group'].value_counts()
# print(atheleteCount)

'''Del 2'''
# lister fra før:    athlete_count_list, athlete_categories 

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))    # Angir dimensjoner for figure-objektet
y = np.arange(len(athlete_count_list))
print(f"type: {type(y)} val {y}")

alder = ['18-34','35-54','55+']
# 2
# alder=[]
# i = 0
# for kategori in thisList:
#     ax.barh(y+i, kategori["athletes count"], height=0.4, label=kategori["age group"])
#     alder.append(kategori["age group"])
#     i-=0.3

# 1
# yngst = thisList[0]["athletes count"]
# mellomst = thisList[1]["athletes count"]
# eldst = thisList[2]["athletes count"]
# athelete_count

# 3
ax.barh(athlete_categories, athlete_count_list, label=athlete_categories)
#NB: nå er alle samme farge

# 1
# ax.barh(y+0.3, yngst, height=0.4, label="18-34")  # Lager stolpediagram alder
# ax.barh(y-0.2, mellomst, height=0.4, label="35-54")  # Lager stolpediagram alder
# ax.barh(y-0.4, eldst, height=0.4, label="55+")  # Lager stolpediagram alder

ax.set_yticks(y, alder)                       # Legger til akseverdier
ax.legend()                                          # Legger til beskrivelse

fig.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet

ax.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)

plt.show()          # Viser diagrammet


'''Del 3'''
# gjør senere