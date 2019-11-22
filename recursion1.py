# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 13:00:45 2019

@author: Manas
"""

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
num=int(input("enter your number"))
factorial=fact(num)
print(factorial)