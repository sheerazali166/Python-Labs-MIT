#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:14:13 2024

@author: sheeraz
"""

def intToStr(i):
    
    digits = '0123456789'
    if i == 0:
        return '0'
    
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10   
    return result
"""
def intToStr(i):
    
    digits = '0123456789'
    if i == 0:
        return '0'
    
    result = ''
    count = 0
    while i > 0:
        result = digits[i%10] + result
        i = i//10
        count = count + 1    
    return result, count
"""

"""

def intToStr(i):
    
    digits = '0123456789'
    if i == 0:
        return '0'
    
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return 'result: ' + result

"""

print(intToStr(0))  
print(intToStr(10))  
  
""" only have to look at loop as
    no function calls
    within while loop, constant
    number of steps
    how many times through
    loop?
    how many times can one
    divide i by 10?
    O(log(i)) """





        