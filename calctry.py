# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:28:09 2019

@author: Manas
"""
try:
    num1=int(input("enter your 1st number "))
    num2=int(input("enter your 2nd number "))
    
    choice=int(input("enter your choice\n1. add\n2. sub\n3. mul\n4. div\n"))
    if choice==1:
        
        add=num1+num2
        print(add)
        
    elif choice==2:
        sub=num1-num2
        print(sub)
    elif choice==3:
        mul=num1*num2
        print(mul)
    elif choice==4:
        div=num1/num2
        print(div)
except ValueError:
    print("value cant be string")
except ZeroDivisionError:
    print("denominator cant be zero")
else:
    print("calc run successfully")
        
    