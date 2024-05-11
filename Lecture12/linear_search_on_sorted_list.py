#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:18:18 2024

@author: sheeraz
"""

"""LINEAR SEARCH ON SORTED LIST"""

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


L = [1, 2, 3, 4, 5, 6]
e = 5

print(search(L, e))    
        