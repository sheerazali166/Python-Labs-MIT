#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:46:52 2024

@author: sheeraz
"""


""" ANALYZING PROGRAMS AND
    THEIR COMPLEXITY """

"""

  combine complexity classes
  
      • analyze statements inside functions
      • apply some rules, focus on dominant term

  Law of Multiplication for O():
    
     • used with nested statements/loops
     • O(f(n)) * O(g(n)) is O( f(n) * g(n) )
    
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
    for j in range(n):
        print('a')


"""

total = 0
for i in range(n):
    for j in range(n):
        print('a')
        total += 1
        
print(total)        

"""

""" is O(n)*O(n) = O(n*n) = O(n2) because the outer loop goes n
    times and the inner loop goes n times for every outer loop iter. """

print(n*n)


