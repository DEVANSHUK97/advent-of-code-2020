import re
import pandas as pd
import numpy as np
import collections
import os
os.getcwd()
f = open(r"2020d16.txt", "r")
text = (f.read()).strip()
parts = text.split('\n\n')
ranges = parts[0]
my = parts[1]
nbr = parts[2]
check = {}
wrong = []
for i in ranges.split('\n'):
    islands = i.split(': ')[1].split(' or ')
    for j in islands:
        lhs = int(j.split('-')[0])
        rhs = int(j.split('-')[1])
        for x in range(lhs, rhs+1):
            check[x] = 1
for tix in nbr.split(':\n')[1].split('\n'):
    for num in tix.split(','):
        if check.get(int(num), False) == 0:
            wrong.append(int(num))
ans = 0
for x in wrong:
    ans = ans + x
print(ans)

#######################################################################
col_num = len(nbr.split(':\n')[1].split('\n')[0].split(','))
nbr_df = pd.DataFrame(columns = ['C'+str(i) for i in range(1, col_num+1)])
idx = 0
for tix in nbr.split(':\n')[1].split('\n'):
    for num in tix.split(','):
        keep = 1
        if check.get(int(num), False) == 0:
            wrong.append(int(num))
            keep = 0
            break
    if keep:
        nbr_df.loc[idx] = list(map(int,tix.split(',')))
        idx = idx + 1
nbr_df.loc[idx] = list(map(int,my.split('\n')[1].split(',')))
rule_map = {}
for i in ranges.split('\n'):
    name = i.split(': ')[0]
    islands = i.split(': ')[1].split(' or ')
    for j in islands:
        lhs = int(j.split('-')[0])
        rhs = int(j.split('-')[1])
        for x in range(lhs, rhs+1):
            rule_map[name] = rule_map.get(name, []) + [x]
            
translation = {}
rule_map_keys = sorted(rule_map.keys())
for i in rule_map.keys():
    for j in nbr_df.columns:
        if nbr_df[j].isin(rule_map[i]).sum() == len(nbr_df[j]) :
            translation[j] = translation.get(j, []) + [i]
            
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
for i in nbr_df.C1:
    if i not in rule_map['departure location']:
        print(i)
sequence = sorted(translation, key = lambda x: len(translation.get(x)))

final = {}
for s in sequence:
    print(s)
    for i in rule_map.keys():
        print(i)
        if i not in final.keys() and nbr_df[s].isin(rule_map[i]).sum() == len(nbr_df[s]) :
            final[i] = s
            break

ans = 1
for i in final:
    if 'departure' in i:
        print(i)
        ans  = ans * nbr_df.loc[190][final[i]]
print(ans)