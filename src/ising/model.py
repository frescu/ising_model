import numpy as np

class IsingModel:
    def __init__ (self, length:int, temperature:float):
        self.length = length
        self.temperature = temperature
        self.spins = np.random.choice([-1,1], size = (length,length))

    def magnetization(self):
        #self.magnetization = sum(sum(self.spins))
        return np.sum(self.spins)


exemple = IsingModel(3,5.0)
M = exemple.magnetization()

print(exemple.spins)
print(M)