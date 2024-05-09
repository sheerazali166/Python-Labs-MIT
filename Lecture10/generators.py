#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:47:31 2024

@author: sheeraz
"""

def genTest():
    
    yield 1
    yield 2
    
    
print(genTest())

foo = genTest()

"""
    Execution will proceed in body of foo, untill
    reaches first yield statement; then returns 
    value associateed with that statement
"""

print(foo.__next__())
print(foo.__next__())


"""
    Execution will resume in body of foo at point
    where stopped, untill reaches next yield statement;
    then return value associated with that statement
"""


#print(foo.__next__())

"""Results in a StopIteration exception"""
print("***************")    

"""
    USING GENERATORS 
    can use a generator inside a looping structure, as it will
    continue until it gets a StopIteration exception:
"""



for n in genTest():
    print(n)







