T=int(input())
def dfs(yx):
    global minimums
    if yx==len(point):
        distance0=[]
        distance1=[]
        for v in range(len(visit)):
            if visit[v]==0:
                distance0.append(abs(point[v][0]-stair[0][0])+abs(point[v][1]-stair[0][1]))
            else:
                distance1.append(abs(point[v][0]-stair[1][0])+abs(point[v][1]-stair[1][1]))
        totaltime0=[0]*(len(distance0))
        totaltime1=[0]*(len(distance1))
        for i in range(len(distance0)):
            totaltime0[i]=distance0[i]+total_map[stair[0][0]][stair[0][1]]+1
        for i in range(len(distance1)):
            totaltime1[i]=distance1[i]+total_map[stair[1][0]][stair[1][1]]+1
        totaltime0=sorted(totaltime0)
        totaltime1=sorted(totaltime1)
        distance0=sorted(distance0)
        distance1=sorted(distance1)

        for j in range(3,len(distance0)):
            if totaltime0[j-3]>distance0[j]:
                totaltime0[j]=totaltime0[j-3]+total_map[stair[0][0]][stair[0][1]]
        for j in range(3,len(distance1)):
            if totaltime1[j-3]>distance1[j]:
                totaltime1[j]=totaltime1[j-3]+total_map[stair[1][0]][stair[1][1]]
        result=totaltime0+totaltime1
        mini=max(result)
        if mini<minimums:
            minimums=mini
        return
    
    dfs(yx+1)
    visit[yx]=1
    dfs(yx+1)
    visit[yx]=0




for t in range(T):
    N=int(input())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    point=[]
    stair=[]
    for y in range(N):
        for x in range(N):
            if total_map[y][x]==1:
                point.append((y,x))
            elif total_map[y][x]>1:
                stair.append((y,x))
    visit=[0]*len(point)
    minimums=999999999
    dfs(0)
    print('#{} {}'.format(t+1,minimums))
    




