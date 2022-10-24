# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:58:05 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

def pairs_factors(lst):
    """passed a list of integers and returns a list of pairs (tuples) that have
    the list element and its factor.
    
    Uses nested list comprehension to iterate through the list, checking if each
    element of the list is a factor of the current element, then packing the
    factors into a list and assigning it to the second element of the tuple.

    """
    return [(x, [y for y in lst if ((x % y == 0) and (x != y))]) for x in lst]

lst = [7, 2, 12, 9, 15, 4, 11, 5]
print('pairs_factors(lst): ', pairs_factors(lst))

# return [(x, [y for y in lst if y not in {x,0,1} and x % y == 0]) for x in lst]