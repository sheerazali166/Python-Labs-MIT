#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:41:20 2024

@author: sheeraz
"""

import matplotlib.pyplot as plt

"""ADDING MORE DOCUMENTATION"""

""" can add a legend that identifies each plot """

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []


for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(i**1.5)
    
    
plt.figure('lin quad')
plt.clf()
"""label each plot"""
plt.plot(mySamples, myLinear, label = 'linear')
plt.plot(mySamples, myQuadratic, label = 'quadratic')
"""can specify a location"""
plt.legend(loc = 'upper left')
plt.title('Linear vs. Quadratic')


plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, label = 'cubic')
plt.plot(mySamples, myExponential, label = 'exponential')
plt.legend()
plt.title('Cubic vs. Exponential')


    

