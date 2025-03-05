import numpy as np
import car_class as c
import cars_class as cs
import road_class as r
import dynamics_class as d
import plotting_simulation as p
import matplotlib

# For the animated plot
matplotlib.use('TkAgg') 

# Set a time setp for the whole simulation
time_step = 0.5

''''''
# Create at most 8 cars with different positions and speeds, assuring that the cars are on the road and not overlapping (otherwise the program will stop)
# Ensure that car 1 is the one at the front of the road, car 2 is the one behind car 1, etc.
car_1 = c.Car(np.array([10, 14]), 5)
car_2 = c.Car(np.array([5, 9]), 9)
car_3 = c.Car(np.array([1, 4]), 12)

# Create a list of cars
cars = cs.Cars([car_1, car_2, car_3])

# Create a road with a starting position and an end position
road = r.Road(0, 500, vertical_position = 150)

initialize_dynamics = d.Dynamics(time_step)

p.animated_plot(cars, road, time_step, initialize_dynamics)
