import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Dynamics:

    def __init__(self,
                 time_step):

        self.time_step = time_step

    def dynamics(self,
                 road, 
                 cars):


        for index, car in enumerate(cars):
            if car.position[1] >= road.end_position or car.position[0] <= road.starting_position: #if front of back of each car is not on the road initially, stop the ability to move
                car.ability_to_move = False
                print(f'\nCar {index} is not on the road.')
            else: # car is on the road, it can move
                car.ability_to_move = True
                print(f'Car {index} is on the road, it may move.')
        
        position_history = [cars.get_positions()]
        time = 0

        while cars[0].position[1] <= road.end_position : #while the first car is still on the road, keep moving the cars

            # Stop the cars if they are too close to the car in front
            for k in range(len(cars)-1):

                if cars[k].position[1] >= cars[k+1].position[0] + 1: #if the front of the car is within 1m of the back of the car in front, stop the ability to move
                    cars[k].ability_to_move = False
                    print(f'\nCar {k} stoped bc it is too close to the car {k+1} in front at time {time} ')
                else:
                    cars[k].ability_to_move = True

            # Move the cars that have the ability to move
            for k in range(len(cars)):

                if cars[k].ability_to_move == True:
                    
                    current_position = cars[k].move(self.time_step)
                    position_history.append(current_position.copy())
                    print(f'\nCar {k} is at {current_position} at {time}.')
                    
                
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