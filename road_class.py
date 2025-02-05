import numpy as np

class Straight_Road():

    def __init__(self,
                 starting_position,
                 end_position):

        self.starting_position = starting_position
        self.end_position = end_position
        self.length = self.end_position -self.starting_position



#road1 = Straight_Road(10, 100)
#print(road1.length)
