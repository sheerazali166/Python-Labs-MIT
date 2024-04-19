#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:23:55 2024

@author: sheeraz
"""

"""
    CREATING A DICTIONARY        

"""

def lyrics_to_frequences(lyrics):
    myDict = {}
    for words in lyrics:
        if words in myDict:
            myDict[words] += 1
        else:
            myDict[words] = 1
    return myDict       
    

word = "Hello World"

print(lyrics_to_frequences(word))

"""

    USING THE DICTIONARY

"""

def most_common_words(freqs):
    
    values = freqs.values()
    
    best = max(values)
    
    words = []
    
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)         

grades = { 'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A'  }

print()        

print(most_common_words(grades))

"""

    LEVERAGING DICTIONARY
    PROPERTIES

"""

def words_often(freqs, minTimes):
    result = []
    done = False
    
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del (freqs[w])              
        else:
            done = True
                
    return result

# can directly mutate directly; makes it easier to iterate

print()




#print(words_often(grades, 5))        


    

        