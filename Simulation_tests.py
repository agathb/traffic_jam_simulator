import numpy as np
import car_class as c
import cars_class as cs
import road_class as r
import dynamics_class as d
import plotting_simulation as p
import matplotlib

# For the animated plot
matplotlib.use('TkAgg')

# Set a time step for the whole simulation
time_step = 0.5

# Create at most 8 cars with different positions and speeds, assuring that the cars are on the road and not overlapping (otherwise the program will stop)
# Ensure that car 1 is the one at the front of the road, car 2 is the one behind car 1, etc
car_1 = c.Car(np.array([40, 44]), 45)
car_2 = c.Car(np.array([36, 38]), 9)
car_3 = c.Car(np.array([31, 34]), 12)
car_4 = c.Car(np.array([27, 29]), 5)
car_5 = c.Car(np.array([21, 25]), 37)
car_6 = c.Car(np.array([17, 19]), 23)
car_7 = c.Car(np.array([12, 15]), 9)
car_8 = c.Car(np.array([5, 10]), 14)

# Create a list of cars
cars = cs.Cars([car_1, car_2, car_3, car_4, car_5, car_6, car_7, car_8])

# Create a road with a starting position and an end position
road = r.Road(0, 200, vertical_position = 160)

initialize_dynamics = d.Dynamics(time_step)

animation, time_to_exit = p.animated_plot(cars, road, time_step, initialize_dynamics)
print(f'\nTime to clear the road: {time_to_exit} s')