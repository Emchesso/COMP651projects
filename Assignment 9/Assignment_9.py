# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 15:09:43 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

from pandas import Series, DataFrame 
import pandas as pd
import numpy as np

# ts=Series((25,50), index = pd.PeriodIndex(['2022-4','2022-10'], freq='Q'))
# print(ts)
# ts=Series([25,50], index = [pd.period_range('1/1/2022','12/1/2022', freq='Q')])
# prng = pd.period_range('1/1/2022','12/1/2022', freq='Q')
# ts=Series([25,50], index = pd.PeriodIndex(['2022-4','2022-10'], freq='Q'))
# print(ts.reindex(index=pd.period_range('1/1/2022','12/1/2022', freq='Q'),method='bfill'))

# print(ts)

# books = np.rec.array([(b'Moby Dick', 1851, 2.7), (b'Ulysses', 1922, 4.2),
#            (b'Tom Jones', 1749, 1.8)],
#           dtype=[('title', 'S25'), ('date', '<i4'), ('weight', '<f4')])

# print(books[0].title)

# data = {'weight': [25.0, 30.0, 35.0, 50.0],
#         'height': [2.2, 2.6, 2.8, 3.0],
#         'age': [2.0, 7.0, 4.0, 10.0]}
# df2 = DataFrame(data, index = ['Fido', 'Rover', 'Lassie', 'Brian'])
# print(df2.sort_values(by='weight').index.tolist())

data2 = {'Exam 1': [39, 42, 37, 41],
        'Exam 2': [42, 44, 39, 42],
        'Exam 3': [37, 40, 32, 39],
        'Exam 4': [44, 45, 35, 38]}
df3 = DataFrame(data2, index = ['Fred', 'Jane', 'Ed', 'Mary'])
# print(df3)
# print()

exam_incrs = Series((2,1,0), index=('Exam 1', 'Exam 3', 'Exam4'))
print(exam_incrs)

exam_incrs1 = exam_incrs.reindex(index=('Exam 1', 'Exam 2', 'Exam 3', 'Exam 4'), fill_value=0)
print(exam_incrs1)
# print()

# print(df3 + exam_incrs1)
# print()

df3['ave'] = np.average(df3.values, axis = 1)
# print(df3)
print()

# print(Series((x - y for x in df3.values.max() for y in df3.values['ave']), index = df3.index))

# print

# print(df3['ave'].squeeze())

# result = lambda df3['ave'].values - df3
# ser = pd.Series(df3['ave'].values, index = df3.index)
# print(ser)
df4 = df3
del df4['ave']

# lambda ave, max: ave-max
# print(df3['Exam 1', 'Exam 2', 'Exam 3', 'Exam 4'].values)
# print(df3.sort_values(by=['Exam 1', 'Exam 2', 'Exam 3', 'Exam 4']))
# print()
# print(df3.max(axis=1)-df3['ave'])
# f = lambda x: x.max() - x['ave'].values
# print(df3.apply(f))

f = lambda x: x-3 if (x<38 and (x-3)>=30) else (30 if (x-3)<30 else x)
# print(df4.applymap(f))
