#!/usr/bin/env python
# coding: utf-8

# In[6]:


li = input()
li = [int(i) for i in li.split()]
for i in range ( 0,len(li) ):
    if (li[i] != li[-1-i]):
        f = False
        break
    f = True
print (f)






