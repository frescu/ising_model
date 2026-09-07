from ising.model import IsingModel
from ising.metropolis import MetropolisSampler
from ising.simulation import Simulation

import numpy as np
import time

start = time.time()

L = 32
n_therm = 5000
n_measur = 50000

temperatures = np.linspace(1.0,3.0,21)

mean_energy = []
mean_magnetisation = []
abs_mean_magnetisation = []
specific_heat = []
magnetic_susceptibility = []

print("Condicions inicials establertes...")

for T in temperatures:
    model = IsingModel(length = L)
    sampler = MetropolisSampler(model = model, temperature = T)
    simulation = Simulation(n_therm = n_therm, n_measur = n_measur,
                             model = model, sampler = sampler)
    
    results = simulation.final_observables()
    
    mean_energy.append(results["mean energy / spin"])
    mean_magnetisation.append(results["mean magnetisation / spin"])
    abs_mean_magnetisation.append(results["abs mean magnetisation / spin"])
    specific_heat.append(results["specific heat"])
    magnetic_susceptibility.append(results["magnetic susceptibility"])

print("Bucles realitzats per totes les T...")



with open("data/mean_energy.txt", "w") as outputFile:
    for T, E in zip(temperatures, mean_energy):
        outputFile.write(str(T)+"\t" +str(E) +"\n")

with open("data/mean_magnetisation.txt", "w") as outputFile:
    for T, M in zip(temperatures, mean_magnetisation):
        outputFile.write(str(T)+"\t" +str(M) +"\n")

with open("data/abs_mean_magnetisation.txt", "w") as outputFile:
    for T, M in zip(temperatures, abs_mean_magnetisation):
        outputFile.write(str(T)+"\t" +str(M) +"\n")

with open("data/specific_heat.txt", "w") as outputFile:
    for T, sp_heat in zip(temperatures, specific_heat):
        outputFile.write(str(T)+"\t" +str(sp_heat) +"\n")

with open("data/magnetic_susceptibility.txt", "w") as outputFile:
    for T, mag_susc in zip(temperatures, magnetic_susceptibility):
        outputFile.write(str(T)+"\t" +str(mag_susc) +"\n")

print("Dades escrites en arxius...")

end = time.time()

with open("data/sim_config.txt", "w") as outputFile:
    outputFile.write("L = " + str(L) + "\n" + "n_therm = "
                      + str(n_therm) + "\n" + "n_measur = " + str(n_measur)
                      + "\n" + "simulation duration = " 
                      + str((end - start) / 60.0) + " minutes"
                      )

print("Temps total: "+ str((end - start) / 60.0) + " minuts")