#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 02:44:02 2024

@author: sheeraz
"""

try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
    print("Okay")
except:
    print("Bug in user input.")
print("Outside")

    
    