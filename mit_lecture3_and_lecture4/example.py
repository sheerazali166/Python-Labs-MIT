#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 07:29:42 2024

@author: sheeraz
"""

# Doing this in python

num = 78
isNeg = False

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''

if num == 0:
    result = ''
while num > 0:
    result = str(num%2) + result
    num = num // 2
if isNeg:
    result = '-' + result
    
print(result)    