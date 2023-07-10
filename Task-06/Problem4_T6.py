#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
evenarr =(np.arange(2,34,2))
arr2D= evenarr.reshape(4,4)
print (arr2D)
sum2D =0
for i in evenarr:
    sum2D+=i 
mean = sum2D/ (arr2D.size)
arr2D =(arr2D - mean)**2
print(arr2D **0.5 == 0.5)

