import matplotlib.pyplot as plt
import numpy as np


''' diverse info
plt.close
axline

annotate
text
figtext

xlabel y
title
# cmap
'''

''' #1
Xs = [3, 6, 9]
Ys = [2, 4, 6]

# plt.plot(Xs, Ys)
plt.scatter(Xs,Ys)
plt.show()

'''

''' #2
x = np.zeros(100)
y = np.zeros(100)
S = np.zeros(100)
a = 0.5

for i in range(len(x)):
    x[i] = S[i-1]+S[i]*a
    
    y[i] = x[i]/2



plt.figure(1)
plt.plot(x,y)
plt.show
plt.savefig
print("ferdig")
'''

# ''' #3
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

# kilde: https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
# '''