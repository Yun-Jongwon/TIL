def combina(present):
    global length
    global r
    if present>length:
        return
    if sum(visited)==r:
        for i in range(len(visited)):
            if visited[i]==1:
                print(data[i],end=' ')
        print()
        return
    visited[present]=1
    combina(present+1)
    visited[present]=0
    combina(present+1)

data=[0,1,2,3,4,5]
r=3
visited=[0]*(len(data)+1)
length=len(data)

combina(1)