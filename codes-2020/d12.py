import re
import pandas as pd
import numpy as np
import collections
import os
os.getcwd()
f = open(r"2020d12.txt", "r")
text = (f.read()).strip()
lines = list(text.split('\n'))

cd_i = 0
cd_j = 1
i = 0
j = 0
for line in lines:
    print(line)
    act = line[0]
    mag = int(line[1:])
    print(f'act {act} mag {mag}')
    if act == 'F':
        i = i + mag*cd_i
        j = j + mag*cd_j
    elif act == 'E':
        j = j + mag
    elif act == 'W':
        j = j - mag
    elif act == 'N':
        i = i - mag
    elif act == 'S':
        i = i + mag
    elif act == 'L':
        turns = (mag//90)%4
        for _ in range(turns):
            cd_i, cd_j = (cd_j*-1), cd_i
    elif act == 'R':
        turns = (mag//90)%4
        print(f'turns {turns}')
        print(f'old {cd_i} {cd_j}')
        for _ in range(turns):
            cd_i, cd_j = cd_j, (cd_i*-1)
            print(f'new {cd_i} {cd_j}')
    else:
        print(line)
    print(f'i {i} j {j}')
            
print(np.abs(i)+ np.abs(j))          
 

#########################################################################
cd_i = -1
cd_j = 10
i = 0
j = 0
for line in lines:
    print(line)
    act = line[0]
    mag = int(line[1:])
    print(f'act {act} mag {mag}')
    if act == 'F':
        i = i + mag*cd_i
        j = j + mag*cd_j
    elif act == 'E':
        cd_j = cd_j + mag
    elif act == 'W':
        cd_j = cd_j - mag
    elif act == 'N':
        cd_i = cd_i - mag
    elif act == 'S':
        cd_i = cd_i + mag
    elif act == 'L':
        turns = (mag//90)%4
        for _ in range(turns):
            cd_i, cd_j = (cd_j*-1), cd_i
    elif act == 'R':
        turns = (mag//90)%4
        print(f'turns {turns}')
        print(f'old {cd_i} {cd_j}')
        for _ in range(turns):
            cd_i, cd_j = cd_j, (cd_i*-1)
            print(f'new {cd_i} {cd_j}')
    else:
        print(line)
    print(f'i {i} j {j}')
            
print(np.abs(i)+ np.abs(j))          
               