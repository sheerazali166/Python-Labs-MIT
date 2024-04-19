#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 22:59:39 2024

@author: sheeraz
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
    for i in range(n):
        result = []
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print("Yes")
    else:
        print("No")

#print(isPal('abcba'))        
#silly(4)

l = ['a', 'b', 'c', 'b', 'a']
p = ['p', 'a', 'l', 'i', 'n', 'n', 'i', 'l', 'a', 'p']
a = ['a', 'b']


print(isPal(l))
print(isPal(p))
print(isPal(a))

#silly(5)
#silly(10)
silly(2)       