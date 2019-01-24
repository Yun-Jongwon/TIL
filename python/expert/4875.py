T=int(input())
for t in range(T):
    table=[]

    for xy in range(int(input())):
        row=input()
        row=[int(i) for i in row]
        table.append(row)

    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    stack=[]

    for i in range(len(table)):
        if 2 in table[i]:
            index=table[i].index(2)
            start=[i,index]
    stack.append(start)


    result=0
    while stack:
        a=stack.pop()
        table[a[0]][a[1]]=1

        for i in range(4):

            if dy[i]+a[0]<len(table) and dy[i]+a[0]>-1 and a[1]+dx[i]<len(table) and a[1]+dx[i]>-1 :
                if table[dy[i]+a[0]][a[1]+dx[i]]==0:
                    stack.append([dy[i]+a[0],a[1]+dx[i]])           
                if table[dy[i]+a[0]][a[1]+dx[i]]==3:
                    result=1

    print(f'#{t+1} {result}')


