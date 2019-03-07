
def DFS(y,x,dir,dis):

    if y==0:
        result[x]=dis
        return

    if dir==0:
        if issafe(y,x+1) and total_map[y][x+1]==1:
            DFS(y,x+1,1,dis+1)
        elif issafe(y,x-1) and total_map[y][x-1]==1:
            DFS(y,x-1,2,dis+1)
        else:
            DFS(y-1,x,0,dis+1)

    elif dir==1:
        if issafe(y,x+1) and total_map[y][x+1]==1:
            DFS(y,x+1,1,dis+1)
        else:
            DFS(y-1,x,0,dis+1)

    elif dir==2:
        if issafe(y,x-1) and total_map[y][x-1]==1:
            DFS(y,x-1,2,dis+1)
        else:
            DFS(y-1,x,0,dis+1)


def issafe(y,x):
    if x>=0 and x<100:
        return True
    else:
        return False


for t in range(10):
    num=int(input())
    total_map=[]
    result=[0]*100
    for i in range(100):
        total_map.append(list(map(int,input().split())))

    for i in range(100):
        if total_map[99][i]>=1:
            y,x=99,i
            DFS(y,x,0,0)
    resultmin=9999999

    for j in range(len(result)-1,-1,-1):
        if result[j]<resultmin and result[j]>0:
            resultmin=result[j]
            result_index=j
    print('#{} {}'.format(t+1,result_index))

