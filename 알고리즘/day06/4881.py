def backtrack(K,N,result):
    global min_result
    for i in range(N):
        if visited[i]==0:
            visited[i]=1
            result+=total_map[K][i]
            if result>min_result:
                visited[i] = 0
                result -= total_map[K][i]
                continue
            if K+1<N:
                backtrack(K+1,N,result)
            else:
                if min_result>result:
                    min_result=result
            visited[i]=0
            result-=total_map[K][i]



T=int(input())
for t in range(T):
    N=int(input())
    total_map=[]
    for n in range(N):
        total_map.append(list(map(int,input().split())))
    visited=[0]*N
    result=0
    result_list=[]
    min_result=999999999

    backtrack(0,N,result)
    print(f'#{t+1} {min_result}')