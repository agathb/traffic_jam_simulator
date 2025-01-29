import numpy as np

class Car:
    
    def __init__(self,
                 position,
                 speed,
                 time_step = None,
                 ability_to_move = None):

        # The car position will be a vector of 2 elements, for both the front and back of the car.
        self.position = position
        self.speed = speed

    def move_straight(self, time_step):

        position_history = []
        time_step = np.array([time_step, time_step]) # Array because car position is an array.

        position_history.append(self.position)
        self.position += self.speed * time_step
        print(f'\nCar at {self.position} after a time of {time_step[0]} s at speed {self.speed} m/s.')

        return position_history

# Test.

time_step = 1

car1 = Car(np.array([1,2]), 2)

print(f'\nStarting position of the car: {car1.position}')

car1.move_straight(1)