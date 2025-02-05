import numpy as np

class Cars(list):

    def __init__(self, list):

        super().__init__(list)

    def get_positions(self):

        return np.array([car.position for car in self])
    
    def get_speeds(self):

        return np.array([car.speed for car in self])