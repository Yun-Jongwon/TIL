def inorder(T):
    if T:
        inorder(left_child[T])
        print('{}'.format(tree[T]), end='')
        inorder(right_child[T])
for t in range(10):
    num=int(input())
    tree=[0]*(num+1)
    left_child = [0] * (num + 1)
    right_child = [0] * (num + 1)
    for n in range(num):
        data=list(input().split())
        tree[n+1]=data[1]
        if len(data)>2:
            left_child[n+1]=int(data[2])
        if len(data)>3:
            right_child[n+1]=int(data[3])
    print("#{} ".format(t+1),end='')
    inorder(1)
    print()


