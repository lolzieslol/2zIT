
import json

filnavn = "skandinavia.json"

with open(filnavn, encoding="utf-8") as fil:
    data = json.load(fil)
    for i in range(3):
        print(data["land"][i]["navn"])
    

# print(data)

data_formatert = json.dumps(data, indent=2)

print(data_formatert)