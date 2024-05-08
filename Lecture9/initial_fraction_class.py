#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:44:07 2024

@author: sheeraz
"""

"""
    INITIAL FRACTION CLASS

"""

class fraction(object):
    
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)
    
    
oneHalf = fraction(1, 2)
twoThirds = fraction(2, 3) 

print(oneHalf)
print(twoThirds)


   
        