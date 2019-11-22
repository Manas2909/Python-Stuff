# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:17:57 2019

@author: Manas
"""

try:
    print(x)
except NameError:
    print("variable x is missing")
except:
    print("something else went wrong")