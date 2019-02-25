import sys
sys.stdin = open('input.txt', 'r')

def dfs(start):
    for p in previous:
        if p[start] == 1:
            p[start] = 0
    if not start in result:
        result.append(start)

    for i in range(1,V + 1):
        if total_map[start][i] == 1 and sum(previous[i]) == 0:
            dfs(i)


for t in range(10):
    V,E=map(int,input().split())
    total_map=[[0]*(V+1) for v in range(V+1)]
    data=list(map(int,input().split()))
    howmany=len(data)//2
    visted=[0]*(V+1)
    for i in range(howmany):
        total_map[data[2*i]][data[2*i+1]]=1
    previous=list(map(list,zip(*total_map)))
    # print(previous)
    result = []

    for i in range(1,len(previous)):
        if sum(previous[i])==0:
            start=i
            dfs(start)
    print(f"#{t+1} ",end="")
    print(result)
    for j in result:
        print(j,end=" ")
    print()



