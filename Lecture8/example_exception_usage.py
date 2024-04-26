#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 06:06:50 2024

@author: sheeraz
"""

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("Input not an integer; try again")
print("Correct input of an integer!")

        
        
    