def dfs(y,x,V):
    for i in range(V+1):
        if tree[y][i] ==1 and visted[i]==0:
            visted[i]=1
            print(visted)
            dfs(i,x,V)
    return

T=int(input())
for t in range(T):
    V,E=map(int,input().split())
    tree=[[0]*(V+1) for i in range(V+1)]
    visted=[0]*(V+1)

    for e in range(E):
        y,x=map(int,input().split())
        tree[y][x]=1
    print(tree)

    ispossible_y,ispossible_x=map(int,input().split())
    dfs(ispossible_y,ispossible_x,V)
    if visted[ispossible_x]==1:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')





