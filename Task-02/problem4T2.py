#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import os
#print (os.getcwd())
file1 = open("grades.txt")
#print(file1.read())
#print(file1.readlines())
#print(file1.readline())
#str = file1.readline().split()
#print(str)
line =file1.readline()
x = line.split()
id = (x[0])
name =x[1]
grade =(x[2])
birthyear=(x[4])
gender = (x[6])

maxB =2020
maxScore= 0
numbers = 0
sumScore =0
dict={}
for line in file1:
    line = line.split()
    #strip => remove (- , :)
    #{0: {'name': 'Elsherbiny', 'score': 100, 'birthyear': 1900, 'gender': 'm'}}
    if line[2]!='N/A':
        dic ={int(line[0]):{'name':line[1] ,'score':int((line[2])) ,'birthyear':int((line[4])) ,'gender':line[6]}}
        dict.update(dic)
        sumScore += int(line[2])
        numbers+=1
        if  int(line[4]) < maxB:
            maxB = int (line[4])
            idB = line[0]
        if int(line[2]) >maxScore:
            maxScore = int(line[2])
            sex = line[6]
dic = dict
print("the ID of the oldest user is :" ,idB)
print("the sex of the user with the highest score is :" , sex)
print ("the average score is :",sumScore/numbers)

    


# In[ ]:




