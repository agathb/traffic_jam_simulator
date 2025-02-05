class Dynamics:

    def __init__(self,
                 time_step):

        self.time_step = time_step

    def dynamics(self,
                 car,
                 road):

        position_history = [car.position.copy()]
        time = 0

        # The car is on the road, so it can move.
        car.ability_to_move = True

        while car.ability_to_move:

            current_position = car.move(self.time_step)
            position_history.append(current_position.copy())
            time += self.time_step

            if car.position[1] >= road.length:
                car.ability_to_move = False
                print(f'\nCar stopped at the end of the road after a time of {time} s.\n')

        return time, position_history