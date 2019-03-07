def whatstone(a):
    if a==1:
        return 1,2
    else:
        return 2,1

T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    total_data=[]
    dx=[0,1,1,1,0,-1,-1,-1]
    dy=[-1,-1,0,1,1,1,0,-1]

    for m in range(M):
        data=list(map(int,input().split()))
        total_data.append(data)
    grid=[[0]*(N+1) for i in range(N+1)]

    grid[N//2+1][N//2]=1
    grid[N // 2 + 1][N // 2+1] = 2
    grid[N // 2 ][N // 2+1] = 1
    grid[N // 2 ][N // 2] = 2
    for i in total_data:
        y=i[1]
        x=i[0]
        grid[y][x]=i[2]
        real_stone,reverse_stone=whatstone(i[2])

        for d in range(8):
            new_y=y+dy[d]
            new_x=x+dx[d]
            if not (new_x > N or new_y > N or new_x <= 0 or new_y <= 0):
                if grid[new_y][new_x]==reverse_stone:
                    will_change=[(new_y,new_x)]
                    while will_change!=[]:
                        new_y=new_y+dy[d]
                        new_x=new_x+dx[d]
                        if new_x>N or new_y>N or new_x<=0 or new_y<=0:
                            break
                        if grid[new_y][new_x]==reverse_stone:
                            will_change.append((new_y,new_x))
                        if grid[new_y][new_x]==real_stone:
                            for w in range(len(will_change)):
                                point=will_change.pop()
                                grid[point[0]][point[1]]=real_stone
                        if grid[new_y][new_x]==0:
                            break






    white_count=0
    black_count=0
    for y in range(1,N+1):
        for x in range(1,N+1):
            if grid[y][x]==1:
                white_count+=1
            elif grid[y][x]==2:
                black_count+=1
    print('#{} {} {}'.format(t+1,white_count,black_count))




