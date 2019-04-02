N,L,U=map(int,input().split())
total_map=[]
dy=[-1,0,1,0]
dx=[0,1,0,-1]
visit=[[0]*N for i in range(N)]
def bfs(list_data)

def issafe(y,x):
    if y>=0 and x>=0 and y<N and x<N:
        return True
    else:
        return False
for n in range(N):
    data=list(map(int,input().split()))
    total_map.append(data)
for y in range(N):
    for x in range(N):
        open=[]
        for dir in range(4):
            if issafe(y+dy[dir],x+dx[dir]) and abs(total_map[y+dy[dir]][x+dx[dir]]-total_map[y][x])>=L and abs(total_map[y+dy[dir]][x+dx[dir]]-total_map[y][x])<=U:


