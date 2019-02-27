
# def dfs(yx,km):
#     global end
#     if not 0 in visited[2:]:
#         km=km+abs(yx[0]-end[0])+abs(yx[1]-end[1])
#         result.append(km)
#         return
#     for v in range(2,len(y_x)):
#         if visited[v]==0:
#             # print(v)
#             visited[v]=1
#             # print(visited)
#             # print(yx)
#             # print(y_x[v])
#             # print(km)
#             pluskm=abs(yx[0]-y_x[v][0])+abs(yx[1]-y_x[v][1])
#             dfs(y_x[v],km+pluskm)
#             visited[v]=0
#
#
# T=int(input())
# for t in range(T):
#     N=int(input())
#     data=list(map(int,input().split()))
#     y_x=[]
#     for n in range(N+2):
#         y_x.append((data[2*n],data[2*n+1]))
#
#     start=y_x[0]
#     end=y_x[1]
#     # print(y_x)
#     visited=[0]*(len(y_x))
#     result=[]
#     dfs(start,0)
#     print(f'#{t+1} {min(result)}')
def dfs(yx,km):
    global end
    global result
    if km>result:
        return
    if not 0 in visited[2:]:
        km=km+abs(yx[0]-end[0])+abs(yx[1]-end[1])
        if km<result:
            result=km
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
    visited=[0]*(len(y_x))
    result=99999999
    dfs(start,0)
    print(f'#{t+1} {result}')


