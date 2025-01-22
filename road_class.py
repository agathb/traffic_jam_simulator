import numpy as np 
import matplotlib.pyplot as plt

class Road():   #This class as car as an input parameter
    def __init__(self, length = 100):
        self.length = np.array([0,length])

    def dynamics(self, car, dt = np.array([1,1])):

        car.speed = car.initial_speed   # initial speed of the car
        car.position = car.initial_position   # initial position of the car
        position_memory = [] # memory of the position of the car

        while car.position[1] < self.length[1]:
            car_position[1] = position_memory.append(car.position)
            car.position += car.speed * dt
            print(f'car at {car.position} after a time {dt} s at speed {car.speed} m/s')

        return dt, position_memory
    
    def car_size(self, car):
        car_size = car.initial_position(1) - car.initial_position(0)
        car_middle = car.initial_position(0) + car_size/2
        return car_size, car_middle
    
    def plot(self, car):
        t, position = self.dynamics(car)
        car_size, car_middle = self.car_size(car)
        time = np.linspace(0, self.length(1), t)
        plt.errorbar(time, np.array(position), fmt = 'x', yerr = car_size/2)
        plt.grid()
        plt.show()

