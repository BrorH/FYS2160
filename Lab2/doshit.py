import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

R = 8.31446261815324
data = np.load("coex_line_better.npy")
Tb, Pb = data.T

plt.plot(Tb, Pb)
plt.show()

dP = np.gradient(np.log(Pb))
dT = np.gradient(1 / Tb)
Hv = - dP / dT * R
print(Hv)
print(np.std(Hv))

plt.plot(Tb, Hv)
plt.show()

Tc = 647.096
Pc = 22.064e3

T = Tb * Tc
P = Pb * Pc

plt.plot(T, P)
plt.show()

a, b = np.polyfit(1 / T, np.log(P), deg=1)
H = - a * R
print(H)