import sys
sys.stdin=open('min.txt','r')
def dfs(y,cost_sum):
    global N,min_cost_sum

    if y==N:
        if cost_sum<min_cost_sum:
            min_cost_sum=cost_sum
        return
    #백트래킹
    if cost_sum>min_cost_sum:
        return
    for x in range(N):
        if visit[x]==0:
            visit[x]=1
            dfs(y+1,cost_sum+total_map[y][x])
            visit[x]=0

T=int(input())
for t in range(T):
    N=int(input())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    visit=[0]*N
    min_cost_sum=987654321
    dfs(0,0)
    print('#{} {}'.format(t+1,min_cost_sum))

