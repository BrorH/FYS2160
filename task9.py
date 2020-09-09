import numpy as np
import matplotlib.pyplot as plt
from LammpsLogReader import LammpsLogReader as LLR


path = "log.lammps"
with open(path, "r") as file:
    data = LLR(file)
    data.readFileToDict()

N = 1000
ke = data.getProperty("KinEng") * N
T = data.getProperty("Temp")

sigmaK = np.sqrt(np.std(ke))
T = np.mean(T)

k = 1
cV = 3 * k / (2 - sigmaK * 4 * N / 3 / k ** 2 / T ** 3)

print(cV)

N = 1000
m = 14
p = 1.0

L = (N * m / p) ** (1 / 3)