import re
import pandas as pd
import numpy as np
import collections
f = open(r"C:\Users\dkhurm\Desktop\Om Saraswataye Namah\advent-of-code-2020\inputs\2020d25.txt", "r")
text = (f.read()).strip().split('\n')

def find_loops(target):
    value = 1
    idx = 0
    while value != target:
        value = value*7
        value = value%20201227
        idx = idx+1
    return idx

def transform(value, num_loops):
    ans = 1
    for _ in range(num_loops):
        ans = (ans%20201227*value%20201227)%20201227
        # print(ans)
    return ans
my_loop = find_loops(int(text[0]))    
door_loop = find_loops(int(text[1]))

public_door = (int(text[1]))
public_card = int(text[0])

ans1 = transform(public_door,my_loop)
ans2 = transform(public_card,door_loop)
print(ans1 == ans2)

