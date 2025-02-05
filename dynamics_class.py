import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Dynamics:

    def __init__(self,
                 time_step):

        self.time_step = time_step

    def dynamics(self,
                 road, 
                 *args):


        for index, car in enumerate(args):
            if car.position[1] >= road.end.position or car.position[0] <= road.starting_position: #if front of back of each car is not on the road initially, stop the ability to move
                car.ability_to_move = False
                print(f'\nCar {index} is not on the road.')
            else: # car is on the road, it can move
                car.ability_to_move = True
                print('All the cars are on the road, they may move.')
        
        position_history = [args.position.copy()]
        time = 0

        while time < 10 : #time is set to 100, can be changed

            for index, car in enumerate(args):

                if car.position[1] >= args(index+1).position[0] + 1: #if the front of the car is within 1m of the back of the car in front, stop the ability to move
                    car.ability_to_move = False
                    print(f'\nCar {index} is too close to the car in front at time ')

                if car.ability_to_move == True:
                    
                    current_position = car.move(self.time_step)
                    position_history.append(current_position.copy())
                    print(f'\nCar {index} is too close to the car in front at time {time}.')
                    break
                
            time += self.time_step
            
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