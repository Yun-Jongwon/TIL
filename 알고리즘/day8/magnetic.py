for i in range(10):
    n=int(input())
    total_map=[list(map(int,input().split())) for j in range(n)]
    count=0
    for x in range(100):
        sign='S'
        for y in range(100):
            if total_map[y][x]==1:
                sign='N'
            elif total_map[y][x]==2 and sign=='N':
                sign='S'
                count+=1
    print(f'#{i+1} {count}')