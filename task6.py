import numpy as np
import matplotlib.pyplot as plt
from LammpsLogReader import LammpsLogReader as LLR
import subprocess


lampfil = "in.heatcapN2"
logfil = "log.lammps"


def change_temp(file, L):
    with open(file, "r") as infile:
        infile.readline()
        rest = infile.read()
    with open(file, "w") as outfile:
        outfile.write(f"variable L equal {L}\n")
        outfile.write(rest)


def run_lammps():
    subprocess.run(f"lmp_stable -in {lampfil}".split())


def read_log():
    with open(logfil, "r") as file:
        data = LLR(file)
        data.readFileToDict()
    return data


n = 15
N = 1000 # number particles
start = 50
end = 10000

Ts = np.linspace(start, end, n)
cV = np.zeros(n)
for i, T in enumerate(Ts):
    change_temp(lampfil, T)
    run_lammps()
    data = read_log()

    T = data.getProperty("Temp")
    U = data.getProperty("TotEng")

    U *= N

    a, b = np.polyfit(T, U, 1)
    c = a

    cV[i] = c

np.save("cV", cV)

plt.plot(Ts, cV, "ro")
plt.xlabel("box length")
plt.ylabel("Heat capacity")
plt.show()
