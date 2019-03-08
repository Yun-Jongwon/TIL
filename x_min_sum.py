T=int(input())
for t in range(T):
    N,K=map(int,input().split())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    result=[]
    for y in range(N-K+1):
        for x in range(N-K+1):
            right_of_x=0
            left_of_x=0
            for k in range(K):
                right_of_x+=total_map[y+k][x+k]
                left_of_x+=total_map[y+k][x+K-1-k]
            result.append(abs(right_of_x-left_of_x))
    print('#{} {}'.format(t+1,min(result)))



