import re
import pandas as pd
import numpy as np
import collections
import os
os.getcwd()
f = open(r"2020d13.txt", "r")
text = (f.read()).strip()
lines = list(text.split('\n'))
ee = int(lines[0])
buses = [int(j) for j in lines[1].split(',') if j != 'x']
wait = ([i - ee%i for i in buses])
print(min(wait)*buses[wait.index(min(wait))])

# #####################################################
def inv(b,m):
    mul = b%m
    tim = 0
    while (mul*tim)%m != 1:
        tim = tim + 1
    return tim
# inv(746611590569, 41)
# inv(3, 11)

dic = {}
ref = -1
for i in lines[1].split(','):
    if i != 'x':
        dic[i] = (-1*lines[1].split(',').index(str(i)))%int(i)
        if dic[i] == 0:
            ref = int(i)
            
m_i = buses[:]
b_i = [dic[str(i)] for i in m_i] 

M = 1
for i in m_i:
    M = M * i
M_i = [int(M/m) for m in m_i]

x_i = []
for i in range(len(M_i)):
    target = 1
    x_i.append(inv(M_i[i], m_i[i]))
    
df = pd.DataFrame({'b_i':b_i, 'm_i':m_i, 'M_i':M_i, 'x_i':x_i})
ans = 0
for i in range(len(M_i)):
    ans = (ans + b_i[i]*M_i[i]*x_i[i])%M
print(ans)
print([ans%i for i in buses])

############
# TODO: With Sieve