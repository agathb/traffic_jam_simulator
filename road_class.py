import numpy as np 
import math

class Straight_Road():

    def __init__(self,
                 starting_position,
                 end_position):

        self.starting_position = starting_position
        self.end_position = end_position
        self.length = math.dist(self.end_position, self.starting_position)

road1 = Straight_Road(np.array([0,0]), np.array([10,10]))

print(road1.length)
