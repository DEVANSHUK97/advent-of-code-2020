# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 02:39:58 2020

@author: dkhurm
"""
import collections

initial = '872495136'

def move(initial, i = 100):
    if i == 0:
        return initial
    
    arr = (list(map(int, list(initial))))
    print(arr)
    curr = arr[0]
    print(curr)
    next3 = arr[1:4]
    print(next3)
    rem = [curr] + arr[4:]
    print(rem)
    x = curr - 1
    if x < min(arr):
        x = max(arr)
    while x not in rem:
        x = x - 1
        if x < min(arr):
            x = max(arr)
    print(x)
    prefix = rem[:rem.index(x)]
    suffix = rem[rem.index(x)+1 :]
    print(prefix)
    new_arr = [x] + next3 + suffix + prefix
    new_curr = new_arr[(new_arr.index(curr) + 1)%len(new_arr)]
    final = new_arr[new_arr.index(new_curr):] + new_arr[:new_arr.index(new_curr)]
    return move(''.join(list(map(str,final))), i-1)

ans_str = move(initial,100)

print(ans_str[ans_str.index('1')+1:]+ans_str[:ans_str.index('1')])

################################################################################################


def move(initial): 
    arr = initial
    # print(arr)
    curr = arr[0]
    # print(curr)
    next3 = arr[1:4]
    # print(next3)
    rem = [curr] + arr[4:]
    # print(rem)
    x = curr - 1
    if x < min(arr):
        x = max(arr)
    while x not in rem:
        x = x - 1
        if x < min(arr):
            x = max(arr)
    # print(x)
    prefix = rem[:rem.index(x)]
    suffix = rem[rem.index(x)+1 :]
    # print(prefix)
    new_arr = [x] + next3 + suffix + prefix
    new_curr = new_arr[(new_arr.index(curr) + 1)%len(new_arr)]
    final = new_arr[new_arr.index(new_curr):] + new_arr[:new_arr.index(new_curr)]
    return list(final)

ans = 0
start = list(initial) 
start = start + list(range(max(start) + 1, 1000001))
for i in range(10000000):
    ans = move(start)
    start = ans
