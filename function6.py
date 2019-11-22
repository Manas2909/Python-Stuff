# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 12:30:23 2019

@author: Manas
"""
def fact():
    num=int(input("enter your number"))
    fact=1
    if num>=0:
        for i in range(num,0,-1):
            fact=fact*i
        print(fact)
fact()