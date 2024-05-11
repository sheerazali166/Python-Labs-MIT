#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:00:54 2024

@author: sheeraz
"""

"""
    LINEAR SEARCH ON UNSORTED LIST
"""


def linear_search(L, e):
    
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
   
    return found


""" speed up a little by 
    returning True here, 
    but speed up doesn't
    impact worst case """


L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
e = 7
e = 3
e = 45

print(linear_search(L, e))


        
        
            