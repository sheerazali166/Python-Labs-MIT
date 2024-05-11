#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:04:38 2024

@author: sheeraz
"""

"""BISECTION SEARCH IMPLEMENTATION 2"""


def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                """not constant"""
                return bisect_search_helper(L, e, low, mid-1)
        else:
            """not constant"""
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
    

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

e = 99

print(bisect_search2(L, e))

        
    
    

            
        
