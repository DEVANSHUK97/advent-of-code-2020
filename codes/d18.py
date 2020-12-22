import re
import pandas as pd
import numpy as np
import collections
import os
import time
from collections import deque

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

os.getcwd()
f = open(r"C:\Users\dkhurm\Desktop\Om Saraswataye Namah\advent-of-code-2020\inputs\2020d18.txt", "r")
lines = (f.read()).strip().split('\n')

tokenized = [re.findall('\d+|[+*()]',line) for line in lines]

def evaluate(token_deque):
    result = 0
    operator = add
    while(token_deque):
        token = token_deque.popleft()
        # print(token_deque)
        # print(result)
    
        if re.match('[0-9]+', token):
            result = operator(result, int(token))
        
        elif token == '+':
            operator = add
        elif token == '*':
            operator = mul
        elif token == '(':
            result = operator(result,evaluate(token_deque))
        elif token == ')':
            break   
    
    return result
    
print(evaluate(deque(re.findall('\d+|[+*()]', '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))' ))))

ans = 0
for t in tokenized:
    ans += evaluate(deque(t))

#################################################
    
def evaluate(token_deque):
    sum = 0
    product = 1
    while(token_deque):
        token = token_deque.popleft()
        # print(token_deque)
        # print(result)
    
        if re.match('[0-9]+', token):
            sum += product * int(token)

        elif token == '*':
            product = sum
            sum = 0
            
        elif token == '(':
            sum += evaluate(token_deque)*product
        elif token == ')':
            break   
    
    return sum

    
print(evaluate(deque(re.findall('\d+|[+*()]', '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))' ))))

ans = 0
for t in tokenized:
    ans += evaluate(deque(t))