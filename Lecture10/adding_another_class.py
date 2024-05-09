#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 07:49:53 2024

@author: sheeraz
"""

from building_inheritance import MITPerson



"""CLEANING UP HIERARCHY"""
class Student(MITPerson):
    pass
              

"""ADDING ANOTHER CLASS"""

class UG(MITPerson):
    
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    """
    def speak(self, utterance):
        return MITPerson.speak(self, " Dube, " + utterance)
    """
    """change UG’s speak method to"""

    def speak(self, utterance):
        return MITPerson.speak(self, ' Yo Bro, ' + utterance)

class Grad(MITPerson):
    pass


"""Now i have to rethink isStudent"""
"""All about mind set"""

class TransferStudent(MITPerson):
    pass

def isstudent(obj):
    return isinstance(obj, UG) or isinstance(obj, Grad)


"""EXAMPLE"""

s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo Di Caprio')
s5 = TransferStudent('Robert diNiro')

print('*************/---------------/***************')

print(s1)
print(s1.getClass())
print(s1.speak('where is the quiz?'))
print(s2.speak('I have no clue!'))






























        