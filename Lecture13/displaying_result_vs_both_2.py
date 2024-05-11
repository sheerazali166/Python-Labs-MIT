#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:14:08 2024

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
    plt.xlim(30*12, 40*12)
    """create sets of labels"""
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '-']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        """pick new label for each month choice"""
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            "pick new label for each rate choice"
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            """create label for plot"""
            plt.plot(xvals, yvals, monthLabel + rateLabel, label = 'retire:' + str(monthly) + ':' + str(int(rate * 100)))
            plt.legend(loc = 'upper left')
            
            
displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)





            
            
            