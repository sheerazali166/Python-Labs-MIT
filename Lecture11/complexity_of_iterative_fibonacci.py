#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:13:29 2024

@author: sheeraz
"""

""" COMPLEXITY OF ITERATIVE FIBONACCI """


def fib_iter(n):
    
    
    if n == 0:
        return 0
    
        """constant O(1)"""
    
    elif n == 1:
        return 1
    
    else:
        """constant O(1)"""
        fib_i = 0
        fib_ii = 1
        
        """linear O(1)"""
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
            
        """constant O(1)"""    
        return fib_ii                


print(fib_iter(10))
print(fib_iter(11))
print(fib_iter(12))
print(fib_iter(13))
print(fib_iter(14))
print(fib_iter(15))
print(fib_iter(16))




""" 
    Best case:
        
        O(1)
   
    Worst case:
        O(1) + O(n) + O(1) => O(n)

"""










