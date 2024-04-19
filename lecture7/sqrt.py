#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:40:40 2024

@author: sheeraz
"""

"""
    BLACK BOX TESTING
    explore paths through specification

"""

def sqrt(x, eps):
    """ Assumes x, eps floats, x >= 0, eps > 0
    Returns res such that x-eps <= res*res <= x+eps """
