def dfs(boofoom_number,w):
    for n in range(N+1):
        if total_map[boofoom_number][n]>=1:
            if basic[n]==1:
                result[n]+=total_map[boofoom_number][n]*w
            else:
                dfs(n,total_map[boofoom_number][n]*w)

N=int(input())
M=int(input())
total_map=[[0]*(N+1) for i in range(N+1)]
for m in range(M):
    y,x,cnt=map(int,input().split())
    total_map[y][x]+=cnt
basic=[0]*(N+1)
result=[0]*(N+1)
for n in range(N+1):
    if sum(total_map[n])==0:
        basic[n]=1
for n in range(N+1):
    if total_map[N][n]>=1:
        if basic[n]==1:
            result[n]+=total_map[N][n]
        else:
            dfs(n,total_map[N][n])

for r in range(len(result)):
    if result[r]>0:
        print('{} {}'.format(r,result[r]))

