T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    total_map=[[0]*(N+1) for i in range(N+1)]
    for m in range(M):
        start,end=map(int,input().split())
        total_map[start][end]=1
        total_map[end][start]=1
    result=set()
    for i in range(N+1):
        if total_map[1][i]==1:
            result.add(i)
    if len(result)>0:
        result_list=list(result)
        for r in result_list:
            for n in range(N+1):
                if total_map[r][n]==1:
                    result.add(n)
    if len(result)==0:
        print("#{} {}".format(t+1,0))
    else:
        print("#{} {}".format(t+1,len(result)-1))


