def divide(starty,startx,N):
    start=total_map[starty][startx]
    for y in range(starty,starty+N):
        for x in range(startx,startx+N):
            if total_map[y][x]!=start:
                size=N//3
                divide(starty,startx,size)
                divide(starty,startx+size,size)
                divide(starty,startx+2*size,size)
                divide(starty+size, startx, size)
                divide(starty+size, startx + size, size)
                divide(starty+size, startx + 2 * size, size)
                divide(starty+ 2 * size, startx, size)
                divide(starty+ 2 * size, startx + size, size)
                divide(starty+ 2 * size, startx + 2 * size, size)
                return
    count[total_map[starty][startx]]+=1
    # print(starty,startx,N)






N=int(input())
total_map=[]
count=[0,0,0]
for n in range(N):
    data=list(map(int,input().split()))
    total_map.append(data)
divide(0,0,N)
print(count[-1])
print(count[0])
print(count[1])