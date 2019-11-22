# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:10:22 2019

@author: Manas
"""

l1=[1,2,3,4,5,6,7]
l2=list(filter(lambda x:x%2!=0,l1))
print(l2)
l3=list(map(lambda x:x**3,l2))
print(l3)
l4=list(map(lambda x:x**3,filter(lambda x:x%2!=0,l1)))
print(l4)