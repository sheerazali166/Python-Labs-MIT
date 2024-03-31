#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:51:43 2024

@author: sheeraz
"""

x = 25
epsilon = 0.01

num_of_guesses = 0

low = 1.0
high = x

ans = (low + high) / 2.0

while abs(ans ** 2 - x) >= epsilon:
    print('Low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    num_of_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high) / 2.0
print('numGuesses' + str(num_of_guesses))

print(str(ans) + ' is close to square root of ' + str(x))   
        
        