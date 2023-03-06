#!/usr/bin/env python
# coding: utf-8

# In[9]:


flag = False
lst =input()
lst = [int (i) for i in lst.split()]
row = lst[0]
if len(lst)==1:
     col =1
else:
    col = lst[1]
for i in range(row):
    lst2 = input()
    lst2 = [ (i) for i in lst2.split()]
    for i in range(col):
        if lst2[i] =='C'or lst2[i]=='M' or lst2[i]=='Y':
            flag = True
            break
if flag:
     print('#Color')
else:
     print('#Black&White')    
        

