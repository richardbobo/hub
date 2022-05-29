# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:03:20 2022

@author: Liangbo
"""

"""
输出100到999之间的水仙花数
水仙花数的含义为 153 个位上的数1*1*1 +5*5*5 +3*3*3 = 153
"""
a = 0
b = 0
c = 0

for item in range(100,1000):
    a = item//100 # 百位数
    b = item//10%10 #十位数
    c = item%10 #个位数
    if a**3+b**3+c**3 == item:
        print(item)

    