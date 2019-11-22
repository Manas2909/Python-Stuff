# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:39:07 2019

@author: Manas
"""

#delete duplicate values from tuple
tup=(1,2,3,3,4)
set1=set(tup)
tup=tuple(set1)
print(tup)
print(max(tup))