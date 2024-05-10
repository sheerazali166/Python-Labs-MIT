#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:05:16 2024

@author: sheeraz
"""

""" O() FOR NESTED LOOPS """

def g(n):
    
    """ assume n >= 0 """
    
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    
    return x


print(g(10))  
print(g(11)) 

""" computes n2 very inefficiently
    when dealing with nested loops, look at the ranges
    nested loops, each iterating n times
    O(n2) """
    
    
    
       