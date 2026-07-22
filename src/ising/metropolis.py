from ising.model import IsingModel

import numpy as np

class MetropolisSampler:
    def __init__(self, model: IsingModel, temperature: float):
        self.model = model
        self.temperature = temperature

    def step(self):
        a = np.random.randint(self.model.length)
        b = np.random.randint(self.model.length)

        dE = self.model.delta_energy(a,b)

        if dE <= 0:
            self.model.spin_flip(a,b)
            return True

        else:
            r = np.exp(- dE / self.temperature)
            aleat = np.random.random()

            if (r >= aleat):
                self.model.spin_flip(a,b)
                return True
            else:
                return False
            
    def sweep(self):
        for _ in range(self.model.length ** 2):
            self.step()



# exemple = IsingModel(length = 64)
# sampler = MetropolisSampler(exemple, temperature = 1.0)

# for i in range(100):
#     for j in range(exemple.length**2):
#         sampler.step()

# exemple.plot_lattice()  
# plt.show()