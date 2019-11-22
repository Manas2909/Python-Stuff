# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:18:29 2019

@author: Manas
"""

import re 
  
p = re.compile('ab*') 
print(p.findall("ababbaabbb"))