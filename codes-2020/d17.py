import re
import pandas as pd
import numpy as np
import collections
import os
import time

os.getcwd()
f = open(r".\inputs\2020d17.txt", "r")
lines = (f.read()).strip().split('\n')
idim = len(lines[0])
times = 6
fdim = idim + 2*times
space = [[['.']*fdim]*fdim]*fdim

patch = []
for line in lines:
    arr = list(line)
    patch.append(arr)
padded_patch = [['.']*fdim]*times
for row in patch:
    padded_patch.append(['.']*times + row + ['.']*times)
for _ in range(times):
    padded_patch.append(['.']*fdim)
space[times] = padded_patch
space


def treat(space, maxdim, k, i, j):
    at = space[k][i][j]
    nbr_acts = 0
    tot_nbrs = 0
    for delta_k in [-1, 0, 1]:
        if k + delta_k >= fdim or k + delta_k < 0:
            continue
        z = k + delta_k
        for delta_i in [-1, 0, 1]:
            if i + delta_i >= fdim or i + delta_i < 0:
                continue
            x = i + delta_i
            for delta_j in [-1, 0, 1]:
                if j + delta_j >= fdim or j + delta_j < 0:
                    continue
                y = j + delta_j
                if (k, i, j) == (z, x, y):
                    # print('all same')
                    continue
                tot_nbrs = tot_nbrs + 1
                nbr = space[z][x][y]
                if nbr == '#':
                    nbr_acts = nbr_acts + 1
    # print(f'{(k, i, j) , tot_nbrs , at , nbr_acts}')

    if at == '.' and nbr_acts == 3:
        # print('#')
        return '#'
    elif at == '#' and nbr_acts not in [2, 3]:
        # print('.')
        return '.'
    else:
        # print(at)
        return at


# delta_space = []
# ans = 0
# for k in range(fdim):
#     plane = []
#     for i in range(fdim):
#         row = []
#         for j in range(fdim):
#             if treat(space,fdim,k,i,j) == '#':
#                 ans += 1
#             row.append(treat(space,fdim,k,i,j))
#         plane.append(row)
#     delta_space.append(plane)

for t in range(times):
    delta_space = []
    ans = 0
    for k in range(fdim):
        plane = []
        for i in range(fdim):
            row = []
            for j in range(fdim):
                if treat(space, fdim, k, i, j) == '#':
                    ans += 1
                row.append(treat(space, fdim, k, i, j))
            plane.append(row)
        delta_space.append(plane)
    space = delta_space.copy()
print(ans)
# ans = 0
# for p in range(fdim):
#     for q in range(fdim):
#         for r in range(fdim):
#             if delta_space[p][q][r] == '#':
#                 ans += 1

# print(ans)

# # delta_space
