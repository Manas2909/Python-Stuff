# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:26:58 2019

@author: Manas
"""

num_key=int(input("enter total number of keys"))
d=dict()
for i in range(1,num_key+1) :
    key=int(input("enter key "))
    
    value=input("enter values ")
    d[key]=value           
print(d)
key_check=int(input("enter the check key"))
flag=0
for i in d.keys():
    if i==key_check:
        flag=1
        break
if flag==1:
    print("key available")
else:
    print("not available")