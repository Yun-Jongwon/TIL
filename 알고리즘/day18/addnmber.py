class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link
def Enqueue(item):
    global head
    newNode=Node(item)
    if head==None:
        head=newNode
    else:
        p=head
        while p.link:
            p=p.link
        p.link=newNode

T=int(input())
for t in range(T):
    head=None
    N,M,L=map(int,input().split())
    data=list(map(int,input().split()))
    for i in data:
        Enqueue(i)
    for m in range(M):
        index,num=map(int,input().split())
        p=head
        newNode=Node(num)
        for dex in range(index-1):
            p=p.link
        newNode.link=p.link
        p.link=newNode
    p=head
    for l in range(L):
        p=p.link
    print(p.data)

