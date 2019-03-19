T=int(input())
for t in range(T):
    n,data=input().split()



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
    result_string=''
    for i in new_data:
        strr=str(i)
        result_string+=strr
    print('#{} {}'.format(t+1,result_string))
