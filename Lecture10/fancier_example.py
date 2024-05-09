#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:17:33 2024

@author: sheeraz
"""

"""
    FANCIER EXAMPLE

"""

def genFib():
    
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 2 #fib(n-2)
    
    while True:
        
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        
        yield next
        
        fibn_2 = fibn_1
        

print("****************")

"""
    FANCIER EXAMPLE
"""

fib = genFib()

"""
    creates a generator object
    calling

"""



print(fib.__next__())        



"""
    generate each number in sequence
    
    evaluating
"""


for n in genFib():
    print(n)
    

"""
    will produce all of the Fibonacci numbers (an infinite sequence)

"""




