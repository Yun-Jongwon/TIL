def dfs(nextpoint,battery):
    global minisum
    if not 0 in visit:
        if battery+total_map[nextpoint][0]<minisum:
            minisum=battery+total_map[nextpoint][0]
        return
    for v in range(len(visit)):
        if visit[v]==0:
            visit[v]=1
            dfs(v,battery+total_map[nextpoint][v])
            visit[v]=0
    




T=int(input())
for t in range(T):
    N=int(input())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    visit=[0]*N
    minisum=99999999
    visit[0]=1
    dfs(0,0)
    print('#{} {}'.format(t+1,minisum))
