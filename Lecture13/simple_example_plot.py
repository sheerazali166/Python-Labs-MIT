#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:39:50 2024

@author: sheeraz
"""

import matplotlib.pyplot as plt

"""SIMPLE EXAMPLE"""

""" basic function plots two lists as x and y values
    other data structures more powerful, use lists to demonstrate
    first, let’s generate some example data """
    
    
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


"""to generate a plot, call"""

plt.plot(mySamples, myLinear)

"""OVERLAPPING DISPLAYS"""

""" suppose we want to display all of the graphs of the
    different orders of growth
    we could just call: """    
        
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

""" impossible to see linear graph, or even quadatic graph """









    