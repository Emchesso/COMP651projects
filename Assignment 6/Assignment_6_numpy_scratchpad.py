# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:56:22 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import numpy as np
# a = np.array([[3, 1, 5], [6, 8, 3], [2, 5, 7]])
# print(a.sum(axis=0))


# print(a[a.sum(axis=1) >= 10])



# b = np.arange(16).reshape(4, 4)

# print(b.sum())

# dot product and straight arithmetic of arrays
# a = np.arange(4)
# b = np.arange(1, 5)
# print(a)
# print(b)
# print(-a + 2*b)
# print(np.dot([[1,2],[3,4]], [[1,2],[2,3]]))
# print(np.array([[1,2],[3,4]]) @ np.array([[1,2],[2,1]]))

# brokem, but operates on two arrays together
# a = np.ones( 2, dtype = int )
# print(a)
# b = np.random.random( 2 )
# print(b)
# print(a += b)

# operate on columns or rows of array
# b = np.arange(9).reshape(3,3)
# print(b)
# # print(b.sum(axis=0))
# # print(b.sum(axis=1))
# print(b.cumsum(axis=0))
# print(b.cumsum(axis=1))

# Lambda to filter an array by value
# arr = np.array([1,14, 6, 9, 4, 7, 12])
# print(np.array(filter(lambda x: 5 <= x <= 10, arr)))
# print(np.array(list(filter(lambda x: 5 <= x <= 10, arr))))

# lambda form to operate on two arrays together
# a = np.array([2**i for i in range(1,5)])
# print(a)
# b = np.arange(1,5)
# print(b)
# c = np.array(list(map(lambda x,y: x-y, a, b)))
# print(c)

# slicing and indexing multiple axis arrays
# b = np.arange(9).reshape(3,3)
# print(b)
# print(b[1,2]) #exact location, row, then column
# print(b[:,1]) # blank slice notation to show whole axis, 2nd column
# print(b[0:2,:]) # slice to get 1st and 2nd entire row
# print(b[-1]) # missing index, so entire last row, same as b[-1,:]

# multidimensional slicing
# c = np.arange(12).reshape(2,2,3)
# print(c)
# print(c[1,...])  	# same as c[1,:,:] or c[1], prints last axis
# print(c[...,2])  	# same as c[:,:,2], prints last columns

# iterating over array
# b = np.arange(9).reshape(3,3)
# for row in b:
#     print(row)
# for element in b.flat:
#     print(element, end=" ")
    
# can index with lists and arrays
# a = np.arange(6) * 2
# print(a)
# i = np.array([0,2,3,2])
# print(a[i])
# print(a[[0,2,3,2]])
# j = np.array([[2,4],[1,3]])
# print(a[j])

# b = np.arange(9).reshape(3,3)
# print(b)
# k = np.array([0,2])
# print(b[k])

# print columns and their sum
# [0 3 6] 9
# [1 4 7] 12
# [2 5 8] 15
# c = np.arange(9).reshape(3,3)
# print(c)
# # for row in c:
# #     print(row)
# # print(c[])
# # print(np.array(list(map(lambda x: x.sum, c))))
# # print(c.sum(axis=0))
# # for col in range(c.shape[1]):
# #     print(c[:, col], c[:, col].sum())
# # print(c.ravel())
# # print(c.transpose())
# # print(c.ravel('F').reshape((3,3), order='C'))



# # array([[2, 1, 0],
# #        [5, 4, 3],
# #        [8, 7, 6]])

# print(c.swap()) # = c[:, [0, 2]]

# d = np.arange(25).reshape(5,5)

# # [v1,v2,v3] = np.array_split(d, 3, axis=0)
# # print(v1)
# # print(v2)
# # print(v3)

# [v1,v2,v3] = np.vsplit(d, (1,3))
# print(v1)
# print(v2)
# print(v3)

# r = np.arange(25).reshape(5,5) * 2
# # print(r)
# # print(np.diagonal(r))
# i,j = np.array([0,1,2,3,4]),np.array([0,1,2,3,4]) #,np.array([2,2]),np.array([3,3]),np.array([4,4])
# print(r[i,j])

# a = np.arange(6) * 2
# print(a)
# j = np.array([[2,4],[1,3]])
# print(a[j])
# a = np.arange(12).reshape(3,4)
# print(a)
# i, j = np.array([0,2]), np.array([1,3])
# print(a[i,j])

# s = np.arange(16).reshape(4, 4)
# print(s)
# b = s >= 10
# print(b)
# print(np.where(s < 10, 0, s))

# x = np.linspace(0, 2*np.pi, 10)
# print(x)
# print()
# print((np.sin(x)**2) + (np.cos(x)**2))


# array([[2, 1, 0],
#        [5, 4, 3],
#        [8, 7, 6]])
c = np.arange(9).reshape(3,3)
print(c)
print()
c[:,[2,0]]=c[:,[0,2]]
print(c)
