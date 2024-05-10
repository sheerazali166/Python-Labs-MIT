#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:35:40 2024

@author: sheeraz
"""

"""WHEN THE INPUT IS A LIST…"""

def sum_list(L):
    
    total = 0
    
    for e in L:
        total = total + e
        
    return total


""" COMPLEXITY OF COMMON PYTHON FUNCTIONS """

"""
    Lists: n is len(L)
    
        • index O(1)
        • store O(1)
        • length O(1)
        • append O(1)
        • == O(n)
        • remove O(n)
        • copy O(n)
        • reverse O(n)
        • iteration O(n)
        • in list O(n
""" 

"""
    Dictionaries: n is len(d)
 
       worst case
       
        • index O(n)
        • store O(n)
        • length O(n)
        • delete O(n)
        • iteration O(n)

"""

"""
    average case
        
        • index O(1)
        • store O(1)
        • delete O(1)
        • iteration O(n)
"""   

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum_list(L))

