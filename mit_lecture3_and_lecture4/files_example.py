#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 09:21:23 2024

@author: sheeraz
"""

#nameHandle = open('kids', 'w')
#for i in range(2):
 #   name = input('Enter name: ')
  #  nameHandle.write(name + '/')
                     
#nameHandle.close()

nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()    
                     