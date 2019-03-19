data='0269FAC9A0'
A,B,C,D,E,F=10,11,12,13,14,15
new_data=[]
for i in data:
    if i=='A':
        new_i=A
    elif i=='B':
        new_i=B
    elif i=='C':
        new_i=C
    elif i=='D':
        new_i=D
    elif i=='E':
        new_i=E
    elif i=='F':
        new_i=F
    else:new_i=int(i)

    for g in range(3,-1,-1):
        result=(new_i&(1<<g))>>g
        new_data.append(result)


pattern=[[0,0,1,1,0,1],
    [0,1,0,0,1,1],
    [1,1,1,0,1,1],
    [1,1,0,0,0,1],
    [1,0,0,0,1,1],
    [1,1,0,1,1,1],
    [0,0,1,0,1,1],
    [1,1,1,1,0,1],
    [0,1,1,0,0,1],
    [1,0,1,1,1,1]]
i=0
while i!=len(new_data)-5:
    for p in range(10):
        if new_data[i:i+6] == pattern[p]:
            print(p, end=' ')
            i+=5
            break
    i+=1

