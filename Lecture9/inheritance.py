#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:49:31 2024

@author: sheeraz
"""

"""
    INHERITANCE

"""

class Animal(object):
    
    def __init__(self, age):
        self.age = age
        self.name = None
        
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, newage):
        self.age = newage
        
    def set_name(self, newname=""):
        self.name = newname
        
        
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)
    
    
    
    
class Cat(Animal):
    
    def speak(self):
        print("meow")
        
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)
    

"""
    USING THE HIERARCHY

"""    
    
jelly = Cat(1)
jelly.set_name("JellyBelly")
print(jelly)
print(Animal.__str__(jelly))

blob = Animal(1)
print(blob)

blob.set_name()
print(blob)













    
    
    
    