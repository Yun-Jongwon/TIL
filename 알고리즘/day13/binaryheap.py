T=int(input())
for t in range(T):
    num=int(input())
    data=list(map(int,input().split()))
    tree=[0]*(num+1)
    for d in range(1,len(data)+1):
        tree[d]=data[d-1]
        if tree[d]<tree[d//2]:
            var=d
            while tree[var]<tree[var//2]:
                tree[var],tree[var//2]=tree[var//2],tree[var]
                var=var//2
    final_node_num=num
    result=0
    parent_node_num=0
    while parent_node_num!=1:
        parent_node_num=final_node_num//2
        result+=tree[parent_node_num]
        final_node_num=parent_node_num
    print("#{} {}".format(t+1,result))








