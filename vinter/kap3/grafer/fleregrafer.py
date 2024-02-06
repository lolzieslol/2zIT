import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)

# Graf 1
yverdier = 0.5*xverdier**2 

plt.subplot(2, 1, 1)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 2
yverdier = -0.3*xverdier**3 

plt.subplot(2, 1, 2)
plt.plot(xverdier, yverdier)
plt.grid()

plt.savefig("min_figur.png", dpi=300)
# plt.show()