#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:16:07 2024

@author: sheeraz
"""

cube = 27
epsilon = 0.01
num_of_guesses = 0
low = 1
high = cube

guess = (low + high) / 2

while abs(guess ** 3 - cube) >= epsilon:
    if guess ** 3 < cube:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0
    num_of_guesses += 1    
    
print("num_guesses =", num_of_guesses)
print(guess, "is close to the cube root of", cube)