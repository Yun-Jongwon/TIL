total_grid=[]
for i in range(19):
    garo=list(map(int,input().split()))
    total_grid.append(garo)
for y in range(19):
    for x in range(19):
        if total_grid[y][x]==1:
            