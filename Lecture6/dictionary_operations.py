#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:38:34 2024

@author: sheeraz
"""

grades = { 'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A' }

print(grades)

# add an entry
grades['Sylvan'] = 'A'

print(grades)

# test if key in dictionary

print('John' in grades)

print('Daniel' in grades)

# delete entry
del (grades['Ana'])

print(grades)

"""
        DICTIONARY
       OPERATIONS

"""

grades = { 'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A'  }

"""
    get an iterable that acts like a tuple of all keys

"""

print()

print(grades.keys())

"""
    get an iterable that acts like a tuple of all values

"""

print(grades.values())

# no order to keys or values!

d = {4: {1: 0}, (1, 3): "twelve", "const": [3.14, 2.7, 8.44]}

print()
print(d)










