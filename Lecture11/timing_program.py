#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 07:15:02 2024

@author: sheeraz
"""

import time

"""
    TIMING A PROGRAM
"""

def c_to_f(c):
    return c * 9/5 + 32



"""start clock"""
t0 = time.perf_counter()
#t0 = time.process_time()

print(t0)

"""call function"""
c_to_f(100000)

t1 = time.perf_counter() - t0


"""stop clock"""
print('t0 =', t0, ':', t1, 's, ')


