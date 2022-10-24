# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:27:15 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml

NA = np.NaN

data = {'Grade': [NA, 'A', 'B', NA, 'C'],
        'Height': [NA, NA, 1.8, 1.7, 1.9],
        'Age': [NA, NA, NA, 34.0, NA]}
df = pd.DataFrame(data, index = ['Ed', 'Sue', 'Al', 'Pam', 'Ken'])
# print(df)
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# print(df.dropna(axis=1, thresh=3))
# print(df.fillna({'Grade':'F','Height':1.5,'Age':39.0}))

# iterables = [["bar", "baz", "foo", "qux"], ["one", "two"]]

# pd.MultiIndex.from_product(iterables, names=["first", "second"])

# data1 = {'One': [8,9,8,7,6,9], 'Two': [6,7,9,10,8,7], 'One'}

# columns1 = [['']]


# multInd1 = pd.MultiIndex.from_product(index1, names = ['Feature', 'Problem'])
data1 = [[8, 6, 5, 7, 6, 6], 
         [9, 7, 7, 6, 8, 8], 
         [8, 9, 6, 7, 9, 6], 
         [7, 10, 4, 8, 6, 7], 
         [6, 8, 5, 7, 6, 7], 
         [9, 7, 8, 9, 6, 8]]
df1 = pd.DataFrame(data1, 
index = [['Design', 'Design', 'Design', 'Execution', 'Execution', 'Execution'],
          ['One', 'Two', 'Three', 'One', 'Two', 'Three']],
columns = [['Ed', 'Ed', 'James', 'James', 'Sam', 'Sam'], 
            ['One', 'Two', 'One', 'Two', 'One', 'Two',]])
df1.index.names = ['Feature', 'Problem']
df1.columns.names = ['Student', 'Assignment']
# print(df1)
# print(df1.groupby(level = 1, axis = 1).mean())

df2 = df1.swaplevel('Feature', 'Problem')
# print(df2.sort_index(level=0))


data3 = {'Name' : ['Ed', 'Ed', 'Ed', 'Al', 'Al', 'Al', 'Sue', 'Sue', 'Sue'],
         'HW': [1,2,3,1,2,3,1,2,3],
         'Design': [8,7,6,9,8,10,9,8,7],
         'Impl': [7,7,5,10,9,9,8,7,9]}
df3 = pd.DataFrame(data3, index = [0,1,2,3,4,5,6,7,8])
# print(df3)

# print(df3.reindex(index = [data3['Name'],data3['HW']],
#                   columns = ['Design', 'Impl'],
#                   ))

print(df3.set_index(['Name','HW']))


