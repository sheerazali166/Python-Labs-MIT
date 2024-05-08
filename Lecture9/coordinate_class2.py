#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:03:15 2024

@author: sheeraz
"""

class Coordinate(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        
        return (x_diff_sq + y_diff_sq) ** 0.5
    
"""
    HOW TO USE A METHOD FROM
    THE Coordinate CLASS

"""    


# conventional way

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(c.distance(origin))

# equivalent to 

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(Coordinate.distance(c, origin))


"""
    PRINT REPRESENTATION OF
    AN OBJECT

"""

c = Coordinate(3, 4)
print(c)
 
 











       