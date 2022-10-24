# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:49:36 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format
# Expand display limits
# pd.options.display.max_rows = 50
# pd.options.display.max_columns = 20

names = ['Code','Date','Open','High','Low','Close','Volume','VWAP','TWAP']

bncDF = pd.read_csv('BNC2_sample.csv', 
                    names = names)
# data = bncDF.to_numpy()

# # print(data)
bncDF2 = bncDF.set_index(['Code', 'Date'])
print(bncDF2)
# index = bncDF2.index
# columns = bncDF2.columns
# # print(bncDF2)

# # data2 = {'Mins': [bncDF2.min()], 'Max': [bncDF2.max()]}
# # bncDFmin = pd.DataFrame(data2, names = names)
# # print(bncDFmin)

# bncPiv = bncDF2.pivot(index = [index],
#                       values = [data],
#                       columns = [columns]
#                       )
# print(bncPiv)

# minDF = pd.DataFrame([bncDF.min(), bncDF.idxmin()])
# print(bncDF.groupby('Code').mean())

