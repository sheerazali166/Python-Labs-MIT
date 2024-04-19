#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:54:40 2024

@author: sheeraz
"""

"""
     GLASS BOX TESTING
     explore paths through code

"""

def abs(x):

    """
        Assumes x is an int
        Returns x if x>=0 and –x otherwise

    """
    if x < -1:
        return -x
    else:
        return x
    
print(abs(10))
print(abs(-10))    
    