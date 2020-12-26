import re
import pandas as pd
import numpy as np
import collections
f = open(r"2020d25.txt", "r")
text = (f.read()).strip()
lines = text.split('\n')
move_dict = {'e':(2,0), 'se':(1,-1), 'sw':(-1,-1), 'nw':(-1,1), 'ne':(1,1), 'w':(-2,0)}
moves = ['e', 'se', 'sw', 'nw', 'ne', 'w']
all_moves = {}
ans = 0
for line in lines:
    size = len(line)
    idx = 0
    x = 0
    y = 0
    while idx < size:
        step = 1
        if line[idx:idx+step] in moves:
            x = x + move_dict[line[idx:idx+step]][0]
            y = y + move_dict[line[idx:idx+step]][1]
        else:
            step = 2
            x = x + move_dict[line[idx:idx+step]][0]
            y = y + move_dict[line[idx:idx+step]][1]
        # print(x,y,line[idx:idx+step], move_dict[line[idx:idx+step]])
        idx = idx + step
    curr = (x,y)
    # print(curr)
    if not all_moves.get(curr,False):
        all_moves[curr] = 'Black'
        ans = ans + 1
    elif all_moves[curr] =='Black':
        all_moves[curr] = 'White'
        ans = ans - 1
    elif all_moves[curr] =='White':
        all_moves[curr] = 'Black'
        ans = ans + 1
    # print(all_moves)
    # print(ans)
print(ans)


########################################################################################
# Part 2
########################################################################################
days = 100
for day in range(days):
    new_all_moves = all_moves.copy()
    for k in all_moves.keys():
        x = k[0]
        y = k[1]
        for move in move_dict.values():
            delta_x = move[0]
            delta_y = move[1]
            nbr = (x + delta_x, y + delta_y)
            if nbr not in all_moves.keys():
                new_all_moves[nbr] = 'White'
    all_moves = new_all_moves.copy()
    new_floor = {}
    for curr in all_moves.keys():
        # print(curr)
        x = curr[0]
        y = curr[1]
        black_count = 0
        for move in move_dict.values():
            delta_x = move[0]
            delta_y = move[1]
            nbr = (x + delta_x, y + delta_y)
            if all_moves.get(nbr,False) == False:
                continue
            if all_moves[nbr] == 'Black':
                black_count = black_count + 1

        if all_moves[curr] == 'Black' and (black_count == 0 or black_count > 2):
            new_floor[curr] = 'White'
            ans -= 1
        elif all_moves[curr] == 'White' and (black_count == 2):
            new_floor[curr] = 'Black'
            ans += 1
        else:
            new_floor[curr] = all_moves[curr]

    all_moves = new_floor.copy()

print(ans)
