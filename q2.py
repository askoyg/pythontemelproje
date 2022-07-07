# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 18:13:40 2022

@author: murat
"""

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l2 = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            l2.append(i)

flatten(l)
print(l2)