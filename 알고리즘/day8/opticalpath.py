
def dfs(yx,km):
    global end
    if not 0 in visited[2:len(visited)+1]:
        km=km+abs(yx[0]-end[0])+abs(yx[1]-end[1])
        result.append(km)
        return
    for v in range(2,len(y_x)):
        if visited[v]==0:
            # print(v)
            visited[v]=1
            # print(visited)
            # print(yx)
            # print(y_x[v])
            # print(km)
            pluskm=abs(yx[0]-y_x[v][0])+abs(yx[1]-y_x[v][1])
            dfs(y_x[v],km+pluskm)
            visited[v]=0


T=int(input())
for t in range(T):
    N=int(input())
    data=list(map(int,input().split()))
    y_x=[]
    for n in range(N+2):
        y_x.append((data[2*n],data[2*n+1]))

    start=y_x[0]
    end=y_x[1]
    # print(y_x)
    visited=[0]*(len(y_x)+1)
    result=[]
    dfs(start,0)
    print(result)


