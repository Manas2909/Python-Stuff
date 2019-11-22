# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:15:37 2019

@author: Manas
"""

import re 
p = re.compile('\d') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 
  
p = re.compile('\d+') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 