T=int(input())
for t in range(T):
    container_count,truck_count=map(int,input().split())
    container=list(map(int,input().split()))
    truck=list(map(int,input().split()))
    container=list(reversed(sorted(container)))
    truck=list(reversed(sorted(truck)))
    result=0
    for co in range(len(container)):
        for tr in range(len(truck)):
            if container[co]<=truck[tr]:
                result+=container[co]
                truck[tr]=0
                break
    print('#{} {}'.format(t+1,result))





