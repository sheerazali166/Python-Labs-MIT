#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:24:00 2024

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
    myExponential.append(i ** 1.5)
    

"""OVERLAPPING DISPLAYS"""


"""
    not very helpful, can’t really see anything but the
    biggest of the plots because the scales are so different
    
    can we graph each one separately?
    
    call
    
    plt.figure(<arg>)
    
          gives a name to this figure; allows us to reference for future use
    
        ◦ creates a new display with that name if one does not
          already exist
        
        ◦ if a display with that name exists, reopens it for
    
    processing

"""    

"""EXAMPLE CODE"""

plt.figure('lin')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.plot(mySamples, myQuadratic)

plt.figure('cube')
plt.plot(mySamples, myCubic)

plt.figure('expo')
plt.plot(mySamples, myExponential)































