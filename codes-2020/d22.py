# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 02:53:38 2020

@author: dkhurm
"""

import re
import pandas as pd
import numpy as np
import collections
f = open(r"C:\Users\dkhurm\Desktop\Om Saraswataye Namah\advent-of-code-2020\inputs\2020d22.txt", "r")
text = (f.read()).strip().split('\n\n')

deck1 = collections.deque(list(map(int,text[0].split('\n')[1:])))
deck2 = collections.deque(list(map(int,text[1].split('\n')[1:])))

while len(deck1) and len(deck2):
    p1 = deck1.popleft()
    p2 = deck2.popleft()
    if p1 > p2:
        deck1.append(p1)
        deck1.append(p2)
    else:
        deck2.append(p2)
        deck2.append(p1)
arr = []
if len(deck1):
    arr = list(deck1)
else:
    arr = list(deck2)
multiplier = len(arr)
ans = 0
for i in arr:
    ans = ans + multiplier*i
    multiplier = multiplier - 1
print(ans)
    