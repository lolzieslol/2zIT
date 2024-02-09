import csv
import matplotlib.pyplot as plt

filnavn = "gjennomsnittlig-rslnn.csv"

year = []
salery = []

with open(filnavn, encoding="utf-8-sig") as fil:
  filecontent = csv.reader(fil, delimiter=";")
  
  for row in filecontent:
    year.append(int(row[0]))
    salery.append(int(row[1]))

plt.plot(year, salery)
plt.title("Årslønn")
plt.xlabel("År")
plt.ylabel("Lønn")
plt.grid()
plt.show()