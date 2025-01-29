import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Dynamics():
    def __init__(self, time_step):
        self.time_step = time_step

    def dynamics(self, car, road):
        car.ability_to_move = True
        position_history = []
        time = 0

        while car.position[1] < road.length[1]:
            position_history.append(car.move(self.time_step))

    
    def animated_plot(self, car, road):
        fig, ax =  plt.subplots()

        position = self.dynamics(car, road)
        x_axis = np.linspace(0, self.length, len(position))
        car_position, = ax.errorbar(x_axis, position, self.map, yerr = self.car_size(car)/2) 

        def animate(i):
            car_position.set_ydata(position[i])  # update the data.
            return car_position,

        ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

