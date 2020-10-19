import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
from LammpsLogReader import LammpsLogReader as LLR
import glob


N = 500
m = 1
rho = 0.001
V = N * m / rho
R = N * m / V

dumps = glob.glob("dump2/*")
dumps = [dump.rsplit(".", 1) for dump in dumps]
dumps = sorted(dumps, key=lambda x: int(x[1]))
dumps = [dump[0] + "." + dump[1] for dump in dumps]

P = np.zeros((3, len(dumps)))
T = np.zeros(len(dumps))

for i, dump in enumerate(dumps):

    with open(dump, "r") as file:
        for _ in range(10):
            file.readline()
        lines = file.readlines()

    v = np.zeros((3, len(lines)))
    for n, line in enumerate(lines):
        try:
            v[:, n] = [float(a) for a in line.split()[-3:]]
        except:
            continue

    vx, vy, vz = v
    Px = R * np.mean(vx ** 2)
    Py = R * np.mean(vy ** 2)
    Pz = R * np.mean(vz ** 2)

    P[:, i] = Px, Py, Pz

    T[i] = m / 3 * np.mean(vx ** 2 + vy ** 2 + vz ** 2)

fault = np.argmax(T)
T[fault] = T[fault - 1]
P[:, fault] = P[:, fault - 1]

print(f"ideal P is {N * np.mean(T) / V}")

print(f"mean of T is {np.mean(T)}")
print(f"mean of Px is {np.mean(P[0])}")
print(f"mean of Py is {np.mean(P[1])}")
print(f"mean of Pz is {np.mean(P[2])}")
print(f"mean of P is {np.mean(P)}")

for i, a in enumerate("x y z".split()):
    plt.plot(P[i], label=f"T mot P_{a}")
plt.xlabel("T")
plt.ylabel("P")
plt.legend()
plt.show()
