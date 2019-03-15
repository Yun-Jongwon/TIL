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
    if item==41:
        newNode.link=head


head=None
for i in range(1,42):
    Enqueue(i)
p=head #1

p=p.link #2
p.link=p.link.link# 2->4


while p.link.link!=p:
    p=p.link# 4
    p=p.link# 5
    p.link=p.link.link
print(p.data)
print(p.link.data)


    

