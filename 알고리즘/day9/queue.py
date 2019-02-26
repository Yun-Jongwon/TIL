queue=[0]*10
front=-1
rear=-1

rear+=1
queue[rear]=1
rear+=1
queue[rear]=2
rear+=1
queue[rear]=3

while front!=rear:
    front+=1
    print(queue[front])