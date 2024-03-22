'''
-- Databehandling --

Del 1: Summer kor mange idrettsutøvere som er i de forskjellige alderskategoriane.
Del 2: Lag eit søylediagram over det
Del 3: Finn ut i kva veke det var mest aktivitet 
    - og vis det fram vha ei oversikt over alle vekene (m/vekenummer) i eit søylediagram

'''

''' Del 1 '''
# Summer kor mange idrettsutøvere som er i de forskjellige alderskategoriane.
# age_group '18-34','35-54','55+'


import pandas as pd

#dataframe
df = pd.read_csv('vaar/test 19032024/run_ww_2020_w-PROVE.csv')

aldersgrupper = ['18-34','35-54','55+']

# nameLAter = df.groupby("age_group")[].count()

atheleteCount = df['age_group'].value_counts()
print(atheleteCount)

# Får ikke ut dataene i det hele tatt, kan ikke løse dette
# print(df['age_group'].items())

# print(df.groupby("age_group"))
# for aldersgruppe in aldersgrupper:
    
#     nameLAter = df.groupby("age_group")[aldersgruppe].count()
# 
#     print(aldersgruppe)
#     atheleteCount = 0
#     for aldersgruppe in df['age_group']:
#         atheleteCount += 1
    
#     print(f'I aldersgruppen {aldersgruppe} er det {atheleteCount} idrettsutøvere')

'''Del 2'''
# kan ikke gjøres 

'''Del 3'''
# kan ikke gjøres