#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:40:14 2024

@author: sheeraz
"""

def bisect_search1(L, e):
    """constant O(1)"""
    if L == []:
        return False

    #"""constant O(1)"""
    elif len(L) == 1:
        return L[0] == e
    else:
        """constant O(1)"""
        half = len(L)//2
        if L[half] > e:
            """not constant, copies list"""
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)
        
        
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

e = 6

print(bisect_search1(L, e))


            