import re
import pandas as pd
import numpy as np
import itertools
import collections

import os
os.getcwd()
f = open(r"C:\Users\dkhurm\Desktop\Om Saraswataye Namah\advent-of-code-2020\inputs\2020d19s1.txt", "r")
text = (f.read()).strip()
lines = text.split('\n\n')[0]
grammar = dict()
for line in lines.split('\n'):
    print(line)
    lhs = (line.split(': ')[0])
    rhs = [x.split(' ') for x in line.split(': ')[1].split(' | ')]
    if rhs == [['"a"']]:
        rhs = 'a'
    if rhs == [['"b"']]:
        rhs = 'b'
    grammar[lhs] = rhs
    
strings = text.split('\n\n')[1].split('\n')

def make_all_strings(pattern, grammar, memo = {}):
    if pattern in ['a', 'b']:
        return pattern
    if memo.get(pattern, False):
        return memo.get(pattern)
    all_strings = set()
    for rules in grammar[pattern]:
        temp = []
        precursor = []
        for token in rules:
            temp = (make_all_strings(token, grammar, memo))

        all_strings.update("".join(x) for x in itertools.product(*temp))       
            for i in cartesian_right_factor:
                cartesian_precursor += (i)
            cartesian_precursor = ''.join(list(set(cartesian_precursor)))
        all_strings.update(cartesian_precursor)
    memo[pattern] = list(all_strings)
    return memo[pattern]

all_strs = make_all_strings('0', grammar)
