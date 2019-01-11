
T=int(input())
for t in range(T):
    n,m,k=map(int,input().split())
    rating=sorted(list(map(int,input().split())))

    count=k
    custom=[]

    result="Possible"
    cyclecount=1
    for i in range(n):
        if i>=k*cyclecount:
            count=k
            cyclecount+=1

        if rating[i]<m*cyclecount: #m*cyclecount=몇초에 오는지로 비교
            result="Impossible"
            break
    
    
        count-=1
    print(f'#{t+1} {result}')
    
