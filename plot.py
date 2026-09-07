import matplotlib.pyplot as plt

#abs-mean-mag
with open("data/abs_mean_magnetisation.txt", "r") as inputFile:
    T = []
    abs_mean_mag = []
    
    #les linies les llegeixen de la fila
    for line in inputFile.readlines():
        lineStripped = line.strip()
        lineSplitted = lineStripped.split("\t")
        #la linia es guarda a la llista
        T.append(float(lineSplitted[0]))
        abs_mean_mag.append(float(lineSplitted[1]))

plt.figure()

plt.plot(
    T,
    abs_mean_mag,
    "-",
    c="blue",
    linewidth=1,
    label=r"$\langle |m| \rangle$"
)

plt.axhline(
    y=1,
    color="lightgray",
    linestyle="--",
    linewidth=1,
    label=r"$m=1$"
)

plt.xlim(1.0, 3.0)
plt.ylim(0, 1.05)

plt.xlabel("T")
plt.ylabel(r"$\langle |m| \rangle$")
plt.legend()

plt.savefig(
    "plots/abs_mean_mag.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()






#magnetic-susceptibility
with open("data/magnetic_susceptibility.txt", "r") as inputFile:
    T = []
    mag_sus = []
    
    #les linies les llegeixen de la fila
    for line in inputFile.readlines():
        lineStripped = line.strip()
        lineSplitted = lineStripped.split("\t")
        #la linia es guarda a la llista
        T.append(float(lineSplitted[0]))
        mag_sus.append(float(lineSplitted[1]))

plt.figure()

plt.plot(
    T,
    mag_sus,
    "-",
    c="cyan",
    linewidth=1,
    label=r"$ \chi $"
)


plt.xlim(1.0, 3.0)

plt.xlabel("T")
plt.ylabel(r"$ \chi $")
plt.legend()

plt.savefig(
    "plots/magnetic_susceptibility.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()






#mean-energy
with open("data/mean_energy.txt", "r") as inputFile:
    T = []
    mean_energy = []
    
    #les linies les llegeixen de la fila
    for line in inputFile.readlines():
        lineStripped = line.strip()
        lineSplitted = lineStripped.split("\t")
        #la linia es guarda a la llista
        T.append(float(lineSplitted[0]))
        mean_energy.append(float(lineSplitted[1]))

plt.figure()

plt.plot(
    T,
    mean_energy,
    "-",
    c="green",
    linewidth=1,
    label=r"$\frac{\langle E \rangle}{N}$"
)

plt.axhline(
    y=-2,
    color="lightgray",
    linestyle="--",
    linewidth=1,
    label=r"$\frac{\langle E \rangle}{N} = -2 $"
)

plt.xlim(1.0, 3.0)

plt.xlabel("T")
plt.ylabel(r"$\frac{\langle E \rangle}{N}$")
plt.legend()

plt.savefig(
    "plots/mean_energy.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()




#specific-heat
with open("data/specific_heat.txt", "r") as inputFile:
    T = []
    spec_heat = []
    
    #les linies les llegeixen de la fila
    for line in inputFile.readlines():
        lineStripped = line.strip()
        lineSplitted = lineStripped.split("\t")
        #la linia es guarda a la llista
        T.append(float(lineSplitted[0]))
        spec_heat.append(float(lineSplitted[1]))

plt.figure()

plt.plot(
    T,
    spec_heat,
    "-",
    c="orange",
    linewidth=1,
    label=r"$ c $"
)

plt.xlim(1.0, 3.0)

plt.xlabel("T")
plt.ylabel(r"$ c $")
plt.legend()

plt.savefig(
    "plots/specific_heat.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()