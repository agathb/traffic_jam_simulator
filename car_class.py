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
                 initial_speed):
        
        self.initial_speed = initial_speed
        self.position = position
        
        