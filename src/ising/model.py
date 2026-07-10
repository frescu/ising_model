import numpy as np

class IsingModel:
    def __init__ (self, length:int, temperature:float):
        self.length = length
        self.temperature = temperature
        self.spins = np.random.choice([-1,1], size = (length,length))

    def magnetisation(self):
        return np.sum(self.spins)

    def spin_flip(self,i,j):
        if (0 <= i <= (self.length - 1)) and (0 <= j <= (self.length - 1)):
            self.spins[i,j] *= -1
        else:
            raise IndexError("Índex fora dels límits del reticle")

    def neighbour_sum(self,i,j):
        right = self.spins[i,(j+1) % self.length]
        left = self.spins[i,(j-1) % self.length]
        up = self.spins[(i-1) % self.length,j]
        down = self.spins[(i+1) % self.length,j]

        neighbour_sum = up+down+left+right

        return neighbour_sum

