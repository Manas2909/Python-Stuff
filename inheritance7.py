# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:09:43 2019

@author: Manas
"""

class company():
    company_name=''
    def __init__(self):
        self.company_name=input("enter name of the company ")
class employee(company):
    def __init__(self):
        super().__init__()
        self.ename=input("enter name of the employee ")
        self.id=input("enter the id of employee ")
        self.age=input("enter your age ")
        self.salary=input("enter salary of the employee ")
    def display(self):
        print("employee details are: ")
        print("cname\t\t ename\t id\tage\tsalary")
        print(self.company_name,"\t",self.ename,"\t",self.id,"\t",self.age,"\t",self.salary)
e1=employee()
e1.display()
    