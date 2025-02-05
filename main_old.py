import numpy as np
import car_class as c
import road_class as r
import dynamics_class_old as d
import plotting_simulation as p
import matplotlib

matplotlib.use('TkAgg') # For the animated plot.

time_step = 0.5

car = c.Car(np.array([1, 4]), 5)

print(f'\nCar starting position of the car: {car.position}')

road = r.Road(0, 80)

initialize_dynamics = d.Dynamics(time_step)

p.animated_plot(car, road, time_step, initialize_dynamics)