def issafe(y,x):
    global N
    if y>=0 and x>=0 and y<N and x<N:
        return True
    else:
        return False
dy=[-1,0,1,0]
dx=[0,1,0,-1]

T=int(input())
for t in range(T):
    N=int(input())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    count=0
    top=-50
    for y in range(N):
        queue=[]
        for x in range(N):
            if total_map[y][x]>0:
                queue.append((y,x))
                count+=1
                if total_map[y][x]>top:
                    top=total_map[y][x]
                while queue!=[]:
                    start=queue.pop(0)
                    total_map[start[0]][start[1]]=-1
                    for d in range(4):
                        if issafe(start[0]+dy[d],start[1]+dx[d]) and total_map[start[0]+dy[d]][start[1]+dx[d]]>0:
                            queue.append((start[0]+dy[d],start[1]+dx[d]))
                        if issafe(start[0]+dy[d],start[1]+dx[d]) and total_map[start[0]+dy[d]][start[1]+dx[d]]>top:
                            top=total_map[start[0]+dy[d]][start[1]+dx[d]]
    print('#{} {} {}'.format(t+1,count,top))







