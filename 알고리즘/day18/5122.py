class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link
def Enqueue(item):
    global head
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
    N,M,L=map(int,input().split())
    data=list(map(int,input().split()))
    head=None
    for d in data:
        Enqueue(d)
    for m in range(M):
        change=list(input().split())

        alpa,index=change[0],int(change[1])
        if len(change)>2:
            num=int(change[2])
        if alpa=='I':
            p=head
            for dex in range(index-2):
                p=p.link
            newnode=Node(num)
            newnode.link=p.link
            p.link=newnode
        elif alpa=='D':
            p=head
            for dex in range(index-1):
                p=p.link
            p.link=p.link.link
        elif alpa=='C':
            p=head
            for dex in range(index):
                p=p.link
            p.data=num
    p=head
    count=0
    for l in range(L):
        
        if p.link==None:
            print('#{} {}'.format(t+1,-1))
            count=1
            break
        else:
            p=p.link
    if count==0:
        print('#{} {}'.format(t+1,p.data))
    # count=0

    # for l in range(L):
    #     p=p.link
    #     if p.link==None:
    #         print('#{} {}'.format(t+1,-1))
    #         count=1
    #         break
    # if count==0:
    #     print('#{} {}'.format(t+1,p.data))

            