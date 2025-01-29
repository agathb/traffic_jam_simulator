import numpy as np
import car_class as c
import road_class as r

time_step = 1

car1 = c.Car(np.array([1, 6]), 10)

print(car1.position)

road = r.Road()
road.plot(car1)