#!/usr/bin/env python
# coding: utf-8

# # COMP 361/651   Data Analytics 
# ## Spring 2022    Assignment 
# 
# 10 points possible <br>
# Solutions should be single lines of Python code unless it is otherwise stated. 

# Define a 3 × 3 “matrix” __`a`__ with 

# In[1]:


import numpy as np
a = np.array([[3, 1, 5], [6, 8, 3], [2, 5, 7]])
a


# Find the sum of the columns of __`a`__.  This should return <br>
# > __`array([11, 14, 15])`__

# In[2]:


# Your code goes here. 0.5 points
a.sum(axis=0)


# Produce an array whose rows are the rows of __`a`__ whose sum is  greater than or equal to 10.  Use Boolean indexing. This gives <br>
# > __`array([[6, 8, 3],
#        [2, 5, 7]])`__

# In[3]:


# Your code goes here. 1 point
a[a.sum(axis=1) >= 10]


# Define a 4×4 array __`b`__ with 

# In[57]:


b = np.arange(16).reshape(4, 4)


# Printed out, this array is as follows, where the upper left 2×2 part of this and the lower right 2×2 part are bold.<br>
# > `[[ `__`0  1`__`  2  3]
#  [ `__`4  5`__`  6  7]
#  [ 8  9 `__`10 11`__`]
#  [12 13 `__`14 15`__`]]`
# 
# With one statement, add the lower right 2×2 part of this array to the upper left part of it. The result is as follows, where the part changed is in bold.<br>
# > `[[`__`10 12`__`  2  3]
#  [`__`18 20`__`  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]`

# In[58]:


# Your code goes here.  1 point
b[:2,:2]+=b[-2:,-2:]
print(b)


# Define a 3×3 “matrix” __`c`__ as follows (where we also print it).

# In[73]:


c = np.arange(9).reshape(3,3)
print(c)


# It’s easy to loop over the rows of __`c`__.  You’re to iterate over the columns, printing out each column and (on the same line) the sum of its elements.  (Do this with two lines: a __`for`__ and a __`print()`__.) The following is the output.<br>
# > __`[0 3 6] 9
# [1 4 7] 12
# [2 5 8] 15`__
# 

# In[8]:


# Your code goes here.  0.5 point
for col in range(c.shape[1]):
    print(c[:, col], c[:, col].sum())


# Convert __`c`__ to the corresponding one-dimensional array in FORTRAN order then reshape it to 3×3. The result is the transpose of __`c`__, as printed below.
# > __`[[0 3 6]
#  [1 4 7]
#  [2 5 8]]`__

# In[16]:


# Your code goes here.  0.5 point
print(c.ravel('C').reshape((3,3), order='F'))


# From __`c`__, produce an array identical to __`c`__ except that the first and last rows have been swapped. Use a single statement. The following is the result.
# > __`array([[6, 7, 8],
#        [3, 4, 5],
#        [0, 1, 2]])`__

# In[38]:


# Your code goes here.  0.5 point use row indexing list, or put rows together with stack op
c[::-1]


# From __`c`__, produce an array identical to __`c`__ except that the first and last columns have been swapped. Use a single statement. The following is the result.
# > __`array([[2, 1, 0],
#        [5, 4, 3],
#        [8, 7, 6]])`__

# In[74]:


# Your code goes here. 0.5 point, can use column stack op
c[:,[2,0]]=c[:,[0,2]]
print(c)


# Create the 5×5 array __`d`__ as follows.

# In[47]:


d = np.arange(25).reshape(5,5)
print(d)


# From __`d`__, with one statement create three arrays: __`d1`__, with the first two columns of __`d`__, __`d2`__, with the next two columns of __`d`__, and __`d3`__, with the last column of __`d`__.  Print out __`d1`__, __`d2`__, and __`d3`__ as shown (respectively) below.<br>
# > __`[[ 0  1]
#  [ 5  6]
#  [10 11]
#  [15 16]
#  [20 21]]`__ 
# __`  `__<br><br>
# __` [[ 2  3]
#  [ 7  8]
#  [12 13]
#  [17 18]
#  [22 23]] `__
# __`  `__<br><br>
# __` [[ 4]
#  [ 9]
#  [14]
#  [19]
#  [24]]`__
# 

# In[51]:


# Your code goes here.  1 point
[d1,d2,d3] = np.array_split(d, 3, axis=1)
print(d1)
print(d2)
print(d3)


# From __`d`__, with one statement create three arrays: __`v1`__, with the first row of __`d`__, __`v2`__, with the next two rows of __`d`__, and __`v3`__, with the last two rows of __`d`__.  Print out __`v1`__, __`v2`__, and __`v3`__ as shown (respectively) below.<br>
#  > __`[[0 1 2 3 4]]`__ 
# __`  `__<br><br>
# __` [[ 5  6  7  8  9]
#  [10 11 12 13 14]] `__
# __`  `__<br><br>
# __` [[15 16 17 18 19]
#  [20 21 22 23 24]]`__
# 

# In[53]:


# Your code goes here.   1 point
[v1,v2,v3] = np.vsplit(d, (1,3))
print(v1)
print(v2)
print(v3)


# Create a 1D, 6-element array __`t`__ as follows.

# In[54]:


t = np.arange(6) * 2
print(t)


# Index __`t`__ with a list to produce the following array.<br>
# > __`array([0, 4, 6, 4])`__

# In[55]:


# Your code goes here.  0.5 point
t[[0,2,3,2]]


# Create the 5×5 array __`r`__ as follows.

# In[59]:


r = np.arange(25).reshape(5,5) * 2
print(r)


# The Numpy function __`diagonal()`__, passed a square array, returns the diagonal of that array as an array. Thus,

# In[60]:


np.diagonal(r)


# We can get the diagonal of an array by indexing it with the appropriate index array used for both the rows and the columns. Use this technique to get the diagonal of __`r`__ (as shown above). (This naturally takes two statements.)

# In[64]:


# Your code goes here.  1 point
i,j = np.array([0,1,2,3,4]),np.array([0,1,2,3,4])
r[i,j]


# Create the 4×4 array __`s`__ as follows.

# In[65]:


s = np.arange(16).reshape(4, 4)
print(s)


# With one statement, using Boolean indexing, replace all elements in __`s`__ less than 10 with 0, resulting in<br>
# > __`array([[ 0,  0,  0,  0],
#        [ 0,  0,  0,  0],
#        [ 0,  0, 10, 11],
#        [12, 13, 14, 15]])`__

# In[68]:


# Your code goes here.  1 point
np.where(s < 10, 0, s)


# Recall the trig identity $\mathrm{sin}(x)^2 + \mathrm{cos}(x)^2 = 1.0$. We apply the left-hand side of this identity in NumPy operating on 10 values between 0 and $2\pi$, these values being in the following array __`x`__.

# In[69]:


x = np.linspace(0, 2*np.pi, 10)
print(x)


# Note the functions __`np.sin()`__ and __`np.cos()`__, and note that __`**`__ is the Python exponentiation operator (e.g., $x^2$ is __`x**2`__). In one __`print()`__ statement, apply the left-hand side of the above identity to array __`x`__, resulting in the following confirmation of the identity for our 10 values.<br>
# > __`[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]`__

# In[71]:


# Your code goes here.   1 point
print((np.sin(x)**2) + (np.cos(x)**2))

