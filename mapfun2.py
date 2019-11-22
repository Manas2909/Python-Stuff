# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 13:35:45 2019

@author: Manas
"""

l1=[]
num=int(input("enter the limit "))
for i in range(0,num):
    elem=int(input("enter the elem "))
    l1.append(elem)
print(l1)
l2=list(map(lambda x:x+10,l1))
print(l2)