
for t in range(1):
    node_many=int(input())
    left_child=[0]*(node_many+1)
    right_child=[0]*(node_many+1)
    tree=[0]*(node_many+1)
    for m in range(1,node_many+1):
        data=list(input().split())
        tree[m]=data[1]
        if len(data)>2:
            left_child[m]=int(data[2])
        if len(data)>3:
            right_child[m]=int(data[3])
    result=[]
    realtree = list(map(list, zip(left_child, right_child)))
    # inorder(1)
    buho=['+','*','-','/']
    while tree[1] in buho:
        for i in range(node_many+1):
            if (not tree[left_child[i]] in buho) and tree[left_child[i]]>0 and (not tree[right_child[i]] in buho) and tree[right_child[i]]>0:
                if tree[i]=='-':
                    tree[i]=tree[left_child[i]]-tree[right_child[i]]
                    tree[left_child[i]]=0
                    tree[right_child[i]]=0
                elif tree[i]=='+':
                    tree[i] = tree[left_child[i]] + tree[right_child[i]]
                    tree[left_child[i]] = 0
                    tree[right_child[i]] = 0
                elif tree[i] == '*':
                    tree[i] = tree[left_child[i]] * tree[right_child[i]]
                    tree[left_child[i]] = 0
                    tree[right_child[i]] = 0
                elif tree[i] == '/':
                    tree[i] = tree[left_child[i]] / tree[right_child[i]]
                    tree[left_child[i]] = 0
                    tree[right_child[i]] = 0
                print(tree[i])
    print(tree[1])





