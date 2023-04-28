#!/usr/bin/env python
# coding: utf-8

# In[3]:


from problem4T2 import dict
f = open("filtered.txt","w")
# dict only has id , name birth
#print(dict[2])
#dict2 ={}
for i in dict:
    name = dict[i]['name']
    birthyear = str (dict[i]['birthyear']) 
    f.write(f'{i} {name} - {birthyear}  \n')

