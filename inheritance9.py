# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:02:11 2019

@author: Manas
"""

class b1():
    def displayb1(self):
        print("in class b1")

class b2():
    def displayb2(self):
        print("in class b2")
        

class b3(b2,b1):
    def displayb3(self):
        super().displayb1()
        super().displayb2()
        print("in class b3")
b=b3()
b.displayb3()