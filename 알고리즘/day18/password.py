class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link
def Enqueue(item):
    global head
    global p
    newnode=Node(item)
    if head==None:
        head=newnode
    else:
        p=head
        while p.link:
            p=p.link
        p.link=newnode
    
T=int(input())
for t in range(T):
    N,M,K=map(int,input().split())
    data=list(map(int,input().split()))
    head=None
    p=head
    for d in data:
        Enqueue(d)
    p=p.link
    p.link=head
    p=head
    for k in range(K):
        for two in range(M-1):
            p=p.link
        newnode=Node(p.data+p.link.data)
        newnode.link=p.link
        p.link=newnode
        p=p.link
    p=head
    count=len(data)+K-1
    print('#{}'.format(t+1),end=' ')
    for pe in range(count+1):
        for co in range(count):
            p=p.link
        print(p.data,end=' ')
        if pe==9:
            break
    print()
    