import numpy as np
import car_class as c
import road_class as r
import dynamics_class as d

time_step = 1

car1 = c.Car(np.array([1, 6]), 10)

print(car1.position)

road = r.Road(100)
#road.plot(car1)

dynamics = d.Dynamics(time_step)
dynamics.handmade_animated_plot(car1, road)