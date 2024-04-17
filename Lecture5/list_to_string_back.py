#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:37:27 2024

@author: sheeraz
"""

s = "I <3 cs" #  s is a string

print(list(s)) # returns ['I',' ','<','3',' ','c','s']

print(s.split('<')) # returns ['I ', '3 cs']

L = ['a', 'b', 'c'] #  L is a list

print(''.join(L)) # returns "abc"

print('_'.join(L)) # returns "a_b_c"

