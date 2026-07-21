import numpy as np
import matplotlib.pyplot as plt

class IsingModel:

    def __init__ (self, length: int):
        self.length = length
        self.spins = np.random.choice([-1,1], size = (length,length))
        self.J = 1.0

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
    
    def delta_energy(self,i,j):
        neighbour_sum = self.neighbour_sum(i,j)
        return (2 * self.J * self.spins[i,j] * neighbour_sum)
    
    def energy(self):
        
        right = np.roll(self.spins,-1,axis=1)
        down = np.roll(self.spins,-1,axis=0)

        return -self.J * np.sum(self.spins * (right + down))

    # def plot_lattice(self, ax=None):

    #     if ax is None:
    #         _, ax = plt.subplots()

    #     ax.imshow(self.spins, cmap="bwr", vmin=-1, vmax=1)
    #     ax.set_title("Ising model 2D; " + f"L = {self.length}")
    #     ax.set_xticks([])
    #     ax.set_yticks([])
    #     return ax

    # AIXÒ HAURIA D'ANAR A UN ALTRE ARXIU NO AQUÍ