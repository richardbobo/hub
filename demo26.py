# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:41:57 2022

@author: Liangbo
"""

a = 1
sum = 0
while a <=100:
    if a%2 == 0:
        sum+=a
    a+=1
print(sum)





a = 0
b = 0
c = 0

for item in range(100,1000):
    a = int(item/100) # 百位数
    b = int((item -a*100)/10) #十位数
    c = int(item-a*100+b*10) #个位数
    if a**3+b**3+c**3 == item:
        print(item)
