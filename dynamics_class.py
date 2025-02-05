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
        position_history = [car.position.copy()]
        time = 0

        while car.ability_to_move == True:

            current_position = car.move_straight(self.time_step)
            position_history.append(current_position.copy())
            time += self.time_step

            if car.position[1] >= road.length[1]:

                car.ability_to_move = False
                print(f'\nCar stopped at the end of the road after a time of {time} s.')

        return time, position_history

    
    # def animated_plot(self, car, road):
    #     fig, ax = plt.subplots()

    #     _, position_list = self.dynamics(car, road)
    #     position = np.array(position_list)
    #     #car_front, car_back = position[:,0], position[:,1]
    #     print(type(position),'position', position, 'position1', position[1])
    #     center_car_position = position[:,0] + car.length/2
    #     #print('center is',center_car_position)
    #     x_axis = np.linspace(0, road.length[1], len(position))
    #     #print(len(x_axis), len(center_position))
    #     car_position, = ax.plot(x_axis, center_car_position, 'x')
    #     #car_position, ( car_bottom, car_tops), verts = ax.errorbar(x_axis, center_car_position, yerr = car.width/2, xerr=car.length/2, fmt='o') 
    #     #road_position = ax.plot(x_axis, road.map(x_axis), color='black')
    #     #y_err = car.width/2
    #     #x_err = car.length/2
        
    #     def init():
    #         car_position.set_data([], [])
    #         return car_position,

    #     def animate(i):
    #         car_position.set_xdata(position[i])  # update
    #         return car_position,

    #     ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(center_car_position), interval=20, blit=False, repeat = False)

    #     plt.show()

    #     return ani

    def handmade_animated_plot(self, car, road):

        time, position_list = self.dynamics(car, road)
        position = np.array(position_list)
        x_linsp = np.linspace(0, len(position), len(position))  
        print(position, x_linsp)

        for t in range(time):
            
            if t == 0:
                line, = plt.plot([], [])
            else: 
                line.set_xdata(position[t])
                line.set_ydata(np.ones(len(position[t])))
            plt.pause(0.1)

        plt.show()          


       
