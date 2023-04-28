#!/usr/bin/env python
# coding: utf-8

# In[194]:


def mean(lst=[]):
     print("Mean:", "%.3f" % (sum(lst)/len(lst)))


# In[156]:


def median(lst=[]):
    lst.sort()
    n=int(len(lst)/2)
    if len(lst) %2 != 0:
        return lst[n]
    num1 =lst[n]
    num2=lst[int((len(lst)-2)/2)]
    return (num1+num2)/2


# In[236]:


def mode(lst=[]):
    lst2=[]
    string =""
    max_count=1
    for num in lst:
        x = lst.count(num)
        if  x != 1 :
            max_count=x
            if (num) not in lst2:
                lst2.append(num) 
    if (max_count ==1):  
        return("mode: No Mode")
    for num in lst2:
        string+= str(num)+" "
    return ("mode: "+string)


# In[239]:


lst=input()
try:
    lst =[int(i) for i in lst.split()]
    mean(lst)
    print(f'median: {median(lst)}')
    print(mode(lst))
except:
     print('enter integer number plz')
#median(lst)


# In[ ]:




