#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 23:44:04 2024

@author: sheeraz
"""

"""
    STEPPING THROUGH
"""

def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False
    
def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter Element: ')
        result.append(elem)
        print(result)
    
    if isPal(result):
        print('Yes')
    else:
        print('Yes')
        
        
l = ['a', 'b', 'c', 'b', 'a']
p = ['p', 'a', 'l', 'i', 'n', 'n', 'i', 'l', 'a', 'p']
a = ['a', 'b']


print(isPal(l))
print(isPal(p))
print(isPal(a))

silly(5)
silly(10)
silly(2)        
    