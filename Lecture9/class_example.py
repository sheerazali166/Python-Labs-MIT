#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:12:35 2024

@author: sheeraz
"""

"""
    DEFINING A CLASS

"""

class Animal(object):
   
    def __init__(self, age):
        self.age = age
        self.name = None
        
        
myanimal = Animal(3)
print(myanimal)
        
        
        
        