#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:42:53 2025

@author: fcalavaro
"""

import numpy as np

class Car:
    
    def __init__(self,
                 position,
                 speed):
        
        self.position = position
        self.speed = speed
        
        
        
# Test
        
car1 = Car(np.array([1,2]), 2)

print(car1.position)
        
        