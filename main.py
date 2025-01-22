import sys

sys.path.append('/Users/fcalavaro/Documents/GitHub/traffic_jam_simulator/')

import numpy as np
import car_class as c
import road_class as r

car1 = c.Car(np.arange(1, 3, 1), 2)

print(car1.initial_position)
