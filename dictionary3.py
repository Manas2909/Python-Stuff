# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:08:28 2019

@author: Manas
"""
num_key=int(input("enter total number of keys"))
d=dict()
for i in range(1,num_key+1) :
    key=int(input("enter key "))
    
    value=input("enter values ")
    d[key]=value           
print(d)
