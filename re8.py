# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:25:49 2019

@author: Manas
"""

import re 
print(re.subn('ub', '~*' , 'Subject has Uber booked already')) 
t = re.subn('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE) 
print(t) 
print(len(t)) 
 
print(t[0]) 