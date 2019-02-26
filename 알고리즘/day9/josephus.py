queue=[0]*10000
front=-1
rear=-1
for i in range(0,41):
    rear=(rear+1)%41
    queue[rear]=i

while rear-front!=2:

    for i in range(2):
        front=(front+1)%41
        cycle=queue[front]
        queue[front]=0
        rear=(rear+1)%41
        queue[rear]=cycle

    front=(front+1)%41
    queue[front]=0
print(queue[rear])
print(queue[front+1])



