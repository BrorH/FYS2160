import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
from LammpsLogReader import LammpsLogReader as LLR


logfil = "log.boiled_400K"
with open(logfil, "r") as file:
    data = LLR(file)
    data.readFileToDict()

T = data.getProperty("Temp")
E = data.getProperty("TotEng")
H = data.getProperty("Enthalpy")
PV = H - E

# plt.plot(T, label="T")
plt.plot(E, label="E")
plt.plot(H, label="H")
plt.legend()
plt.show()
