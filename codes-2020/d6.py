# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 02:05:46 2020

@author: dkhurm



"""
import re
f = open(r"2020d6.txt", "r")
text = (f.read()).strip()
groups = text.split('\n\n')
ans = 0
for group in groups:
    members = group.split('\n')
    questions = ''.join(members)
    how_many = len(set([i for i in questions]))
    ans = ans + how_many
print(ans)


ans2 = 0
for group in groups:
    arr = []
    members = group.split('\n')
    first = members[0]
    for i in first:
        keep = True
        for j in range(1,len(members)):
            if i not in members[j]:
                keep = False
        if keep:
            arr = arr + [i]
    ans2 = ans2 + len(set(arr))
                
    
    questions = ''.join(members)
    how_many = len(set([i for i in questions]))
    ans2 = ans2 + how_many
print(ans)

