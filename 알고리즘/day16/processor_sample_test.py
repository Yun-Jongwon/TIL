def dfs():
    for y in range(1,N-1):
        for x in range(1,N-1):
            if total_map[y][x]==1:
                for dir in range(4):



T=int(input())
for t in range(T):
    N=int(input())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)


