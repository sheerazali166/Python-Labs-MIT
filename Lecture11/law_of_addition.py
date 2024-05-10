#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:28:51 2024

@author: sheeraz
"""

""" ANALYZING PROGRAMS AND
    THEIR COMPLEXITY """

"""
  combine complexity classes
  
     • analyze statements inside functions
     • apply some rules, focus on dominant term

  Law of Addition for O():
            
     • used with sequential statements
     • O(f(n)) + O(g(n)) is O(f(n) + g(n))
                
     • for example,

"""
    
#n = 4
#n = 5
#n = 6
#n = 7
#n = 8
#n = 9
#n = 10
#n = 11
#n = 12
#n = 13
#n = 14
#n1 = 15
#n2 = 5
#n = n1 - n2
n = 16
#n = 17
#n = 18

for i in range(n):
    print('i: ', i, ' = ', 'a')
    
for j in range(n * n):
    print ('j: ', j, ' = ', 'b')
    
"""is O(n) + O(n*n) = O(n+n2) = O(n2) because of dominant term"""    

    
