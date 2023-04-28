#!/usr/bin/env python
# coding: utf-8

# In[13]:


list = input()
list =[int(i) for i in list.split()]
tnum = int (input())
for i in range (0,len(list)):
    if list[i] == tnum:
        for j in range (0,i):
            if (j < i -1):
                print(j , end =", ")
            else:
                print(j ," ")
        break

