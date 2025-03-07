import numpy as np
import car_class as c
import cars_class as cs
import road_class as r
import dynamics_class_example as d
import plotting_simulation as p
import matplotlib

# For the animated plot
matplotlib.use('TkAgg') 

# Set a time step for the whole simulation
time_step = 0.5

# Create at most 8 cars with different positions and speeds, assuring that the cars are on the road and not overlapping (otherwise the program will stop)
# Ensure that car 1 is the one at the front of the road, car 2 is the one behind car 1, etc
car = []
i = 0

for position in range(100,0,-8):
    car.append(c.Car(np.array([position - 3, position]), 10))
    i += 1

# Create a list of cars
cars = cs.Cars([car_i for car_i in car])

# Create a road with a starting position and an end position
road = r.Road(0, 160, vertical_position = 140)

initialize_dynamics = d.Dynamics_example(time_step)

animation, time_to_exit = p.animated_plot(cars, road, time_step, initialize_dynamics)
print(f'\nTime to clear the road: {time_to_exit} s')