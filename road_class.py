import numpy as np 
#import car_class as car 

class Road():   #This class as car as an input parameter
    def __init__(self, length = 100):
        self.length = length

    def dynamics(self, car):

        car.speed = car.initial_speed   # initial speed of the car
        distance = 0 # at the beginning of the road

        for dt in range(self.length):

            distance += car.speed * dt
            print(f'{distance} m travelled after a time {dt} s at speed {car.speed} m/s')

            if distance > self.length:
                print('End of road')
                break

        return car.speed
