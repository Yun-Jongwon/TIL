T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    total_map=[]
    for n in range(N):
        garo=" ".join(input())
        total_map.append(list(garo.split()))
    result=None



    for i in total_map:
        for k in range(N-M+1):
            one=i[k:N+k]
            reone=list(reversed(one))
            if one==reone:
                result=one


    total_map_revers=list(map(list,zip(*total_map)))


    for i in total_map_revers:
        for k in range(N-M+1):
            one=i[k:N+k]
            reone=list(reversed(one))
            if one==reone:
                result=one

    result_string=''
    for i in result:
        result_string+=i

    print(f'#{t+1} {result_string}')


