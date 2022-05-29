# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:33:31 2022

@author: Liangbo
"""

print(1+1)
print(9-0)
print(12/3)
print(11%2)
print(2**3)
print(9%-4)
print(-9%4)


print("------------------分割线---------------------------")
a=b=c=20
print(a,b,c)
a+=20
print(a)
a-=10
print(a)
a*=10
print(a)
a/=8
print(a)
a//=3
print(a)

print("----------------------")
a,b,c= 20,23,46
print(a,b,c)


print("交换两个变量的值")
a,b = 10,20
print("交换前a,b",a,b)
a,b = b,a
print("交换后a,b",a,b)
print("a>b",a>b)
print("a>=b",a>=b)
print("a==b",a==b)
print("a!=b",a!=b)

print("-------------------------")

a = 10
b = 10
print("a==b",a==b)
print("a is b",a is not b)

print(id(a))
print(id(b))

list1 = [11,23,244]
list2 = [11,23,244]

print("list1 is list2",list1 is not list2)
print(id(list1),id(list2))


a,b = 1,2

print(a ==1 and b ==2)


s = "helloworld"
print ("k" in s)


a = 11011
b = 8

print(a|b)

print(oct(a>>4))