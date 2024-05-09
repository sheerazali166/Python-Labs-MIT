#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 07:16:25 2024

@author: sheeraz
"""

"""
    MORE CLASSES IN HIERARCHY

"""

from building_inheritance import MITPerson


class UG(MITPerson):
    
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
        
    def getClass(self):
        return self.year        
    
    def speak(self, utterance):
        return MITPerson.speak(self," Dude, " + utterance)
    

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj, UG) or isinstance(obj, Grad)


"""EXAMPLE"""

s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = UG('Leonardo di Caprio', 2029)

print(s1)
print(s1.getClass())
print(s1.speak('where is the quiz?'))
print('I have no clue!')

"""TypeError: UG.__init__() missing 1 required positional argument: 'classYear'"""










