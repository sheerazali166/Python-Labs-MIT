#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:03:36 2024

@author: sheeraz
"""

def printName(firstName, lastName, reverse):

    if reverse:
        
        print(lastName + ', ' + firstName)
    
    else:
        
        print(firstName, lastName)
        

printName('Mr', 'Hacker',reverse= True) 

printName('Eric', 'Grimson', False)
printName('Eric', 'Grimson', reverse = False)
printName('Eric', lastName = 'Grimson', reverse = False)
printName(lastName = 'Eric', firstName = 'Grimson', reverse = False)                     