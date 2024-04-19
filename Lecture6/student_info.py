#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 01:21:48 2024

@author: sheeraz
"""

"""

     HOW TO STORE STUDENT INFO
     
     so far, can store using separate lists for every info

"""

names = ['Ana', 'John', 'Denise', 'Katy']

grade = ['B', 'A+', 'A', 'A']

course = [2.00, 6.0001, 20.002, 9.01]

print(names)

print(grade)

print(course)

def get_grade(student, name_list, grade_list, course_list):
    
    i = name_list.index(student)
    
    grade = grade_list[i]
    
    course = course_list[i]
    
    return (course, grade)

print()

print(get_grade("Ana", names, grade, course))
print(get_grade("John", names, grade, course))
print(get_grade("Denise", names, grade, course))
print(get_grade("Katy", names, grade, course))

