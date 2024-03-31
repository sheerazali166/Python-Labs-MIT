#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:00:20 2024

@author: sheeraz
"""

def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b -1)



print(mult_iter(5, 7))
print(mult(7, 9))            
      
  