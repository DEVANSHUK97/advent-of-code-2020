import re
import pandas as pd
import numpy as np
import collections
import os
os.getcwd()
f = open(r"2020d14.txt", "r")
text = (f.read()).strip()
lines = list(text.split('\n'))
mem = {}
def d2b(d):
    ans = ''
    while(d):
        q = d//2
        r = d%2
        d = q
        ans = str(r) + ans
    ans = '0'*(36-len(ans))+ans
    return ans
def b2d(b):
    ans = 0
    val = 1
    for i in b[::-1]:
        if i == '1':
            ans = ans + val
        val = val * 2
    return ans
def mas(val,mask):
    b = d2b(val)
    ans= ''
    if len(mask)!=len(mask):
        raise("dude wtf!")
    for i in range(len(mask)):
        if mask[i] == '1':
            ans = ans + '1' 
        elif mask[i] == '0':
            ans = ans + '0' 
        elif mask[i] == 'X':
            ans = ans + b[i]
        else:
            print(mask, val, i)
    return b2d(ans)
for i in lines:
    if i[1] == 'a':
        mask = i.split('= ')[1].strip()
    elif i[1] == 'e':
        loc = int(i.split(']')[0][4:])
        val = int(i.split(' = ')[1])
        mem[loc] = mas(val, mask) 
ans = 0
for i in mem.values():
    ans = ans + i
print(ans)

############################################################
def all_locs(arr, idx, results):
    if len(arr[idx:])==0:
        results.append(arr)
        return results
    if arr[idx] == 'X':
        results = all_locs(arr[:idx]+'0'+arr[idx+1:], idx + 1,results)
        results = all_locs(arr[:idx]+'1'+arr[idx+1:], idx + 1, results)
        return results
    results = all_locs(arr, idx + 1, results)
    return results

def mas(val,mask):
    b = d2b(val)
    ans= ''
    if len(mask)!=len(mask):
        raise("dude wtf!")
    for i in range(len(mask)):
        if mask[i] == '1':
            ans = ans + '1' 
        elif mask[i] == '0':
            ans = ans + b[i]
        elif mask[i] == 'X':
            ans = ans + 'X'
        else:
            print(mask, val, i)
    locs = all_locs(ans, 0, [])
    return [b2d(i) for i in locs]

mem = {}
for i in lines:
    if i[1] == 'a':
        mask = i.split('= ')[1].strip()
    elif i[1] == 'e':
        loc = int(i.split(']')[0][4:])
        val = int(i.split(' = ')[1])
        locs = mas(loc, mask) 
        for x in locs:
            mem[x] = val
ans = 0
for i in mem.values():
    ans = ans + i
print(ans)    