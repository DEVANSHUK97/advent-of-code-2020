# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:50:40 2020

@author: dkhurm
"""
import re
import pandas as pd
import numpy as np
f = open(r"C:\Users\dkhurm\Desktop\Om Saraswataye Namah\aoc\inputs\2020d10.txt", "r")
text = (f.read()).strip()
lines = text.split('\n')
lines_sorted = sorted(list(map(int, lines)))
lines_helper = lines_sorted[1:] + [lines_sorted[-1]+3]
diffs = np.array(lines_helper) - np.array(lines_sorted)

c1 = 1
c3 = 0
for i in diffs:
    if i == 3 :
        c3 = c3 + 1
    if i == 1 :
        c1 = c1 + 1
print(c1 * c3)

#######################################################################
lines_sorted = [0] + lines_sorted 
memo = {}
stack = [lines_helper[-1]]
while len(stack) > 0:
    pick = stack[-1]
    print(pick)
    stack.pop()
    count = 0
    for diff in [1,2,3]:
        print(pick - diff)
        if (pick - diff) in lines_sorted:
            count = count + 1
            print(count)
            if memo.get(pick-diff, -1) == -1:
                stack.append(pick - diff)
                print(stack) 
    memo[pick] = count
    print(memo)
memo[0] = 1
ans = [i for i in memo.values()]
product = 1
for i in ans: 
    product = product * i
print(product)
############################################################################################
all_nodes = [0] + sorted(list(map(int, lines))) + [3 + max(list(map(int, lines)))]

import networkx as nx
g = nx.DiGraph()
for node in all_nodes:
    g.add_node(node)
    for diff in [1,2,3]:
        if node + diff in all_nodes:
            g.add_edge(node, node+diff)

adj = nx.to_numpy_matrix(g)

ans = 0
for n in range(1,len(all_nodes)+1):
    ans = ans + np.linalg.matrix_power(adj, n)[0,-1]
print(ans)