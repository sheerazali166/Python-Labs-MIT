#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:24:07 2024

@author: sheeraz
"""


import matplotlib.pyplot as plt

"""CLEANING UP WINDOWS"""

""" we are reusing a previously created display window
    need to clear it before redrawing
    because we are calling plot in a new version of a
    window, system starts with first choice of color (hence
    the same); we can control (see later) """
    
    
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
plt.title('linear')
plt.clf()
plt.plot(mySamples, myLinear)


plt.figure('quad')
plt.title('quadratic')
plt.clf()
plt.plot(mySamples, myQuadratic)


plt.figure('cube')
plt.title('cubic')
plt.clf()
plt.plot(mySamples, myCubic)


plt.figure('expo')
plt.title('exponential')
plt.clf()
plt.figure(mySamples, myExponential)



















    
    
    