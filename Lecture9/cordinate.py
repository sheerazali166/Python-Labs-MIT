#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:41:05 2024

@author: sheeraz
"""

class Coordinate(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
"""
    ACTUALLY CREATING AN
    INSTANCE OF A CLASS

"""

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(c.x)
print(origin.x)        