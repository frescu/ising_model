from ising.model import IsingModel
from ising.metropolis import MetropolisSampler
from ising.observables import Observables

import numpy as np


class Simulation:

    def __init__(self, n_therm, n_measur, 
                 model: IsingModel,sampler: MetropolisSampler):
        
        self.model = model
        self.sampler = sampler

        self.n_therm = n_therm
        self.n_measur = n_measur


    def all_energies_magnetisation(self):
        
        E = []
        M = []

        for _ in range(self.n_therm):
            self.sampler.sweep()
        
        for _ in range(self.n_measur):
            self.sampler.sweep()
            E.append(self.model.energy())
            M.append(self.model.magnetisation())

        return E,M
    
    def final_observables(self):
        
        E,M = self.all_energies_magnetisation()

        observ = Observables(E=E, M=M, L=self.model.length, T=self.sampler.temperature)

        magnetisation_mean = observ.magnetisation_mean_spin() 
        # AQUEST EL CALCULO A PART JA QUE TAMBÉ VULL EL VALOR ABSOLUT

        return{

            "mean energy / spin": observ.energy_mean_spin(),
            "mean magnetisation / spin": magnetisation_mean,
            "abs mean magnetisation / spin": abs(magnetisation_mean),
            "specific heat": observ.specific_heat(),
            "magnetic susceptibility": observ.magnetic_susceptibility()

        }