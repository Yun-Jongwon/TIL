T=int(input())
for t in range(T):
    N,k=map(int,input().split())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    count=0
    for y in range(N):
        for x in range(N):
            if total_map[y][x]==0 and x+k+1<=N and sum(total_map[y][x+1:x+k+2])==k and (x+k+1==N or total_map[y][x+k+1]==0):
                count+=1
            if x==0 and total_map[y][x]==1 and sum(total_map[y][x:x+k+1])==k and (x+k==N or total_map[y][x+k]==0):
                count+=1
    total_map_reverse=list(map(list,zip(*total_map)))
    for y in range(N):
        for x in range(N):
            if total_map_reverse[y][x]==0 and x+k+1<=N and sum(total_map_reverse[y][x+1:x+k+2])==k and (x+k+1==N or total_map_reverse[y][x+k+1]==0):
                count+=1
            if x==0 and total_map_reverse[y][x]==1 and sum(total_map_reverse[y][x:x+k+1])==k and (x+k==N or total_map_reverse[y][x+k]==0):
                count+=1

    print(count)