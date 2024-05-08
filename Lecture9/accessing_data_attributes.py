#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:51:04 2024

@author: sheeraz
"""

"""
    ACCESSING DATA ATTRIBUTES

"""

class fraction(object):
    
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)
    
    def getNumer(self):
        return self.numer
    
    def getDenom(self):
        return self.denom
    
    
# ACCESSING DATA ATTRIBUTES

oneHalf = fraction(1, 2)
twoThirds = fraction(2, 3)

print(oneHalf.getNumer())
print(fraction.getDenom(twoThirds))


