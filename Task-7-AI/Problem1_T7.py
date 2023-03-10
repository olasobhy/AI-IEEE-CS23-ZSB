#!/usr/bin/env python
# coding: utf-8

# In[13]:


flip_num = int(input('The number of flips: '))
coin = input('Head or Tail? ')
apper_num = int(input(f'The number of {coin} appearance: '))
p = float(input(f'The probability of {coin} (< 1):' ))
#sample_space = 2 ** flip_num
answer = 0
v1 = 1
v2 =1
ap = apper_num
f = flip_num
j = 1
#calculate how many ways can put (apper_num) in (flip num) => v1
while ap>0:
    v1 *= f
    ap -= 1
    f  -= 1
    #number of ways to rearange (apper_num) => v2
    v2 *= j 
    j  += 1
possbility_num = int(v1/v2)
prob=1
for i in range(1,apper_num+1):
    prob =p*prob
for j in range(1,(flip_num - apper_num)+1):
    prob =prob*((1 -p))
    
for i in range (possbility_num):
    answer += prob 
print('Answer is:','%.3f' %(answer))

