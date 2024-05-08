#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:16:59 2024

@author: sheeraz
"""

class Animal(object):
    
    def __init__(self, age):
        self.age = age
        self.Name = None
           
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, newage):
        self.age = newage
        
    def set_name(self, newname = ""):
        self.name = newname
        
        
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)
    
    
a = Animal(3)

print(a.age)
print(a.get_age())    
        
        