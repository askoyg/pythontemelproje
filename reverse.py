# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:14:33 2022

@author: murat
"""
import numpy as np
list1 = [[1, 2], [3, 4], [5, 6, 7]]
list1.reverse()
for i in (list1):
       if type(i) != type([]):
           list1=list1.reverse()
print(list1)