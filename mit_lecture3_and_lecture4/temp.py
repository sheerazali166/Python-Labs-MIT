# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Reviewing Loops

#ans = 0
#neg_flag = False

#x = int(input("Integer an integer: "))

#if x < 0:
 #   neg_flag = True
  #  while ans ** 2 < x:
   #     ans = ans + 1
#if ans ** 2 == x:
 #   print("Square root of", x, "is", ans)
#else:
 #   print(x, "is not a perfect square")
  #  if neg_flag:
   #     print("Just checking... did you mean", -x, "?")
        

#s = "abc"

#print(len(s))

#print(s[0])
#print(s[1])
#print(s[3])

#print("Because three takli hai then why they are at that post")

# Strings

# s = "abcdefgh"

# print(s[::-1]) # evaluates to "hgfedbca"
# print(s[3:6]) # evaluates to "def"
# print(s[-1]) # evaluates to "h"

# strings are “immutable” – cannot be modified

# s = "hello"
# print(s[0])
#s[0] = 'y' # is allowed

# s = 'y'+s[1:len(s)]
# s is a new object
# print(s)

#s = "abcdefgh"

#for index in range(len(s)):
 #   if s[index] == 'i' or index == 'u':
  #      print('There is an i or you')


#for char in s:
 #   if char == 'i' or char == 'u':
  #      print('There is an i or u')

# String And Loops

s = 'abcdefgh'

for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print('There is an i or you')
        
        
for char in s:
    if char == 'i' or char == 'u':
        print('There is an error i or u')
        

# Code Example

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! "  + char)
    i += 1

print("What does that spell?")

for i in range(times):
    print(word, "!!!")






    
        
        
















        
        
        
        
        
        
        









