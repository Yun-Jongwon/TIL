def issafe(y,x):
    if y>=0 and x>=0 and y<N and x<N:
        return True
    else:
        return False

N,M,K=map(int,input().split())
A=[]
total_map=[[[] for i in range(N)]for j in range(N)]
rest_energy=[[5]*N for j in range(N)]
for n in range(N):
    data=list(map(int,input().split()))
    A.append(data)
for m in range(M):
    x,y,z=map(int,input().split())
    total_map[x-1][y-1].append(z)

dy=[-1,-1,-1,0,0,1,1,1]
dx=[-1,0,1,-1,1,-1,0,1]



for k in range(K):
    #봄
    for y in range(N):
        for x in range(N):
            if total_map[y][x]!=[]:
                total_map[y][x]=list(sorted(total_map[y][x]))
                for to in range(len(total_map[y][x])):
                    if total_map[y][x][to]<=rest_energy[y][x] :

                        rest_energy[y][x]-=total_map[y][x][to]
                        total_map[y][x][to] += 1
                    else:
                        total_map[y][x][to]=-total_map[y][x][to]
    #여름
    for y in range(N):
        for x in range(N):
            if total_map[y][x]!=[]:
                # print(total_map[y][x])
                for to in range(len(total_map[y][x])):
                    # print(to)
                    if total_map[y][x][to]<0:
                        rest_energy[y][x]+=-total_map[y][x][to]//2
                        total_map[y][x][to]=0
                for zero in range(total_map[y][x].count(0)):
                    total_map[y][x].remove(0)
    #가을
    for y in range(N):
        for x in range(N):
            if total_map[y][x]!=[]:
                for to in range(len(total_map[y][x])):
                    if total_map[y][x][to]%5==0:
                        for dir in range(8):
                            if issafe(y+dy[dir],x+dx[dir]):
                                total_map[y+dy[dir]][x+dx[dir]].append(1)

    #거울
    for y in range(N):
        for x in range(N):
            rest_energy[y][x]+=A[y][x]
# print(total_map)
result=0
for y in range(N):
    for x in range(N):
        if total_map[y][x] != []:
            result+=len(total_map[y][x])
print(result)


