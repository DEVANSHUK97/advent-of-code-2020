# -*- coding: utf-8 -*-
"""
@author: dkhurm
"""

import re
import pandas as pd
import numpy as np
f = open(r"C:\Users\dkhurm\Desktop\Om Saraswataye Namah\aoc\inputs\2020d8.txt", "r")
text = (f.read()).strip()
lines = text.split('\n')
acc = 0

i = 0
seen = {}

while seen.get(i,-1) == -1:
    if lines[i].split(' ')[0] == 'acc':
        acc = acc + int(lines[i].split(' ')[1])
        seen[i] = 1
        i = i + 1
        
    elif lines[i].split(' ')[0] == 'nop':
        seen[i] = 1
        i = i + 1
    
    else:
        seen[i] = 1
        i = i + int(lines[i].split(' ')[1])
print(acc)

#################################################################



jmps = []
for i in range(len(lines)):
    if lines[i].split(' ')[0] == 'jmp':
        jmps.append(i)
        

nops = []
for i in range(len(lines)):
    if lines[i].split(' ')[0] == 'nop':
        nops.append(i)

def check(lines):
    i = 0
    seen = {}
    acc = 0
    while seen.get(i,-1) == -1 and i < len(lines):
        if lines[i].split(' ')[0] == 'acc':
            acc = acc + int(lines[i].split(' ')[1])
            seen[i] = 1
            i = i + 1
            
        elif lines[i].split(' ')[0] == 'nop':
            seen[i] = 1
            i = i + 1
        
        else:
            seen[i] = 1
            i = i + int(lines[i].split(' ')[1])
    if i == len(lines):
        print(acc,i)
        return 1
    print(f'i is {i}')
    return 0

for i in jmps:
    orig = lines[i]
    mod = ' '.join(['nop', lines[i].split(' ')[1]])
    lines[i] = mod
    if check(lines):
        lines[i] = orig
        print('Done!')
        break
    lines[i] = orig
    
for i in nops:
    orig = lines[i]
    mod = ' '.join(['jmp', lines[i].split(' ')[1]])
    lines[i] = mod
    if check(lines):
        lines[i] = orig
        break
    lines[i] = orig
        
        

    

