import numpy as np
import car_class as c
import road_class as r

car1 = c.Car(np.array([1, 2]), 2)

print(car1.initial_position)

road = r.Road()
road.plot(car1)