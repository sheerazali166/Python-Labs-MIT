#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:32:13 2024

@author: sheeraz
"""


def quotient_and_remainder(x, y):
    
    q = x // y
    r = x % y
    
    return (q, r)

(quot, rem) = quotient_and_remainder(4, 5)

print(quot)
print(rem)


def get_data(aTuple):
    
    nums = ()
    words = ()
    
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
            
    min_nums = min(nums)
    max_nums = max(nums)
    
    unique_words = len(words)
    
    return (min_nums, max_nums, unique_words)
