import re
import pandas as pd
import numpy as np
import collections
import os
import math
os.getcwd()
f = open(r'2019d3.txt', "r")
text = (f.read()).strip()
lines = text.split('\n')
records = set()
steps_records = dict()
total_steps_common = dict()
for i in range(len(lines)):
    arr = lines[i].split(',')
    x = 0
    y = 0
    steps_taken = 0
    for element in arr:
        direction = element[0]
        steps = int(element[1:])
        if direction == 'R':
            for j in range(1,steps+1):
                x += 1
                records.add((i,x,y))
                steps_taken += 1
                if steps_records.get((i,x,y), False) == False:
                    steps_records[(i,x,y)] = steps_taken
                    if i == 1 and steps_records.get((0,x,y), False):
                        total_steps_common[(x,y)] = steps_records.get((0,x,y)) + steps_records.get((1,x,y))
        if direction == 'L':
            for j in range(1,steps+1):
                x += -1
                records.add((i,x,y))
                steps_taken += 1
                if steps_records.get((i,x,y), False) == False:
                    steps_records[(i,x,y)] = steps_taken
                    if i == 1 and steps_records.get((0,x,y), False):
                        total_steps_common[(x,y)] = steps_records.get((0,x,y)) + steps_records.get((1,x,y))
        if direction == 'U':
            for j in range(1,steps+1):
                y += 1
                records.add((i,x,y))
                steps_taken += 1
                if steps_records.get((i,x,y), False) == False:
                    steps_records[(i,x,y)] = steps_taken
                    if i == 1 and steps_records.get((0,x,y), False):
                        total_steps_common[(x,y)] = steps_records.get((0,x,y)) + steps_records.get((1,x,y))
        if direction == 'D':
            for j in range(1,steps+1):
                y += -1
                records.add((i,x,y))
                steps_taken += 1
                if steps_records.get((i,x,y), False) == False:
                    steps_records[(i,x,y)] = steps_taken
                    if i == 1 and steps_records.get((0,x,y), False):
                        total_steps_common[(x,y)] = steps_records.get((0,x,y)) + steps_records.get((1,x,y))
                
        

        
pos1 = set([(x,y) for (i,x,y) in records if i == 0])
pos2 = set([(x,y) for (i,x,y) in records if i == 1])

common = pos1.intersection(pos2)

manhattan = [math.fabs(x) + math.fabs(y) for (x,y) in common]
print(min(manhattan))

###########Part 2

print(min(total_steps_common.values()))
