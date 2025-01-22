import numpy as np 

class Road():   #This class as car as an input parameter
    def __init__(self, length = 100):
        self.length = np.array([0,length])

    def dynamics(self, car, dt = np.array([1,1])):

        car.speed = car.initial_speed   # initial speed of the car
        car.position = car.initial_position   # initial position of the car

        while car.position(1) < self.length(1):

            car.position += car.speed * dt
            print(f'car at {car.position} after a time {dt} s at speed {car.speed} m/s')

        return car.speed
