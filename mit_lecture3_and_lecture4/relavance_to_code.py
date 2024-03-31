#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:13:47 2024

@author: sheeraz
"""

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b - 1)

print(mult(3, 4))
print(mult(6, 9))

    