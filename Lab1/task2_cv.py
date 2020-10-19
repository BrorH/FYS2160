import numpy as np
import matplotlib.pyplot as plt
from LammpsLogReader import LammpsLogReader as LLR


path = "log.lammps"
with open(path, "r") as file:
    data = LLR(file)
    data.readFileToDict()

T = data.getProperty("Temp")
U = data.getProperty("TotEng")
P = data.getProperty("Press")
V = 125
N = 500

U *= N

print(f"mean of T is {np.mean(T)}")
print(f"mean of P is {np.mean(P)}")

a, b = np.polyfit(T, U, 1)
cV = a
dcV = np.sqrt(np.std(U)**2 + np.std(T)**2)

f = 2 * cV / N

lab = f"a = {a:.4}, b = {b:.4}"
plt.plot(T, a * T + b, "--", c="k", label=lab)
plt.plot(T, U, label="data")

plt.title(rf"$c_V = {cV:.4} \pm {dcV:.4}, f = {f:.4}$")
plt.xlabel("T")
plt.ylabel("U")
plt.legend()
plt.show()
