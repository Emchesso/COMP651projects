# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:11:08 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""


def my_slice(lst, start=0, length=None, step=2):
    """by default returns a slice consisting of every 2nd element of the list
    passed to it.

    Can be passed other arguments that modify its behavior, including adjusting
    the index of the starting point for the slice notation, the step length
    between each slice, and the length of the final returned slice."""
    
    return lst[start:length:step]

lst = [7, 2, 12, 9, 15, 4, 11, 5]

print('my_slice(lst): ', my_slice(lst))
print('my_slice(lst, start=2, step=1): ', my_slice(lst, start=2, step=1))
print('my_slice(lst, start=2, length=5): ', my_slice(lst, start=2, length=5))
print('my_slice(lst, length=5): ', my_slice(lst, length=5))


# if length and start + length > len(lst): length = None
# return ls[start:start+length:step] if length else lst[start::step]