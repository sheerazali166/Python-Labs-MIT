#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:59:39 2024

@author: sheeraz
"""

import matplotlib.pyplot as plt


"""CHANGING DATA DISPLAY"""

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
"""string specifies color and style"""
plt.plot(mySamples, myLinear, '-b', label = 'linear')
plt.plot(mySamples, myQuadratic, 'ro', label = 'quadratic')
plt.legend(loc = 'upper left')
plt.title('Linear vs. Quadratic')


plt.figure('cube exp')
plt.clf()
"""see documentation for coices of color and style"""
plt.plot(mySamples, myCubic, 'g^', label = 'cubic')
plt.plot(mySamples, myExponential, 'r--', label = 'exponential')
plt.legend()
plt.title('Cubic vs. Exponential')






    