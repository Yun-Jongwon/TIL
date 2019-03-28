# 1 2 3
# 1 3 4
# 2 4 5
# 3 2 1
# 3 4 4
# 3 5 5
# 4 5 3
# 4 6 4
# 5 6 5
total_map=[[987654321]*7 for i in range(7)]

for t in range(9):
    start,end,cost=map(int,input().split())
    total_map[start][end]=cost

distance=total_map[1][:]
T=[i for i in range(7)]
p=[1]*7
while sum(T)!=1:
    mini=98765432
    for i in range(len(distance)):
        if T[i]!=0:
            mini=min(mini,distance[i])


    for d in range(len(distance)):
        if T[d]!=0:
            if distance[d]==mini:
                v=d#최소값의 인덱스
                break
    for tt in range(len(T)):
        if T[tt]==v:
            T[tt]=0
            break
    for t in T:
        if t!=0:
            if distance[t]>distance[v]+total_map[v][t]:
                distance[t]=distance[v]+total_map[v][t]
                p[t]=v

# print(p)
i=6
result=[]
while p[i]!=i:
    result.append(i)
    i=p[i]
result.append(1)
print(list(reversed(result)))

print(distance[6])
# 1 2 3 4 5 6
# 0 3 4 - - -





