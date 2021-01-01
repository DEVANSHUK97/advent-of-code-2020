import re
import pandas as pd
import numpy as np
import collections
import os
os.getcwd()
f = open(r"2020d11.txt", "r")
text = (f.read()).strip()
lines = list(text.split('\n'))
x = []
for line in lines: 
    x.append(list(line))
    
current = x

def change(arr):
    h = len(arr)
    w = len(arr[0])
    # print(h,w)
    changed = []
    for i in range(h):
        row = []
        for j in range(w):
            at = arr[i][j]
            if at == '.':
                row.append('.')
                continue
            else:
                ngbrs = []
                for p in [-1,0,1]:     
                    for q in [-1,0,1]:
                        n_j = j + q
                        n_i = i + p
                        if (n_i == i and n_j == j):
                            continue
                        
                        while ( n_i in range(h) and n_j in range(w) and arr[n_i][n_j] == '.'):
                            n_i = n_i + p
                            n_j = n_j + q
                        if n_i in range(h) and n_j in range(w):
                            ngbrs.append(arr[n_i][n_j])
                            
                count = collections.Counter(ngbrs)
                if count['#'] == 0 and at == 'L':
                    row.append('#')
                elif at == '#' and count['#'] > 4:
                    row.append('L')
                else:
                    row.append(at)
                '''
                # print(at)
                ngbrs = []
                for p in [-1,0,1]:
                    n_i = i + p
                    for q in [-1,0,1]:
                        n_j = j + q
                        if n_i not in range(h) or n_j not in range(w) or (n_i == i and n_j == j):
                            continue
                        else:
                            # print(n_i, n_j)
                            nbr = arr[n_i][n_j]
                            ngbrs.append(nbr)
                count = collections.Counter(ngbrs)
                if count['#'] == 0 and at == 'L':
                    row.append('#')
                elif at == '#' and count['#'] > 3:
                    row.append('L')
                else:
                    row.append(at)
                '''
        changed.append(row)
    return changed






after = change(current)
print(after)
print("#################")
while current != after:
    current = after
    after = change(after)
    print(after)

ans = 0
for i in after:
    for j in i:
        if j == '#':
            ans = ans + 1
print(ans)
