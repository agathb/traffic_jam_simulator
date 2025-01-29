import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Dynamics():

    def __init__(self,
                 time_step):

        self.time_step = time_step

    def dynamics(self,
                 car,
                 road):

        car.ability_to_move = True
        position_history = [car.position]
        time = 0

        while car.ability_to_move == True:

            position_history.append(car.move_straight(self.time_step))
            time += self.time_step

            if car.position[1] >= road.length[1]:

                car.ability_to_move = False
                print(f'\nCar stopped at the end of the road after a time of {time} s.')

        return time, position_history

    
    def animated_plot(self, car, road):
        fig, ax =  plt.subplots()

        time, position = self.dynamics(car, road)
        print(position)
        x_axis = np.linspace(0, road.length, len(position))
        car_position, = ax.errorbar(x_axis, position, yerr = car.length/2, xerr=car.width/2) 

        def animate(i):
            car_position.set_ydata(position[i])  # update the data.
            return car_position,

        ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

