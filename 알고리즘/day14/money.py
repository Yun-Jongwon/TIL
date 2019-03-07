def dfs(money_count):
    global result
    if money_count >= 40:
        return
    if money_count > result:
        result = money_count
    for i in range(len(data)):
        visited[i] = 1
        dfs(money_count + data[i])
        visited[i] = 0


money=int(input())
n=int(input())
data=list(map(int,input().split()))
visited=[0]*len(data)
result=0
dfs(0)
print(result)

