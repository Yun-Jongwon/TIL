for t in range(10):
    num=int(input())
    tree=[0]*(num+1)
    left_child = [0] * (num + 1)
    right_child = [0] * (num + 1)
    inspect=['+','-','*','/']
    for n in range(num):
        data=list(input().split())
        tree[n+1]=data[1]
        if len(data)>2:
            left_child[n+1]=int(data[2])
        if len(data)>3:
            right_child[n+1]=int(data[3])
    result=1
    for i in range(1,num+1):
        if left_child[i]!=0 and right_child[i]!=0 and (not tree[i] in inspect):
            result=0
        if (left_child[i]==0 or right_child==0) and tree[i] in inspect:
            result=0
    print('#{} {}'.format(t+1,result))


