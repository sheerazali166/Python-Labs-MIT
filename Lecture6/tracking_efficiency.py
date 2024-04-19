#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:19:40 2024

@author: sheeraz
"""

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
def fibef(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fibef(n-1, d) + fibef(n-2, d)
        d[n] = ans
        return ans
    

# TRACKING EFFICIENCY

numFibCalls = 0

print(fib(12))
print('function calls', numFibCalls)

numFibCalls = 0

d = {1:1, 2:2}

print(fibef(12, d))
print('function calls', numFibCalls)
    