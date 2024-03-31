#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 08:38:46 2024

@author: sheeraz
"""

def fib(x):
    """
        Assume x an int >= 0
        return fibbonacci of x
    
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

print(fib(3))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(9))
print(fib(10))
print(fib(11))
print(fib(12))
print(fib(13))
print(fib(14))
print(fib(15))
print(fib(16))
print(fib(18))   

print("i said no husky")
print("Bravo")    