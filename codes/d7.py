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
    contents = [' '.join(i.strip().split(' ')[1:-1]) for i in rhs]
    if 'other' in contents:
        contents = []
    dic[lhs] = contents

tracker = {}

def f(src,tracker,dic):
    if src == 'shiny gold':
        # print('found it, returning')
        return 1
    
    if tracker.get(src,-1) != -1:
        return tracker.get(src)

    mx = 0
    for x in dic[src]:
        mx = max(mx, f(x, tracker, dic))
    tracker[src] = mx
    
    return mx
    


counter = 0
for i in list(dic.keys()):
    # print('1--:',i)
    if i != 'shiny gold':
        # print('1--:',i, counter)
        counter = counter + f(i, tracker, dic)
        # print('over with ',i,'\n', tracker)
