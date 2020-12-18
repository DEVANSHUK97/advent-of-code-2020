# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 05:15:25 2020

@author: dkhurm
"""

import re
import pandas as pd
import numpy as np
f = open(r"2020d7.txt", "r")
text = (f.read()).strip()
lines = text.split('\n')
counter = 0
dic = {}
for line in lines:
    lhs = ' '.join(line.split('contain')[0].split(' ')[:2])
    rhs = line.split('contain')[1].split(',')
    rhs = [i.strip() for i in rhs]
    contents = dict([(' '.join(i.strip().split(' ')[1:-1]), (i.split(' ')[:1][0]) )  for i in rhs])
    dic[lhs] = contents
    for i in dic.keys():
        for j in dic[i].keys():
            if j=='other':
                dic[i] = {'0':'0'}
    

tracker = {}
for i in dic.keys():
    if dic[i] == {'0':'0'}:
        tracker[i] = 1
        
def f(src,tracker,dic):
    print(src)    
    if tracker.get(src,-1) != -1:
        return tracker.get(src)
    indic = dic[src]
    print(indic)
    mx = 0
    for x in indic.keys():        
        mx = mx + int(indic[x]) * f(x, tracker, dic)
        print(mx)
    print(f'done with {src}')
    tracker[src] = mx
    return mx
        


print(f('shiny gold',tracker,dic))
