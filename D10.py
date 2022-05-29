# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:30:05 2022

@author: Liangbo
"""

import re
def numJewelsInStones(J,S):
    pattern = re.compile("["+J+"]")
    rs = pattern.findall(S)
    return len(rs)

j = "aA"
s = "aAAAbaaabbb"

print(numJewelsInStones(j,s))
