from ising.model import IsingModel

import numpy as np
import random


class MetropolisSampler:
    def __init__(self, model: IsingModel):
        self.model = model

    def step(self):
        a = random.randint(0, self.model.length - 1)
        b = random.randint(0, self.model.length - 1)

        dE = self.model.delta_energy(a,b)

        if dE <= 0:
            self.model.spin_flip(a,b)
            return True

        else:
            r = np.exp(- dE / (self.model.K_B * self.model.temperature))
            aleat = random.random()

            if (r >= aleat):
                self.model.spin_flip(a,b)
                return True
            else:
                return False
