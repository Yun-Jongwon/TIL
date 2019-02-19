T=int(input())
for t in range(T):
    color_count=int(input())
    grid = [[0 for i in range(10)] for j in range(10)]
    for painting in range (color_count):
        paint=list(map(int,input().split()))
        start_y=paint[0]
        start_x=paint[1]
        end_y=paint[2]
        end_x=paint[3]
        color=paint[4]
        for y in range(paint[0],paint[2]+1):
            for x in range(paint[1],paint[3]+1):
                grid[y][x]+=color
    count=0
    for i in grid:
        for j in range(10):
            if i[j]==3:
                count+=1
    print(f'#{t+1} {count}')

