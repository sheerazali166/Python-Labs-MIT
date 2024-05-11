#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:50:09 2024

@author: sheeraz
"""

import matplotlib.pyplot as plt


"""DISPLAYING RESULTS vs. RATE"""

"""AN EXAMPLE: compound interest"""
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
        
    return base, savings 


def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        """put informative label on each"""
        plt.plot(xvals, yvals, label = 'retire:' + str(month) + ':' + str(int(rate*100)))
        plt.legend(loc = 'upper left')
        
        
displayRetireWRates(800, [.03, .05, .07], 40*12)
        
        
        
        
        


