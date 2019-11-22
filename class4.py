# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:17:16 2019

@author: Manas
"""

class car():
    brand_name=""
    model_name=""
    cost=0
    def __init__(self):
        print()
    def accept(self):
        self.brand_name=input("enter the brand name ")
        self.model_name=input("enter the model name ")
        self.cost=input("enter the cost")
        
    def display(self):
        print("Brand Name of car is",self.brand_name)
        print("Model name of car is",self.model_name)
        print("cost of car is",self.cost)
    
    def modify(self):
        self.cost=input("enter the modified cost ")
        
        
        
car1=car()
car1.accept()
car1.display()

car1.display()
car2=car()
car2.accept()
car2.display()
car2.modify()
car2.display()
car1.display()
