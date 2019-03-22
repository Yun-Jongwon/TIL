def issafe(y,x):
    global num
    if y>=0 and x>=0 and y<num and x<num:
        return True
    else:
        return False
def dfs(starty,startx,minisum):
    global result
    if starty==num-1 and startx==num-1:
        if minisum<result:
            result=minisum
        return

    if issafe(starty+1,startx):
        dfs(starty+1,startx,minisum+total_map[starty+1][startx])
    if issafe(starty,startx+1):
        dfs(starty,startx+1,minisum+total_map[starty][startx+1])


T=int(input())
for t in range(T):
    num=int(input())
    total_map=[]
    for n in range(num):
        data=list(map(int,input().split()))
        total_map.append(data)
    result=999999999
    dfs(0,0,total_map[0][0])
    print('#{} {}'.format(t+1,result))
    