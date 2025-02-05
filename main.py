import numpy as np
import car_class as c
import road_class as r
<<<<<<< Updated upstream
import dynamics_test as d
=======
import dynamics_class as d
import cars_class as cs
>>>>>>> Stashed changes
import matplotlib

matplotlib.use('TkAgg') # For the animated plot.

time_step = 0.1

car1 = c.Car(np.array([5, 8]), 5)
car2 = c.Car(np.array([2, 4]), 5)

#print(f'\nCar starting position of the car: {car.position}')

road = r.Road(1, 100)

dynamics = d.Dynamics(time_step)
#dynamics.dynamics(road, car1, car2)

car_lists = cs.Cars([car1, car2])
print(car_lists.get_positions())

#dynamics.handmade_animated_plot(car, road)