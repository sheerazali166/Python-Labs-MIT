#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:16:07 2024

@author: sheeraz
"""

def printName(firstName, lastName, reverse = True):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)
        

printName('Eric', 'Grimson')
printName('Eric', 'Grimson', True)        