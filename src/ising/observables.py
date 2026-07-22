import numpy as np

class Observables:
    def __init__(self,E,M,L,T):
        self.E = E
        self.M = M
        self.L = L
        self.T = T

    def energy_mean_spin(self):
        return np.mean(self.E) / self.L**2
    
    def squared_energy_mean_spin(self):
        return np.mean(np.square(self.E)) / self.L**2
    
    def magnetisation_mean_spin(self):
        return np.mean(self.M) / self.L**2
    
    def squared_magnetisation_mean_spin(self):
        return np.mean(np.square(self.M)) / self.L**2
    

    def specific_heat(self):
        return (
            self.squared_energy_mean_spin() 
            - self.energy_mean_spin()**2 * self.L ** 2
            ) / self.T ** 2
    
    def magnetic_susceptibility(self):
        return (
            self.squared_magnetisation_mean_spin() 
            - self.magnetisation_mean_spin()**2 *self.L ** 2
            ) / self.T
        