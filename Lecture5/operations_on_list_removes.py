#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:20:27 2024

@author: sheeraz
"""

# # do below in order
L = [2, 1, 3, 6, 3, 7, 0]
print(L)

L.remove(2) # L = [1,3,6,3,7,0] 
print(L)

L.remove(3) # mutates L = [1,6,3,7,0]
print(L)

del L[1] # [1,3,7,0]
print(L)

L.pop() #  returns 0 and mutates L = [1,3,7]
print(L)