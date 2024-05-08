#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:29:29 2024

@author: sheeraz
"""

class Animal(object):
    
    def __init__(self, age):
        self.years = age
        
    def get_age(self):
        return self.years
    
    
a = Animal(3)    
    
#print(a.age)

print(a.years)

a.size = "tiny"

print(a.size)

def get_age(self):
    a.get_age()
    Animal.get_age(a)



print(get_age(3))

def set_name(self, newname=""):
    a.set_name()
    a.set_name("fluffy")
    
 
    