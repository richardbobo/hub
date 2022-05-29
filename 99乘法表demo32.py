# -*- coding: utf-8 -*-
"""
Created on Mon May  2 22:26:52 2022

@author: Liangbo
"""

for i in range(1,10):
    for j in range(1,i+1):
        print(j,"*",i,"=",j*i,end = "\t")
    print()