# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:55:22 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

def split_dict(x, d):
    """
    Splits a dictionary into separate dicts, one with values > x, the other <= x
    
    Sets up two dictionaries within the function call and uses a for loop and 
    dictionary comprehension to assign the key:value pairs of dict 'd' to the 
    new dictionaries.  d1 is for values less than or equal to x, d2 for values
    greater than x.  Returns the two dictionaries as a tuple.
    """
    
    d1 = dict()
    d2 = dict()

    for k,v in d.items():
        if v <= x:
            d1[k] = v
        else:
            d2[k] = v
    return (d1,d2)

d = dict([('a', 2), ('b', 10), ('c', 2), ('d', 9), ('e', 5)])
x = 3

print(split_dict(x, d))
