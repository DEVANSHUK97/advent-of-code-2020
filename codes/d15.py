import re
import pandas as pd
import numpy as np
import collections
import os
os.getcwd()
f = open(r"\2020d15.txt", "r")
text = (f.read()).strip()
start = list(map(int,text.split(',')))
mem = {}
spoken = start[:]
for i in range(len(spoken)):
    mem[spoken[i]] = mem.get(spoken[i],[]) + [i]
        
prev = spoken[-1]
for i in range(len(spoken), 2020):
    if len(mem[prev]) == 1:
        spoken.append(0)
    else:
        spoken.append(mem[prev][-1] - mem[prev][-2])
    mem[spoken[-1]] = mem.get(spoken[i],[]) + [i]
    prev = spoken[-1]

print(spoken[-1])

