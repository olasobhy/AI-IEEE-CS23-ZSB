#!/usr/bin/env python
# coding: utf-8

# In[57]:

def mean(lst=[]):
    return sum(lst)/len(lst)
     

def mid(lst=[]):
    lst.sort()
    n=int(len(lst)/2)
    if len(lst) %2 != 0:
        return lst[n]
    num1 =lst[n]
    num2=lst[int((len(lst)-2)/2)]
    return (num1+num2)/2


# In[61]:


def qu(lst=[]):
    mn = min(lst)
    mx = max(lst)
    rng = mx - mn
    lst.sort()
    if len (lst) >3:
        q1 =lst[:len(lst)//2]
        if len(lst) % 2 !=0:
            n = int(len(lst)//2 +1)
            q3 =lst[n:]
        else:
            n = int(len(lst)/2)   
            q3 =lst[n:]
    elif len(lst)<4:
        q1 =[lst[0]]
        q3 =[lst[len(lst)-1]]
    
    print (f'min: {mn}')
    print (f'Q1: {mid(q1)}')
    print (f'Q2: {mid(lst)}')
    print (f'Q3: {mid(q3)}')
    print (f'max: {mx}')
    print (f'range: {rng}')
    print (f'IQR: {mid(q3)-mid(q1)}')
        
    


# In[62]:


def StandardDeviation(lst=[]):
    sum = 0
    m = mean(lst)
    for i in lst:
        x =(i-m)**2
        sum +=x
        sd =sum/len(lst)
    print('Variance:','%.3f' %(sd))
    print ('Standard deviation:','%.3f'%(sd**0.5))


# In[67]:


lst=input()
try:
    lst=[float(i) for i in lst.split()]
    (qu(lst))
    StandardDeviation(lst)
except ValueError:
    print ("enter valid input plz")

    


# In[ ]:




