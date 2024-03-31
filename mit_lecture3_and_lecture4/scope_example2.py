#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:26:30 2024

@author: sheeraz
"""

def f(y):
    x = 1
    x += 1
    print(x)
    
x = 5
f(2)
print(x)

print("*************")

def g(y):
    print(x)

x = 5
g(2)
print(x)

print("*************")



def h(y):
    x = x + 1
    
x = 5
h(2)
print(x)    
