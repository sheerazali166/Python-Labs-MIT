#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:49:07 2024

@author: sheeraz
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


class Person(Animal):
    
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
        
    def get_friends(self):
        return self.friends
    
    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")
    
    
    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        
        
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
        
        def __str__(self):
            return "person:" + str(self.name) + ":" + str(self.age)
        
        
"""USING THE HIERARCHY""" 

eric = Person("Eric", 45)
john = Person('John', 55)

eric.speak()

eric.age_diff(john)

Person.age_diff(john, eric)












       
        
        
        
        
        
        
        
        
   
        
        










    
    

            