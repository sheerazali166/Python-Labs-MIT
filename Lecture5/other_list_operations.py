#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:45:32 2024

@author: sheeraz
"""

L = [9, 6, 0, 3]

print(sorted(L))

print(L)
L.sort()
print(L)

L.reverse()
print(L)

"""
    BRINGING TOGETHER LOOPS,
    FUNCTIONS, range, and LISTS

"""

print(range(5))

print(range(2, 6))

print(range(5, 2, -1))


cool = ['blue', 'green', 'grey']
chill = ['blue', 'green', 'grey']

print(cool)
print(chill)

chill[2] = 'blue'

print(cool)
print(chill)


"""
     ALIASES

     hot is an alias for warm– changing one changes the
     other!
     
     append() has a side effect

"""

a = 1
b = a

print(a)
print(b)

warm = ['red', 'yellow', 'orange']
print(warm)

hot = warm
print(hot)

hot.append('pink')

print(hot)
print(warm)

"""
    CLONING A LIST
   
    create a new list and copy every element using
    chill = cool[:]

"""

print("\n")

cool = ['blue', 'green', 'grey']

chill = cool[:]

print(cool)
print(chill)

chill.append('black')

print(chill)
print(cool)

"""
    SORTING LISTS
    
    calling sort() mutates the list, returns nothing
    calling sorted() does not mutate list, must assign
    result to a variable

"""

print('\n')

warm = ['red', 'yellow', 'orange']
sortedWarm = warm.sort()

print(warm)
print(sortedWarm)

cool = ['cool', 'grey', 'blue']
sortedCool = sorted(cool)

print(cool)
print(sortedCool)


"""
    LISTS OF LISTS OF LISTS OF….
    
    can have nested lists
    side effects still possible after mutation
    
"""

print('\n')

warm = ['yellow', 'orange']
hot = ['red']

brightColors = [warm]

print(warm)
print(hot)
print(brightColors)

print('\n')

brightColors.append(hot)
print(brightColors)

print('\n')

hot.append('pink')

print(hot)
print(brightColors)

print('\n')

print(hot + warm)
print(hot)













































 












 