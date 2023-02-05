#!/usr/bin/env python
# coding: utf-8

# In[ ]:


str =input("for boys :").split(",")
str2 = input("for girls :").split(",")
dic1 ={}
dic2={}
for i in str:
    key,value = i.split(":")
    dic1[key] = value
for i in str2:
    key,value = i.split(":")
    dic2[key] = value
    
dic1.update(dic2)
print(dic1)

