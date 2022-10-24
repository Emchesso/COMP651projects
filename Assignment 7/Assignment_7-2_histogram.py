# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:31:17 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import matplotlib.pyplot as plt
import numpy as np

# Problem 2

x = np.random.normal(1.8, 0.4, 1000)
plt.hist(x, bins = 40, histtype = 'step')
plt.xlabel('Kilometers')
plt.ylabel('Number of Persons')
plt.xticks(rotation=45)
plt.title('Average distance walked per day, Greensboro residents')

plt.savefig('Assignment_7-2_histogram.png')
