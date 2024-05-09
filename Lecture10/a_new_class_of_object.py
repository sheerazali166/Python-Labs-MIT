#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 08:20:51 2024

@author: sheeraz
"""

from building_inheritance import MITPerson
from adding_another_class import UG

"""A NEW CLASS OF OBJECT"""

class Professor(MITPerson):
    
    """this will shadow MITPerson speak method"""
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
        
    """note use of MITPerson speak"""
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)
    
        
    """note use of own speak method"""
    def lecture(self, topic):
        return self.speak('It is obvious that ' + topic)
        

"""EXAMPLE USAGE"""


print('************---------???---------****************')


"""uses MITPerson speak method"""

m1 = MITPerson('Gates')
print(m1.speak('hi there'))    



"""uses UG metthod speak method, which uses MITPerson method"""

s1 = UG('Damon', 2017)

print(s1.speak('hi there'))


"""uses professor speak method, which uses MITPerson method"""

faculty = Professor('Arrogant', 'Six')
print(faculty.speak('hi there'))


"""Lecture method uses Professor speak method"""

print(faculty.lecture('hi there'))


"""EXAMPLE USAGE"""

print("**************//////////------------///////////***************")


"""
    changes to MITPerson speak method affect all classes use as base 
    method for their own speak methods
"""



m1 = MITPerson('Mark Zuckerburg')
print(m1.speak('hi there'))

s1 = UG('Matt Damon', 2017)
print(s1.speak('hi there'))


faculty = Professor('Doctor Arrogant', 'Six')
print(faculty.speak('hi there'))











 




















    