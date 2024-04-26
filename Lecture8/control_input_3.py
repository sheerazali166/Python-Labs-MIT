#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 06:57:46 2024

@author: sheeraz
"""

data = []
file_name = input('Provide a name of a file of data ')

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') #remove trailing \n
            data.append(addIt)
finally:
    fh.close() # close file even if fail

gradesData = []

if data:
    for student in data:
        try:
            name = student[0: -1]
            grades = int(student[-1])
            gradesData.append([[name, [grades]]])
        except ValueError:
            gradesData.append([student[:], []])
            
             
