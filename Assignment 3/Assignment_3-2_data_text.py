# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 18:17:36 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

def write_files(doc):
    """
    Reads a data file and writes two new files using that data.

    Takes a .txt document and reads its lines into a list.  Then loops over the
    list, extracting the number data using split() method and converting the
    first two to float and adding them together, and the second two to int and
    adding them together.  Then writes two new files, inserting the name string
    followed by the float sum in the first output, and the name followed by the
    int sum in the secon.
    """
    lines = doc.readlines()

    for line in lines[:-1:]:
        data = line.split()
        x = f"{(float(data[1]) + float(data[2])):.2f}"
        y = int(data[3]) + int(data[4])

        out1.write(f"{data[0]} {x}\n")
        out2.write(f"{data[0]} {y}\n")

    data = lines[-1].split()
    x = f"{(float(data[1]) + float(data[2])):.2f}"
    y = int(data[3]) + int(data[4])

    out1.write(f"{data[0]} {x}")
    out2.write(f"{data[0]} {y}")

# ***MUST REWRITE FILEPATH OF 'doc = open('...')'***
doc = open('C:/Users/Ethan/Coding/COMP 651/ass3data.txt', 'r')
out1 = open('output1.txt', 'w')
out2 = open('output2.txt', 'w')

write_files(doc)

doc.close()
out1.close()
out2.close()
