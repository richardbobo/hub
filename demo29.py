# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:51:55 2022

@author: Liangbo
"""

for item in range(3):
    pwd = input("请输入密码")
    if pwd == "8888":
        print("密码正确")
        break
    else:
        print("密码错误，请重新输入")
else:
    print("密码输入超时")
        