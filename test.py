import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from LammpsLogReader import LammpsLogReader as LLR
import time


path = "log.lammps"
with open(path, "r") as file:
    data = LLR(file)
    data.readFileToDict()


T = data.getProperty("Temp")
P = data.getProperty("Press")

plt.plot(T, P)
plt.show()