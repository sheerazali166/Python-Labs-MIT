#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:22:55 2024

@author: sheeraz
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
    
    def __add__(self, other):
        
        numerNew = other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
        
        denomNew = other.getDenom() * self.getDenom() 
        return fraction(numerNew, denomNew)
    
    def convert(self):
        return self.getNumer() / self.getDenom()
    
    
    
""" ADDING MORE METHODS """

oneHalf = fraction(1, 2)
twoThirds = fraction(2, 3)

new = oneHalf + twoThirds

print(oneHalf)
print(twoThirds)
print(new)

print(new.convert())



    
    
    
    
    