def issafe(y,x):
    if y>=0 and x>=0 and y<4 and x<4:
        return True
    else:
        return False

def dfs(y,x,string,cnt):
    if cnt==7:
        result.add(string)
        return
    for dir in range(4):
        if issafe(y+dy[dir],x+dx[dir]):
            dfs(y+dy[dir],x+dx[dir],string+str(total_map[y+dy[dir]][x+dx[dir]]),cnt+1)





dy=[-1,0,1,0]
dx=[0,1,0,-1]
T=int(input())
for t in range(T):
    total_map=[]
    for i in range(4):
        data=list(map(int,input().split()))
        total_map.append(data)
    result=set()
    for y in range(4):
        for x in range(4):
            dfs(y,x,'',0)
    print("#{} {}".format(t+1,len(result)))



