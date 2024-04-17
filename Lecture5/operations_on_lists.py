#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:23:40 2024

@author: sheeraz
"""

L = [2, 1, 3]
print(L)

L.append(5)  # L is now [2,1,3,5]
print(L)

L1 = [2, 1, 3]

L2 = [4, 5, 6]

L3 = L1 + L2

#  L3is [2,1,3,4,5,6]
print(L3)

# mutated L1to [2,1,3,0,6]
L1.extend([0,6])

print(L1)