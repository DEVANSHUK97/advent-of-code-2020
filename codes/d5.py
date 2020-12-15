# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 02:05:46 2020

@author: dkhurm



"""
import re
f = open(r"2020d5.txt", "r")
text = (f.read()).strip()
lines = text.split('\n')
mx = 0
arr = []
for i in lines:
    col = i[:7]
    row = i[7:]
    l = 0
    r = 127
    diff = 128
    for x in col:
        diff = diff/2
        if x == 'F':
            r = l + diff  - 1
        else:
            l = r - diff + 1
        if col[-1] == 'F':
            ans1 = l
        else:
            ans1 = r
    
    l = 0
    r = 7   
    diff = 8
    for y in row:
        diff = diff/2
        if y == 'L':
            r = l + diff - 1
        else:
            l = r - diff + 1
        if row[-1] == 'F':
            ans2 = l
        else:
            ans2 = r
    ans = 8*ans1+ans2
    arr = arr + [ans]
    mx = max(mx,ans)
print(mx)
    
arr.sort()
arr2 = [0] + arr[:-1]
arr3 = []
for i in range(len(arr)):
    arr3 = arr3 + [arr[i]-arr2[i]]
    