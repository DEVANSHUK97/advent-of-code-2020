import re
import pandas as pd
import numpy as np
import collections
import os
os.getcwd()
f = open(r'2019d1.txt', "r")
text = (f.read()).strip()
lines = list(map(int,text.split('\n')))
ans1 = 0
final = []
for line in lines:
    ans1 = (line//3 - 2)
    ans = 0
    while ans1 > 0:
        ans += ans1
        ans1 = (ans1//3 - 2)
    final.append(ans)
    
print(sum(final))
