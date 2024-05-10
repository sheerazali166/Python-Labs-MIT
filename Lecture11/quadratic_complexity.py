#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:34:12 2024

@author: sheeraz
"""

""" QUADRATIC COMPLEXITY """

def isSubset(L1, L2):
    
    for e1 in L1:
        matched = False
        
        for e2 in L2:
            if e1 == e2:
                matched = True
                break    
            
    if not matched:
        return False
    
    return True


"""
    outer loop executed len(L1)
    times

    each iteration will execute
    inner loop up to len(L2)
    times

    O(len(L1)*len(L2))
    worst case when L1 and L2
    same length, none of

    elements of L1 in L2
    O(len(L1)^2)

"""

L2 = set({1, 2, 3, 4, 5, 6})
L1= set({2, 3, 4})
L3 = set({1, 5, 6})

print(isSubset(L1, L2))
print(isSubset(L1, L3))
print(isSubset(L2, L3))


""" find intersection of two lists, return a list with each element
    appearing only once """
    
def intersect(L1, L2):
    
    temp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                temp.append(e1)
                
    res = []
    
    for e in temp:
        
        if not (e in res):
            res.append(e)
            
            
    return res



print(intersect(L1, L2))
print(intersect(L1, L3))
print(intersect(L2, L3))
print(234-156)




        
                 
    
    
    
    
    
    
    
    
    
    
    







    
        
        