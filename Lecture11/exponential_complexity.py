#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:14:51 2024

@author: sheeraz
"""


"""EXPONENTIAL COMPLEXITY"""

def genSubsets(L):
    
    res = []
    if len(L) == 0:
        return [[]] #list of empty list
    
    smaller = genSubsets(L[:-1])  # all subsets without last element
    
    extra = L[-1:]  # create a list of just last element
    
    new = []
    
    for small in smaller:
        new.append(small + extra) # for all smaller solutions, add one with last element
    
    return smaller + new  # combine those with last element and those without

"""
    assuming append is
    constant time
    
    time includes time to solve
    smaller problem, plus time
    needed to make a copy of
    
    all elements in smaller
    problem

"""    

"""
    but important to think
    about size of smaller
    
    know that for a set of size
    k there are 2k cases
    so to solve need 2n-1 + 2n-2
    
    + … +20 steps
    math tells us this is O(2n)

"""

L = [1, 2, 3, 4, 5, 6]

print(genSubsets(L))

lSub = genSubsets(L)


for s in lSub:
    print(s)
    
    
print('Bravo')

"""COMPLEXITY CLASSES"""
"""
    O(1) denotes constant running time
    
    O(log n) denotes logarithmic running time
    
    O(n) denotes linear running time
    
    O(n log n) denotes log-linear running time
    
    O(nc) denotes polynomial running time (c is a
    constant)
    
    O(cn) denotes exponential running time (c is a
    constant being raised to a power based on size of
    input)

"""




    
    
    





















        


    
    
    




