#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 08:39:37 2024

@author: sheeraz
"""

def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x

x = 3
z = f(x)

print(z)