# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:01:53 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

def table_drawer(doc):
    """
    Takes a file and formats its contents into a neat table.

    Uses readlines method to divide the data in the file into a list of strings
    before printing a header, formatting the field width and alignment.  Then
    loops through the list of data from the file to extract its numbers and
    convert them into different data types. The first is an int that shows a +
    sign if it is positive, the second is a float with precsion of 3, and the
    last is general type with precision of 7.  These are then printed under the
    columns using the same alignment formatting as the header.

    """
    lines = doc.readlines()
    print(f'{"Name":<12}{"| Measure 1":<12}{"| Measure 2":<12}{"| Measure 3":<12}')
    print("-" * 48)
    for entries in lines:
        entry = entries.split()
        n = entry[0]
        m1 = "{0:+}".format(int(entry[1]))
        m2 = "{0:.3f}".format(float(entry[2]))
        m3 = "{0:.7G}".format(float(entry[3]))
        print(f'{n:<12}|{m1:>10} |{m2:>10} |{m3:>10}')
        
# ***MUST REWRITE FILEPATH OF 'doc = open('...')'***
doc = open('C:/Users/Ethan/Coding/COMP 651/ass3values.txt', 'r')
table_drawer(doc)
doc.close()
