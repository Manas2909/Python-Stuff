# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:35:17 2019

@author: Manas
"""

import array as arr
Arr=arr.array('i',[])
flag=0
i=0
while flag==0:
    elem=int(input("enter the element \n"))
    Arr.append(elem)    
    i=i+1
    flag=int(input("do you want to add more, press 0 to continue and 1 to exit\n"))
list1=list(Arr)
print(list1)
for i in list1:
    print("count of",i,"is")
    print(list1.count(i))