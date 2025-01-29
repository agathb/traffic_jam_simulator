import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Road():   #This class as car as an input parameter
    def __init__(self, length = 100):
        self.length = np.array([0,length])

    def dynamics(self, car, dt = 1):

        position_memory = [] # memory of the position of the car
        time_step = np.array([dt,dt])
        time = 0

        while car.position[1] < self.length[1]:
            position_memory.append(car.position[1])
            car.position += car.speed * time_step
            time += dt
            print(f'car at {car.position} after a time {time} s at speed {car.speed} m/s')

        return time, dt, position_memory
    
    def car_size(self, car):
        car_size = car.position[1] - car.position[0]
        return car_size
    
    def plot(self, car):
        t, dt, position = self.dynamics(car)
        car_size = self.car_size(car)
        time = np.linspace(0, t, len(position))
        print(t, dt, time, position)
        plt.errorbar(time, np.array(position), fmt='.', color='green', markersize=8,
                    capsize=0, elinewidth=10, alpha=0.5, yerr = car_size/2, xerr = car_size/40)
        plt.grid()
        plt.tight_layout()
        plt.show()

    def animated_plot(self, car):
        fig, ax =  plt.subplots()

        t, dt, position = self.dynamics(car)
        time = np.linspace(0, t, len(position))
        car_position = ax.plot(time, position)

    def animate(i):
        

        

