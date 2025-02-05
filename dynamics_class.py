class Dynamics:

    def __init__(self,
                 time_step):

        self.time_step = time_step

    def dynamics(self,
                 road, 
                 cars):

        for index, car in enumerate(cars):

            # If the front or back of each car is not on the road initially, stops the ability to move.
            if car.position[1] >= road.end_position or car.position[0] <= road.starting_position:

                car.ability_to_move = False
                print(f'\nCar {index} is not on the road.')

            else: # The car is on the road, so it can move.
                car.ability_to_move = True
                print(f'\nCar {index} is on the road, at {car.position} it may move.')
        
        position_history = [cars.get_positions()]
        time = 0

        while cars[0].position[1] < road.end_position : # While the first car is still on the road, keep moving the cars.

            # Stops the cars if they are too close to the car in front.
            for k in range(len(cars)-1, 1, -1): # The loop starts with the last car and goes to the first car.

                # If the front of the car is within 1m of the back of the car in front, this stops the ability to move.
                if cars[k].position[1] >= cars[k-1].position[0] - 1:

                    cars[k].ability_to_move = False
                    print(f'\nCar {k} at position {cars[k].position[1]} and car {k-1} at position {cars[k-1].position[0]}')
                    print(f'\nCar {k} stopped at {cars[k].position[1]} because it is too close to the car {k-1} at {cars[k-1].position[0]} in front, at time {time}')

                else:

                    cars[k].ability_to_move = True

            # Moves the cars that have the ability to move.
            for k in range(len(cars)):

                print(f'\nCar {k} is at {cars[k].position} at {time}.')

                if cars[k].ability_to_move == True:
                    
                    cars[k].position = cars[k].move(self.time_step)
                    #print(f'\nCar {k} is at {cars[k].position} at {time}.')

            position_history.append(cars.get_positions().copy())
                
            time += self.time_step

        print(f'\nFinal positions of the cars: {cars.get_positions()}')
        print(f'\nPosition history: {position_history}')

        return time, position_history

'''

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

        return ani

    '''