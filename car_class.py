#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:42:53 2025

@author: fcalavaro
"""

import numpy as np

class Car:
    
    def __init__(self,
                 initial_position,
                 initial_speed):
        
        self.initial_position = initial_position
        self.initial_speed = initial_speed
        
car1 = Car(np.arange(1, 3, 1), 2)

print(car1.position)
        
        