#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 00:18:12 2024

@author: sheeraz
"""

"""
    STEPPING THROUGH
"""

def isPal(x):
    assert type(x) == list
    temp = x[:]
    print('before reverse', temp, x)
    temp.reverse()
    print('after reverse', temp, x)
    
    if temp == x:
        return True
    else:
        return False
    
def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
        
    if isPal(result):
        print('Yes')
    else:
        print('No')
        
l = ['a', 'b', 'c', 'b', 'a']
p = ['p', 'a', 'l', 'i', 'n', 'n', 'i', 'l', 'a', 'p']
a = ['a', 'b']


print(isPal(l))
print(isPal(p))
print(isPal(a))

silly(5)
silly(10)
silly(2)

print('Bravo')         