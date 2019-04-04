T=int(input())
for t in range(T):
    N=int(input())
    da=list(map(int,input().split()))
    visit=[0]*10001
    re=[0]
    for d in da:
        for i in range(len(re)):
            if visit[re[i]+d]==0:
                re+=[re[i]+d]
                visit[re[i]+d]=1
            # print(re)
    print("#{} {}".format(t+1,len(set(re))))
