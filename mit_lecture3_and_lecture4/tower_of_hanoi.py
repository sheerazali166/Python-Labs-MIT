#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:09:20 2024

@author: sheeraz
"""

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(n, fr, spare, to)
        Towers(n-1, spare, to, fr)
        
        
        