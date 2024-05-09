#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 01:58:49 2024

@author: sheeraz
"""

import datetime

class Person(object):
    
    def __init__(self, name):
        """create a person called name""" 
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        
    def getLastName(self):
        """return self's last name"""
        return self.lastName
    
    def __str__(self):
        """return self's name"""
        return self.name
    
    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        
        """returns self's current age in days"""
        if self.birthday == None:
            
            raise ValueError
       
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        
        """ return True if self's name is lexicographically
          less than other's name, and False otherwise """
               
        if self.lastName == other.lastName:
            
            return self.name < other.name
      
        return self.lastName < other.lastName



"""BUILDING INHERITANCE"""



class MITPerson(Person):
    
    nextIdNum = 0 # next ID number to assign
    
    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.idNum = MITPerson.nextIdNum  # MITPerson attribute: unique ID
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    
    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum  < other.idNum
    """
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)
    """
    
    """change MITPERSON’s speak method to"""
    def speak(self, utterance):
        return self.name + ' says: ' + utterance
    
    

"""EXAMPLE"""

m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3, 5, 14, 84)

m2 = MITPerson('Drew Houston')
Person.setBirthday(m2, 3, 4, 83)

m1 = MITPerson('Bill Gates')
Person.setBirthday(m1, 10, 28, 55)

MITPersonList = [m1, m2, m3]


"""EXAMPLE OF SORTING BY <"""

for e in MITPersonList:
    print(e)


print('--------*************----------')


MITPersonList.sort()

for e in MITPersonList:
    print(e)



print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

"""EXAMPLE USING HIERARCHY"""

p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')
    
"""TRY TO COMPARE"""
print(p1 < p2) 
#print(p2 < p4)
"""AttributeError: 'Person' object has no attribute 'idNum'"""

print(p4 < p1)




   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    