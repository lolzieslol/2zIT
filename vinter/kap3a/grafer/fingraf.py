

import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**2

xverdier = np.linspace(0, 10, 50)
yverdier = f(xverdier)


# Skriver ut en oversikt over tilgjengelige stiler
print(plt.style.available)

# Angir at vi vil bruke stilen "bmh"
plt.style.use("bmh")

plt.axhline(10, color="black", zorder=0)
plt.axvline(4, color="black", zorder=0)
plt.plot(xverdier, yverdier, color="coral", linestyle="dashed", zorder=1)

plt.grid()

plt.title("Funksjonen $f(x)=x^2$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0, 10)
plt.ylim(0, 150)

plt.show()

