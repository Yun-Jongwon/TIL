
T=int(input())
for t in range(T):
    n,m,k=map(int,input().split())
    rating=list(map(int,input().split()))

    count=k
    custom=[]
    cycle=n//k+1
    if cycle>0:
        for i in range(cycle):
            custom.append(0)

    result="Possible"
    cyclecount=1
    for i in range(n):
        if i>=k*cyclecount:
            count=k
            cyclecount+=1

        if rating[i]<m: #m*cyclecount=몇초에 오는지로 비교
            result="Impossible"
            break
        
        if rating[i]//m:
            custom[rating[i]//m-1]+=1

    
        count-=1
    for i in custom:
        if i>k:
            result="Impossible"
    print(f'#{t+1} {result}')
    
