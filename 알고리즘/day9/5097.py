T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    queue=list(map(int,input().split()))
    for m in range(M):
        x=queue.pop(0)
        queue.append(x)
    print(f'#{t+1} {queue[0]}')