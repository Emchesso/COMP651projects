# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:30:56 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

def with_factors(lst, factors):
    """finds the numbers in a list with factors from a second list

    passed two lists of integers and returns a list containing the elements in
    the first list that have at least one element in the second list as a
    factor"""
    
    def has_factor(x, fcts):
        isFct = False
        for f in fcts:
            if x % f == 0:
                isFct = True
        return isFct
    for x in lst:
        fctList = list(filter(lambda x: has_factor(x, factors), lst))
    return fctList

lst = [7, 2, 12, 9, 15, 4, 11, 5]
print('with_factors(lst, [2, 5]): ', with_factors(lst, [2, 5]))

# do not need to loop through the lambda statement, it does that by itself
# return list(filter(lambda z: has_factor(z, fcts) lst))

# also, for has_factor(x, fcts):
    # for y in fcts:
        #if x % y == 0:
            # return True
        # else:
            # return False