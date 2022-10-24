# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:13:33 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import csv

def update_lists(x):
    for row in x:
        if int(row[-1]) == 0:
            x0.append(float(row[0]))
            y0.append(float(row[1]))
            z0.append(float(row[2]))
            m0.append(float(row[3]))
        elif int(row[-1]) == 1:
            x1.append(float(row[0]))
            y1.append(float(row[1]))
            z1.append(float(row[2]))
            m1.append(float(row[3]))
        else:
            print("Line is ill-formed")
            
def get_area(r):
    return np.pi*(r**2)
    

x0,x1,y0,y1,z0,z1,m0,m1 = ([] for i in range(8))

with open('data.txt', 'r') as f:
    data_reader = csv.reader(f, delimiter = " ")
    update_lists(data_reader)
    

m0 = [get_area(r) for r in m0]
m1 = [get_area(r) for r in m1]

ax = plt.axes(projection="3d")
ax.scatter3D(x0, y0, z0, s = m0, color = 'r', marker = '^')
ax.scatter3D(x1, y1, z1, s = m1, color = 'b', marker = '.') 
plt.title("A 3D scatter plot")
plt.savefig('Assignment_7-4_3D_scatter')