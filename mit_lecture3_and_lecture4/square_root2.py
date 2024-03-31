#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:26:02 2024

@author: sheeraz
"""

x = 25
epsilon = 0.01
numGuesses = 0

low = 1.0
high = x

ans = (high + low) / 2.0

while abs(ans ** 2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    
    ans = (high + low) / 2.0
print("numGuesses = ", str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
    