#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:12:07 2024

@author: sheeraz
"""

L = [2, 1, 3]
print(L)

L[1] = 5
print(L)

total = 0

for i in range(len(L)):
    total += L[i]
    
print(total)

total = 0

# like strings, can iterate over list elements directly
for i in L:
    total += i
    print(total)    