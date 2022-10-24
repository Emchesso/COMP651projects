# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:41:22 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import re

def sum_score_aux(matchobj):
    """casts the matched object groups as int and sums them together"""
    sc1 = int(matchobj.group(1))
    sc2 = int(matchobj.group(2))
    return str(sc1 + sc2)

def sum_scs_file(scsfname, sumfname):
    """iterates through file to find regex matches, writes to new file"""
    scsf = open(scsfname, 'r')
    sumscf = open(sumfname, 'w')
    p = re.compile(r'\((\d+), (\d+)\)')
    firstLine = True
    for line in scsf:
        if firstLine:
            sumscf.write("The combined scores of Team 1 and Team 2\n")
            firstLine = False
        else:
            sumscf.write(p.sub(sum_score_aux, line))
    scsf.close()
    sumscf.close()


if __name__ == '__main__':
    sum_scs_file('scores.txt', 'sum_scores.txt')
    