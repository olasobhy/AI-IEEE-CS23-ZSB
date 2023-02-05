#!/usr/bin/env python
# coding: utf-8

# In[31]:


dict1 = {
     "A":[20,30,100,49],
      "B":[00,199,201,29],
     "C":[40,90,69,18]
}
mRange = 0
for k in dict1:
        temp = max(dict1[k]) - min(dict1[k])
        if temp > mRange:
            mRange = temp
            key = k
print (key)

