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
    N,M=map(int,input().split())
    head=None
    Enqueue(0)
    for m in range(M):
        
        
        dataa=list(map(int,input().split()))
        if m==0:
            for d in dataa:
                Enqueue(d)
        else:    
            p=head
            while p.link.data<=dataa[0]:
                if p.link.link==None:
                    p=p.link
                    break
                else:
                    p=p.link
            if p.link==None:
                temp=None
            else:
                temp=p.link
            for d in dataa:
                newnode=Node(d)
                p.link=newnode
                p=p.link
            p.link=temp
        # p=head
        # while p.link:
        #     print(p.data,end=' ')
        #     p=p.link
        # print(p.data)
    p=head
    while p.link.link.link.link.link.link.link.link.link.link:
        p=p.link
    print("#{}".format(t+1),end=' ')
    print(p.link.link.link.link.link.link.link.link.link.data,end=" ")
    print(p.link.link.link.link.link.link.link.link.data,end=" ")
    print(p.link.link.link.link.link.link.link.data,end=" ")
    print(p.link.link.link.link.link.link.data,end=" ")
    print(p.link.link.link.link.link.data,end=" ")
    print(p.link.link.link.link.data,end=" ")
    print(p.link.link.link.data,end=" ")
    print(p.link.link.data,end=" ")
    print(p.link.data,end=" ")
    print(p.data,end=" ")
    print()



        
            

        
