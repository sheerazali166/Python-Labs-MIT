#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 08:17:25 2024

@author: sheeraz
"""

"""

    OPTION 1: FLAG THE ERROR
    BY PRINTING A MESSAGE

"""

"""

    decide to notify that something went wrong with a msg

"""

def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print('No grades data')
        
test = [[['peter', 'parker'], [10.0, 5.0, 85.0], 15.416666666666666],
        [['bruce', 'wayne'], [10.0, 8.0, 74.0], 13.833333333333334],
        [['captain', 'america'], [8.0, 10.0, 96.0], 17.5],
        [['deadpool'], [], None]]

#avg(test)

test2 = [10.0, 5.0, 85.0, 15.416666666666666, 10.0, 8.0, 74.0, 13.833333333333334, 8.0, 10.0, 96.0, 17.5]

test3 = []

print(avg(test2))
avg(test3)

        