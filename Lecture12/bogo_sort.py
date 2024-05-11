#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:51:28 2024

@author: sheeraz
"""

import random

"""COMPLEXITY OF BOGO SORT"""

def bogo_sort(L):
    while not sorted(L):
        random.shuffle(L)
      
   
    