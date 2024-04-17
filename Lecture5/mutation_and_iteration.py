#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:38:38 2024

@author: sheeraz
"""

"""

    avoid mutating a list as you are iterating over it

"""

L1 = [2, 6, 3]

L2 = [4, 5, 6]

""" XXXXXXXX """

def remove_dums(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
        print(e)    
            

remove_dums(L1, L2)  

"""  YES """ 

print()

def remove_dums_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
        print(e)    
        
        
remove_dums_new(L1, L2)

       