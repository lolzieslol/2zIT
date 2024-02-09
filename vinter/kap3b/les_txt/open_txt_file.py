import os
from dotenv import load_dotenv

load_dotenv("myfile.env") #legg path her

filnavn = os.getenv('filnavn')

with open(filnavn, encoding="utf-8") as fil:
  for linje in fil:
    # print(linje,end="")
    print(linje.rstrip(),end="-")