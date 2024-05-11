#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:00:54 2024

@author: sheeraz
"""

"""
    LINEAR SEARCH ON UNSORTED LIST
"""


def linear_search(L, e):
    
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
   
    return found


        
        
            