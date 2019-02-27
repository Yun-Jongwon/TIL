# for t in range(10):
#     num,start=map(int,input().split())
#     total_map=[[0]*101 for i in range(101)]
#     distance=[0]*101
#     vistied=[0]*101
#     queue=[]
#     data=list(map(int,input().split()))
#     for i in range(len(data)//2):
#         total_map[data[2*i]][data[2*i+1]]=1
#
#     queue.append(start)
#     vistied[start] = 1
#     distance[start] = 0
#     result = []
#     while queue != []:
#         start = queue.pop(0)
#         for next in range(len(total_map[start])):
#             if total_map[start][next] == 1 and vistied[next] == 0:
#                 queue.append(next)
#                 vistied[next] = 1
#                 distance[next] = distance[start] + 1
#     for i in range(len(distance)):
#         if distance[i]==max(distance):
#             result.append(i)
#     print(f'#{t+1} {max(result)}')
#
#
#
#
#

def dfs(start,dis):
    if distance[start]>dis:
        distance[start]=dis

    for i in range(101):
        if total_map[start][i]==1 and vistied[i]==0:
            vistied[i]=1
            dfs(i,dis+1)
            vistied[i]=0



for t in range(10):
    num,start=map(int,input().split())
    total_map=[[0]*101 for i in range(101)]
    distance=[9999]*101
    vistied=[0]*101
    data=list(map(int,input().split()))
    for i in range(len(data)//2):
        total_map[data[2*i]][data[2*i+1]]=1

    vistied[start] = 1
    distance[start] = 0
    result = []
    dfs(start,0)
    for i in range(len(distance)):
        if distance[i]==9999:
            distance[i]=0
    for i in range(len(distance)):
        if distance[i]==max(distance):
            result.append(i)
    print(f'#{t+1} {max(result)}')