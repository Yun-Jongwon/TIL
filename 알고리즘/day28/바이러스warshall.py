N=int(input())
connect_count=int(input())
total_map=[[0]*(N+1) for i in range(N+1)]
for c in range(connect_count):
    y,x=map(int,input().split())
    total_map[y][x]=1
    total_map[x][y]=1
for via in range(1,N+1):
    for start in range(1,N+1):
        if start!=via:
            for stop in range(1,N+1):
                if start!=stop and stop!=via:
                    total_map[start][stop]=total_map[start][stop]|(total_map[start][via]&total_map[via][stop])
print(sum(total_map[1]))







