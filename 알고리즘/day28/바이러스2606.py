def makeset(x):
    p[x]=x
def find_p(x):
    if p[x]==x:
        return x
    else:
        return find_p(p[x])
def union(a,b):
    p[find_p(b)]=find_p(a)




N=int(input())
connect_count=int(input())
p=[0]*(N+1)
for i in range(1,N+1):
    makeset(i)
for c in range(connect_count):
    a,b=map(int,input().split())
    union(a,b)
count=0
for i in range(2,N+1):
    if find_p(i)==find_p(1):
        count+=1
print(count)
