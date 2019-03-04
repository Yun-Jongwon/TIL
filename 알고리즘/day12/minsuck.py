T=int(input())
for t in range(T):
    N,K=map(int,input().split())
    notsubmit=list(map(int,input().split()))
    result=[]
    for i in range(1,N+1):
        if not i in notsubmit:
            result.append(i)
    print(f'#{t+1} ',end='')
    for i in result:
        print(f'{i} ',end='')
    print()
