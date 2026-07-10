import numpy as np

class IsingModel:
    def __init__ (self, length:int, temperature:float):
        self.length = length
        self.temperature = temperature
        self.spins = np.random.choice([-1,1], size = (length,length))

    def magnetization(self):
        #self.magnetization = sum(sum(self.spins))
        return np.sum(self.spins)

    def spin_flip(self,i,j):
        if (0 <= i <= (self.length - 1)) and (0 <= j <= (self.length - 1)):
            self.spins[i,j] *= -1
        else:
            raise IndexError("Índex fora dels límits del reticle")

exemple = IsingModel(3,5.0)

print(exemple.spins)

exemple.spin_flip(0,0)

print(exemple.spins)
