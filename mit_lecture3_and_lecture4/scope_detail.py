#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:54:38 2024

@author: sheeraz
"""

# scope details

def g(x):
    def h():
        x = 'abc'
    x = x + 1

    print('in g(x): x =', x)

    h()

    return x

x = 3

z = g(x)

    