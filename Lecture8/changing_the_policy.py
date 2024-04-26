#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 08:28:30 2024

@author: sheeraz
"""

"""
    OPTION 2: CHANGE THE POLICY

"""

def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0
    except TypeError:
        print('no grade data type error')
    
test_grade = [10.0, 5.0, 85.0, 15.416666666666666, 10.0, 8.0, 74.0, 13.833333333333334, 8.0, 10.0, 96.0, 17.5,0.0]

test_grade_2 = []

print(avg(test_grade))

avg(test_grade_2)

test_grade_3 = [None, None, None]

avg(test_grade_3)


    