f = open(r"2020d1.txt", "r")
text = (f.read()).strip()
inputs = [int(i) for i in text.split('\n')[:-1]]
for i in inputs:
    if (2020-(i)) in inputs:
        print(i*(2020-i))
        
for i in range(len(inputs)):
    for j in range(i+1,len(inputs)):
        for k in range(j+1,len(inputs)):
            if inputs[i]+inputs[j]+inputs[k] == 2020:
                print(inputs[i]*inputs[j]*inputs[k])

