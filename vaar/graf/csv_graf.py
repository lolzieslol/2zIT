# kilde: https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/3-databehandling/3b-reelle-datasett/lese-og-bruke-csv-filer
import csv
import matplotlib.pyplot as plt

# filnavn = "IT/vaar/graf/befolkning_1951-2022.csv"
# filnavn = "IT\vaar\graf\befolkning_1951-2022.csv"
filnavn ="befolkning_1951-2022.csv"

# Listene til grafen
aarstall = []
befolkning = []

#åpner filen
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    #henter overskrifter fra toppen av csv filen
    overskrifter = next(filinnhold)
    print(overskrifter)

    # henter ut dataen rad etter rad
    for rad in filinnhold:
        aarstall.append(int(rad[0]))
        befolkning.append(int(rad[1]))

# Tegner grafen
plt.style.use('dark_background')
plt.plot(aarstall, befolkning,color="y",linestyle="solid",marker="X")

x = aarstall
y = befolkning

plt.xlabel("$x$ - årstall")
plt.ylabel("$y$ - befolkning")
plt.title("Befolkning 1951-2022")

plt.ticklabel_format(style="plain")

plt.ylim(min(y),max(y))
plt.xlim(min(x),max(x))

# plt.style.use("classic")
# plt.style.use("fivethirtyeight")
plt.style.use('dark_background')
plt.grid()

plt.show()
# plt.savefig("befolkningsgraf_1951-2022",dpi=300)
