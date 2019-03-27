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
for dis in range(1,N):
    if dis==1:
        y=1
    elif dis==2:
        y=0
    elif dis==3:
        y=-1
    elif dis%2==0:
        y=dis//2
    elif dis%2==1:
        y=-dis//2
    for x in range(N):
        if total_map[y][x]# 크기가 작고 유클리드 거리(y-y,x-x)가 dis고 갈 수 있으면
            #거리만큼 시간 더하고 아기상어 위치 옮기기



