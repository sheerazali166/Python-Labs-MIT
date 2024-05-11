#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:24:41 2024

@author: sheeraz
"""

def merge(left, right):
    result = []
    i, j = 0, 0
    """:- left right sublists
          are ordered - move indices for
          sublist deping on which sublist holds
          next smallest element """
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    """when right sublist is empty"""
    while (i < len(left)):
        result.append(left[i])
        i += 1
    """when left sublists is empty"""
    while(j < len(right)):
        result.append(right[j])
        j += 1
    return result

"""MERGE SORT ALGORITHM -- RECURSIVE"""


def merge_sort(L):
    """base case"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        """divide"""
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        """conquer with the merge step"""
        return merge(left, right)
    
    
L = [2, 5, 1, 9, 8, 3, 6, 7, 0, 4]
print(merge_sort(L))    
        
""" at first recursion level
        • n/2 elements in each list
        • O(n) + O(n) = O(n) where n is len(L)
    
    at second recursion level
        • n/4 elements in each list
        • two merges  O(n) where n is len(L)
    each recursion level is O(n) where n is len(L)
    dividing list in half with each recursive call
        • O(log(n)) where n is len(L)
          overall complexity is O(n log(n)) where n is len(L) """        
          
          
"""SORTING SUMMARY -- n is len(L)""" 

""" bogo sort
    • randomness, unbounded O()
   bubble sort
    • O(n2)
   selection sort
    • O(n2)
    • guaranteed the first i elements were sorted
   merge sort
    • O(n log(n))
      O(n log(n)) is the fastest a sort can be """         
          
          
          





