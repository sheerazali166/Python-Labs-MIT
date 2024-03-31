#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:49:30 2024

@author: sheeraz
"""

def factorial_iter(n):
    
    prod = 1
    
    for i in range(1, n+1):
        prod *= i
        
    return prod


def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        
 
print(factorial_iter(5))
print(factorial(6))        