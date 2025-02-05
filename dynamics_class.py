import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Dynamics:

    def __init__(self,
                 time_step):

        self.time_step = time_step

    def dynamics(self,
                 car,
                 road):

        
        position_history = [car.position.copy()]
        time = 0
        # set it to false if outside of road

        # car is on the road, it can move
        car.ability_to_move = True

        while car.ability_to_move == True:

            current_position = car.move(self.time_step)
            position_history.append(current_position.copy())
            time += self.time_step

            if car.position[1] >= road.length:

                car.ability_to_move = False
                print(f'\nCar stopped at the end of the road after a time of {time} s.\n')
        # obstacle list input as *args, that stops the ability to move if near obstacle


        return time, position_history

    def handmade_animated_plot(self, car, road):
        time, position_list = self.dynamics(car, road)
        position = np.array(position_list)
        x_linsp = np.linspace(0, road.length, len(position))
        x_axis = np.ones(len(position))

        fig, ax = plt.subplots()
        line, = ax.plot([], [])
        ax.set_xlim([0, road.length])
        ax.set_ylim([0, road.length])

        def update(frame):

            line.set_xdata([x_axis[frame], x_axis[frame]])
            line.set_ydata(position[frame])

            return line,

        ani = animation.FuncAnimation(fig, update, frames=len(position), interval=100, blit=True)
        plt.show()
#pause button, timer, roads
        return ani
