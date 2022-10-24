# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:37:45 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import numpy as np
# a1 = np.arange(0, 6)
# b1 = np.arange(5, -1, -1)


# c1 = np.greater.outer(a1,b1).astype(int)
# print(c1)

# d1 = np.add.reduce(c1, axis=1)
# print(d1)

# e1 = np.matrix([[2, 3, 1], [1, 2, 3]])
# f1 = np.matrix([[1, 3, 1], [2, 4, 1], [3, 2, 5]])
# print(e1*np.linalg.inv(f1))

# 5 x1 – x2 = 7
# 6 x1 + 9 x2 = 2

# g1 = np.array([[5, -1], [6, 9]])
# h1 = np.array([7,2])
# print(np.linalg.inv(g1).dot(h1))

i1 = np.arange(8).reshape(2,2,2)
j1 = np.array([[1,2],[2,1]])
print(i1 + j1)