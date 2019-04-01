import collections
def issafe(y,x):
    global N
    if y>=0 and x>=0 and Y<N and x<N:
        return True
    else:
        return False



N=int(input())
total_map=[]
for n in range(N):
    data=list(map(int,input().split()))
    total_map.append(data)
for y in range(N):
    for x in range(N):
        if total_map[y][x]==9:
            baby_shark=(y,x)
baby_shark_size=2
baby_shark_eat_count=0
time=0
visit=[[0]*N for i in range(N)]

dy=[-1,0,1,0]
dx=[0,-1,0,1]

queue=collections.deque([baby_shark])
while queue!=[]:
    point=queue.popleft()
    y=point[0]
    x=point[1]
    if total_map[y][x]<baby_shark_size:
        baby_shark_eat_count+=1
    for dir in range(4):
        if issafe(y+dy[dir],x+dx[dir]) and visit[y+dy[dir]][x+dx[dir]]==0 and total_map[y+dy[dir]][x+dx[dir]]<=baby_shark_size:
            if total_map[y+dy[dir]][x+dx[dir]] < baby_shark_size:
                baby_shark_eat_count += 1
                time+=abs(baby_shark[0]-y)+abs(baby_shark[1]-x)
                baby_shark=(y+dy[dir],x+dx[dir])
                queue=collections.deque([baby_shark])

            else:
                queue.append((y+dy[dir],x+dx[dir]))






