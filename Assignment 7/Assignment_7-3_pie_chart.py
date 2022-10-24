# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:51:57 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import matplotlib.pyplot as plt

# Problem 3
cnts = {}

with open('ints.txt', 'r') as f:
    ls = [int(x) for x in f.readlines()]

m = max(ls)

for n in range(m+1):
    cnts.update({n:ls.count(n)})
    if int(n) not in ls:
        raise Exception(f'No elements {n}, with max = {m}')
        
vals = [i for x,i in sorted(cnts.items())]
labels = [x for x in range(m+1)]
max_index = vals.index(max(vals))
explode = [0 for x in range(m+1)]
explode[max_index] = 0.1

fig1, ax1 = plt.subplots()
ax1.pie(vals, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True)
plt.title('Relative frequencies of the numbers')
plt.savefig('Assignment_7-3_pie_chart.png')
