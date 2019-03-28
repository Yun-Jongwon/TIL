def issafe(y,x):
    if y>=0 and x>=0 and y<N and x<N:
        return True
    else:
        return False
dy=[0,1,0,-1]
dx=[1,0,-1,0]

T=int(input())
for t in range(T):
    N=int(input())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    mountain=[[9999999]*N for i in range(N)]
    mountain[0][0]=0
    queue=[(0,0)]
    while queue!=[]:
        start=queue.pop(0)
        for dir in range(4):
            if issafe(start[0]+dy[dir],start[1]+dx[dir]):
                if (total_map[start[0] + dy[dir]][start[1] + dx[dir]] - total_map[start[0]][start[1]]) > 0:
                    plus = (total_map[start[0] + dy[dir]][start[1] + dx[dir]] - total_map[start[0]][start[1]]) + 1
                else:
                    plus = 1
                if mountain[start[0]][start[1]]+plus <= mountain[start[0]+dy[dir]][start[1]+dx[dir]] :
                    mountain[start[0] + dy[dir]][start[1] + dx[dir]]=mountain[start[0]][start[1]]+plus
                    if not (start[0]+dy[dir],start[1]+dx[dir]) in queue:
                        queue.append((start[0]+dy[dir],start[1]+dx[dir]))
    print('#{} {}'.format(t+1,mountain[N-1][N-1]))




