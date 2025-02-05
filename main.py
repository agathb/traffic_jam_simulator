import numpy as np
import car_class as c
import road_class as r
import dynamics_test as d
import matplotlib

matplotlib.use('TkAgg') # For the animated plot.

time_step = 0.1

car = c.Car(np.array([1, 4]), 5)

print(f'\nCar starting position of the car: {car.position}')

road = r.Road(1, 100)

dynamics = d.Dynamics(time_step)
dynamics.handmade_animated_plot(car, road)