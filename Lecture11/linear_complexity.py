#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:34:35 2024

@author: sheeraz
"""

def addDigits(s):
    
    
    val = 0
    
    for c in s:
        val += int(c)
        
    return val

""" O(len(s)) """

s = '01234566789'
print(addDigits(s))







    
        


