#!/usr/bin/env python
# coding: utf-8

# In[33]:


def bSort(list =[]):
    for j in range(0,len(list)-1):
        for i in range (0,len(list)-j-1):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return 
    
  
        
    


# In[66]:


def firstLast(tNum , list =[] ,list2 =[]):
    bSort(list)
    for i in range(0 , len(list)):
        if (tNum == list[i]):
            list2.append(i)
    x= min(list2)
    y= max (list2)
    print (x , y)

    


# In[68]:


list =input()
list =[int(i) for i in list.split()]
tNum = input()
firstLast(tNum,list)

