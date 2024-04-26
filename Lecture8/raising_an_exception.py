#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 07:19:00 2024

@author: sheeraz
"""

def get_ratios(L1, L2):
    
    """
        Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i]
    """
    
    ratios = []
    
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) #NaN = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios


"""

    EXAMPLE OF EXCEPTIONS

""" 

test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
               [['bruce', 'wayne'], [100.0, 80.0, 74.0]]   
               ]

grades = [[['peter','parker'], [80.0, 70.0, 85.0], 78.33333],
    [['bruce', 'wayne'], [100.0, 80.0, 74.0], [84.666667]]]
     
get_ratios(test_grades, grades)
