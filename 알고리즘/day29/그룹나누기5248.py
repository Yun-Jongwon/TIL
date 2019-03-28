def makeset(x):
    p[x]=x
def find_p(x):
    if p[x]==x:
        return x
    else:
        return find_p(p[x])
def union(a,b):
    p[find_p(b)]=find_p(a)


T=int(input())
for t in range(T):


    N,M=map(int,input().split())
    data=list(map(int,input().split()))
    p=[0]*(N+1)
    for i in range(1,N+1):
        makeset(i)
    for m in range(M):
        union(data[2*m],data[2*m+1])
    count=0
    standard=[]
    for pp in p:
        if not find_p(pp) in standard:
            count+=1
            standard.append(find_p(pp))

    print('#{} {}'.format(t+1,count-1))
