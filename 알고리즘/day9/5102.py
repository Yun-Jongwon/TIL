T=int(input())
for t in range(T):
    V,E=map(int,input().split())

    total_map=[[0]*(V+1) for i in range(V+1)]

    for e in range(E):
        y,x=map(int,input().split())
        total_map[y][x]=1
        total_map[x][y]=1

    start,end=map(int,input().split())
    queue=[]
    vistied=[0]*(V+1)
    distance=[-1]*(V+1)
    queue.append(start)
    vistied[start]=1
    distance[start]=0
    result=[1]
    while queue!=[]:
        start=queue.pop(0)
        for next in range(len(total_map[start])):
            if total_map[start][next]==1 and vistied[next]==0:
                queue.append(next)
                vistied[next] = 1
                distance[next]=distance[start]+1
    if distance[end]==-1:
        distance[end]==0
    print(f'#{t+1} {distance[end]}')




