import numpy as np

class Dynamics_example:

    def __init__(self,
                 time_step):

        self.time_step = time_step

    def check_intial_car_positions(self, 
                                   cars, 
                                   road):

        # For each car in cars list
        for index, car in enumerate(cars):

            # If the front or back of each car is not on the road initially, stop the program
            if car.position[1] >= road.end_position or car.position[0] <= road.starting_position:
                raise ValueError(f'\nCar {index} is not on the road.')
            
           # For all the cars except the last car
            if index in range(len(cars)-1):

                # If the back of the car is overlapping with the front of the car behind, stop the program
                if car.position[0] < cars[index+1].position[1]: 
                    raise ValueError(f'\nCar {index} is overlapping with car {index+1}.')

    def no_impact(self, 
                  car, 
                  car_in_front):

        # If the front of the car is within 1m of the back of the car in front, return false
        if car.position[1] >= car_in_front.position[0] - 1:
            return False
        else :
            return True


    def dynamics(self,
                 cars, 
                 road):
        
        # Check the initial car position, will return an error if the cars are not on the road or overlapping
        self.check_intial_car_positions(cars, road)

        # Initialize the position history with the initial positions of the cars and set the time to 0
        position_history = [cars.get_positions()]
        time = 0
        initial_speed = cars.get_speeds()

        # While at least one car is still on the road, keep moving the cars.
        while np.any(cars.get_positions() < road.end_position) : 
            

            for index, car in enumerate(cars):

                # Create a copy of the car position before moving and a copy of the car position after moving
                before_moving = car.position.copy()
                after_moving = car.move(self.time_step)
                #car.speed = initial_speed[index]

                # If the car is the first car, it can always move because there is no car in front 
                if index == 0:
                    car.ability_to_move = True            
                # Else, check if moving does not make it impact the car in front (no_impact returns false if there is an impact)              
                else :
                    car.ability_to_move = self.no_impact(car, cars[index-1]) 
                    if index == 1 and time < 2:
                        car.speed = car.speed/4
                    elif index == 1 and time > 2:
                        car.speed = initial_speed[index]
                        

                # If the car can move (no impact with the car in front), update the car position to the new position
                if car.ability_to_move:
                    car.position = after_moving
                # Else, keep the car at the same position, effectively not making it move this time step
                else:
                    car.speed =  car.speed/2
                    if self.no_impact(car, cars[index-1]):
                        car.position = after_moving
                        car.speed = car.speed*2
                    else:
                        car.position = before_moving
                    #car.speed = initial_speed[index]*2
                    
                    

            # Append the positions of all the cars after one time step
            position_history.append(cars.get_positions().copy())
            time += self.time_step

        return time, position_history
