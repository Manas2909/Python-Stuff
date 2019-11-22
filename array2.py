# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:11:00 2019

@author: Manas
"""

#1.to create array by accepting input from user & print elements.
import array as arr
Arr=arr.array('i',[])
flag=0
i=0
while flag==0:
    elem=int(input("enter the element \n"))
    Arr.append(elem)    
    i=i+1
    flag=int(input("do you want to add more, press 0 to continue and 1 to exit\n"))
print(Arr)
for j in Arr:
    print(j,end=' ')
print()
for i in range(-1,-len(Arr)-1,-1):
    print(Arr[i],end=' ')
print()  
print(Arr.__len__())