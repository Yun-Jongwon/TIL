def dfs(couple):
    global m
    global count
    if sum(visited)==len(visited):
        count+=1
        return
    for V in range(n):
        if visited[V]==0:
            visited[V]=1
            v=V
            break
    for w in range(n):
        if total_map[v][w]==1 and visited[w]==0:
            visited[w]=1
            dfs(couple+1)
            visited[w]=0
    visited[V]=0


T=int(input())
for t in range(T):
    n,m=map(int,input().split())
    visited=[0]*n
    data=list(map(int,input().split()))
    total_map=[[0]*n for i in range(n)]
    count=0
    for M in range(m):
        a=data[2*M]
        b=data[2*M+1]
        total_map[a][b]=1
        total_map[b][a]=1
    dfs(0)
    print(count)
    # print(total_map)





