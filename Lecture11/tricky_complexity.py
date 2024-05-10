#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:02:13 2024

@author: sheeraz
"""

"""TRICKY COMPLEXITY"""

def h(n):
    
    """assume n an int >= 0"""
    answer = 0
    s = str(n)
    
    """ linearO(len(s))
        but what in terms
        input of n? """
        
    for c in s:
        answer += int(c)
        
    return answer


print(h(10))

"""
 adds digits of a number together
 
 tricky part
    • convert integer to string
    • iterate over length of string, not magnitude of input n
    • think of it like dividing n by 10 each iteration
 
 O(log n)– base doesn’t matter

"""




    
    