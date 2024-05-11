#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:06:44 2024

@author: sheeraz
"""

import matplotlib.pyplot as plt

"""CHANGING LIMITS ON AXES"""

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
    
    
plt.figure('lin')
plt.clf()
plt.ylim(0, 1000)
plt.plot(mySamples, myLinear)

plt.figure('lin')
plt.title('Linear')


plt.figure('quad')
plt.clf()
plt.ylim(0, 1000)
plt.plot(mySamples, myQuadratic)


plt.figure('quad')
plt.title('Quadratic')



    
    




    