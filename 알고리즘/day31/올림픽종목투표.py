T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    jongmok=list(map(int,input().split()))
    limit=list(map(int,input().split()))
    cnt=[0]*len(jongmok)
    for L in limit:
        for j in range(len(jongmok)-1):
            if jongmok[j]<=L:
                cnt[j]+=1
                break
    for c in range(len(cnt)):
        if cnt[c]==max(cnt):
            print('#{} {}'.format(t+1,c+1))
            break


