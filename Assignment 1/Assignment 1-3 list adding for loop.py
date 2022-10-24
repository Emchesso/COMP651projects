# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:46:20 2022

@author: Ethan Chesson
COMP 651-001
Dr. Esterline
"""

lst1 = eval(input("Enter a list of numbers: "))
lst2 = eval(input("Enter a second list of numbers: "))
lst3 = []
loopRange = min(len(lst1), len(lst2))
for i in range(loopRange):
    lst3.append(lst1[i] + lst2[i])

print(lst3)