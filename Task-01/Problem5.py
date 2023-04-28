#!/usr/bin/env python
# coding: utf-8

# In[11]:


list = input()
list1=[]
list2=[]
list =[str (i) for i in list.split()]
for i in range (0,len(list)):
    if (len (list[i]) % 2 == 0):
        fHalf = list[i][0:int( len (list[i]) /2)]
        list1.append(fHalf)
        sHalh = list[i][int( len (list[i]) /2):]
        list2.append(sHalh)
    else:
        fHalf = list[i][0:int( len (list[i]) /2 +1)]
        list1.append(fHalf)
        sHalh = list[i][int( len (list[i]) /2)+1:]
        list2.append(sHalh)
print(list1)
print(list2)
    

