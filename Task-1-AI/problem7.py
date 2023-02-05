#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list = input()
list=[int(i) for i in list.split()]
rNum = int (input())
while rNum != 0:
    list.insert(0,list[len(list)-1])
    list.pop()
    rNum -=1
print (list)


# In[ ]:




