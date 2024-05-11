#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:37:23 2024

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
    
    

"""PROVIDING LABELS"""

""" Should really label the axes
    functions to label axes """

plt.figure('lin')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)


plt.figure('quad')
plt.plot(mySamples, myQuadratic)
    
plt.figure('cube')
plt.plot(mySamples, myCubic)

plt.figure('expo')
plt.plot(mySamples, myExponential)

"""note you must make figure active before invoking labeling"""

plt.figure('quad')
plt.ylabel('quadratic function')

"""note no label on x axis as no invocation while that display was active"""























 