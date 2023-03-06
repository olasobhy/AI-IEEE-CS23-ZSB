#!/usr/bin/env python
# coding: utf-8

# In[28]:


n = int(input())
lst=input()
lst=[int (i) for i in lst.split()]
sum1 =0
sum2=0
for i in range(n):
    left=lst[0]
    right=lst[len(lst)-1]
    if i% 2==0:
        if left > right:
            sum1+=left
            lst.remove(left)
        else:
            sum1+=right
            lst.remove(right)
    else:
        if left > right:
            sum2+=left
            lst.remove(left)
        else:
            sum2+=right
            lst.remove(right)
        
print(f'{sum1} {sum2}')            

