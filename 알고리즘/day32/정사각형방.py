def dfs(y,x,cnt,start_point):
    global maximum
    global point_value
    if visit[y][x]>cnt+1:
        return
    else:
        visit[y][x]=cnt+1
    flag=0
    for dir in range(4):
        if issafe(y+dy[dir],x+dx[dir]) and visit[y+dy[dir]][x+dx[dir]]<=cnt+1 and total_map[y][x]-total_map[y+dy[dir]][x+dx[dir]]==-1:
            dfs(y+dy[dir],x+dx[dir],cnt+1,start_point)
            flag=1
    if flag==0:
        if cnt+1>maximum :
            maximum=cnt+1
            point_value=start_point
        elif cnt+1==maximum:
            if total_map[point_value[0]][point_value[1]]>total_map[start_point[0]][start_point[1]]:
                point_value=start_point






def issafe(y,x):
    if x>=0 and y>=0 and y<N and x<N:
        return True
    else:
        return False
T=int(input())
dy=[-1,0,1,0]
dx=[0,1,0,-1]
for t in range(T):
    N=int(input())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    visit=[[0]*N for i in range(N)]
    maximum=0
    point_value=()
    for y in range(N):
        for x in range(N):
            dfs(y,x,0,(y,x))
    print("#{} {} {}".format(t+1,total_map[point_value[0]][point_value[1]],maximum))


