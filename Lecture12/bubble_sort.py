#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:02:51 2024

@author: sheeraz
"""

"""COMPLEXITY OF BUBBLE SORT"""

def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L            
                
L = [2, 5, 1, 9, 8, 3, 6, 7, 0, 4]

print(L)
print(bubble_sort(L))

"""
    inner for loop is for doing the comparisons
    outer while loop is for doing multiple passes until no more swaps
    
    O(n2) where n is len(L)
    to do len(L)-1 comparisons and len(L)-1 passes

"""                