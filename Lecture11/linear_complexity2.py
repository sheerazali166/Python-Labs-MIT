#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:14:35 2024

@author: sheeraz
"""

""" complexity can depend on number of recursive calls """

def fact_iter(n):
    
    prod = 1
    for i in range(1, n + 1):
        prod *= i
        
    return prod

print(fact_iter(10))
print(fact_iter(11))

""" O() FOR RECURSIVE
    FACTORIAL """
    
    
def fact_recur(n):
    
    """ assume n >= 0 """    
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n-1)
    
print('*****************')
print(fact_recur(10))



    
        
    
    