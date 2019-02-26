
def issafe(y,x):
    if y<n and x<n and y>=0 and x>=0:
        return True



T=int(input())
for t in range(T):
    table=[]
    n=int(input())
    for xy in range(n):
        row=input()
        row=[int(i) for i in row]
        table.append(row)

    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    queue=[]

    for i in range(len(table)):
        if 2 in table[i]:
            index=table[i].index(2)
            start=(i,index)
    queue.append(start)


    result=0
    count=0
    table[start[0]][start[1]]=-1
    while queue:
        start=queue.pop(0)

        for i in range(4):
            if issafe(start[0]+dy[i],start[1]+dx[i]) and table[start[0]+dy[i]][start[1]+dx[i]]==0:
                queue.append((start[0]+dy[i],start[1]+dx[i]))
                table[start[0] + dy[i]][start[1] + dx[i]]= table[start[0]][start[1]]-1
            elif issafe(start[0]+dy[i],start[1]+dx[i]) and table[start[0]+dy[i]][start[1]+dx[i]]==3:
                result = table[start[0]][start[1]]
                queue=[]
                break
    result=-result-1
    if result==-1:
        result=0
    print(f'#{t+1} {result}')









