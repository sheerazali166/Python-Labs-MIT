#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:27:05 2024

@author: sheeraz
"""

"""COMPLEXITY OF SELECTION SORT"""

def selection_sort(L):
    suffixSt = 0
    """len(L) times => O(len(L))"""
    while suffixSt != len(L):
        """len(L) - suffixSt times => O(len(L))"""
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

    return L

L = [2, 5, 1, 9, 8, 3, 6, 7, 0, 4]
print(L)
print(selection_sort(L))


"""
    outer loop executes len(L) times
    inner loop executes len(L) – i times
    complexity of selection sort is O(n2) where n is len(L)
"""                   