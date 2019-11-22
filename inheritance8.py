# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:22:47 2019

@author: Manas
"""

class college():
    cname=''
    address=''
    def __init__(self):
        self.cname=input("enter college name ")
        self.address=input("enter college address ")
    def display_college_details(self):
        print("college name is: ",self.cname)
        print("college address is: ",self.address)
class dept(college):
    dname=''
    def __init__(self):
        super().__init__()
        self.dname=input("enter department name ")
    def display_dept_details(self):
        super().display_college_details()
        print("department name is: ",self.dname)
class div(dept):
    divname=''
    def __init__(self):
        super().__init__()
        self.divname=input("enter division name ")
    def display_div_details(self):
        super().display_dept_details()
        print("division name is: ",self.divname)
class student(div):
    sname=''
    def __init__(self):
        super().__init__()
        self.sname=input("enter name of the student ")
        self.id=input("enter the id of student ")
        self.age=input("enter your age ")
        
    def display(self):
        super().display_div_details()
        print("student details are: ")
        print("student name is: ",self.sname)
        print("student id is: ",self.id)
        print("student age is: ",self.age)
s1=student()
s1.display()
    
