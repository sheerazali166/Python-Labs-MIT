#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:19:18 2024

@author: sheeraz
"""


"""AN EXAMPLE: compound interest"""
def retire(monthly, rate, terms):
    saving = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        saving += [saving[-1] * (1 + mRate) + monthly]
        
    return base, saving 

 
monthly = 5600
rate = .05
terms = 40 * 12   

print(retire(monthly, rate, terms))    