#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:27:41 2024

@author: sheeraz
"""

class Coordinate(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.x - other.y) ** 2
        
        return (x_diff_sq + y_diff_sq) ** 0.5
    
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
"""
    WRAPPING YOUR HEAD
    AROUND TYPES AND CLASSES

"""

c = Coordinate(3, 4)
print(c)
    
print(type(c))

# this makes sense since
print(Coordinate, type(Coordinate))

"""
    use isinstance() to check if an object is a Coordinate

"""

print(isinstance(c, Coordinate))





