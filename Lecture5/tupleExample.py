#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:20:58 2024

@author: sheeraz
"""

t = ()
t = (2, "One", 3)

print(t[0])

print((2, "One", 3) + (5, 6))

print(t[1: 2])

print(t[1: 3])

""" gives error, can’t modify object 

    'tuple' object does not support item assignment

"""
#t[1] = 4 

"""
conda update anaconda
conda install spyder=5.5.1

"""