#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 07:49:29 2024

@author: sheeraz
"""

class_lsit = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
              [['bruce', 'wayne'], [100.0, 80.0, 74.0]]]


def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        #new_stats.append(elt[0], elt[1], avg(elt[1]))
        new_stats.append(elt)
    return new_stats


def avg(grades):
    return sum(grades)/len(grades)


class_list_grade = [80.0, 70.0, 85.0, 100.0, 80.0, 74.0]

print(get_stats(class_lsit))
print("Grade AVG: ", avg(class_list_grade))


test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
               [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
               [['captain', 'america'], [8.0,10.0,96.0]],
               [['deadpool'], []]] 


test_list_grade = [10.0, 5.0, 85.0, 10.0, 8.0, 74.0, 8.0,10.0,96.0]

print("********///////////**********")

print(get_stats(test_grades))
print("Test Grade AVG: ", avg(test_list_grade))
    