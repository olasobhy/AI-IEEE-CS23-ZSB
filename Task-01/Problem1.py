#!/usr/bin/env python
# coding: utf-8

# In[19]:


li = input()
# split => split elements in list
li =[ int (i) for i in li.split()]
li.sort()
if (len(li)>3):
    print (li[-2],li[1])
elif(len(li) == 2):
    print (li[1],li[0])
else:
    print (li[0] , li[0])
   





