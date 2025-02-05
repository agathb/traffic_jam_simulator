import numpy as np
import car_class as c
import road_class as r
import dynamics_class as d
import matplotlib

matplotlib.use('TkAgg')

time_step = 1

car1 = c.Car(np.array([1, 6]), 10)

print(car1.position)

road = r.Straight_Road([1,1], [70, 70])

dynamics = d.Dynamics(time_step)
dynamics.handmade_animated_plot(car1, road)