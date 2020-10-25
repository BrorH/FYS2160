import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

font = {"family": "DejaVu Sans", "weight": "normal", "size": 22}
plt.rc("font", **font)

class This:
    def __init__(self):
        self.b = True


T = This()
points = []

Vmin = 0.55
Vmax = 5
That = 0.9


def onpress(event):
    if event.key == "v":
        print(f"Point recorded: {That}, {event.xdata}")
        points.append([That, event.xdata])
    if event.key == "b":
        T.b = False

while T.b:
    try:
        Vmin = float(input("Vmin "))
        Vmax = float(input("Vmax "))
        That = float(input("That "))
    except:
        continue

    fig, ax = plt.subplots()
    cid = fig.canvas.mpl_connect("key_press_event", onpress)
    Vhat = np.linspace(Vmin, Vmax, 20000)
    Phat = 8 * That / (3 * Vhat - 1) - 3 / Vhat ** 2
    # Ghat = 8 / 3 * That * np.log(3 * Vhat - 1) + Phat / 3 + 1 / Vhat ** 2 - 6 / Vhat
    Ghat = -8 / 3 * That * np.log(3 * Vhat - 1) - 3 / Vhat + Phat * Vhat

    ax.plot(Phat, Ghat, lw=5, label=(f"T = {That}"))
    plt.xlabel("P")
    plt.ylabel("G")
    plt.legend()

    plt.show()
    print()

points = np.asarray(points)
np.save("tmp.npy", points)
Tb, Pb = points.T

plt.plot(Tb, Pb, lw=5)
plt.xlabel("Temperature")
plt.ylabel("Pressue")
plt.title("Coexsitence line")
plt.show()
