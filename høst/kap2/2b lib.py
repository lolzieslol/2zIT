from datetime import datetime # dato i formatet vanlig i USA
from tidspunkt import Tidspunkt # dato i formatet vanlig i Norge

now = datetime.now()
# print(now)
# print(now.timestamp)
print(now.strftime("%d.%m.%Y (Europa elrns) er samme dato som %D (USA)"))

## (ikke første gang jeg bruker dette biblioteket, men her er det uansett)

dato = datetime.fromtimestamp(1649329200)

print(dato.strftime(" dato fra 'fromtimestamp': %D"))

## norsk dato
nå = Tidspunkt()
print(f"datoen nå er {nå.dato()}, altså månden er {nå.måned}, dagen i måneden er {nå.dag}, timen er")

tidligere = Tidspunkt()
print(f"datoen tidligere var {tidligere.dato()}")