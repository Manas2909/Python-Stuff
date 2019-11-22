# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:57:53 2019

@author: Manas
"""

class decoratorexample:
    def __init__(self):
        print("hello world")
    @staticmethod
    def example_decorator():
        print("decorator method")
de = decoratorexample.example_decorator()