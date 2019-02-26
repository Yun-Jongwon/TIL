data=[1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
total_map=[[0]*8 for i in range(8)]

for i in range(len(data)//2):
    total_map[data[2*i]][data[2*i+1]]=1


queue=[]
vistied=[0]*8
distance=[-1]*8
queue.append(1)
vistied[1]=1
distance[1]=0
parents=[0]*8
result=[1]
while queue!=[]:
    start=queue.pop(0)
    for next in range(len(total_map[start])):
        if total_map[start][next]==1 and vistied[next]==0:
            queue.append(next)
            result.append(next)
            vistied[next] = 1
            distance[next]=distance[start]+1
            parents[next]=start
print(result)
print(distance)
print(parents)
print(vistied)




