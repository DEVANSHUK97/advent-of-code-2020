import re
import pandas as pd
import numpy as np
import collections
import os
os.getcwd()
f = open(r'2019d2.txt', "r")
text = (f.read()).strip()
arr = list(map(int,text.split(',')))
idx = 0
arr[1] = 12
arr[2] = 2
while arr[idx] != 99:
    if arr[idx] == 1:
        arr[arr[idx+3]] = (arr[arr[idx+1]] + arr[arr[idx+2]])
    elif arr[idx] == 2:
        arr[arr[idx+3]] = (arr[arr[idx+1]] * arr[arr[idx+2]])
    elif arr[idx] == 99:
        break
    else:
        print('dude wtf!')
    idx += 4


################################
ans = False
for noun in range(0,100):
    for verb in range(0,100):
        idx = 0
        arr = list(map(int,text.split(',')))
        arr[2] = verb
        arr[1] = noun
        while arr[idx] != 99:
            # if arr[idx+1] > len(arr) or arr[idx+2] > len(arr) or arr[idx+3] > len(arr):
            #     idx += 4
            #     continue
            if arr[idx] == 1:
                arr[arr[idx+3]] = (arr[arr[idx+1]] + arr[arr[idx+2]])
            elif arr[idx] == 2:
                arr[arr[idx+3]] = (arr[arr[idx+1]] * arr[arr[idx+2]])
            elif arr[idx] == 99:
                break
            else:
                print('dude wtf!')
            idx += 4
        if arr[0] == 19690720:
            ans = (noun, verb)
            break
    if ans:
        break
print(ans[0]*100 + ans[1])
