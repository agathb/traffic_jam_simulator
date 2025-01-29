import numpy as np

class Car:
    
    def __init__(self,
                 position,
                 speed,
                 time_step
                 movement_status):
        
        self.position = position
        self.speed = speed
        self.time_step = time_step

    def move(self, time_step):

        position_history = []
        time_step = np.array([time_step, time_step])
        current_time = 0

        while movement = True: # car.position[1] is the position of the front of the car
            position_memory.append(car.position[1])
            car.position += car.speed * time_step
            time += dt
            print(f'car at {car.position} after a time {time} s at speed {car.speed} m/s')

        return time, dt, position_memory

# Test
        
car1 = Car(np.array([1,2]), 2)

print(car1.position)