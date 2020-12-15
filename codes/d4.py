# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 02:05:46 2020

@author: dkhurm


byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

"""
import re
f = open(r"2020d4.txt", "r")
text = (f.read())
lines = text.split('\n\n')
counter = 0

for i in lines:
    valid = 0
    for f in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if f in i:
            valid = valid + 1
    if valid == 7:
            counter = counter + 1
print(counter)

##### Part II

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 02:05:46 2020

@author: dkhurm


byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

"""
import re
import pandas as pd
import numpy as np
f = open(r"2020d4.txt", "r")
text = (f.read()).strip()
lines = text.split('\n\n')
counter = 0
dic = {}

for i in lines:
    valid = 0
    for f in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if f in i:
            valid = valid + 1
    if valid == 7:
        j = i.split('\n')
        for k in j:
            arr = k.split(' ')
            for x in arr:
                if x.split(':')[0] in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
                    dic[x.split(':')[0]] = dic.get(x.split(':')[0],[]) + [(x.split(':')[1])]
df = pd.DataFrame(dic)
df['byr'] = df['byr'].apply(lambda x: int(x) if int(x) in range(1920,2003) else np.nan)
df['iyr'] = df['iyr'].apply(lambda x: int(x) if int(x) in range(2010,2021) else np.nan)
df['eyr'] = df['eyr'].apply(lambda x: int(x) if int(x) in range(2020,2031) else np.nan)
df['hgt'] = df['hgt'].apply(lambda x: np.nan if x[-2:] not in ['cm', 'in'] else x)
df = df.dropna()
df['hgt'] = df['hgt'].apply(lambda x: x if \
                            (x[-2:] == 'cm' and int(x[:-2]) in range(150,194)) or\
                             (x[-2:] == 'in' and int(x[:-2]) in range(59,77))    else np.nan)

df['hcl'] = df['hcl'].apply(lambda x: x if re.match('#[0-9|a-f]{6}',x) else np.nan)
df['ecl'] = df['ecl'].apply(lambda x: x if x in 'amb blu brn gry grn hzl oth'.split(' ') else np.nan)
df['pid'] = df['pid'].apply(lambda x: x if re.match('[0-9]{9}',x) else np.nan)
df = df.dropna()

print(len(df))

