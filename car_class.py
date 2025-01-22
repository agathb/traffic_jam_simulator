#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:42:53 2025

@author: fcalavaro
"""

import numpy as np
import sys

sys.path.append('/Users/fcalavaro/Documents/GitHub/traffic_jam_simulator/car_class.py')

class Car:
    
    def __init__(self,
                 initial_position,
                 initial_speed):
        
        self.initial_position = initial_position
        self.initial_speed = initial_speed
        
        
        
# Test
        
car1 = Car(np.array([1,2]), 2)

print(car1.initial_position)
        
        