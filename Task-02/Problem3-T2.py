#!/usr/bin/env python
# coding: utf-8

# In[9]:


list = input()
list =[int (i) for i in list.split()]
list1 =[]
list2 =[]
for i in range(0,len(list)):
    if list[i] > 0:
        list1.append(list[i])
    else:
        list2.append(list[i])
        
if len(list1)==len(list):
    list2.append(min(list1))
    list1.remove(min(list1))
    list2.append(min(list1))
if len(list2)==len(list):
    list1.append(max(list2))
    list2.remove(max(list2))
    list1.append(max(list2))
if len(list1)==1:
    list1.append(max(list2))
if len(list2) ==1:
    list2.append(min(list1))
    
print(list1,"({})".format(sum(list1)))
print(list2,"({})".format(sum(list2)))
    
    

