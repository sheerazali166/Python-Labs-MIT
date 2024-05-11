#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:20:48 2024

@author: sheeraz
"""

import matplotlib.pyplot as plt


"""AN EXAMPLE: compound interest"""
def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
        
    return base, savings 

"""DISPLAYING RESULTS vs. MONTH"""

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    """clear frame so can reuse"""
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        """put informative label on each"""
        plt.plot(xvals, yvals, label = 'retire:' + str(monthly))
        plt.legend(loc = 'upper left')
        
        
displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], 0.5, 40 * 12)


        