#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:22:31 2024

@author: sheeraz
"""

import matplotlib.pyplot as plt

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

""" each pair of calls within
    the same active display  window """

plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)

plt.figure('lin quad')
plt.title('Linear vs. Quadratic')


plt.figure('cube exp')
plt.clf()

""" each pair of calls within
    the same active display window """

plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

plt.figure('cube exp')
plt.title('Cubic vs. Exponential')









    
