#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:57:36 2024

@author: sheeraz
"""

"""MERGING SUBLISTS STEP"""


def merge(left, right):
    result = []
    i, j = 0, 0
    """:- left right sublists
          are ordered - move indices for
          sublist deping on which sublist holds
          next smallest element """
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    """when right sublist is empty"""
    while (i < len(left)):
        result.append(left[i])
        i += 1
    """when left sublists is empty"""
    while(j < len(right)):
        result.append(right[j])
        j += 1
    return result


L = [1, 2, 3]
L2 = [1, 2, 3, 4, 5, 6]
L1 = [2, 5, 1, 9, 8, 3, 6, 7, 0, 4]
print(merge(L, L2))        
print("*********************")
print(merge(L, L1))
print("*********************")
print(merge(L1, L2))      

