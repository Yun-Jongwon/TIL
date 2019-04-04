def dfs(result):
    if sum(visit)==len(visit):
        # print(result)
        vector.append(result[:])
        result.pop()
        return
    for i in range(N):
        if visit[i]==0:
            visit[i]=1
            a=total_data[i]
            for j in range(N):
                if visit[j]==0:
                    visit[j]=1
                    b=total_data[j]
                    result.append((a[0]-b[0],a[1]-b[1]))
                    # print(result)
                    dfs(result)
                    visit[j]=0


            visit[i]=0
    if len(result)>=1:
        result.pop()




T=int(input())
for t in range(T):
    N=int(input())
    total_data=[]
    for n in range(N):
        data=tuple(map(int,input().split()))
        total_data.append(data)

    visit=[0]*N

    vector=[]
    dfs([])
    value=80000000000
    for v in range(len(vector)):
        x=0
        y=0
        for one in range(len(vector[v])):
            x+=vector[v][one][0]
            y+=vector[v][one][1]
        candi=x**2+y**2
        if candi<value:
            value=candi

    print(value)


