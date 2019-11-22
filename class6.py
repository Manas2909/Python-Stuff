# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:14:18 2019

@author: Manas
"""

class demo():
    x=10
    @classmethod
    def modify(cls):
        cls.x+=1
d=demo()
d2=demo()
d2.modify()
print(d.x)
print(d2.x)