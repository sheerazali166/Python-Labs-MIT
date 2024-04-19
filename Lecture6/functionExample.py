#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:29:06 2024

@author: sheeraz
"""

import math


def applyToEach(L, f):

    """
        assumes L is a list, f a function
        mutates L by replacing each element,
        e, of L by f(e)
    
    """
    
    for i in range(len(L)):
        L[i] = f(L[i])
        
   
    # ?
    return L    
        
L = [1, -2, 3.4]

print(applyToEach(L, abs))

print(applyToEach(L, int))

#applyToEach(L, fact)
 
#applyToEach(L, fib)       


"""

    LISTS OF FUNCTIONS    

"""

print()

def applyFuns(L, x):
    for f in L:
        print(f(x))
        
        
        
        

#applyFuns([abs, int, fact, fib], 4)

applyFuns([abs, int], 4)

print()

for elt in map(abs, [1, -2, 3, -4]):
    print(elt)
    
"""

    general form – an n-ary function and n collections of arguments

"""    
 
print()
   
L1 = [1, 28, 36]
L2 = [2, 57, 9]

for elt in map(min, L1, L2):
    print(elt)
    
    
    









