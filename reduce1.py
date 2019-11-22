# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:29:15 2019

@author: Manas
"""
import functools
#from functools import *
l=[1,2,3,4,5,6,7,8,9,10]
l2=functools.reduce(lambda a,b:a+b,l)
print(l2)