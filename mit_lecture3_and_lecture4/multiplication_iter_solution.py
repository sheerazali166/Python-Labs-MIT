#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:33:23 2024

@author: sheeraz
"""

def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
        
    return result

print(mult_iter(3, 4))    