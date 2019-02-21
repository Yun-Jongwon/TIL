
def DFS(y,x,dir,total_map):
    if y==0:
        return x

    if dir==0:
        if issafe(y,x+1):
            if total_map[y][x+1]==1:
                print(y,x+1)
                return DFS(y,x+1,1,total_map)
        elif issafe(y,x-1):
            if total_map[y][x-1]==1:
                print(y,x-1)
                return DFS(y,x-1,2,total_map)
        else:
            print(y-1,x)
            return DFS(y-1,x,0,total_map)

    elif dir==1:
        if issafe(y,x+1):
            if total_map[y][x+1]==1:
                return DFS(y,x+1,1,total_map)
        else:
            return DFS(y-1,x,0,total_map)

    elif dir==2:
        if issafe(y,x-1):
            if total_map[y][x-1]==1:
                return DFS(y,x-1,2,total_map)
        else:
            return DFS(y-1,x,0,total_map)


def issafe(y,x):
    if x>=0 and x<100:
        return True
    else:
        return False


for t in range(10):
    num=int(input())
    total_map=[]
    for i in range(100):
        total_map.append(list(map(int,input().split())))
    for i in range(100):
        if total_map[99][i]==2:
            y,x=99,i
            break
    print(DFS(y,x,0,total_map))
