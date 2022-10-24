# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:18:33 2022

@author: Ethan Chesson
COMP 651-001
Dr. Esterline
"""

lst = eval(input("Enter a list of numbers with at least 5 numbers: "))

if lst[0] > lst[len(lst) - 1]:
    lst[0], lst[len(lst) - 1] = lst[len(lst) - 1], lst[0]
elif lst[0] < lst[len(lst) - 1]:
    lst[0] += 1
    lst[len(lst) - 1] += 1
else:
    lst[0] = 0
    lst[len(lst) - 1] = 0
    
half = len(lst) // 2
print(f"The first half is {lst[0:half]}")
print(f"The second half is {lst[half:]}")
print(f"The updated list is {lst}")