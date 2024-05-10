#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:28:49 2024

@author: sheeraz
"""

""" COMPLEXITY OF RECURSIVE FIBONACCI """


def fib_recur(n):
    
    """ assumes n an int >= 0 """
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)
        
 
""" Worst case:
        O(2n) """



print(fib_recur(10))      