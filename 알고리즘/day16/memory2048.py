T=int(input())
for t in range(T):
    N,direction=input().split()
    total_map=[]
    N=int(N)
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    if direction=='up':
        for x in range(N):
            y = 0
            while y < N - 1:
                if total_map[y][x]!=0:
                    for candi in range(y + 1, N):
                        if total_map[y][x] == total_map[candi][x]:
                            total_map[y][x] = 2 * total_map[candi][x]
                            total_map[candi][x] = 0
                            y = candi
                            break
                        elif total_map[y][x] != total_map[candi][x]:
                            if total_map[candi][x]==0:
                                continue
                            else:
                                break
                y += 1
        for x in range(N):
            temp=[]
            for y in range(N):
                if total_map[y][x]!=0:
                    temp.append(total_map[y][x])
                    total_map[y][x]=0
            for te in range(len(temp)):
                total_map[te][x]=temp[te]

    elif direction=='down':
        for x in range(N):
            y = N - 1
            while y > 0:
                if total_map[y][x] != 0:
                    for candi in range(y - 1, -1, -1):
                        if total_map[y][x] == total_map[candi][x]:
                            total_map[y][x] = 2 * total_map[candi][x]
                            total_map[candi][x] = 0
                            y = candi
                            break
                        elif total_map[y][x] != total_map[candi][x]:
                            if total_map[candi][x]==0:
                                continue
                            else:
                                break
                y -= 1
        for x in range(N):
            temp=[]
            for y in range(N-1,-1,-1):
                if total_map[y][x]!=0:
                    temp.append(total_map[y][x])
                    total_map[y][x]=0
            for te in range(len(temp)):
                total_map[N-1-te][x]=temp[te]



    elif direction=='right':
        for y in range(N):
            x=N-1
            while x>0:
                if total_map[y][x] != 0:
                    for candi in range(x-1,-1,-1):
                        if total_map[y][x]==total_map[y][candi]:
                            total_map[y][x]=2*total_map[y][candi]
                            total_map[y][candi]=0
                            x=candi
                            break
                        elif total_map[y][x]!=total_map[y][candi]:
                            if total_map[y][candi]==0:
                                continue
                            else:
                                break
                x-=1
        for y in range(N):
            temp=[]
            for x in range(N-1,-1,-1):
                if total_map[y][x]!=0:
                    temp.append(total_map[y][x])
                    total_map[y][x]=0
            for te in range(len(temp)):
                total_map[y][N-1-te]=temp[te]
    else: #left
        for y in range(N):
            x=0
            while x<N-1:
                if total_map[y][x] != 0:
                    for candi in range(x+1,N):
                        if total_map[y][x]==total_map[y][candi]:
                            total_map[y][x]=2*total_map[y][candi]
                            total_map[y][candi]=0
                            x=candi
                            break
                        elif total_map[y][x]!=total_map[y][candi]:
                            if total_map[y][candi]==0:
                                continue
                            else:
                                break
                x+=1
        for y in range(N):
            temp=[]
            for x in range(N):
                if total_map[y][x]!=0:
                    temp.append(total_map[y][x])
                    total_map[y][x]=0
            for te in range(len(temp)):
                total_map[y][te]=temp[te]
    print('#{}'.format(t+1))
    for i in total_map:
        for j in i:
            print(j,end=' ')
        print()




