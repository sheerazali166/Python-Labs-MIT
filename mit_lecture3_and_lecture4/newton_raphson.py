#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 08:07:21 2024

@author: sheeraz
"""

epsilon = 0.01
y = 24.0

guess = y / 2.0

numGuesses = 0

while abs(guess * guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess ** 2) - y)/ (2*guess))
    
print("numGuesses = " + str(numGuesses))
print('Square root of ' + str(y) + ' is about' + str(guess))

