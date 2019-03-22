T=int(input())
for t in range(T):
    N,M,K=map(int,input().split())
    total_map=[[],[]]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map[0].append(data)
        total_map[1].append(data[:])
    print(total_map)
    total_map[0][0][1]=50
    print(total_map)
