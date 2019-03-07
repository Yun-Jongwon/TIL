def isoutside(y,x,sero,garo):
    if x==0 or y==0 or x==garo-1 or y==sero-1:
        return True
def isoutside2(y,x):
    for d in range(4):
        if total_map[y+dy[d]][x+dx[d]]==-1:
            return True
def direction(y,x,d):
    global garo,sero,start_x,start_y
    if d==0:
        if x+dx[d]==garo-start_x:
            return 1
        else:
            return d
    elif d==1:
        if y+dy[d]==sero-start_y:
            return 2
        else:
            return d
    elif d==2:
        if x+dx[d]==start_x-1:
            return 3
        else:
            return d
    elif d==3:
        if y+dy[d]==start_y-1:
            start_y+=1
            start_x+=1
            return 0
        else:
            return d

def issafe(x,y):
    if x<garo and y<sero and x>=0 and y>=0:
        return True
    else:
        return False


def bfs(y,x):
    queue=[]
    queue.append((y,x))
    while queue!=[]:
        starty,startx=queue.pop(0)
        for d in range(4):
            if issafe(startx+dx[d],starty+dy[d]) and total_map[starty+dy[d]][startx+dx[d]]==0:
                total_map[starty + dy[d]][startx + dx[d]] = -1
                queue.append((starty+dy[d],startx+dx[d]))






sero,garo=map(int,input().split())
total_map=[]
for i in range(sero):
    garo_data=list(map(int,input().split()))
    total_map.append(garo_data)
dy=[0,1,0,-1]
dx=[1,0,-1,0]
count=0
break_point=1




y=0
x=0
d=0
start_x=0
start_y=0
while y != sero//2+1 or x!=garo//2:

    if total_map[y][x]==0 and (isoutside(y,x,sero,garo) or (start_x!=0 and isoutside2(y,x))):
        total_map[y][x]=-1

    d=direction(y,x,d)
    y=y+dy[d]
    x=x+dx[d]




while True:

    while True:
        zerocount=0
        for y in range(sero):
            for x in range(garo):
                if total_map[y][x]==0:
                    bfs(y,x)
                    zerocount=1
        if zerocount==0:
            break





    for y in range(sero):
        for x in range(garo):
            if total_map[y][x]==1:
                for d in range(4):
                    if total_map[y + dy[d]][x + dx[d]] == -1:
                        total_map[y][x]=0
                        break


    count+=1
    break_point=0

    for y in range(sero):
        for x in range(garo):
            if total_map[y][x]==1:
                break_point=1
    if break_point==0:
        break
    cheese_count=0
    for y in range(sero):
        for x in range(garo):
            if total_map[y][x]==1:
                cheese_count+=1
    # print(cheese_count)

print(count)
print(cheese_count)
