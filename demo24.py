# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:31:46 2022

@author: Liangbo
"""
a = 153
x=0
y=0
z=0
x = int(a/100)
y = int((a-x*100)/10)
z = a-x*100-y*10



print(x**3+y**3+z**3 == a)