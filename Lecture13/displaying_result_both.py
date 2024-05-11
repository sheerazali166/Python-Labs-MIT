#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:01:13 2024

@author: sheeraz
"""

import matplotlib.pyplot as plt

"""DISPLAYING RESULTS vs. BOTH"""

"""AN EXAMPLE: compound interest"""
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
        
    return base, savings 

def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    """focus on last stages of fund"""
    plt.xlim(30*12, 40*12)
    for monthly in monthlies:
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            """put informative label on each"""
            plt.plot(xvals, yvals, label = 'retire:' + str(monthly) + ':' + str(int(rate * 100)))
            plt.legend(loc = 'upper left')
            
 
displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)
    
    
    