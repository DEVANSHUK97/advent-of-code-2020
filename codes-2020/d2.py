
f = open(r"2020d2.txt", "r")
text = (f.read()).strip()
inputs = [i for i in text.split('\n')]
counter = 0
for i in inputs:
    policy = i.split(': ')[0]
    pswd  =i.split(': ')[1]
    mn = int(policy.split('-')[0])
    mx = int(policy.split('-')[1].split(' ')[0])
    loi = policy.split('-')[1].split(' ')[1]
    valid = 0
    for x in pswd:
        if x == loi:
            valid = valid + 1
    if valid <= mx and valid >= mn:
        counter = counter + 1
print(counter)

counter = 0
for i in inputs:
    policy = i.split(': ')[0]
    pswd  =i.split(': ')[1]
    mn = int(policy.split('-')[0])
    mx = int(policy.split('-')[1].split(' ')[0])
    loi = policy.split('-')[1].split(' ')[1]
    valid = 0
    for x in [pswd[mn-1], pswd[mx-1]]:
        if x == loi:
            valid = valid + 1
    if valid == 1:
        counter = counter + 1
print(counter)
