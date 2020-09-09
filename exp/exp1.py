import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

f_K0 = [269, 387, 525, 653, 780, 908, 1038, 1164, 1295, 1424]
f_K1 = [227, 327, 430, 546, 651, 759, 867, 973, 1082, 1191]
f_K2 = [285, 419, 563, 701, 840, 979, 1118, 1257, 1396, 1537]
f_K3 = [459, 607, 757, 907, 1057, 1208, 1359, 1509, 1662, 1812]
f_K4 = [317, 453, 595, 739, 885, 1030, 1175, 1321, 1468, 1614]

L0 = 1241e-3
L1 = 1241e-3
L2 = 1243e-3
L3 = 1244e-3
L4 = 1244e-3
dL = 1.5e-3
L = [L0, L1, L2, L3, L4]
R0 = 104e3
R1 = 111.2e3
R2 = 102.02e3
R3 = 17.523e3
R4 = (38.02 + 37.96) / 2 * 1e3
r = [R0, R1, R2, R3, R4]
freqs = [f_K0, f_K1, f_K2, f_K3, f_K4]
names = [r"$K_0$", r"$K_1$", r"$K_2$", r"$K_3$", r"$K_4$"]
a = []
for i, f in enumerate(freqs):
    a_, _, _, _, da = linregress(range(len(f)), f)
    a.append([a_, da])
#     plt.plot(f, label=f"{names[i]}, a = {round(a_,3)}")
# plt.ylabel(r"$\nu$ [Hz]")
# plt.xlabel("n")
# plt.grid()
# plt.legend()
# plt.savefig("freqs.png")
# plt.show()

c = []
for L_, a_ in zip(L, a):
    c.append(2 * L_ * a_[0])
print(c)

R = 8.3144598


def c_id(T, f, Mm):
    return np.sqrt((f + 2) * R * T / (f * Mm))


T_C = lambda r: 25 - 24 * np.log(r * 1e-5)

Mm = [39.948, 44.01, 28.97, 28.97, 28.97]
f = [3, 5, 5, 5, 5]
c_teo = []
for r_, f_, Mm_ in zip(r, f, Mm):
    T = T_C(r_) + 273.15
    print(T)
    c_teo.append(c_id(T, f_, Mm_ / 1000))
print(c_teo)


df = pd.DataFrame(
    {"$K_0$": f_K0, "$K_1$": f_K1, "$K_2$": f_K2, "$K_3$": f_K3, "$K_4$": f_K4}
)
print(df.to_latex(index=False, escape=False, caption="CAPTION HERE", label="label"))
