def dfs(total_map,start,weight_sum):
    global min_price

    if start==int(n) and weight_sum<min_price:
        min_price=weight_sum
        return
    if weight_sum>min_price:
        return
    count = 0
    for x in range(1,int(n)+1):
        if total_map[start][x]!=0 and visted[x]==0:
            weight_sum+=total_map[start][x]
            visted[x]=1
            dfs(total_map,x,weight_sum)
            weight_sum-=total_map[start][x]
            visted[x]=0
            count+=1




n,m=input().split()
total_map=[[0]*(int(n)+1) for i in range(int(n)+1)]
for i in range(int(m)):
    start,end,weight=map(int,input().split())
    total_map[start][end]=weight
    total_map[end][start]=weight
min_price=999999999
visted=[0]*(int(n)+1)
dfs(total_map,1,0)
print(min_price)

