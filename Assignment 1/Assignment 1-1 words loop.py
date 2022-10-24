# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:07:26 2022

@author: Ethan Chesson
COMP 651-001
Dr. Esterline
"""

prompt = True
words = []
while prompt:
    word = input("Enter a word: ")
    if word == "":
        prompt = False
    else:
        words.append(word)
        
print(' '.join([str(word) for word in words]))