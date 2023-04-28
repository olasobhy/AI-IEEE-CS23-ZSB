#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list =input()
list=[int(i) for i in list.split()]
list2 =[]
for i in list:
    evenNum = list(filter(lambda i :(i%2 == 0) , list))
print (len(evenNum))

