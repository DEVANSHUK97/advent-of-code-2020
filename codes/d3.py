
f = open(r"2020d3.txt", "r")
text = (f.read()).strip()
counter1 = 0
lines = text.split('\n')

ans = lines[:]
j = 0
i = 0
while i <  len(lines) - 1:
    j = (j+3)%len(lines[0])
    i = i+1
    if lines[i][j] == '#':
        ans[i] = ans[i][:j] + 'X' + ans[i][j+1:]
        counter1 = counter1 +1
    else:
        ans[i] = ans[i][:j] + 'O' + ans[i][j+1:]
print(counter1)


counter2 = 0
j = 0
i = 0
while i <  len(lines) - 1:
    j = (j+1)%len(lines[0])
    i = i+1
    if lines[i][j] == '#':
        ans[i] = ans[i][:j] + 'X' + ans[i][j+1:]
        counter2 = counter2 +1
    else:
        ans[i] = ans[i][:j] + 'O' + ans[i][j+1:]
print(counter2)


counter3 = 0
j = 0
i = 0
while i <  len(lines) - 1:
    j = (j+5)%len(lines[0])
    i = i+1
    if lines[i][j] == '#':
        ans[i] = ans[i][:j] + 'X' + ans[i][j+1:]
        counter3 = counter3 +1
    else:
        ans[i] = ans[i][:j] + 'O' + ans[i][j+1:]
print(counter3)


counter4 = 0
j = 0
i = 0
while i <  len(lines) - 1:
    j = (j+7)%len(lines[0])
    i = i+1
    if lines[i][j] == '#':
        ans[i] = ans[i][:j] + 'X' + ans[i][j+1:]
        counter4 = counter4 +1
    else:
        ans[i] = ans[i][:j] + 'O' + ans[i][j+1:]
print(counter4)

counter5 = 0
ans = lines[:]
j = 0
i = 0
while i <  len(lines) - 1:
    j = (j+1)%len(lines[0])
    i = i+2
    if lines[i][j] == '#':
        ans[i] = ans[i][:j] + 'X' + ans[i][j+1:]
        counter5 = counter5 +1
    else:
        ans[i] = ans[i][:j] + 'O' + ans[i][j+1:]
print(counter5)
