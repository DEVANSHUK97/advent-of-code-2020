# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:11:16 2020

@author: dkhurm
"""


import re
import pandas as pd
import numpy as np
f = open(r"2020d9.txt", "r")
text = (f.read()).strip()
lines = text.split('\n')
lines = list(map(int, lines))

i = 26
l = len(lines)
while i < l:
    keep = False
    start = i - 25
    check = lines[start:i]
    target = lines[i]
    for el in check:
        if target - el in check:
            keep = True
            break
    if not keep:
        print(target)
        break
    i = i + 1
    
left = 0
right = 0
window = lines[left]

while window != target:
    if window < target:
        right = right + 1
        if right >= window:
            break
        window = window + lines[right]
    else:
        window = window - lines[left]
        left = left + 1
        if left > right:
            window = window - lines[right]
            right = right + 1
            if right >= window:
                break
            window = lines[right]
            
            
print((min(lines[left:right+1]) + max(lines[left:right+1])))
        
sum(lines[left:right+1])
