#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:58:57 2024

@author: sheeraz
"""

import matplotlib.pyplot as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []


""" select 1.5 keep displays 
    visible, more likely value for order
    of growth example would be 2  """


for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(i**1.5)
    
    
    
"""ADDING TITLES"""

plt.figure('lin')
plt.plot(mySamples, myLinear)
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.title('Linear')


plt.figure('quad')
plt.plot(mySamples, myQuadratic)
plt.xlabel('sample points')
plt.ylabel('quadratic function')
plt.title('Quadratic')

plt.figure('cube')
plt.plot(mySamples, myCubic)
plt.xlabel('sample points')
plt.ylabel('cubic function')
plt.title('Cubic')



plt.figure('expo')
plt.plot(mySamples, myExponential)
plt.xlabel('sample points')
plt.ylabel('exponential function')
plt.title('Exponential')

"""why are axes still labeled?"""
"""why are colors the same in the two plots"""








































    





